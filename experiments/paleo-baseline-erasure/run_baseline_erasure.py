#!/usr/bin/env python3
"""
Paleo baseline-erasure re-analysis — runner (UNEXECUTED SKELETON).

Operationalizes docs/tier6-baseline-erasure-research-scope-2026-07-02.md via a pre-registered
re-analysis of already-published fungal sedaDNA cores. This file has NOT been run; it is the
pre-registration reference implementation. Cores, gates, responses, and conversion criteria come
from config.yaml / cores.yaml, which must be frozen and hashed before any run.

GOVERNING BOUNDARY (fail-closed, checked at import and asserted into every row):
    Tests mycorrhizal COMPOSITION / RICHNESS and its COINCIDENCE with human impact.
    Does NOT test past network TOPOLOGY or FUNCTION. `FUNCTIONAL_LAYER = "OUT_OF_REACH_ALWAYS"`
    is written into every output row so no downstream reader can quietly upgrade the claim.

Enforced invariants (fail-closed):
  - GATE:  a core enters the H1 pool only if ALL inclusion_gates pass; ineligible cores are logged, not dropped.
  - N-1:   every richness response is rarefied to common read depth; raw-count richness never reported alone.
  - N-4:   the mycorrhizal breakpoint is tested against BOTH human-impact and climate proxies; collinear
           proxies disqualify a core from H1 (collinearity_guard).
  - H3:    the negative-control guild must NOT show the anthropogenic breakpoint; if it does -> INSTRUMENT_FAILURE.
  - PROV:  the frozen (config+cores+this file+queries) hash is bound into every output row.
"""
from __future__ import annotations
import json, sys, hashlib
from dataclasses import dataclass, asdict, field
from pathlib import Path

try:
    import yaml  # pyyaml
except ImportError:
    sys.exit("pip install pyyaml")

HERE = Path(__file__).parent
CONFIG = yaml.safe_load((HERE / "config.yaml").read_text())
CORES = yaml.safe_load((HERE / "cores.yaml").read_text())

FUNCTIONAL_LAYER = "OUT_OF_REACH_ALWAYS"  # the category boundary; never mutated


# ---------------------------------------------------------------------------
# Provenance: hash the frozen pre-registration so every output row binds to the exact design.
def prereg_hash() -> str:
    parts = []
    for name in ("config.yaml", "cores.yaml", Path(__file__).name):
        p = HERE / name
        parts.append(hashlib.sha256(p.read_bytes()).hexdigest())
    qdir = HERE / "queries"
    if qdir.exists():
        for q in sorted(qdir.rglob("*")):
            if q.is_file():
                parts.append(hashlib.sha256(q.read_bytes()).hexdigest())
    return hashlib.sha256("".join(parts).encode()).hexdigest()[:16]


# ---------------------------------------------------------------------------
@dataclass
class GateResult:
    core_id: str
    passed: bool
    failed_gate: str | None
    detail: str


def screen_core(core: dict) -> GateResult:
    """Apply config.inclusion_gates. Log pass/fail; NEVER silently include a failing core.
    Skeleton: real implementation reads the core's released data table + metadata and checks each gate."""
    gates = CONFIG["inclusion_gates"]
    for gate, required in gates.items():
        if gate in ("on_ineligible", "min_samples_across_transition"):
            continue
        # observed = _check_gate(core, gate)  <-- wire to the core's deposited data
        observed = None  # UNIMPLEMENTED: screening reads DOI/accession data
        if observed is None:
            return GateResult(core["id"], False, gate, "UNIMPLEMENTED: screen against primary data deposit")
        if bool(observed) != bool(required):
            return GateResult(core["id"], False, gate, f"gate {gate} = {observed}, required {required}")
    return GateResult(core["id"], True, None, "eligible")


# ---------------------------------------------------------------------------
@dataclass
class ChangePoint:
    series: str            # "R1_richness" | "R2_ecto_share" | "R3_composition" | "negative_control"
    age_median: float      # calibrated yr BP / CE
    age_ci: tuple          # propagated from age-model posterior (N-1/H5)
    method_agreement: bool # bayesian vs PELT agree within tolerance


def detect_changepoint(series_values, ages, age_posteriors) -> ChangePoint:
    """Bayesian change-point + PELT cross-check, Monte-Carlo over the age-depth posterior.
    Skeleton only — no numerics here."""
    raise NotImplementedError("wire bayesian_changepoint + PELT; propagate age uncertainty")


def attribution(myco_cp: ChangePoint, human_cp: ChangePoint, climate_cp: ChangePoint) -> dict:
    """Primary estimand: does the mycorrhizal breakpoint align with HUMAN impact more than CLIMATE,
    beyond age-model error? Collinear human/climate proxies -> core cannot support H1 (flag)."""
    raise NotImplementedError("compute alignment deltas + collinearity guard; return per-core H1 evidence")


# ---------------------------------------------------------------------------
def classify_outcome(pool: list[dict]) -> str:
    """Mirror config.outcomes. H3 (negative control) is checked FIRST: if the method lights up where it
    must not, the run reports INSTRUMENT_FAILURE and makes no baseline claim either way."""
    # if any(core.negative_control_shows_anthropogenic_breakpoint for core in pool): return "INSTRUMENT_FAILURE"
    # if H1 and H2 and H4: return "SUPPORTED"
    # if (not H1) or H2_directionless or (not H4): return "REFUTED"
    raise NotImplementedError("evaluate H1..H4 over the random-effects meta-analysis; H3 gate first")


def emit_row(**kw) -> str:
    row = {"prereg_hash": prereg_hash(), "functional_layer": FUNCTIONAL_LAYER, **kw}
    return json.dumps(row, default=str)


# ---------------------------------------------------------------------------
def main() -> None:
    print(f"[paleo-baseline-erasure] prereg_hash={prereg_hash()}  functional_layer={FUNCTIONAL_LAYER}")
    eligible, excluded = [], []
    for core in CORES["candidate_cores"]:
        g = screen_core(core)
        (eligible if g.passed else excluded).append(g)
        print(emit_row(stage="screen", **asdict(g)))
    print(f"[paleo-baseline-erasure] eligible={len(eligible)} excluded={len(excluded)} "
          f"(excluded cores are part of the result, not discarded)")
    # For each eligible core: detect_changepoint on R1/R2/R3 + negative control, then attribution(...).
    # Meta-analyze (random effects), run the forgetting_test (H4), then classify_outcome(...).
    print("[paleo-baseline-erasure] SKELETON — analysis steps raise NotImplementedError by design.")
    print("[paleo-baseline-erasure] Freeze config.yaml + cores.yaml + this file, hash, then implement + run.")


if __name__ == "__main__":
    main()
