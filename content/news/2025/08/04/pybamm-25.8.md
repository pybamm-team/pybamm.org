---
title: PyBaMM 25.8 has been released!
summary: PyBaMM version 25.8 has now been released with several new features and improvements.
date: 2025-08-04
shortcutDepth: 1
---

PyBaMM 25.8 has now been released! We would like to thank all the [contributors](https://pybamm.org/teams/) who made this release possible.

The full list of changes can be found in the [CHANGELOG](https://pybamm.org/changelog/) file, but here we provide a deeper overview of the main features of this release.

## Python 3.9 support removed

Support for Python 3.9 has been removed in this release. The supported Python versions are now 3.10 to 3.12.

## SPM + 3D thermal model
_Implemented by [Rishab Kumar Jha](https://github.com/Rishab87)_

This version brings several features that allow for 2D and 3D simulations in PyBaMM. The main features of this release are the 3D mesh support for prismatic and cylindrical geometries, plotting functionality for 2D&3D variables and, more importantly the `Basic3DThermalSPM`, which couples a 3D geometry (pouch or cylindrical) for the thermal problem with the Single Particle Model for the electrochemical problem.

For more details, check the [example scripts for 3D models](https://github.com/pybamm-team/PyBaMM/tree/develop/examples/scripts/3d_examples). 2D and 3D functionality is ongoing work and will be further developed in the upcoming releases.

## Improvements on `DiscreteTimeSum`
_Implemented by [Martin Robinson (Oxford RSE)](https://github.com/martinjrobins)_

The `DiscreteTimeSum` class can now be used inside an expression (not just as a root node) , including better handling of time discretization and improved performance for large-scale simulations. Moreover it also now works with the `output_variables` option in the solver (and so does `ExplicitTimeIntegral`).

## Renaming and small improvements on hysteresis models
_Implemented by [Rob Timms (Ionworks)](https://github.com/rtimms)_

The hysteresis models have been renamed for clarity and some small improvements have been made to their implementation. The options `"Axen"` and `"Wycisk"` are now `"one-state hysteresis"` and `"one-state differential capacity hysteresis"`. The old option names still work but will raise a warning.

Several small improvements have been introduced regarding hysteresis models, for more information see [the relevant pull request](https://github.com/pybamm-team/PyBaMM/pull/4893). The most important ones are the inclusion of the heat generation term due to hysteresis, that initial hysteresis state can be a function of position through the electrode and that hysteresis decay rates can be a function of stoichiometry and temperature.

The main breaking change that these changes introduce is that the user needs to explicitly give the equilibrium, delithiation, and lithiation OCPs when using a hysteresis model. E.g. one must provide all three of `"Negative electrode OCP [V]"`, `"Negative electrode delithiation OCP [V]"`, and `"Negative electrode lithiation OCP [V]"`.

## IREE code from IDAKLU solver removed
_Implemented by [Eric Kratz](https://github.com/kratman)_

The IREE code has been removed from the IDAKLU solver in this release. This code posed some maintenance challenges and, as far as we are aware, its use was minimal.
