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

Similar to the voltage components, now the `pybamm.plot_thermal_components` can be used to plot heat generation (both instantaneous and cumulative) split into the various thermal components: lumped total cooling, Ohmic heating, irreversible electrochemical heating and reversible heating:

```python3
model = pybamm.lithium_ion.SPM({"thermal": "lumped"})
sim = pybamm.Simulation(
    model, parameter_values=pybamm.ParameterValues("ORegan2022")
)
sol = sim.solve([0, 3600])
pybamm.plot_thermal_components(sol)
```

## Custom experiment steps

Building upon the custom experiment termination conditions introduced in the last release, this release incoporates custom experiment steps. Custom steps can be defined using either explicit or implicit control. In explicit control, the user specifies the current explicitly as a function of other variables in the model using the `pybamm.step.CustomStepExplicit`, which takes a function that defines the imposed current in terms of the model variables. For example, if we were to impose constant power we could write:

```python3
def custom_step_power(variables):
    target_power = 4
    voltage = variables["Voltage [V]"]
    return target_power / voltage

step = pybamm.step.CustomStepExplicit(custom_step_power, duration=600)
```

We can also specify a custom step using implicit control. This comes with "algebraic" or "differential" control. In algebraic control (the default), the user specifies the equation that must be satisfied at all times, and the model adjusts the current to satisfy this equation. For example, we could define a constant voltage experiment as

```python3
def constant_voltage(variables):
    return variables["Voltage [V]"] - 3.8


step = pybamm.step.CustomStepImplicit(constant_voltage, duration=600)
```

Alternatively, we can use differential control to impose the derivative of the current

```python3
def custom_voltage(variables):
    return 100 * (variables["Voltage [V]"] - 3.8)


step = pybamm.step.CustomStepImplicit(
    custom_voltage, duration=600, period=10, control="differential"
)
```


More details on the implementation of the custom steps are provided in the [custom experiments notebook](https://docs.pybamm.org/en/stable/source/examples/notebooks/simulations_and_experiments/custom-experiments.html).

## Hysteresis submodel

The hysteresis submodel from [Wycisk et al (2022)](https://doi.org/10.1016/j.est.2022.105016) is now available. The submodel can be used through the model options as:

```python3
model = pybamm.lithium_ion.DFN(
    {
        "open-circuit potential": "Wycisk",
    }
)
```

Note that additional parameter values might be required for the model to run. For more details, please see the [corresponding notebook](https://docs.pybamm.org/en/latest/source/examples/notebooks/models/differential-capacity-hysteresis-state.html).

## Print parameter information

The `print_parameter_info` method in PyBaMM models now takes the keyword argument `by_submodel` (`False` by default). If set to `True`, the information is split by submodel:

```python3
model = pybamm.lithium_ion.DFN()
model.print_parameter_info(by_submodel=True)
```


## macOS arm64 M-series support

From version 24.5, PyBaMM suppports macOS arm64 (M-series) platforms.

## BPX v0.4.0 support

PyBaMM now supports [BPX v0.4.0](https://github.com/FaradayInstitution/BPX/releases/tag/v0.4.0). This version allows for blended electrodes and user-defined parameters in BPX.