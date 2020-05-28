#!/usr/bin/env python
from __future__ import print_function
from setuptools import setup, find_packages

with open("README.md",'r',encoding='utf-8') as f:
    long_description = f.read()

setup = (
    name='pycolor',
    author='zack',
    version='1.0',
    license='MIT',
    description='print colorful string',
    url = "",
    packages = find_packages(),
    platform = "any",
    install_requires = []
)
