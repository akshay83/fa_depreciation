# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='fa_depreciation',
    version=version,
    description='Provides Report for Depreciation on Fixed Assets',
    author='Akshay Mehta',
    author_email='mehta.akshay@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
