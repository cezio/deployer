#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from distutils.core import setup

setup(
    name="deployer",
    version="0.1",
    author="Cezary Statkiewicz",
    author_email="c.statkiewicz@gmail.com",
    description="simple deployment server",
    long_description=(read('README.rst')),
    # Full list of classifiers can be found at:
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
    license="BSD",
    keywords="flask github deployment infrastructure git",
    url='',
    packages=['deployer',],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask'
    ],
)
