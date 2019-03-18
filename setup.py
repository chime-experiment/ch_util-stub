#!/usr/bin/python3

import setuptools

setuptools.setup(
    name='ch_util',
    author="The CHIME Collaboration",
    author_email="rick@phas.ubc.ca",
    description="A stub module to use as a mock import of the private ch_util"
                " repository",
    packages=['ch_util', 'ch_util.data_index', 'ch_util.ephemeris',
              'ch_util.fluxcat'],
    url="https://github.com/chime-experiment/ch_util-stub"
)

