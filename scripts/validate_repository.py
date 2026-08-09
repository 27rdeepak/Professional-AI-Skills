#!/usr/bin/env python3
from pathlib import Path
import re,sys
R=Path(__file__).resolve().parents[1]; errors=[]; warnings=[]
# Quality-lint signatures: these pass structural checks but signal shallow, templated skills.
GENERIC_DESC="needs a structured, evidence-aware judgment in this domain"
PLACEHOLDER_EXAMPLE="to analyze this material"
GENERIC_EXAMPLE="Apply the workflow, expose evidence gaps, and deliver the default output"
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
 # Non-fatal quality lint (surfaces templated content the structural checks miss)
 if GENERIC_DESC in desc: warnings.append(f"{f}: generic boilerplate description (no concrete triggers)")
 if PLACEHOLDER_EXAMPLE in t or GENERIC_EXAMPLE in t: warnings.append(f"{f}: placeholder example")
 if re.search(rf"`{re.escape(name)}`\s+for\b", t): warnings.append(f"{f}: related-skills lists itself")
if len(files)<20: errors.append(f"expected at least 20 skills, found {len(files)}")
for required in ["skills/enterprise-it","skills/microsoft365","skills/cybersecurity","skills/business","skills/leadership","frameworks","templates","personas","playbooks","evaluations","platform"]:
 if not (R/required).exists(): errors.append(f"missing {required}")
if errors: print("\n".join("ERROR: "+x for x in errors));sys.exit(1)
if warnings:
 print(f"QUALITY WARNINGS ({len(warnings)}) — structurally valid but templated, prioritize for rewrite:")
 print("\n".join("  WARN: "+x for x in warnings))
print(f"Validated {len(files)} skills and repository foundation.")
