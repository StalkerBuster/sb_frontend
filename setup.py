#!/usr/bin/env python

import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    # see
    # https://docs.pytest.org/en/3.0.0/goodpractices.html#manual-integration
    # to learn what happens here.
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def run_tests(self):
        # late-import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(name='sb_frontend',
      version='0.1.dev0',
      description='StalkerBuster web frontend',
      author='ulif and datenzwerg.in',
      author_email='stalkerbuster@gnufix.de',
      url='https://github.com/stalkerbuster/sb_frontend',
      package_dir={'': 'src'},
      install_requires=['flask'],
      tests_require=['pytest'],
      cmdclass={'test': PyTest},
      entry_points={
          'console_scripts': [
              'stalkerbuster = sb_frontent:main',
              ],
          },
      )
