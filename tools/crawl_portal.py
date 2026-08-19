#!/usr/bin/env python3
"""Crawlt design.roteskreuz.at: alle internen Seiten, speichert HTML + Textextrakt."""
import re, sys, time, json, pathlib, urllib.request, urllib.parse
from html.parser import HTMLParser

BASE = "https://design.roteskreuz.at"
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "portal-scrape")
(OUT / "html").mkdir(parents=True, exist_ok=True)
(OUT / "text").mkdir(parents=True, exist_ok=True)

HDRS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36",
        "Accept-Language": "de-AT,de;q=0.9"}

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for k, v in attrs:
                if k == "href" and v: self.links.append(v)

BLOCK_TAGS = {"p","div","section","article","li","ul","ol","table","tr","br","header","footer","nav","figure","figcaption","blockquote"}
class TextParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.out=[]; self.skip=0; self.href=None
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag in ("script","style","noscript"): self.skip+=1
        elif tag in ("h1","h2","h3","h4","h5","h6"):
            self.out.append("\n\n"+"#"*int(tag[1])+" ")
        elif tag=="li": self.out.append("\n- ")
        elif tag in BLOCK_TAGS: self.out.append("\n")
        elif tag=="a" and a.get("href"): self.href=a["href"]
        elif tag=="img":
            alt=a.get("alt",""); src=a.get("src","")
            self.out.append(f" [BILD: {alt} | {src}] ")
        elif tag in ("td","th"): self.out.append(" | ")
    def handle_endtag(self, tag):
        if tag in ("script","style","noscript"): self.skip=max(0,self.skip-1)
        elif tag in ("h1","h2","h3","h4","h5","h6"): self.out.append("\n")
        elif tag=="a" and self.href:
            self.out.append(f" ({self.href})" if self.href.startswith(("http","/")) else "")
            self.href=None
    def handle_data(self, d):
        if not self.skip: self.out.append(d)

def norm(url):
    u = urllib.parse.urljoin(BASE + "/", url.split("#")[0].split("?")[0])
    return u.rstrip("/")

def is_page(u):
    if not u.startswith(BASE): return False
    path = u[len(BASE):]
    if re.search(r"\.(pdf|zip|png|jpe?g|svg|gif|mp[34]|wav|docx?|pptx?|xlsx?|potx|dotx|ase|eps|ai|indd|idml|otf|ttf|woff2?|ico|webp|css|js|xml|txt)$", path, re.I):
        return False
    if "/fileadmin/" in path or "/typo3" in path or "/@" in path: return False
    return True

def slug(u):
    p = u[len(BASE):].strip("/") or "startseite"
    return p.replace("/", "__")

seen, queue, pages, files = set(), [BASE], {}, set()
while queue:
    url = norm(queue.pop(0))
    if url in seen: continue
    seen.add(url)
    try:
        req = urllib.request.Request(url, headers=HDRS)
        with urllib.request.urlopen(req, timeout=20) as r:
            if "text/html" not in r.headers.get("Content-Type",""): continue
            html = r.read().decode("utf-8", "replace")
    except Exception as e:
        print(f"FEHLER {url}: {e}", flush=True); continue
    s = slug(url)
    (OUT/"html"/f"{s}.html").write_text(html)
    tp = TextParser(); tp.feed(html)
    text = re.sub(r"[ \t]+", " ", "".join(tp.out))
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    (OUT/"text"/f"{s}.md").write_text(f"<!-- Quelle: {url} | abgerufen {time.strftime('%Y-%m-%d')} -->\n\n{text}\n")
    pages[url] = s
    lp = LinkParser(); lp.feed(html)
    for l in lp.links:
        u2 = norm(l)
        if u2.startswith(BASE):
            if is_page(u2):
                if u2 not in seen: queue.append(u2)
            else:
                files.add(u2)
    print(f"OK  {url}", flush=True)
    time.sleep(0.4)

(OUT/"seiten-index.json").write_text(json.dumps(
    {"basis": BASE, "stand": time.strftime("%Y-%m-%d"), "seiten": pages,
     "dateilinks": sorted(files)}, ensure_ascii=False, indent=1))
print(f"\nFERTIG: {len(pages)} Seiten, {len(files)} Dateilinks -> {OUT}")
