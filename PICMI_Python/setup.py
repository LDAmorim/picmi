#!/usr/bin/env python
# To use:
#       python setup.py install

from setuptools import setup

setup(name = 'picmistandard',
      version = '0.0.3',
      description = 'Python base classes for PICMI standard',
      platforms = 'any',
      packages = ['picmistandard'],
      package_dir = {'picmistandard': '.'},
      )

