# https://docs.python.org/3/distutils/setupscript.html#additional-meta-data

import pathlib
import pkg_resources
import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

with pathlib.Path("requirements.txt").open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement in pkg_resources.parse_requirements(requirements_txt)
    ]

name = "mylittleci"
url = "https://github.com/fredrikaverpil/mylittleci"
description = "Template Python project"
package_dir = "src"
cli_modules = [
    "example=mylittleci.cli.example:main",
]

setuptools.setup(
    setup_requires=["setuptools_scm"],
    use_scm_version={"local_scheme": "node-and-timestamp"},
    name=name,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    packages=setuptools.find_packages(package_dir),
    package_dir={"": package_dir},
    entry_points={"console_scripts": cli_modules},
    include_package_data=True,
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
)
