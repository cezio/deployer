#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from distutils.core import setup

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name="deployer",
    version="0.1",
    author="Cezary Statkiewicz",
    author_email="c.statkiewicz@gmail.com",
    description="simple deployment server",
    long_description=read('README.rst'),
    # Full list of classifiers can be found at:
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
    license="MIT",
    keywords="flask github deployment infrastructure git",
    url='',
    packages=['deployer',],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask'
    ],
)
