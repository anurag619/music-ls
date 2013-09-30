#!/usr/bin/env python
"""music app"""
from setuptools import find_packages, setup


setup(name = 'music-ls',
    version = '0.1',
    description = "Script to play songs according to your taste in gaana.com",
    platforms = ["Linux"],
    author = "Anurag",
    author_email = "anurag3rdsep@gmail.com",
    url = "https://github.com/anurag619/music-ls",
    license = "MIT",
    packages = find_packages(),
    install_requires = ['fbconsole', 'google==1.05', 'selenium'],

    dependency_links = ['https://pypi.python.org/pypi/fbconsole/0.2',
                        'https://pypi.python.org/pypi/google',
                        'https://pypi.python.org/pypi/selenium'
],
    )

