from io import StringIO
from pathlib import Path

import nox

_PROJECT_ROOT: Path = Path(__file__).parent.resolve()

# Coverage
_COVERAGE_FILE: Path = (_PROJECT_ROOT / "coverage").resolve()
_CODE_FILES: Path = (_PROJECT_ROOT / "tlab").resolve()
_MIN_COVERAGE_PRECENT: int = 90

# Ruff
_RUFF_CONFIG_FILE: Path = (_PROJECT_ROOT / "ruff.toml").resolve()
_RUFF_OUTPUT_FORMAT: str = "grouped"
_RUFF_OUTPUT_FILE: Path = (_PROJECT_ROOT / "lint_output.txt").resolve()


nox.options.default_venv_backend = "none"
nox.options.reuse_existing_virtualenvs = True


@nox.session(tags=["test", "ci"])
def test(
    session: nox.Session,
) -> None:
    junit_file: Path = _PROJECT_ROOT / "junit.xml"
    session.run(
        "coverage",
        "run",
        f"--data-file={_COVERAGE_FILE!s}",
        f"--source={_CODE_FILES!s}",
        "-m",
        "pytest",
        f"{_PROJECT_ROOT!s}",
        "--full-trace",
        "--showlocals",
        "--show-capture=all",
        f"--junit-xml={junit_file!s}",
    )


@nox.session(tags=["test", "ci"])
def coverage(
    session: nox.Session,
) -> None:
    html_dir: Path = (_PROJECT_ROOT / "html_cov").resolve()
    xml_cov: Path = (_PROJECT_ROOT / "coverage.xml").resolve()

    session.run(
        "coverage",
        "html",
        f"--directory={html_dir!s}",
        f"--title={_PROJECT_ROOT.stem!s}",
        f"--data-file={_COVERAGE_FILE!s}",
    )
    session.run(
        "coverage",
        "xml",
        "-o",
        f"{xml_cov!s}",
        f"--data-file={_COVERAGE_FILE!s}",
    )
    session.run(
        "coverage",
        "report",
        f"--data-file={_COVERAGE_FILE!s}",
        f"--fail-under={_MIN_COVERAGE_PRECENT!s}",
    )


@nox.session(tags=["lint", "ci"])
def lint(
    session: nox.Session,
) -> None:
    session.run(
        "ruff",
        "check",
        f"{_PROJECT_ROOT!s}",
        f"--config={_RUFF_CONFIG_FILE!s}",
        f"--output-format={_RUFF_OUTPUT_FORMAT!s}",
        f"--output-file={_RUFF_OUTPUT_FILE!s}",
    )


@nox.session(tags=["lint", "ci"])
def check_format(
    session: nox.Session,
) -> None:
    format_output_file: Path = (_PROJECT_ROOT / "format_output.txt").resolve()
    with format_output_file.open(mode="w", encoding="UTF8") as output_file:
        session.run(
            "ruff",
            "format",
            f"--config={_RUFF_CONFIG_FILE!s}",
            "--check",
            "--diff",
            f"{_PROJECT_ROOT!s}",
            stdout=output_file,
        )
