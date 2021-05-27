#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages


setup(
    name="coloriage",
    version="0.0.1",
    description="Manual selection of regions from networkX graph",
    author="Valentin Bonnet, Gustave Ronteix",
    author_email="gustave.ronteix@pasteur.fr",
    url="https://github.com/microfluidix/graphs-on-chip",
    install_requires=[
        "bokeh",
        "networkx",
        "numpy",
        "pip",
    ],
    #package_dir={"": "byograph"},
    #packages = find_packages("byograph") 
    
    packages = ['coloriage']
)
