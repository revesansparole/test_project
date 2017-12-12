#!/usr/bin/env python
# -*- coding: utf-8 -*-

# {# pkglts, pysetup.kwds
# format setup arguments

from setuptools import setup, find_packages


short_descr = "belle petite description"
readme = open('README.rst').read()
history = open('HISTORY.rst').read()


# find version number in src/test_project/version.py
version = {}
with open("src/test_project/version.py") as fp:
    exec(fp.read(), version)

# find packages
pkgs = find_packages('src')



setup_kwds = dict(
    name='test_project',
    version=version["__version__"],
    description=short_descr,
    long_description=readme + '\n\n' + history,
    author="revesansparole",
    author_email="revesansparole@gmail.com",
    url='https://github.com/revesansparole/test_project',
    license='cecill-c',
    zip_safe=False,

    packages=pkgs,
    package_dir={'': 'src'},
    setup_requires=[
        "pytest-runner",
        ],
    install_requires=[
        ],
    tests_require=[
        "coverage",
        "pytest",
        "pytest-cov",
        "pytest-mock",
        "sphinx",
        ],
    entry_points={},
    keywords='',
    )
# #}
# change setup_kwds below before the next pkglts tag

# do not change things below
# {# pkglts, pysetup.call
setup(**setup_kwds)
# #}
