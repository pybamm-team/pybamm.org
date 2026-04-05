---
title: PyBaMM Roadmap
summary: This page is a working document of the main features PyBaMM aims to provide
---

This page contains a summary of the main features we are working towards and might provide ideas for funding applications.

The fact that an item is listed in this roadmap does not mean that it will necessarily happen. On the other hand, an item not being listed in the roadmap for a year does not indicate it cannot be included in future iterations. Note that the ideas here correspond to big features. Smaller features are tracked in the [issue tracker](https://github.com/pybamm-team/PyBaMM/issues). For more details on the current technical roadmap, see the [2024 roadmap discussion](https://github.com/pybamm-team/PyBaMM/issues/3839) and [2025 roadmap discussion](https://github.com/pybamm-team/PyBaMM/issues/5064).

## Battery models

We strive to keep PyBaMM up with the state-of-the-art in battery models, which advances in two directions:

1. Including additional effects and physics (e.g. thermal, degradation) for existing chemistries (e.g. lithium-ion, lead-acid).
2. Implementing models for new chemistries (e.g. sodium-ion, lithium-air).

We are also working to rationalise the submodel interface and options, making it easier to define models and understand what is being solved. See [pybamm-team/PyBaMM#5103](https://github.com/pybamm-team/PyBaMM/issues/5103) for details.

## Solver improvements

We are continuously aiming to improve PyBaMM's solver capabilities, with a particular focus on sensitivity calculations to enable efficient parameter inference with tools such as [PyBOP](https://github.com/pybop-team/PyBOP). See [pybamm-team/PyBaMM#5101](https://github.com/pybamm-team/PyBaMM/issues/5101) for details.

## Higher-dimensional modelling

We are expanding PyBaMM's spatial methods to support 2D and 3D simulations, enabling more detailed multi-physics models. See [pybamm-team/PyBaMM#5102](https://github.com/pybamm-team/PyBaMM/issues/5102) for details.

## Interfaces

PyBaMM can generate [CasADi](https://web.casadi.org/) code, which underpins many of its solver integrations. Ongoing efforts include integrating with [Diffsol](https://github.com/martinjrobins/diffsol) and exporting PyBaMM models to Rust.

## Performance and infrastructure

Performance is monitored via [airspeed velocity](https://asv.readthedocs.io/en/stable/) (benchmarks available at [pybamm.org/benchmarks](https://pybamm.org/benchmarks)).

<!-- We also work to keep PyBaMM up to date with newer Python releases, dependencies, and hardware architectures including ARM devices, WebAssembly, and free-threading -->

## Suggestions

If you have any suggestions for this roadmap, please feel free to open a [discussion](https://github.com/pybamm-team/PyBaMM/discussions).
