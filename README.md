# mylittleci

![mylittleci](https://user-images.githubusercontent.com/994357/80336623-15a73280-8858-11ea-89c1-b8b3a1b7a054.png)

[![mylittleci](https://github.com/fredrikaverpil/mylittleci/workflows/mylittleci/badge.svg?branch=master)](https://github.com/fredrikaverpil/mylittleci/actions?query=workflow%3Amylittleci)

A Python project template. See the [Github Actions runs](https://github.com/fredrikaverpil/mylittleci/actions?query=workflow%3Amylittleci) for details.

## Quickstart

### Get the code and execute it

```bash
git clone [this repo]
cd [this repo]
python3 -m venv venv
. venv/bin/activate
pip install -U pip
pip install -e .

# Run binaries found in venv/bin, e.g. the "example" app
example --help
```

### Run linting, formatting, dead code search, static type checking, tests and build docs

```bash
pip install nox
nox
```

Use Nox option `-r` to re-use the nox venv for faster execution. See [noxfile.py](noxfile.py) for detailed info on the different sessions you can run individually using `nox -s <session_name>`.

More info on Nox usage [here](https://nox.thea.codes/en/stable).

### Add your own code

- Create a new Python module or package in e.g. `src/mylittleci/cli` for command line interface (CLI) applications
- Add its entrypoint (ususally a "main" function), if any, in `setup.py`
- Add any dependencies into `requirements.txt`
- In the mylittleci `venv`, use a local development install: `pip install -U -e .`
- Run the executable representing your entrypoint from `venv/bin`
- Add test for the tool in `tests`
- Run tests quickly to test your changes by executing Pytest: `pytest <path to your test file.py>`
- Finally, run all tests, coverage and linting by executing Nox: `nox`

Try to keep tool documentation within the module/package as module/class/function docstrings.

### Build wheel

In the `venv`:

```python
pip install -U wheel
python setup.py bdist_wheel
# Find your wheel in the 'dist' folder
```

### Bump Python package version

The Python package and wheels will base its version on the latest git tag.

```bash
# create tag
git tag 1.0.0

# push
git push origin 1.0.0

# or for gerrit, push ref:
git push origin 1.0.0 HEAD:refs/for/master
```

### Further customization

See [CUSTOMIZE.md](CUSTOMIZE.md).
