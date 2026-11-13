import sys, re, html, subprocess, pathlib
src, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
b = src.read_bytes()
if b[:4] == b'%PDF':
    t = subprocess.run(['pdftotext','-layout',str(src),'-'],capture_output=True,text=True).stdout
else:
    s = b.decode('utf-8','replace')
    s = re.sub(r'(?is)<(script|style|noscript|svg|head|nav|footer|header)[^>]*>.*?</\1>',' ',s)
    s = re.sub(r'(?s)<[^>]+>',' ',s)
    t = html.unescape(s)
t = re.sub(r'[ \t\r\f\v]+',' ',t)
out.write_text(t)
print(f"{src.name:22s} {len(t.split()):7d} words")
