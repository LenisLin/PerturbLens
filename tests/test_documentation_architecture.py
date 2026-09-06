from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = REPO_ROOT / "docs"
DOMAINS = {
    "tasks",
    "data",
    "metrics",
    "visualization",
    "manuscript",
    "governance",
    "history",
}
RETIRED_REFERENCE = re.compile(
    r"docs/(?:contracts/|plotting/|redesign_checkpoint\.md|data_contracts\.md|"
    r"manuscript_master\.md|tmp_stage_planning_freeze\.md|"
    r"governance/(?:repo_conventions|local_storage_policy|team-and-governance)\.md)"
)


def active_documents() -> list[Path]:
    documents = [
        document
        for document in DOCS_ROOT.rglob("*.md")
        if document.relative_to(DOCS_ROOT).parts[0] != "history"
    ]
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


def test_active_documents_do_not_reference_retired_contract_paths() -> None:
    stale = [
        str(document.relative_to(REPO_ROOT))
        for document in active_documents()
        if RETIRED_REFERENCE.search(document.read_text(encoding="utf-8"))
    ]
    assert not stale, f"Retired contract references remain in: {stale}"


def test_local_markdown_links_resolve() -> None:
    missing = []
    documents = active_documents() + list((DOCS_ROOT / "history").rglob("*.md"))
    for document in documents:
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


def test_fm_document_preserves_machine_readable_active_families() -> None:
    contract = (DOCS_ROOT / "data" / "representations" / "fm.md").read_text(encoding="utf-8")
    active_section = contract.split("## Active FM Families\n", 1)[1].split("\n## ", 1)[0]
    families = [
        line[2:].strip().strip("`") for line in active_section.splitlines() if line.startswith("- ")
    ]
    assert families == [
        "scgpt",
        "geneformer",
        "scbert",
        "scfoundation",
        "uce",
        "state",
        "tahoe-x1",
    ]
