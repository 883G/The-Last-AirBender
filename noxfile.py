from pathlib import Path

import nox

_MIN_COVERAGE_PRECENT: int = 90
_PROJECT_ROOT: Path = Path(__file__).parent.resolve()
_CODE_FILES: Path = (_PROJECT_ROOT / "tlab").resolve()
_COVERAGE_FILE: Path = (_PROJECT_ROOT / "coverage").resolve()

# nox.options.force_venv_backend = "none"
nox.options.default_venv_backend = "none"
nox.options.reuse_existing_virtualenvs = True


@nox.session
def test(
    session: nox.Session,
):
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


@nox.session
def coverage(
    session: nox.Session,
):
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


@nox.session
def lint(
    session: nox.Session,
):
    pass


@nox.session
def format(
    session: nox.Session,
):
    pass
