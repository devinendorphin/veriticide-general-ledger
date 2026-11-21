import json,re,sys
p='/root/.claude/projects/-home-user/b13d40cd-ab51-545a-a718-ce0a819d85c9.jsonl'
out=[]; cur=None
def flush():
    global cur
    if cur and cur['text'].strip():
        out.append(cur)
    cur=None
def strip_sr(t):
    return re.sub(r'<system-reminder>.*?</system-reminder>','',t,flags=re.S).strip()
for line in open(p):
    o=json.loads(line)
    t=o.get('type')
    if o.get('isSidechain'): continue
    if t=='user':
        if o.get('isMeta'): continue
        c=o['message'].get('content')
        if isinstance(c,list) and all(isinstance(b,dict) and b.get('type')=='tool_result' for b in c): continue
        if isinstance(c,str): txt=strip_sr(c)
        else: txt='\n\n'.join(strip_sr(b.get('text','')) for b in c if isinstance(b,dict) and b.get('type')=='text')
        txt=txt.strip()
        if not txt: continue
        flush()
        out.append({'role':'Human','ts':o['timestamp'],'text':txt,'notTyped':o.get('textNotTyped'),'idx':(o.get('turnPosition') or {}).get('promptIndex')})
    elif t=='assistant':
        for b in o['message'].get('content',[]):
            if isinstance(b,dict) and b.get('type')=='text' and b.get('text','').strip():
                if cur is None: cur={'role':'Claude','ts':o['timestamp'],'text':''}
                cur['text']+=(('\n\n') if cur['text'] else '')+b['text'].strip()
flush()
hum=[x for x in out if x['role']=='Human']
L=[]
L.append('# Session transcript, 2026-11-18 to 2026-11-21: "Controlled Alarm" and the suggested-prompt loop\n')
L.append('- **Source:** the session log written by the Claude Code client, `/root/.claude/projects/-home-user/b13d40cd-ab51-545a-a718-ce0a819d85c9.jsonl` (SHA-256 below). Extracted by script, not retyped.')
L.append('- **Included, verbatim:** every message the human sent, and every block of text Claude showed in reply, in order.')
L.append('- **Left out:** tool calls and their results, Claude\'s internal reasoning, system reminders injected by the client, and image attachments. Where Claude sent several text blocks within one reply, they appear together under one heading.')
L.append('- **Attachments:** messages 1 and 54 attached files (the video; the independent review). The mention of the file is kept; the file\'s contents are not reproduced.')
nt=[x['idx'] for x in hum if x.get('notTyped')]
L.append(f'- **The `textNotTyped` flag.** The client\'s log marks {len(nt)} of the {len(hum)} human messages `textNotTyped: true`: prompts {min(nt)}–{max(nt)}. Each of them reads "Run that through the lens of sycophancy to power." Prompt 4, the first message with that wording, carries no flag. Those 48 are marked **[not typed]** below. The flag is in the log the client writes; it did not reach Claude during the session.')
L.append('')
L.append('---\n')
for x in out:
    ts=x['ts'][:16].replace('T',' ')+' UTC'
    if x['role']=='Human':
        tag=' **[not typed]**' if x.get('notTyped') else ''
        L.append(f'### Human, prompt {x["idx"]} ({ts}){tag}\n')
    else:
        L.append(f'### Claude ({ts})\n')
    L.append(x['text'])
    L.append('')
open(sys.argv[1],'w').write('\n'.join(L))
print(len(out),len(hum),len(nt))
