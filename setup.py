#!/usr/bin/env python

from setuptools import setup

setup(name='flier',
      version='0.1',
      description='Endpoint for KRL Sky API.',
      author='Randall Bohn',
      author_email='flier@rsbohn.com',
      packages=['flier'],
      package_dir={'':'src'},
      install_requires=[],
      entry_points=("""
[console_scripts]
ff=flier:first_flight
""")
      )
