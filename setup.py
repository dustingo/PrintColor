#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import print_function
from setuptools import setup, find_packages
import platform
pyversion = platform.python_version()
if pyversion.startswith("3"):
    py_modules = ["printcolor"]
else:
    py_modules = ["printcolor2"]

with open("README.md",'r') as f:
    long_description = f.read()

setup(name = "printcolor",
    version = "1.1.2",
    description = "print colorful string",
    author = "zack",
    author_email = "514838728@qq.com",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/dustingo/PrintColor.git",
    packages = find_packages(),
    install_requires = [],
    py_modules = py_modules,
    platforms = ["linux"],
)
