---
title: PyBaMM 25.4 has been released!
summary: PyBaMM version 25.4 has now been released with several new features and improvements.
date: 2025-04-02
shortcutDepth: 1
---

PyBaMM 25.4 has now been released! We would like to thank all the [contributors](https://pybamm.org/teams/) who made this release possible.

The full list of changes can be found in the [CHANGELOG](https://pybamm.org/changelog/) file, but here we provide a deeper overview of the main features of this release.

## Mechanical models compatible with particle size distributions
_Implemented by [Alec Bills (Ionworks)](https://github.com/aabills)_

Continuing the work from the previous release, on cross-compatibility of submodels, the mechanical models in PyBaMM are now compatible with particle size distributions. This means that the mechanical models can be used with any of the particle size distribution models available in PyBaMM, for example

```python3
pybamm.lithium_ion.MPM(
    options={"particle mechanics": "swelling and cracking"}
)
```

## Hysteresis model from Axen et al (2022)
_Implemented by [chtamar](https://github.com/chtamar)_

A new hysteresis submodel has been added to PyBaMM, based on the work of [Axen et al (2022)](https://doi.org/10.1016/j.est.2022.103985). This model can be accessed via the model options, e.g.

```python3
pybamm.lithium_ion.DFN(
    {
        "open-circuit potential": (("single", "Axen"), "single"),
        "particle phases": ("2", "1"),
    }
)
```

For more information on this and the other hysteresis models available in PyBaMM, see [the hysteresis notebook](https://docs.pybamm.org/en/stable/source/examples/notebooks/models/differential-capacity-hysteresis-state.html).

## Experiments compatible with input parameters
_Implemented by [Rishab Kumar Jha](https://github.com/Rishab87)_

Input parameters can now be used when defining experiment steps. This improves performance when testing multiple operation conditions as the input parameter is only evaluated at the solving stage, so the model does not need to be processed again. For example, to define a current step with the value as an input parameter we can use:

```python3
step = pybamm.step.current(
    pybamm.InputParameter("I_app"),
    termination="< 2.5 V",
)
```

## pchip method for interpolants
_Implemented by [Rishab Kumar Jha](https://github.com/Rishab87)_

The `pchip` method is now available in `pybamm.Interpolant` in addition to `linear` and `cubic`. This interpolator preserves monotonicity in the interpolation data and does not overshoot if the data is not smooth.

## Summary variables dictionary
_Implemented by [Pip Liggins (Oxford RSE)](https://github.com/pipliggins)_

The method `get_summary_variables` is now available to return a dictionary of all degradation summary variables in the model versus cycle number. This is useful for further processing of the degradation data.
