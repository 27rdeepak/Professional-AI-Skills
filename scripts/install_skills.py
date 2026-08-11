#!/usr/bin/env python3
"""Install the skills where Claude Code discovers them.

`skills/<category>/<name>/SKILL.md` is the canonical source. Claude Code loads
skills from a flat `<root>/skills/<name>/SKILL.md` layout, so this script
flattens the library into a `.claude/skills/` mount.

Usage:
  python3 scripts/install_skills.py            # mirror into ./.claude/skills (travels with the repo)
  python3 scripts/install_skills.py --global   # install into ~/.claude/skills (available in every project)
  python3 scripts/install_skills.py --check     # verify the repo mirror is in sync (no writes); exit 1 if not

Only SKILL.md is copied; OpenAI agent metadata stays in the source tree.
"""
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCES = sorted(ROOT.glob("skills/*/*/SKILL.md"))


def desired():
    """Map skill name -> SKILL.md text from the canonical source."""
    out = {}
    for src in SOURCES:
        out[src.parent.name] = src.read_text()
    return out


def check(dest_root):
    want = desired()
    have = {p.parent.name: p.read_text() for p in dest_root.glob("*/SKILL.md")}
    missing = sorted(set(want) - set(have))
    stale = sorted(set(have) - set(want))
    drifted = sorted(n for n in want if n in have and have[n] != want[n])
    if missing or stale or drifted:
        if missing: print(f"MISSING ({len(missing)}): {', '.join(missing)}")
        if stale:   print(f"STALE ({len(stale)}): {', '.join(stale)}")
        if drifted: print(f"DRIFTED ({len(drifted)}): {', '.join(drifted)}")
        print(f"\n{dest_root} is out of sync — run: python3 scripts/install_skills.py"
              + ("" if dest_root == ROOT / ".claude/skills" else f" (target {dest_root})"))
        return 1
    print(f"{dest_root}: in sync ({len(want)} skills).")
    return 0


def install(dest_root):
    want = desired()
    dest_root.mkdir(parents=True, exist_ok=True)
    written = 0
    for name, text in want.items():
        d = dest_root / name
        d.mkdir(exist_ok=True)
        (d / "SKILL.md").write_text(text)
        written += 1
    # Remove stale skill dirs this installer previously created.
    for p in dest_root.glob("*/SKILL.md"):
        if p.parent.name not in want:
            shutil.rmtree(p.parent)
            print(f"removed stale: {p.parent.name}")
    print(f"Installed {written} skills into {dest_root}")
    return 0


def main():
    args = sys.argv[1:]
    dest = Path.home() / ".claude/skills" if "--global" in args else ROOT / ".claude/skills"
    if "--check" in args:
        return check(dest)
    return install(dest)


if __name__ == "__main__":
    sys.exit(main())
