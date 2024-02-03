#
# ODE solver setuptools script
#
from setuptools import setup, find_packages


def get_version():
    """
    Get version number from the abm_model module.

    The easiest way would be to just ``import abm_model``, but note that this may
    fail if the dependencies have not been installed yet. Instead, we've put
    the version number in a simple version_info module, that we'll import here
    by temporarily adding the oxrse directory to the pythonpath using sys.path.
    """
    import os
    import sys

    sys.path.append(os.path.abspath('solver'))
    from version_info import VERSION as version
    sys.path.pop()

    return version


def get_readme():
    """
    Load README.md text for use as description.
    """
    with open('README.md') as f:
        return f.read()


# Go!
setup(
    # Module name (lowercase)
    name='solver',

    # Version
    version=get_version(),

    description='ODE-solver',

    long_description=get_readme(),

    license='MIT license',

    # author='',

    # author_email='',

    maintainer='Tom Reed',

    maintainer_email='thomas.reed@wolfson.ox.ac.uk',

    url='https://github.com/tomcodewizard/ODE-solvers',

    # Packages to include
    packages=find_packages(include=('solver')),

    # List of dependencies
    install_requires=[
        # Dependencies go here!
        'numpy',
        'matplotlib',
        'pandas',
        'scipy',
    ],
    extras_require={
        'docs': [
            # Sphinx for doc generation. Version 1.7.3 has a bug:
            'sphinx>=1.5, !=1.7.3',
            # Nice theme for docs
            'sphinx_rtd_theme',
        ],
        'dev': [
            # Flake8 for code style checking
            'flake8>=3',
            'pytest',
            'pytest-cov',
        ],
    },
)
