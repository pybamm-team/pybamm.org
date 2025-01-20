---
title: PyBaMM 25.1 has been released!
summary: PyBaMM version 25.1 has now been released with several new features and improvements.
date: 2025-01-15
shortcutDepth: 1
---

PyBaMM 25.1 has now been released! We would like to thank all the [contributors](https://pybamm.org/teams/) who made this release possible.

The full list of changes can be found in the [CHANGELOG](https://pybamm.org/changelog/) file, but here we provide a deeper overview of the main features of this release.

## Increased compatibility of submodels
_Implemented by [Alec Bills (Ionworks)](https://github.com/aabills) and [Simon O'Kane](https://github.com/DrSOKane)_

Several submodels have been updated to enhance the compatibility with other submodels. The new compatibilities are:

* SEI models with particle size distributions.
* Composite electrodes with particle size distributions.
* Porosity change with composite electrodes.

This means that almost all submodels are cross-compatible!

## SEI models are now for a single layer only
_Implemented by [Valentin Sulzer (Ionworks)](https://github.com/valentinsulzer)_

All SEI models in PyBaMM are now defined for a single layer SEI, and the double layer SEI models have been removed. Note that by double layer we mean an SEI with inner and outer SEI layers, not the interface capacitance double layer. This change should make SEI models easier to understand and compare.

## Two new SEI models
_Implemented by [Kawa Manmi (University of Warwick)](https://github.com/kawaMANMI)_

Two new SEI models have been added to PyBaMM: the `"tunnelling limited"` model (from [Tang et al (2012)](https://iopscience.iop.org/article/10.1149/2.025211jes)) and the `"VonKolzenberg2020"` model (from [Von Kolzenberg et al (2020)](https://doi.org/10.1002/cssc.202000867)). These models can be enabled by passing the relevant `"SEI"` in the model options dictionary. Note that additional parameters are required for this model, and the parameter set dictionary needs to be updated manually.

## Improved `search` method in PyBaMM dictionaries
_Implemented by [Medha Bhardwaj (IIIT Lucknow)](https://github.com/medha-14)_

The `search` method in PyBaMM dictionaries, for example in a `ParameterValues` or a `model.variables` dictionary, has been enhanced so it can take lists of strings. This allows for more flexibility when searching for variables or parameters in a dictionary. For example, if we want to search for all variables related to potentials in the negative electrode, we can now do

```python3
model.variables.search(["negative", "potential"])
```

## Geometric parameters as input parameters
_Implemented by [Alec Bills (Ionworks)](https://github.com/aabills)_
PyBaMM now includes `SymbolicUniform1DSubMesh`, which allows for the definition of geometric parameters as input parameters without need to rebuild the model. The mesh is internally defined to be defined between 0 and 1, and the discretised operators take care of the contribution of the domain lengths.

This mesh does not work straight out of the box with default models, but it can be used in custom-built models.

## Improved distribution and packaging for PyPI and conda-forge
_Implemented by [Eric Kratz (Ionworks)](https://github.com/kratman)_

The C/C++ solvers included in PyBaMM (e.g. `IDAKLUSolver`) have been moved to a standalone package called [`pybammsolvers`](https://pypi.org/project/pybammsolvers/). This change makes PyBaMM a pure Python package, simplifying significantly the installation process from source (including Windows), which benefits PyBaMM developers and contributors.

_Implemented by [Saransh Chopra (ARC, University College London RSE)](https://github.com/Saransh-cpp)_

The conda-forge distribution has been migrated to a `noarch` recipe, making it platform independent. Additionally, a new conda-forge package, `pybamm-base`, has been developed to enable installing PyBaMM only with required dependencies. The `pybamm` package on conda-forge has been updated to include all the available optional dependencies (equivalent to `pybamm[all,jax]` on PyPI). Similar to the PyPI change, these changes simplify the installation process for both users and developers.
## State variables are always included as output variables
_Implemented by [Martin Robinson (Oxford RSE)](https://github.com/martinjrobins)_

The state variables of a PyBaMM model are now automatically included as output variables, if they are not already present. This makes the process of building custom models more robust avoiding, for example, errors with the `set_initial_conditions_from` method when output variables were not correctly defined.

## Support for BPX 0.5.0
_Implemented by [Eric Kratz (Ionworks)](https://github.com/kratman)_

PyBaMM now supports [BPX](https://github.com/FaradayInstitution/BPX) 0.5.0, which was released in December 2024. This version of BPX uses Pydantic v2.
