[![Operating systems](https://github.com/tomcodewizard/ODE-solvers/actions/workflows/os_versions.yml/badge.svg)](https://github.com/tomcodewizard/ODE-solvers/actions/workflows/os_versions.yml)
[![Python package](https://github.com/tomcodewizard/ODE-solvers/actions/workflows/python_versions.yml/badge.svg)](https://github.com/tomcodewizard/ODE-solvers/actions/workflows/python_versions.yml)
[![Style tests (flake8)](https://github.com/tomcodewizard/ODE-solvers/actions/workflows/style.yml/badge.svg)](https://github.com/tomcodewizard/ODE-solvers/actions/workflows/style.yml)
[![Documentation Status](https://readthedocs.org/projects/ode-solvers/badge/?version=latest)](https://ode-solvers.readthedocs.io/en/latest/?badge=latest)

# ODE Solvers

*ODE Solvers* is a python package that contains a number of numerical solver functions for Ordinary Differential Equations (ODEs). 

This package was made as part of the *Modelling and Scientific Computing* module. 

This package was used in a report write-up to compare different ODE methods when solving a SIR model. 

Example output of a SIR plot is given below: 

<img src="images/forwardeuler_SIR_graph.png" width="500" height="400">

## Numerical Methods

*ODE Solvers* contains a number of methods in `solver\ODE_methods.py`

These include:

- Forward Euler
- Backward Euler
- Midpoint Method
- Heun's Method
- Runge Kutta RK4
- Adams-Bashforth
- Adams-Moulton

## Installing ODE-Solvers

You can install from the repository, by typing the following into a command terminal:
```
$ git clone git@github.com:tomcodewizard/ODE-solvers.git
$ cd ODE-solvers
$ pip install -e .[dev,docs]
```

To uninstall, type:
```
$ pip uninstall solver
```
