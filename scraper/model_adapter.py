"""
Model provider adapter.

One seam between the formatter and whatever produces a draft analysis. Three
things it exists to guarantee:

- The collector runs offline. With no provider configured, capture still works
  and the entry is written as a raw capture awaiting analysis.
- The provider and model are configuration, not a literal buried in the
  formatter. Rotating providers is a limited control, but it should at least
  not require a code change.
- Interruption is visible. A response carries its stop reason, so an output cut
  off at the token limit cannot be read as a finished analysis.

BOUNDARY. This module establishes which provider was asked, what it returned,
and whether the return was complete. It does not establish that the content of
a completed response is correct, supported, or free of the deference pattern
the Reflexivity Clause names. No adapter here may be treated as an independent
witness to its own output.
"""

import os
from dataclasses import dataclass


@dataclass
class ModelResponse:
    text: str = ""
    stop_reason: str = ""
    provider: str = ""
    model: str = ""
    error: str = ""

    @property
    def available(self) -> bool:
        return not self.error

    @property
    def truncated(self) -> bool:
        """True when the provider reports the output was cut short."""
        return self.stop_reason in {"max_tokens", "length", "content_filter", "pause_turn"}

    @property
    def complete(self) -> bool:
        return self.available and self.stop_reason == "end_turn"


class NullAdapter:
    """No provider configured. Capture proceeds; analysis does not."""

    name = "none"
    model = "none"

    def complete(self, system: str, prompt: str) -> ModelResponse:
        return ModelResponse(
            provider=self.name,
            model=self.model,
            error="no model provider configured (offline capture)",
        )


class AnthropicAdapter:
    name = "anthropic"

    def __init__(self, model: str, max_tokens: int = 4096, api_key: str = ""):
        self.model = model
        self.max_tokens = max_tokens
        self._api_key = api_key
        self._client = None

    def _get_client(self):
        if self._client is None:
            import anthropic
            self._client = anthropic.Anthropic(api_key=self._api_key)
        return self._client

    def complete(self, system: str, prompt: str) -> ModelResponse:
        try:
            message = self._get_client().messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                system=system,
                messages=[{"role": "user", "content": prompt}],
            )
        except Exception as e:  # network, auth, rate limit, SDK absent
            return ModelResponse(provider=self.name, model=self.model, error=str(e))
        blocks = [b for b in getattr(message, "content", []) if getattr(b, "type", "text") == "text"]
        text = "".join(getattr(b, "text", "") for b in blocks)
        return ModelResponse(
            text=text.strip(),
            stop_reason=getattr(message, "stop_reason", "") or "",
            provider=self.name,
            model=self.model,
        )


class FakeAdapter:
    """Test double. Returns scripted responses; never touches a network."""

    name = "fake"

    def __init__(self, responses=None, model: str = "fake-model"):
        self.model = model
        self._responses = list(responses or [])
        self.calls = []

    def complete(self, system: str, prompt: str) -> ModelResponse:
        self.calls.append({"system": system, "prompt": prompt})
        if not self._responses:
            return ModelResponse(provider=self.name, model=self.model,
                                 error="fake adapter exhausted")
        nxt = self._responses.pop(0)
        if isinstance(nxt, ModelResponse):
            nxt.provider = nxt.provider or self.name
            nxt.model = nxt.model or self.model
            return nxt
        return ModelResponse(text=str(nxt), stop_reason="end_turn",
                             provider=self.name, model=self.model)


DEFAULT_MODEL = "claude-haiku-4-5"


def build_adapter(settings: dict = None, env: dict = None):
    """
    Resolve the adapter from configuration, then environment.

    settings (scraper/config.yaml, `settings.model:`):
        provider: none | anthropic
        name: <model id>
        max_output_tokens: <int>

    Environment overrides: VERITICIDE_MODEL_PROVIDER, VERITICIDE_MODEL,
    VERITICIDE_MODEL_MAX_TOKENS. An `anthropic` provider with no
    ANTHROPIC_API_KEY resolves to NullAdapter rather than failing a run.
    """
    settings = settings or {}
    env = os.environ if env is None else env
    cfg = settings.get("model", {}) or {}

    provider = (env.get("VERITICIDE_MODEL_PROVIDER") or cfg.get("provider") or "").strip().lower()
    model = (env.get("VERITICIDE_MODEL") or cfg.get("name") or DEFAULT_MODEL).strip()
    try:
        max_tokens = int(env.get("VERITICIDE_MODEL_MAX_TOKENS") or cfg.get("max_output_tokens") or 4096)
    except (TypeError, ValueError):
        max_tokens = 4096

    if not provider:
        # Back-compatible default: a key in the environment enables analysis.
        provider = "anthropic" if env.get("ANTHROPIC_API_KEY") else "none"

    if provider == "anthropic":
        api_key = env.get("ANTHROPIC_API_KEY", "")
        if not api_key:
            return NullAdapter()
        return AnthropicAdapter(model=model, max_tokens=max_tokens, api_key=api_key)
    return NullAdapter()
