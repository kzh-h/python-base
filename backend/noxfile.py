"""Configuration Nox."""
from nox_poetry import session


@session
def lint(session):
    """Lint."""
    session.install("flake8")
    session.run("flake8", "src")


@session(python=["3.11"])
def test(session):
    """Pytest."""
    session.install("pytest")
    session.run("pytest")
