---
title: PyBaMM 23.9 has been released!
date: 2023-11-20
summary: PyBaMM 23.9 has been released with several new features and improvements.
toc: true
shortcutDepth: 1
---

PyBaMM 23.9 is finally here! This release marks the change to a new release schedule with three releases a year, aiming to publish the new versions at the end of January, May and September (ish). We would like to thank all the contributors who made this release possible.

The full list of changes can be found in the [CHANGELOG](https://pybamm.org/changelog/) file, but here we provide a deeper overview of the main features of this release.

## Installation of optional dependencies

The number of required dependencies for PyBaMM has now been reduced to: [NumPy](https://numpy.org/), [SciPy](https://docs.scipy.org/doc/scipy/), [CasADi](https://web.casadi.org/docs/), [XArray](https://docs.xarray.dev/en/stable/) and [anytree](https://github.com/c0fec0de/anytree). This will be the only dependencies installed when running
```bash
pip install pybamm
```

In addition, PyBaMM has a number of optional dependencies for different functionalities. If using `pip`, optional PyBaMM dependencies can be installed as optional extras, e.g.
```bash
pip install pybamm"[dev,plot]"
```
where `[dev,plot]` specify the optional sets of dependencies to install (see [the docs](https://docs.pybamm.org/en/stable/source/user_guide/installation/index.html#optional-dependencies) for more information about all the options).

To install all optional dependencies the command is
```bash
pip install pybamm"[all]"
```

## SEI and plating models for both electrodes

From this version onwards, SEI (including SEI on cracks) and lithium plating models an be included in both the positive and the negative electrodes by passing a tuple of options, e.g.
```python3
model = pybamm.lithium_ion.DFN({"SEI": ("reaction limited", "reaction limited")})
```

To maintain the previous functionality, if a tuple is not given and `"working electrode"` is set to `"both"` (i.e. a full cell) then the setting will be applied only to the negative electrode. This change allows to use degradation models in half-cells, as shown in [this example notebook](https://docs.pybamm.org/en/stable/source/examples/notebooks/models/half-cell.html).

Note that this functionality introduced a breaking change as now all the variables corresponding to SEI, SEI on cracks and lithium plating have domains, e.g. `SEI thickness [m]` is no longer valid and `Negative SEI thickness [m]` or `Positive SEI thickness [m]` need to be used instead.

## Empirical hysteresis models

Another feature available in this version is empirical hysteresis for the particle diffusivity and the intercalation exchange-current density, which add to the existing functionality for hysteresis of the open-circuit potential. This means that these parameter functions can now be defined separately for lithiation and delithiation.

This functionality can be enabled by passing additional options to the model:
```python3
model = pybamm.lithium_ion.SPMe(
    {
        "open-circuit potential": ("current sigmoid", "single"),
        "exchange-current density": ("current sigmoid", "single"),
        "diffusivity": ("current sigmoid", "single"),
    }
)
```
where the tuples specify different behaviours for each electrode. The parameter values then need to be updated to provide the values for lithiation and delithiation accordingly, as shown in [this example script](https://github.com/pybamm-team/PyBaMM/blob/develop/examples/scripts/empirical_hysteresis.py).

## NumPy functions

NumPy functions now work with PyBaMM symbols, which means they can be used directly (e.g. `np.exp(pybamm.Symbol("a"))`) instead of calling the PyBaMM function (e.g. `pybamm.exp(pybamm.Symbol("a"))`). Additionally, NumPy arrays are now automatically converted to PyBaMM arrays, so the former can be combined with PyBaMM objects.

## MSMR model

The Multi-Species Multi-Reaction (MSMR) model, from [Baker & Verbrugge (2018)](https://iopscience.iop.org/article/10.1149/2.0771816jes) is now available in PyBaMM. The syntax of the model is
```python3
model = pybamm.lithium_ion.MSMR({"number of MSMR reactions": ("6", "4")})
```
and the number of reactions in each electrode needs to be specified (in this case we use 6 reactions in the negative electrode and 4 reactions in the positive one). An example of this model, with detailed explanation, can be found [in this notebook](https://docs.pybamm.org/en/stable/source/examples/notebooks/models/MSMR.html).

## Thermal pouch model

The notation around thermal models for pouch cells has now been improved. The main breaking change is that now the `"lumped"` thermal option always uses the parameters `"Cell cooling surface area [m2]"`, `"Cell volume [m3]"` and `"Total heat transfer coefficient [W.m-2.K-1]"` to compute the cell cooling regardless of the chosen `"cell geometry"` option. When accounting for a pouch cell, the correct values for these parameters must be provided by the user.

The example notebooks for [thermal models](https://docs.pybamm.org/en/stable/source/examples/notebooks/models/thermal-models.html) and [pouch cell models](https://docs.pybamm.org/en/stable/source/examples/notebooks/models/pouch-cell-model.html) have now been updated to reflect these changes.
