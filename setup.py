from setuptools import setup

setup(name='ODE-solvers',
      version='0.1',
      author='Tom Reed',
      packages=['core'],
      install_requires = ["numpy", "matplotlib", "scipy"],
      license='GPLv3')
