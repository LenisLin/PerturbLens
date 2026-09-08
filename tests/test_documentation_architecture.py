from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = REPO_ROOT / "docs"
DOMAINS = {
    "research",
    "tasks",
    "data",
    "metrics",
    "visualization",
    "manuscript",
    "governance",
}


def active_documents() -> list[Path]:
    documents = list(DOCS_ROOT.rglob("*.md"))
    documents.extend([REPO_ROOT / "README.md", REPO_ROOT / "AGENTS.md", REPO_ROOT / "project.yaml"])
    documents.extend((REPO_ROOT / ".agents" / "skills").rglob("SKILL.md"))
    return sorted(documents)


def test_documentation_root_has_three_entries_and_seven_domains() -> None:
    assert {document.name for document in DOCS_ROOT.glob("*.md")} == {
        "README.md",
        "project.md",
        "roadmap.md",
    }
    assert {directory.name for directory in DOCS_ROOT.iterdir() if directory.is_dir()} == DOMAINS


def test_no_active_legacy_project_contracts() -> None:
    forbidden_paths = {
        DOCS_ROOT / "tasks" / "task1.md",
        DOCS_ROOT / "tasks" / "task2.md",
        DOCS_ROOT / "tasks" / "study_map.md",
        DOCS_ROOT / "data" / "snapshots" / "task1.md",
    }
    assert not any(path.exists() for path in forbidden_paths)

    stale_pattern = re.compile(r"\bM2M-Bench\b|docs/tasks/task[12]\.md|/ProjectData/M2M/")
    stale = [
        str(document.relative_to(REPO_ROOT))
        for document in active_documents()
        if stale_pattern.search(document.read_text(encoding="utf-8"))
    ]
    assert not stale, f"Legacy active references remain in: {stale}"


def test_local_markdown_links_resolve() -> None:
    missing = []
    for document in active_documents():
        content = re.sub(r"```.*?```", "", document.read_text(encoding="utf-8"), flags=re.S)
        for target in re.findall(r"!?\[[^\]]*\]\(([^\s)]+)\)", content):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            linked_path = document.parent / unquote(parsed.path)
            if not linked_path.exists():
                missing.append(f"{document.relative_to(REPO_ROOT)} -> {target}")
    assert not missing, "Missing documentation links:\n" + "\n".join(missing)


def test_code_formatted_documentation_paths_resolve() -> None:
    missing = []
    for document in active_documents():
        for target in re.findall(
            r"`(docs/[A-Za-z0-9_./-]+\.md)`", document.read_text(encoding="utf-8")
        ):
            if not (REPO_ROOT / target).is_file():
                missing.append(f"{document.relative_to(REPO_ROOT)} -> {target}")
    assert not missing, "Missing contract paths:\n" + "\n".join(missing)


def test_primary_fm_families_are_registered() -> None:
    contract = (DOCS_ROOT / "data" / "representations" / "fm.md").read_text(encoding="utf-8")
    for family in ["scgpt", "geneformer", "scbert", "scfoundation", "uce", "state", "tahoe-x1"]:
        assert f"`{family}`" in contract
