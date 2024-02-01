---
title: PyBaMM v0.4.0 Release
date: 2021-03-29
summary: PyBaMM version 0.4.0 has now been released.
---

_March 29, 2021_

PyBaMM version 0.4.0 has now been released. This release introduces:

* Several new models, including reversible and irreversible plating submodels, submodels for loss of active material, Yang et al.'s (2017) coupled SEI/plating/pore clogging model, and the Newman-Tobias model.
* Internal optimizations for solving models, particularly for simulating experiments, with more accurate event detection and more efficient numerical methods and post-processing.
* Parallel solutions of a model with different inputs.
* A cleaner installation process for Mac when installing from PyPI, no longer requiring a Homebrew installation of Sundials.
* Improved plotting functionality, including adding a new 'voltage component' plot.
* Several other new features, optimizations, and bug fixes, summarized below.

For more information, please see the full [CHANGELOG](https://github.com/pybamm-team/PyBaMM/blob/v0.4.0/CHANGELOG.md).
