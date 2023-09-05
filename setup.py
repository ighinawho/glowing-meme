#! /usr/bin/env python
"""
Set up for mymodule
"""
from setuptools import setup
import os

def get_requirements():
    """
    Read the requirements from a file
    """
    requirements = []
    if os.path.exists('requirements.txt'):
        with open('requirements.txt') as req:
            for line in req:
                # skip commented lines
                if not line.startswith('#'):
                    requirements.append(line.strip())
    return requirements

setup(
    name='mymodules', # the name of the module
    packages=['mymodules'], # the location of the module
    version=0.1,
    install_requires=get_requirements(),
    python_requires='>=3.8',
    scripts=['scripts/runme'],
    entry_points={'console_scripts':['sky_sim= mymodules.sky_sim:main']}
)