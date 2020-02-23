#!/usr/bin/python3

import setuptools

setuptools.setup(
    name='ch_util',
    author="The CHIME Collaboration",
    author_email="rick@phas.ubc.ca",
    description="A stub module to use as a mock import of the private ch_util"
                " repository",
    packages=['ch_util', 'ch_util.andata', 'ch_util.finder',
        'ch_util.ephemeris', 'ch_util.fluxcat', 'ch_util.rfi', 'ch_util.tools', 'ch_util.cal_utils'],
    url="https://github.com/chime-experiment/ch_util-stub"
)

