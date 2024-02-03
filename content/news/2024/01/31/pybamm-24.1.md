---
title: PyBaMM 24.1 has been released!
summary: PyBaMM version 24.1 has now been released with several new features and improvements.
date: 2024-01-31
toc: true
shortcutDepth: 1
---

PyBaMM 24.1 has now been released! This release continues the previous release schedule conforming to three releases a year and marks the first release of 2024. We would like to thank all the [contributors](https://pybamm.org/teams/) who made this release and the previous three pre-releases possible.

The full list of changes can be found in the [CHANGELOG](https://pybamm.org/changelog/) file, but here we provide a deeper overview of the main features of this release.

## Support for Python 3.12

PyBaMM now includes support for Python 3.12, which was released in October 2023.

&nbsp;

{{< notice warning >}}

We have deprecated support for the `JaxSolver`, i.e., the `[jax]` optional dependency on Python 3.8 and it is supported on Python 3.9 and above for macOS, Linux, and Windows.

{{< /notice >}}

{{< notice note >}}

The `scikits.odes` solver is not supported on Python `3.12` yet. It is supported on Python versions `3.8` to `3.11`, for macOS and Linux.

{{< /notice >}}

## Custom experiment terminations

PyBaMM now supports custom experiment terminations.

## Reference electrode



## Serialisations

PyBaMM now supports serialisation of models, parameters, and variables. This allows users to save and load models, parameters, and variables to and from disk. This is useful for saving the results of long simulations or drive cycles, or for sharing models and parameters with other users in JSON format.

## A `get_parameter_info` function

PyBaMM now includes a `get_parameter_info` function that returns a dictionary of information about the parameters in a model.

<!-- feel free to expand this and/or add information to the previous sections. -->
