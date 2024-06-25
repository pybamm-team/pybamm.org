---
title: PyBaMM 24.5 has been released!
summary: PyBaMM version 24.5 has now been released with several new features and improvements.
date: 2024-06-25
toc: true
shortcutDepth: 1
---

PyBaMM 24.5 has now been released! This release continues the previous release schedule conforming to three releases a year and marks the second release of 2024. We would like to thank all the [contributors](https://pybamm.org/teams/) who made this release and the previous X pre-releases possible.

The full list of changes can be found in the [CHANGELOG](https://pybamm.org/changelog/) file, but here we provide a deeper overview of the main features of this release.

## Transport efficiency submodels

Several new transport efficiency submodels are now available in PyBaMM to define the effective transport properties in the porous electrodes. In addition to the existing Bruggeman model, we have introduced 7 new submodels (see the [documentation](https://docs.pybamm.org/en/latest/source/api/models/submodels/transport_efficiency/index.html) for a full list). The model options can be used to specify a transport efficiency model other than the default (Bruggeman). For example, if we want to use the DFN model with a tortuosity factor submodel, we call:

```python3
model = pybamm.lithium_ion.DFN(
    options={"transport efficiency": "tortuosity factor"}
)
```

Note that changing the transport efficiency submodel might require additional parameters values. For a full example on transport efficiency submodels, please see [this notebook](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/tortuosity_models.html).

## Basic models compatible with experiments

PyBaMM contains some "basic" models (e.g. `BasicDFN`, `BasicSPM`) which are models that are define in a single file, as opposed of a combination of several submodels. Until now, these models had limited functionality and they could not be used with experiments. From this release, basic models can be used with experiments, for example:

```python3
model = pybamm.lithium_ion.BasicDFN()
experiment = pybamm.Experiment(
    [
        "Discharge at C/3 until 3.5V",
        "Hold at 3.5V for 1 hour",
        "Rest for 10 min",
    ]
)
sim = pybamm.Simulation(model, experiment=experiment)
sim.solve()
```

This change, even though it does not make a big functionality change, is part of our effort into simplifying how users can define their own models in PyBaMM, which is one of the areas of our [technical roadmap](https://github.com/pybamm-team/PyBaMM/issues/3908).

## Plot thermal components
## Plating with composite electrodes
## Custom experiment steps
## Hysteresis submodel
## Print parameter info
## macOS arm64 M-series support
## BPX support
