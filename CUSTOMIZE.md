# Customize

This project serves as a template for a generic Python project.

To make it your own, go through the below steps in a fork or copy of this repository.

## Decide on CI features

Edit [noxfile.py](noxfile.py) and the requirements*.txt files to use the features you want. A recommendation is e.g. to pick either black _or_ yapf, not both.

If you feel pylint is too picky, just go with flake8, rather than adding a truckload of non-default settings to pylint.

## Adjust any preferences in setup.cfg

All pytest plugins, linters, formatters etc can be configured from within [setup.cfg](setup.cfg). Remove what you don't need and customize to your heart's content.

Black is the exception, which do not offer setting anything up from within setup.cfg. If you must configure black (which goes against one the core ideas behind black) use its [pyproject.toml](https://github.com/psf/black#pyprojecttoml) or add command line arguments to the `black` command.

A general recommendation is to keep the non-defaults to a minimum for easier integration with other projects or when copy-pasting code to others and from e.g. [Stack Overflow](https://stackoverflow.com) :wink:

Line lengths have been set to accomodate for black's default line length of 88.

## Documentation

Documentation is done with [Sphinx](https://www.sphinx-doc.org/en/master/), and you can find all configuration in [docs/conf.py](docs/conf.py). View the built documentation by downloading it from one of the the [Github Actions runs](https://github.com/fredrikaverpil/mylittleci/actions?query=workflow%3Amylittleci).

## Tests

Enter the `test` folder. In here you can use the [tests/TEST_PLAN.md](tests/TEST_PLAN.md) and the [tests/TEST_STRATEGY.md](tests/TEST_STRATEGY.md) to define your test plan and test strategy.

Add/remove test category folders as needed. You might want to create separate nox sessions in [noxfile.py](noxfile.py) so you can easily run e.g. the unit tests separately from other tests.

## Replace the "mylittleci" dummy project name

I've left the hardest part to last... :wink:

Replace every occurance of `mylittleci`, in this repo with the name of your project, preferably using a search-replace tool. Don't forget the `src/mylittleci` folder.
