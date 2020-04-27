"""Test for known security vulnerabilities."""

import subprocess

import pytest


def test_safety_of_installed_packages(capfd: pytest.Class) -> None:
    """Check installed packages for known security vulnerabilities."""
    cmd = ["safety", "check"]
    proc = subprocess.run(cmd, check=False)
    captured = capfd.readouterr()
    assert "No known security vulnerabilities found." in captured.out
    assert proc.returncode == 0


def test_safety_of_requirements_files(
    capfd: pytest.Class, repo_root: pytest.Class
) -> None:
    """Check installed packages for known security vulnerabilities.

    Note:
        Unpinned packages are not checked.
    """
    filepaths = repo_root.glob("requirements*.txt")
    assert filepaths != []
    for filepath in filepaths:
        cmd = ["safety", "check", "-r", str(filepath)]
        proc = subprocess.run(cmd, check=False)
        captured = capfd.readouterr()
        print(captured.out)
        assert "No known security vulnerabilities found." in captured.out
        assert proc.returncode == 0
