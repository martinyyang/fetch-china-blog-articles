#!/usr/bin/env python3
"""Sync GitHub Issues -> Notion Fetch China kanban (read-only mirror)."""

from __future__ import annotations

import os
import re
import sys

import requests

NOTION_VERSION = "2022-06-28"
DATABASE_ID = os.environ.get("NOTION_DATABASE_ID", "62d957d4-c80e-4876-ac98-ce829461ef0b").replace("-", "")
TOKEN = os.environ.get("NOTION_TOKEN", "")
REPO = os.environ.get("GITHUB_REPOSITORY", "martinyyang/fetch-china-blog-articles")


def stage_from_issue(issue: dict) -> str:
    labels = {l["name"] for l in issue.get("labels", [])}
    if issue.get("state") == "closed":
        return "✅ 完成"
    if "status:blocked" in labels:
        return "⛔ 阻塞"
    if "status:in-progress" in labels:
        return "🔨 AI 实现中"
    if "ai:ready" in labels:
        return "▶️ 拖到这里→AI开工"
    return "📥 新 Issue"


def implementer_from_labels(labels: set[str]) -> str:
    if "ai:glm" in labels:
        return "GLM-5.3"
    if "ai:general" in labels:
        return "General agent"
    if "ai:composer" in labels:
        return "Composer (Cursor)"
    return "Unassigned"


def rich_text(s: str) -> dict:
    s = (s or "")[:2000]
    return {"rich_text": [{"type": "text", "text": {"content": s}}]}


def select(name: str) -> dict:
    return {"select": {"name": name}}


def find_page(session: requests.Session, issue_url: str) -> str | None:
    body = {
        "filter": {"property": "GitHub Issue", "url": {"equals": issue_url}},
        "page_size": 1,
    }
    r = session.post(f"https://api.notion.com/v1/databases/{DATABASE_ID}/query", json=body, timeout=60)
    r.raise_for_status()
    results = r.json().get("results") or []
    return results[0]["id"] if results else None


def parse_body_fields(body: str) -> tuple[str, str]:
    handoff = ""
    acceptance = ""
    if not body:
        return handoff, acceptance
    m = re.search(r"### Handoff[\s\S]*?\n([\s\S]*?)(\n### |\Z)", body)
    if m:
        handoff = m.group(1).strip()
    m = re.search(r"### Acceptance[\s\S]*?\n([\s\S]*?)(\n### |\Z)", body)
    if m:
        acceptance = m.group(1).strip()
    if not handoff and not acceptance:
        handoff = body[:1500]
    return handoff, acceptance


def upsert_issue(issue: dict) -> None:
    session = requests.Session()
    session.headers.update(
        {
            "Authorization": f"Bearer {TOKEN}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json",
        }
    )
    issue_url = issue["html_url"]
    labels = {l["name"] for l in issue.get("labels", [])}
    stage = stage_from_issue(issue)
    handoff, acceptance = parse_body_fields(issue.get("body") or "")

    props = {
        "Issue": {"title": [{"text": {"content": issue["title"][:200]}}]},
        "Stage": select(stage),
        "Implementer AI": select(implementer_from_labels(labels)),
        "GitHub Issue": {"url": issue_url},
        "Repo": select("fetch-china-blog-articles"),
        "Type": select("Issue"),
        "Dispatch log": rich_text(
            f"Synced from GitHub #{issue['number']} @ {issue.get('updated_at','')} | labels={sorted(labels)}"
        ),
    }
    if handoff:
        props["Handoff"] = rich_text(handoff)
    if acceptance:
        props["Acceptance"] = rich_text(acceptance)

    page_id = find_page(session, issue_url)
    if page_id:
        session.patch(f"https://api.notion.com/v1/pages/{page_id.replace('-','')}", json={"properties": props}, timeout=60).raise_for_status()
        print(f"updated notion for issue #{issue['number']}")
    else:
        session.post(
            "https://api.notion.com/v1/pages",
            json={"parent": {"database_id": DATABASE_ID}, "properties": props},
            timeout=60,
        ).raise_for_status()
        print(f"created notion for issue #{issue['number']}")


def main() -> None:
    if not TOKEN:
        print("NOTION_TOKEN not set", file=sys.stderr)
        sys.exit(1)
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if event_path and os.path.isfile(event_path):
        import json

        with open(event_path, encoding="utf-8") as f:
            payload = json.load(f)
        issue = payload.get("issue")
        if issue:
            upsert_issue(issue)
            return
    # scheduled/manual: sync all open issues
    gh_token = os.environ.get("GITHUB_TOKEN")
    if not gh_token:
        print("No event issue and no GITHUB_TOKEN for full sync", file=sys.stderr)
        sys.exit(0)
    r = requests.get(
        f"https://api.github.com/repos/{REPO}/issues",
        headers={"Authorization": f"Bearer {gh_token}", "Accept": "application/vnd.github+json"},
        params={"state": "all", "per_page": 100},
        timeout=60,
    )
    r.raise_for_status()
    for item in r.json():
        if "pull_request" in item:
            continue
        upsert_issue(item)


if __name__ == "__main__":
    main()
