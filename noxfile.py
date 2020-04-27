"""Manage CI using Nox."""

import glob
import os
import shutil
import tempfile

import nox


def _install_wheel(session):
    with tempfile.TemporaryDirectory() as tmp_dir:
        session.run("python", "setup.py", "bdist_wheel", f"--dist-dir={tmp_dir}")
        for filepath in glob.glob(f"{tmp_dir}/*.whl"):
            session.run("pip", "install", "-U", filepath)
            if not os.path.exists("dist"):
                os.makedirs("dist")
            shutil.copy(filepath, "dist")


@nox.session
def linting(session):
    session.install("-r", "requirements.txt", "-r", "requirements_linting.txt")
    session.run("pip", "check")  # until pip comes with deps resolver
    # session.run("pylint", "src")
    session.run("flake8", "--doctests", "src")
    session.run("pycodestyle", "src")
    session.run("pydocstyle", "src")
    session.run("isort", "--recursive", "--diff", "src")


@nox.session
def formatting(session):
    session.install("-r", "requirements.txt", "-r", "requirements_formatting.txt")
    session.run("black", "--check", "src")
    # session.run("yapf", "--recursive", "--diff", "src")


@nox.session
def dead_code_search(session):
    session.install("vulture")
    session.run("vulture", "src")


@nox.session
def static_type_checking(session):
    session.install("-r", "requirements.txt", "-r", "requirements_typing.txt")
    session.run("pip", "check")  # until pip comes with deps resolver
    session.run("mypy", "src")


@nox.session
def tests(session):
    """Run tests using pytest.

    The wheel is built and installed into the nox venv,
    so that packaging issues can be caught by the tests.
    """
    session.install("-r", "requirements_tests.txt")
    _install_wheel(session)
    session.run("pip", "check")  # until pip comes with deps resolver
    session.run("pytest")


@nox.session
def build_docs(session):
    session.install("-r", "requirements.txt", "-r", "requirements_docs.txt")
    _install_wheel(session)
    session.run("pip", "check")  # until pip comes with deps resolver
    session.run("sphinx-build", "docs", "docs/_build/html")