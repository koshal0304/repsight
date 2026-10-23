"""E0-T01: the workspace skeleton matches the playbook (05 §4.1, §4.4, §4.5)."""

import json
import re
import subprocess
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PLAYBOOK = (ROOT / "docs/05-build-playbook.md").read_text()
PACKAGE = json.loads((ROOT / "package.json").read_text())


def section(number: str) -> str:
    """Playbook text from the `### <number> ` heading to the next `### ` heading."""
    start = PLAYBOOK.index(f"\n### {number} ")
    return PLAYBOOK[start : PLAYBOOK.index("\n### ", start + 1)]


def test_nfr_038_toolchain_pins_are_exact() -> None:
    uv = tomllib.loads((ROOT / "pyproject.toml").read_text())["tool"]["uv"]
    assert re.fullmatch(r"pnpm@\d+\.\d+\.\d+\+sha512\.[0-9a-f]{128}", PACKAGE["packageManager"])
    assert re.fullmatch(r"==\d+\.\d+\.\d+", uv["required-version"])
    # Canon §10.2 and 05 §4.1 pins; changing them needs an ADR.
    assert (ROOT / ".python-version").read_text().strip() == "3.14.8"
    assert PACKAGE["engines"]["node"] == "22.13.x"
    assert (ROOT / ".nvmrc").read_text().startswith("22.13.")


def test_nfr_038_npm_dependencies_are_pinned_exactly() -> None:
    # Same globs as pnpm-workspace.yaml, so node_modules is never scanned.
    workspace = [*ROOT.glob("apps/*/package.json"), *ROOT.glob("packages/*/package.json")]
    loose = [
        f"{path.relative_to(ROOT)}: {name}@{spec}"
        for path in [ROOT / "package.json", *workspace]
        for field in ("dependencies", "devDependencies", "optionalDependencies")
        for name, spec in json.loads(path.read_text()).get(field, {}).items()
        if spec != "workspace:*" and not re.fullmatch(r"\d+\.\d+\.\d+(-[0-9A-Za-z.-]+)?", spec)
    ]
    assert loose == []


def test_env_example_defines_every_playbook_variable() -> None:
    name_cells = [row.split("|")[1] for row in section("4.5").splitlines() if row.startswith("| `")]
    expected = {name for cell in name_cells for name in re.findall(r"`([A-Z][A-Z0-9_]+)`", cell)}
    defined = set(re.findall(r"^([A-Z][A-Z0-9_]+)=", (ROOT / ".env.example").read_text(), re.M))
    assert expected, "no variables parsed from 05 §4.5"
    assert expected - defined == set()


def test_root_scripts_cover_playbook_bootstrap_commands() -> None:
    commands = "\n".join(line.split("#")[0] for line in section("4.4").splitlines())
    expected = set(re.findall(r"\bpnpm ([a-z][a-z:]*)", commands)) - {"install"}
    assert expected, "no pnpm commands parsed from 05 §4.4"
    assert expected - set(PACKAGE["scripts"]) == set()


def test_gr_12_env_file_is_git_ignored() -> None:
    assert subprocess.run(["git", "check-ignore", "-q", ".env"], cwd=ROOT).returncode == 0
