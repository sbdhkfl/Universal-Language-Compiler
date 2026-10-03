"""Browser interface for the Universal Language Compiler."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import html, json, webbrowser
from urllib.parse import parse_qs, urlparse
from core.translator import translate
from targets import NAMES

HOST, PORT = "127.0.0.1", 8765

PAGE = """<!doctype html><html><head><meta charset="utf-8"><title>Universal Language Compiler</title>
<style>body{font-family:Arial;max-width:950px;margin:40px auto;padding:0 20px;background:#f5f7fb}textarea,select,button{font:inherit}textarea{width:100%;height:170px;padding:12px}select,button{padding:11px;margin-top:10px}button{cursor:pointer}pre{background:#111;color:#eee;padding:18px;overflow:auto;border-radius:8px}.card{background:white;padding:24px;border-radius:14px;box-shadow:0 2px 12px #0001}h1{margin-top:0}.error{color:#b00020}</style></head>
<body><div class="card"><h1>Universal Language Compiler</h1><p>Tell it what you want to build, then choose the language.</p>
<form method="post"><textarea name="text" placeholder="Example: make a program that prints Hello World"></textarea><br>
<select name="target">TARGETS</select><br><button>GENERATE CODE</button></form>RESULT</div></body></html>"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.respond(render("", "python", ""))
    def do_POST(self):
        n=int(self.headers.get("Content-Length","0")); data=parse_qs(self.rfile.read(n).decode())
        text=data.get("text",[""])[0].strip(); target=data.get("target",["python"])[0]
        result=""
        if text:
            try: result=translate(text,target)
            except Exception as e: result='<div class="error"><b>Could not generate code:</b> '+html.escape(str(e))+'</div>'
        self.respond(render(text,target,result))
    def respond(self,body):
        raw=body.encode(); self.send_response(200); self.send_header("Content-Type","text/html; charset=utf-8"); self.send_header("Content-Length",str(len(raw))); self.end_headers(); self.wfile.write(raw)

def render(text,target,result):
    opts="".join(f'<option value="{html.escape(k)}" {"selected" if k==target else ""}>{html.escape(k)}</option>' for k in sorted(set(NAMES)))
    result_html=f"<h2>Generated code</h2><pre>{html.escape(result)}</pre>" if result and not result.startswith("<div") else result
    return PAGE.replace("TARGETS",opts).replace('name="text" placeholder="Example: make a program that prints Hello World"></textarea>',f'name="text" placeholder="Example: make a program that prints Hello World">{html.escape(text)}</textarea>').replace("RESULT",result_html)

if __name__ == "__main__":
    server=ThreadingHTTPServer((HOST,PORT),Handler)
    url=f"http://{HOST}:{PORT}"
    print(f"Universal Language Compiler: {url}")
    webbrowser.open(url)
    try: server.serve_forever()
    except KeyboardInterrupt: pass
    finally: server.server_close()
