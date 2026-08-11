#!/usr/bin/env python3
"""Forward-test runner for skills.

Turns the prose rubric in evaluations/forward-tests.md into executable,
deterministic checks. Each skill is scored against the contract every
production skill must satisfy: a correct trigger, a real workflow, a
bounded output, a worked example, safe uncertainty handling, and resolving
cross-links. Runs without a model; complements scripts/validate_repository.py
(structure/frontmatter) with quality-contract enforcement.

Exit 1 if any skill fails a hard check.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = sorted(ROOT.glob("skills/*/*/SKILL.md"))
NAMES = {p.parent.name for p in SKILLS}

GENERIC_DESC = "needs a structured, evidence-aware judgment in this domain"
PLACEHOLDER_EXAMPLE = "to analyze this material"
WORKFLOW_STUB = re.compile(r"combine with", re.I)


def section(text, title):
    """Return the body of a `## <title>` section, or None if absent."""
    m = re.search(rf"^## {re.escape(title)}\s*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    return m.group(1).strip() if m else None


def frontmatter_desc(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return ""
    for line in m.group(1).splitlines():
        if line.startswith("description:"):
            return line.split(":", 1)[1].strip()
    return ""


def check_skill(path):
    """Return a list of (check_id, message) failures for one skill."""
    name = path.parent.name
    text = path.read_text()
    desc = frontmatter_desc(text)
    fails = []

    # C1 — correct trigger: concrete, discoverable, single clean sentence set
    if len(desc) < 80:
        fails.append(("trigger", "description under 80 chars"))
    elif "Use when" not in desc:
        fails.append(("trigger", "description lacks 'Use when' trigger language"))
    elif GENERIC_DESC in desc:
        fails.append(("trigger", "generic boilerplate description (no concrete triggers)"))
    elif "|" in desc:
        fails.append(("trigger", "pipe-delimited description (workflow crammed into triggers)"))

    # C2 — clear workflow: real, multi-step, not a cross-link stub
    wf = section(text, "Workflow")
    if wf is None:
        fails.append(("workflow", "missing ## Workflow section"))
    else:
        steps = [s for s in re.findall(r"^\s*\d+\.\s+(.*)$", wf, re.M) if s.strip()]
        if len(steps) < 3:
            fails.append(("workflow", f"workflow has {len(steps)} step(s); need >= 3"))
        elif any(WORKFLOW_STUB.search(s) for s in steps):
            fails.append(("workflow", "workflow is a 'Combine with ...' stub, not a procedure"))
        elif any(len(s.strip()) < 15 for s in steps):
            fails.append(("workflow", "a workflow step is too short to be actionable"))

    # C3 — bounded output: a named artifact or an explicit output contract list
    out = section(text, "Output")
    if out is None:
        fails.append(("output", "missing ## Output section"))
    else:
        has_artifact = re.search(r"\*\*[^*]+\*\*", out)
        list_items = re.findall(r"^\s*(?:\d+\.|[-*])\s+\S", out, re.M)
        if not has_artifact and len(list_items) < 3:
            fails.append(("output", "no named artifact and no output-contract list"))
    if len(text.splitlines()) > 500:
        fails.append(("output", "SKILL.md exceeds 500 lines"))

    # C4 — representative example: present and not a placeholder
    ex = section(text, "Example")
    if ex is None:
        fails.append(("example", "missing ## Example section"))
    elif PLACEHOLDER_EXAMPLE in ex:
        fails.append(("example", "placeholder example ('analyze this material')"))
    elif len(ex) < 60:
        fails.append(("example", "example too thin to be worked"))

    # C5 — safe uncertainty handling: a named failure-modes / failure-recovery section
    if section(text, "Failure modes") is None and section(text, "Failure recovery") is None:
        fails.append(("uncertainty", "missing ## Failure modes / ## Failure recovery"))

    # C6 — cross-links resolve and are not self-referential
    rel = section(text, "Related skills")
    if rel:
        refs = set(re.findall(r"`([a-z0-9][a-z0-9-]*)`", rel))
        broken = sorted(r for r in refs if r not in NAMES)
        if broken:
            fails.append(("links", f"related-skills link(s) do not resolve: {', '.join(broken)}"))
        if name in refs:
            fails.append(("links", "related-skills lists the skill itself"))

    # C7 — agent metadata present and wired to the skill name
    agent = path.parent / "agents/openai.yaml"
    if not agent.exists():
        fails.append(("agent", "missing agents/openai.yaml"))
    elif f"${name}" not in agent.read_text():
        fails.append(("agent", f"agents/openai.yaml does not reference ${name}"))

    return fails


def check_regression_suite():
    """Every $skill referenced in the regression suite must exist."""
    suite = ROOT / "tests/regression-suite.md"
    if not suite.exists():
        return [("regression-suite", "tests/regression-suite.md missing")]
    refs = set(re.findall(r"\$([a-z0-9][a-z0-9-]*)", suite.read_text()))
    return [("regression-suite", f"references unknown skill ${r}")
            for r in sorted(refs) if r not in NAMES]


def check_mirror():
    """The committed .claude/skills mount must match the canonical source."""
    mount = ROOT / ".claude/skills"
    if not mount.exists():
        return []  # no committed mirror; nothing to enforce
    want = {p.parent.name: p.read_text() for p in SKILLS}
    have = {p.parent.name: p.read_text() for p in mount.glob("*/SKILL.md")}
    fails = []
    for n in sorted(set(want) - set(have)):
        fails.append(("mirror", f".claude/skills missing {n} (run scripts/install_skills.py)"))
    for n in sorted(set(have) - set(want)):
        fails.append(("mirror", f".claude/skills has stale {n} (run scripts/install_skills.py)"))
    for n in sorted(n for n in want if n in have and want[n] != have[n]):
        fails.append(("mirror", f".claude/skills/{n} drifted from source (run scripts/install_skills.py)"))
    return fails


def check_site():
    """The committed catalog page must match what build_site would generate."""
    page = ROOT / "docs/index.html"
    if not page.exists():
        return []
    sys.path.insert(0, str(ROOT / "scripts"))
    try:
        import build_site
    except Exception as e:  # pragma: no cover
        return [("site", f"could not import build_site: {e}")]
    if build_site.render() != page.read_text():
        return [("site", "docs/index.html is stale (run scripts/build_site.py)")]
    return []


def main():
    by_check = {}
    failing_skills = 0
    for path in SKILLS:
        fails = check_skill(path)
        if fails:
            failing_skills += 1
        for cid, msg in fails:
            by_check.setdefault(cid, []).append(f"{path.parent.name}: {msg}")

    for cid, msg in check_regression_suite() + check_mirror() + check_site():
        by_check.setdefault(cid, []).append(msg)

    total = sum(len(v) for v in by_check.values())
    order = ["trigger", "workflow", "output", "example", "uncertainty",
             "links", "agent", "regression-suite", "mirror", "site"]
    for cid in sorted(by_check, key=lambda c: order.index(c) if c in order else 99):
        items = by_check[cid]
        print(f"\n[{cid}] {len(items)} failure(s):")
        for line in items[:25]:
            print(f"  - {line}")
        if len(items) > 25:
            print(f"  ... and {len(items) - 25} more")

    print("\n" + "=" * 60)
    passed = len(SKILLS) - failing_skills
    print(f"{passed}/{len(SKILLS)} skills pass all checks; "
          f"{total} failure(s) across {len(by_check)} check type(s).")
    if total:
        print("FAIL")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
