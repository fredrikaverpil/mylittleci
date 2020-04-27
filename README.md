# mylittleci

![mylittleci](https://user-images.githubusercontent.com/994357/80336623-15a73280-8858-11ea-89c1-b8b3a1b7a054.png)

[![mylittleci](https://github.com/fredrikaverpil/mylittleci/workflows/mylittleci/badge.svg?branch=master)](https://github.com/fredrikaverpil/mylittleci/actions?query=workflow%3Amylittleci)
[![Documentation Status](https://readthedocs.org/projects/mylittleci/badge/?version=latest)](https://mylittleci.readthedocs.io/en/latest/?badge=latest)


A Python project template with focus on CI. See the [Github Actions runs](https://github.com/fredrikaverpil/mylittleci/actions?query=workflow%3Amylittleci) for details.

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

This project serves as a template for a generic Python project.

To make it your own, go through the below steps in a fork or copy of this repository.

#### Decide on CI features

Edit [noxfile.py](noxfile.py) and the requirements*.txt files to use the features you want. A recommendation is e.g. to pick either black _or_ yapf, not both.

If you feel pylint is too picky, just go with flake8, rather than adding a truckload of non-default settings to pylint.

#### Adjust any preferences in setup.cfg

All pytest plugins, linters, formatters etc can be configured from within [setup.cfg](setup.cfg). Remove what you don't need and customize to your heart's content.

Black is the exception, which do not offer setting anything up from within setup.cfg. If you must configure black (which goes against one the core ideas behind black) use its [pyproject.toml](https://github.com/psf/black#pyprojecttoml) or add command line arguments to the `black` command.

A general recommendation is to keep the non-defaults to a minimum for easier integration with other projects or when copy-pasting code to others and from e.g. [Stack Overflow](https://stackoverflow.com) :wink:

Line lengths have been set to accomodate for black's default line length of 88.

#### Documentation

Documentation is done with [Sphinx](https://www.sphinx-doc.org/en/master/), and you can find all configuration in [docs/conf.py](docs/conf.py). View the built documentation by downloading it from one of the the [Github Actions runs](https://github.com/fredrikaverpil/mylittleci/actions?query=workflow%3Amylittleci).

You can import your documentation into readthedocs e.g. by entering the details manually [here](https://readthedocs.org/dashboard/import/manual). Then [set up a webhook](https://docs.readthedocs.io/en/stable/webhooks.html) to make pushed commits rebuild your docs.

#### Tests

Enter the `test` folder. In here you can use the [tests/TEST_PLAN.md](tests/TEST_PLAN.md) and the [tests/TEST_STRATEGY.md](tests/TEST_STRATEGY.md) to define your test plan and test strategy.

Add/remove test category folders as needed. You might want to create separate nox sessions in [noxfile.py](noxfile.py) so you can easily run e.g. the unit tests separately from other tests.

#### Replace the "mylittleci" dummy project name

I've left the hardest part to last... :wink:

Replace every occurance of `mylittleci`, in this repo with the name of your project, preferably using a search-replace tool. Don't forget the `src/mylittleci` folder.
