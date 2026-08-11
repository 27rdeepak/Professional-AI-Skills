#!/usr/bin/env python3
"""Generate a searchable catalog site (docs/index.html) from the skills.

Self-contained single page: inline CSS + JS, no external requests. Serve it
with GitHub Pages (Settings -> Pages -> Deploy from a branch -> main -> /docs).
Each skill links to its SKILL.md on GitHub so links work even off Pages.
"""
from pathlib import Path
import html
import re

ROOT = Path(__file__).resolve().parents[1]
REPO = "27rdeepak/Professional-AI-Skills"
BRANCH = "main"
BLOB = f"https://github.com/{REPO}/blob/{BRANCH}"

TITLES = {
    "core": "Core reasoning", "business": "Business & strategy",
    "communication": "Communication", "cybersecurity": "Cybersecurity",
    "enterprise-it": "Enterprise IT", "microsoft365": "Microsoft 365",
    "leadership": "Leadership", "research": "Research",
    "software-engineering": "Software engineering", "productivity": "Productivity",
    "ai-product": "AI product",
}


def load():
    by_cat = {}
    for f in sorted(ROOT.glob("skills/*/*/SKILL.md")):
        cat, name = f.parent.parent.name, f.parent.name
        m = re.match(r"^---\n(.*?)\n---\n", f.read_text(), re.S)
        desc = ""
        if m:
            for line in m.group(1).splitlines():
                if line.startswith("description:"):
                    desc = line.split(":", 1)[1].strip()
        by_cat.setdefault(cat, []).append((name, desc))
    return by_cat


def render():
    by_cat = load()
    total = sum(len(v) for v in by_cat.values())
    cats = sorted(by_cat, key=lambda c: TITLES.get(c, c).lower())
    sections = []
    for c in cats:
        cards = []
        for name, desc in sorted(by_cat[c]):
            url = f"{BLOB}/skills/{c}/{name}/SKILL.md"
            cards.append(
                f'<a class="card" href="{url}" data-text="{html.escape((name+" "+desc+" "+TITLES.get(c,c)).lower())}">'
                f'<h3>{html.escape(name)}</h3><p>{html.escape(desc)}</p>'
                f'<span class="dom">{html.escape(TITLES.get(c,c))}</span></a>'
            )
        sections.append(
            f'<section class="group" data-cat="{c}"><h2>{html.escape(TITLES.get(c,c))} '
            f'<span class="n">{len(by_cat[c])}</span></h2><div class="grid">{"".join(cards)}</div></section>'
        )
    return TEMPLATE.replace("{{TOTAL}}", str(total)).replace("{{SECTIONS}}", "\n".join(sections))


TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Professional AI Skills — Catalog</title>
<style>
:root{--bg:#fff;--fg:#111;--muted:#606770;--card:#f6f8fa;--line:#e5e7eb;--accent:#2563eb}
@media (prefers-color-scheme:dark){:root{--bg:#0d1117;--fg:#e6edf3;--muted:#9198a1;--card:#161b22;--line:#30363d;--accent:#4d9fff}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.wrap{max-width:1040px;margin:0 auto;padding:32px 20px 80px}
header h1{font-size:2rem;margin:0 0 6px}
.tag{color:var(--muted);margin:0 0 20px;font-size:1.05rem}
.install{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px 14px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.9rem;overflow-x:auto;white-space:nowrap}
.controls{position:sticky;top:0;background:var(--bg);padding:16px 0;border-bottom:1px solid var(--line);margin:24px 0 8px;z-index:5}
#q{width:100%;padding:12px 14px;font-size:1rem;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--fg)}
#count{color:var(--muted);font-size:.9rem;margin-top:8px}
.group{margin:28px 0 8px}
.group h2{font-size:1.15rem;border-bottom:1px solid var(--line);padding-bottom:6px;display:flex;align-items:center;gap:8px}
.group h2 .n{color:var(--muted);font-weight:400;font-size:.85rem}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px;margin-top:14px}
.card{display:block;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px;text-decoration:none;color:inherit;transition:border-color .15s,transform .05s}
.card:hover{border-color:var(--accent);transform:translateY(-1px)}
.card h3{margin:0 0 6px;font-size:1rem;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--accent)}
.card p{margin:0 0 10px;font-size:.88rem;color:var(--fg)}
.card .dom{font-size:.72rem;color:var(--muted);text-transform:uppercase;letter-spacing:.04em}
footer{margin-top:48px;color:var(--muted);font-size:.85rem;text-align:center}
a.repo{color:var(--accent)}
.hidden{display:none!important}
</style>
</head>
<body>
<div class="wrap">
<header>
<h1>Professional AI Skills</h1>
<p class="tag">{{TOTAL}} professional AI skills — each tested against a quality contract. <a class="repo" href="https://github.com/27rdeepak/Professional-AI-Skills">View on GitHub →</a></p>
<div class="install">python3 scripts/install_skills.py --global&nbsp;&nbsp;# then /risk-analysis, /threat-modeling, …</div>
</header>
<div class="controls">
<input id="q" type="search" placeholder="Search {{TOTAL}} skills by name, description, or domain…" autocomplete="off" aria-label="Search skills">
<div id="count"></div>
</div>
<main id="list">
{{SECTIONS}}
</main>
<footer>Free &amp; open source under the MIT License. Click any skill to read its full SKILL.md.</footer>
</div>
<script>
var q=document.getElementById('q'),count=document.getElementById('count'),
cards=[].slice.call(document.querySelectorAll('.card')),
groups=[].slice.call(document.querySelectorAll('.group'));
function apply(){
  var t=q.value.trim().toLowerCase(),shown=0;
  cards.forEach(function(c){var m=!t||c.dataset.text.indexOf(t)>-1;c.classList.toggle('hidden',!m);if(m)shown++;});
  groups.forEach(function(g){var any=g.querySelectorAll('.card:not(.hidden)').length>0;g.classList.toggle('hidden',!any);});
  count.textContent=shown+' skill'+(shown===1?'':'s')+(t?' matching “'+t+'”':'');
}
q.addEventListener('input',apply);apply();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    (ROOT / "docs/index.html").write_text(render())
    print("Wrote docs/index.html")
