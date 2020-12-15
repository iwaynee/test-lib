from setuptools import setup, find_packages
import pathlib

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="test-lib",
    version=1.0,
    install_requires=[
        "autobahn",
        "twisted"
    ],

    packages=find_packages(where='src'),  # Required
)