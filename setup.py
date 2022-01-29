#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os
from pkg_resources import Requirement
from setuptools import find_packages, setup

NAME = "validator"
DESCRIPTION = "A file validator pipeline"
URL = "https://github.com/clemcrafts/validator"
EMAIL = "clement@gmail.com"
AUTHOR = "Clement"
REQUIRES_PYTHON = ">=3.8.0"
REQUIRED = []

with open("requirements.txt", "r") as f:
    for line in f.readlines():
        try:
            REQUIRED.append(str(Requirement.parse(line)))
        except ValueError:
            pass

setup(
    name=NAME,
    version="v1",
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(
        exclude=["tests", "validator", "docs"]
    ),
    install_requires=REQUIRED,
    include_package_data=True,
    classifiers=[
        "License :: Other/Proprietary License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
