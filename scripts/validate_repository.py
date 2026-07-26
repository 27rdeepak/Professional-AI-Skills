#!/usr/bin/env python3
from pathlib import Path
import re,sys
R=Path(__file__).resolve().parents[1]; errors=[]
for x in ["README.md","LICENSE","CHANGELOG.md","ROADMAP.md","CONTRIBUTING.md","CODE_OF_CONDUCT.md","SECURITY.md","docs/style-guide.md","docs/skill-specification.md"]:
 if not (R/x).exists(): errors.append(f"missing {x}")
files=sorted((R/"skills").glob("*/*/SKILL.md")); names=set()
for f in files:
 t=f.read_text();m=re.match(r"^---\n(.*?)\n---\n",t,re.S)
 if not m: errors.append(f"{f}: invalid frontmatter");continue
 lines=[x for x in m.group(1).splitlines() if x.strip()]; keys=[x.split(":",1)[0] for x in lines if ":" in x]
 vals=dict(x.split(":",1) for x in lines if ":" in x); name=vals.get("name","").strip(); desc=vals.get("description","")
 if keys!=["name","description"]: errors.append(f"{f}: frontmatter keys")
 if name!=f.parent.name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*",name): errors.append(f"{f}: invalid name")
 if name in names: errors.append(f"duplicate {name}")
 names.add(name)
 if len(desc)<80 or "Use when" not in desc: errors.append(f"{f}: weak description")
 a=f.parent/"agents/openai.yaml"
 if not a.exists() or f"${name}" not in a.read_text(): errors.append(f"{f}: invalid agent metadata")
 if len(t.splitlines())>500: errors.append(f"{f}: too long")
if len(files)!=20: errors.append(f"expected 20 skills, found {len(files)}")
if errors: print("\n".join("ERROR: "+x for x in errors));sys.exit(1)
print(f"Validated {len(files)} skills and repository foundation.")
