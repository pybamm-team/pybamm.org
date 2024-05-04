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

PyBaMM now includes support for Python 3.12, which was released in October 2023. There is some functionality still not yet fully supported in Python 3.12 plus some functionality deprecated for Python 3.8 (see warnings below), but versions 3.9 to 3.11 support all functionality.

&nbsp;

{{< admonition caution >}}
We have deprecated support for the `JaxSolver`, i.e., the `[jax]` optional dependency on Python 3.8 and it is supported on Python 3.9 and above for macOS, Linux, and Windows.

{{< /admonition >}}

{{< admonition note >}}

The `scikits.odes` solver is not supported on Python `3.12` yet. It is supported on Python versions `3.8` to `3.11`, for macOS and Linux.

{{< /admonition >}}

## Custom termination conditions

Experiment termination conditions can now be customised, and defined in terms of any model variable. The condition is defined as a Python method that is positive in the feasible operating region, zero when the condition is met and negative in the non-feasible region. For example, to define a termination condition based on the negative electrode potential we can define

```python3
def anode_potential_cutoff(variables):
    return variables["Anode potential [V]"] - 0.02
```


This method can then be converted into a termination condition by using the `CustomTermination` class and passed to an experiment:

```python3
termination = pybamm.step.CustomTermination(
    name="Anode potential cut-off [V]", event_function=anode_potential_cutoff
)

experiment = pybamm.Experiment(
    [
        pybamm.step.c_rate(-1, termination=termination),
        pybamm.step.c_rate(-0.5, termination=termination),
    ]
)
```

For a full example please see [this notebook](https://docs.pybamm.org/en/stable/source/examples/notebooks/simulations_and_experiments/custom-experiments.html).


## Reference electrodes

By default, PyBaMM takes the reference of potential to be at the negative current collector. The new reference electrode functionality allows the users to extract the potential versus a reference electrode, which is a common experiment. The method `insert_reference_electrode` allows the user to specify the position where to insert the reference electrode (the default option is the midpoint of the separator). Then, the model includes the new variables `"Reference electrode potential [V]"`, `"Negative electrode 3E potential [V]"` and `"Positive electrode 3E potential [V]"` which can be plotted and postprocessed as usual. For a full example please see [this notebook](https://docs.pybamm.org/en/stable/source/examples/notebooks/models/simulate-3E-cell.html).


## Serialisation of models, parameters and variables

PyBaMM now supports serialisation of models, parameters, and variables, allowing users to save them to and load them from disk. This is useful for saving the results of long simulations or drive cycles, or for sharing models and parameters with other users in JSON format.

More information can be found in [the docs](https://docs.pybamm.org/en/stable/source/api/expression_tree/operations/serialise.html) and [this notebook](https://docs.pybamm.org/en/stable/source/examples/notebooks/models/saving_models.html).

## A `get_parameter_info` function

The functionality to print which parameters does a model depend on has now been improved. The method `print_parameter_info` still prints on screen the parameters a model depends on and which type they are (i.e. `Parameter` or `FunctionParameter`) but now as table, which improves readability. The new `get_parameter_info` method outputs the information as a dictionary, which makes it easy to process the information and enables, amongst other things, to easily extract the parameters required to run a specific model from a larger parameter set. The [parameterisation notebook](https://docs.pybamm.org/en/stable/source/examples/notebooks/parameterization/parameterization.html) has now been updated to showcase this functionality.
