from __future__ import annotations

import ast
import re
import runpy
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_URL = "https://github.com/LenisLin/PerturbLens"


def test_package_and_project_identity_agree() -> None:
    project = yaml.safe_load((REPO_ROOT / "project.yaml").read_text(encoding="utf-8"))
    metadata = (REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8")
    project_section = metadata.split("[project]\n", 1)[1].split("\n[", 1)[0]
    fields = dict(re.findall(r'^([a-z_-]+) = "([^"]*)"$', project_section, flags=re.M))
    package = runpy.run_path(str(REPO_ROOT / "src" / "perturblens" / "__init__.py"))

    assert project["name"] == fields["name"] == "perturblens"
    assert project["title"] == "PerturbLens"
    assert fields["version"] == package["__version__"]
    assert project["repository"] == REPOSITORY_URL
    assert f'Repository = "{REPOSITORY_URL}"' in metadata
    assert REPOSITORY_URL in (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    assert 'include = ["perturblens*"]' in metadata


def test_repo_skills_have_discoverable_names() -> None:
    skill_root = REPO_ROOT / ".agents" / "skills"
    expected = {"perturblens-grounding", "perturblens-evidence", "perturblens-execution"}
    assert {path.name for path in skill_root.iterdir() if path.is_dir()} == expected
    for name in sorted(expected):
        content = (skill_root / name / "SKILL.md").read_text(encoding="utf-8")
        assert content.startswith("---\n"), f"Missing skill metadata: {name}"
        metadata = yaml.safe_load(content.split("---", 2)[1])
        assert metadata["name"] == name
        assert metadata["description"]


def test_retired_local_tasks_are_outside_active_entrypoints() -> None:
    assert not list((REPO_ROOT / "scripts").glob("task[12]*.py"))
    assert not list((REPO_ROOT / "tests").glob("test_task[12]*.py"))
    assert "/.local/" in (REPO_ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()


def test_extractor_interfaces_identify_legacy_status() -> None:
    extractor_root = REPO_ROOT / "scripts" / "fm_extractors"
    for path in sorted(extractor_root.glob("extract_*.py")):
        source = path.read_text(encoding="utf-8")
        description = ast.get_docstring(ast.parse(source))
        assert description is not None
        assert description.startswith("PerturbLens ")
        assert "legacy snapshot CLI" in description
        assert "not an R2-R6 runner" in source


def test_runtime_identity_uses_current_namespace() -> None:
    extractor_root = REPO_ROOT / "scripts" / "fm_extractors"
    state = (extractor_root / "extract_state.py").read_text(encoding="utf-8")
    foundation = (extractor_root / "extract_scfoundation.py").read_text(encoding="utf-8")
    assert 'os.environ["PERTURBLENS_STATE_PYTHON"]' in state
    assert 'f"perturblens_{MODEL_NAME}_' in foundation
    for path in sorted(extractor_root.glob("*.py")):
        assert not re.search(r"\bM2M_|\bm2m_", path.read_text(encoding="utf-8"))
