from setuptools import setup, find_packages
import pathlib

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="sampleproject",
    version=1.0,

    install_requires = [
        "autobahn",
        "crochet",
        "pyserial",
        "schema",
        "twisted"
    ],
    dependency_links = [
        'git+https://github.com/twisted/twisted.git#egg=twisted'
    ],

    package_dir={'': 'src'},  # Optional
    packages=find_packages(where='src'),  # Required
)