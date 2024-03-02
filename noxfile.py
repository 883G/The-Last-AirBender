from collections.abc import Collection
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


def get_python_prefix() -> Collection[str]:
    return ["python", "-m"]


@nox.session(tags=["test", "ci"])
def test(
    session: nox.Session,
) -> None:
    session.debug("Running The tests.")
    junit_file: Path = _PROJECT_ROOT / "junit.xml"
    session.run(
        # Added python -m as it did problems on windows.
        *get_python_prefix(),
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
        "-n",
        "auto",
        f"--junit-xml={junit_file!s}",
    )
    session.debug("Ran The tests.")


@nox.session(tags=["test", "ci"])
def coverage(
    session: nox.Session,
) -> None:
    session.debug("Creating coverage report.")
    html_dir: Path = (_PROJECT_ROOT / "html_cov").resolve()
    xml_cov: Path = (_PROJECT_ROOT / "coverage.xml").resolve()

    session.run(
        # Added python -m as it did problems on windows.
        *get_python_prefix(),
        "coverage",
        "html",
        f"--directory={html_dir!s}",
        f"--title={_PROJECT_ROOT.stem!s}",
        f"--data-file={_COVERAGE_FILE!s}",
    )
    session.run(
        # Added python -m as it did problems on windows.
        *get_python_prefix(),
        "coverage",
        "xml",
        "-o",
        f"{xml_cov!s}",
        f"--data-file={_COVERAGE_FILE!s}",
    )
    session.run(
        # Added python -m as it did problems on windows.
        *get_python_prefix(),
        "coverage",
        "report",
        f"--data-file={_COVERAGE_FILE!s}",
        f"--fail-under={_MIN_COVERAGE_PRECENT!s}",
    )
    session.debug("Finished creating coverage report.")


@nox.session(tags=["lint", "ci"])
def lint(
    session: nox.Session,
) -> None:
    session.debug("Linting the code with Ruff.")
    session.run(
        "ruff",
        "check",
        f"{_PROJECT_ROOT!s}",
        f"--config={_RUFF_CONFIG_FILE!s}",
        f"--output-format={_RUFF_OUTPUT_FORMAT!s}",
        f"--output-file={_RUFF_OUTPUT_FILE!s}",
    )
    session.debug("Linted the code with Ruff.")


@nox.session(tags=["lint", "ci"])
def check_format(
    session: nox.Session,
) -> None:
    session.debug("Checking the format of the code with Ruff.")
    format_output_file: Path = (_PROJECT_ROOT / "format_output.txt").resolve()
    session.debug(
        f'Writing the foramt check with ruff output to: "{format_output_file!s}".',
    )
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
        session.debug("Checked the format of the code with Ruff.")
