# -*- coding: utf-8 -*-
from codecs import open
from os import path

from setuptools import find_packages
from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="padio",
    version="0.0.0",
    description="Zero pad numeric filenames",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.iamthefij.com/iamthefij/padio.git",
    download_url=(
        "https://git.iamthefij.com/iamthefij/padio.git/archive/master.tar.gz"
    ),
    author="iamthefij",
    author_email="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="",
    packages=find_packages(
        exclude=[
            "contrib",
            "docs",
            "examples",
            "scripts",
            "tests",
        ]
    ),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "padio=padio:main",
        ],
    },
)
