#!/usr/bin/env python3
"""Thread hygiene scanner.

Parses YAML frontmatter from all .plans~/ threads and .agent/thread-registry.md.
Outputs a JSON report of threads needing attention (stale, abandoned, orphaned, over budget).

Usage:
    python3 .github/scripts/thread-hygiene.py [--max-active 10] [--stale-days 14] [--abandon-days 28]

Exit codes:
    0 = clean or report-only issues
    1 = actions required
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import date, timedelta
from pathlib import Path

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)
YAML_LINE_RE = re.compile(r'^(\w[\w-]*):\s*"?([^"\n]*)"?\s*$')

ACTIVE_STATUSES = {"active", "blocked"}
CLOSEABLE_STATUSES = {"stale", "good-enough"}


def parse_frontmatter(path: Path) -> dict | None:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return None
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        lm = YAML_LINE_RE.match(line.strip())
        if lm:
            fm[lm.group(1)] = lm.group(2).strip()
    fm["_path"] = str(path)
    return fm


def parse_date(s: str) -> date | None:
    try:
        return date.fromisoformat(s)
    except Exception:
        return None


def find_threads(root: Path) -> list[dict]:
    threads = []
    for pattern in ["**/.plans~/**/*.md", "PLANS~/**/*.md"]:
        for p in root.glob(pattern):
            if p.name.startswith("."):
                continue
            fm = parse_frontmatter(p)
            if fm and fm.get("thread-id"):
                threads.append(fm)
    return threads


def scan(root: Path, max_active: int, stale_days: int, abandon_days: int) -> dict:
    today = date.today()
    threads = find_threads(root)
    issues = []
    active_count = 0

    for t in threads:
        tid = t.get("thread-id", t["_path"])
        status = t.get("status", "unknown")
        updated = parse_date(t.get("updated", ""))
        age = (today - updated).days if updated else None

        if status in ACTIVE_STATUSES:
            active_count += 1

        # Stale detection: active/blocked but not updated within stale_days
        if status in ACTIVE_STATUSES and age is not None and age > stale_days:
            issues.append({
                "thread": tid,
                "path": t["_path"],
                "issue": "stale",
                "action": "set_stale",
                "detail": f"Status '{status}' but not updated in {age} days (threshold: {stale_days})",
            })

        # Abandon detection: already stale/good-enough and not updated within abandon_days
        if status in CLOSEABLE_STATUSES and age is not None and age > abandon_days:
            issues.append({
                "thread": tid,
                "path": t["_path"],
                "issue": "abandoned",
                "action": "close",
                "detail": f"Status '{status}' and not updated in {age} days (threshold: {abandon_days})",
            })

        # Missing frontmatter fields
        missing = [f for f in ("parent", "status", "updated", "thread-id") if not t.get(f)]
        if missing:
            issues.append({
                "thread": tid,
                "path": t["_path"],
                "issue": "incomplete_frontmatter",
                "action": "fix_frontmatter",
                "detail": f"Missing: {', '.join(missing)}",
            })

    # Budget check
    budget_issue = None
    if active_count > max_active:
        budget_issue = {
            "issue": "over_budget",
            "active_count": active_count,
            "max_active": max_active,
            "detail": f"{active_count} active threads exceeds budget of {max_active}",
        }

    return {
        "date": today.isoformat(),
        "total_threads": len(threads),
        "active_threads": active_count,
        "max_active": max_active,
        "issues": issues,
        "budget": budget_issue,
    }


def main():
    parser = argparse.ArgumentParser(description="Thread hygiene scanner")
    parser.add_argument("--max-active", type=int, default=10)
    parser.add_argument("--stale-days", type=int, default=14)
    parser.add_argument("--abandon-days", type=int, default=28)
    parser.add_argument("--root", type=str, default=".")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    report = scan(root, args.max_active, args.stale_days, args.abandon_days)
    print(json.dumps(report, indent=2))
    sys.exit(1 if report["issues"] or report["budget"] else 0)


if __name__ == "__main__":
    main()
