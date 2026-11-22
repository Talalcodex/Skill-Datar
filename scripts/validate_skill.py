#!/usr/bin/env python3
"""Validate a skill folder: frontmatter, referenced files, secrets, placeholders.
Usage: python validate_skill.py <skill-dir>
"""
import re, sys
from pathlib import Path

SECRET = re.compile(r"(sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{30,}|-----BEGIN [A-Z ]*PRIVATE KEY-----)")
PLACEHOLDER = re.compile(r"\b(TODO|TBD|FIXME|lorem ipsum)\b", re.I)


def report(results):
    width = max(len(n) for n, _, _ in results)
    for n, s, note in results:
        print(f"[{s}] {n.ljust(width)}  {note}")
    fails = sum(1 for _, s, _ in results if s == "FAIL")
    print(f"\n{len(results) - fails} passed, {fails} failed")
    return 1 if fails else 0


def main(root):
    root = Path(root)
    results = []

    def check(name, ok, note=""):
        results.append((name, "PASS" if ok else "FAIL", note))

    sk = root / "SKILL.md"
    check("SKILL.md exists", sk.is_file())
    if not sk.is_file():
        return report(results)
    text = sk.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    check("Frontmatter present", bool(m))
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip()
    name = fm.get("name", "")
    check("name valid (lowercase-hyphen)", bool(re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name)), name)
    check("name matches folder", name == root.resolve().name, f"{name} vs {root.resolve().name}")
    desc = fm.get("description", "")
    check("description present", len(desc) >= 40, f"{len(desc)} chars")
    check("description under 1024 chars", len(desc) <= 1024, f"{len(desc)} chars")
    lines = text.count("\n") + 1
    check("SKILL.md under 500 lines", lines <= 500, f"{lines} lines")

    refs = set(re.findall(r"`((?:references|templates|scripts|examples|tests|adapters)/[^`\s]+)`", text))
    for r in sorted(refs):
        if "<" in r:
            continue
        check(f"referenced file exists: {r}", (root / r).exists())

    bad_secret, bad_ph = [], []
    for f in root.rglob("*"):
        if f.is_file() and f.suffix in {".md", ".py", ".txt", ".json", ".yml", ".yaml"} and f.name != "validate_skill.py":
            t = f.read_text(encoding="utf-8", errors="ignore")
            if SECRET.search(t):
                bad_secret.append(str(f.relative_to(root)))
            if PLACEHOLDER.search(t):
                bad_ph.append(str(f.relative_to(root)))
    check("no secrets detected", not bad_secret, ", ".join(bad_secret))
    check("no TODO/TBD placeholders", not bad_ph, ", ".join(bad_ph))
    empty = [str(f.relative_to(root)) for f in root.rglob("*") if f.is_file() and f.stat().st_size == 0]
    check("no empty files", not empty, ", ".join(empty))
    return report(results)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: validate_skill.py <skill-dir>")
    sys.exit(main(sys.argv[1]))
