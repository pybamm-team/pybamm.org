---
title: PyBaMM 24.11 has been released!
summary: PyBaMM version 24.11 has now been released with several new features and improvements.
date: 2024-11-21
shortcutDepth: 1
---

PyBaMM 24.11 has now been released! This off-band release slightly differs from the previous release schedule conforming to three releases a year and marks the fourth release of 2024. We would like to thank all the [contributors](https://pybamm.org/teams/) who made this release possible.

The full list of changes can be found in the [CHANGELOG](https://pybamm.org/changelog/) file, but here we provide a deeper overview of the main features of this release.

## Telemetry data collection announcement
_Implemented by [Valentin Sulzer (Ionworks)](https://github.com/valentinsulzer)_

With this release, we have introduced a new **opt-in** telemetry collection system to help us better understand how PyBaMM is being used. This system collects anonymous usage data, such as the version of PyBaMM being used, the operating system, and the Python version. This data will help us make informed decisions about the future of PyBaMM. We would like to assure you that no personal data is collected, and the data is only used by the PyBaMM team. Here are some details:

- **What is collected**: Basic usage information like PyBaMM version, Python version, and which functions are run.
- **Why**: To understand how PyBaMM is used and prioritize development efforts.
- **Permanent opt-out**: To disable telemetry permanently, set the environment variable `PYBAMM_DISABLE_TELEMETRY=true` (or any value other than `false`) or use `pybamm.telemetry.disable()` in your code. You can also select "no" when PyBaMM asks if you would like to enable telemetry.
- **Privacy**: No personal information (name, email, etc) or sensitive information (parameter values, simulation results, etc) is ever collected. The data is used only by the PyBaMM team and is not shared with any third parties. The data is stored securely and is only accessible to the PyBaMM team. Please read PostHog's policy on [GDPR compliance](https://posthog.com/docs/privacy/gdpr-compliance) for more.

## Experiment simulations now support output variables
_Implemented by [Pip Liggins (Oxford RSE)](https://github.com/pipliggins)_

Simulations using experiments now support the use of output variables from the `IDAKLUSolver`. This means that the model can be solved only storing the specified output variables (instead of the whole state vector), which provides benefits both in terms of computational speed and memory usage. For example, if we want to run a long simulation of the SPM model and only store time, current and voltage we can run:

```python3
    model = pybamm.lithium_ion.SPM()

    output_variables = ["Time [s]", "Current [A]", "Voltage [V]"]

    solver = pybamm.IDAKLUSolver(output_variables=output_variables)

    experiment = pybamm.Experiment(
        [
            (
                "Charge at 1C until 4.2 V",
                "Hold at 4.2 V until C/50",
                "Rest for 1 hour",
            )
        ] * 1000
    )

    sim = pybamm.Simulation(model, experiment=experiment, solver=solver)

    sol = sim.solve()
```

## Solver and processed variables speed improvements

This new release comes with several performance associated to the solvers.

### IDAKLU Solver
_Implemented by [Marc Berliner (Ionworks)](https://github.com/MarcBerliner) and [Martin Robinson (Oxford RSE)](https://github.com/martinjrobins)_

This release leverages several features of SUNDIALS to improve the performance of the IDAKLU solver. The solver now uses Hermite interpolation which significantly speeds up processing variables after solving the model. It also improves the plots, especially when the solution has very few timesteps. The initialisation and reinitialisation of ODEs is now done directly by SUNDIALS, which improves the performance of the solver. This is particularly noticeable when solving models with a evaluation times vector `t_eval`.

Finally, the IDAKLU solver can now run multiple simulations in parallel using OpenMP. This is particularly relevant when running parameter sweeps. For a given `model` the parallelisation can be run by
```python3
    options = {"num_threads": num_threads, "num_solvers": num_solvers}
    solver = pybamm.IDAKLUSolver(options=options)
    t_eval = [0, 1]
    ninputs = 8
    inputs_list = [{"C-rate": 0.1 * (i + 1)} for i in range(ninputs)]

    solutions = solver.solve(
        model, t_eval, inputs=inputs_list
    )
```

### JAX Solver
_Implemented by [Brady Planden (University of Oxford)](https://github.com/BradyPlanden)_

The JAX Solver has been refactored to improve its performance. The default method is now `"BDF"` which has better performance than the previous default `"RK45"`. Bugs related to calculating sensitivities have now been fixed too. For more details please see this [example script](https://github.com/pybamm-team/PyBaMM/blob/v24.11.0/examples/scripts/multiprocess_jax_solver.py).

## DFN model for sodium-ion batteries
_Implemented by [Ferran Brosa Planella (University of Warwick & Ionworks)](https://github.com/brosaplanella)_

PyBaMM now includes a DFN model for sodium-ion batteries. The model is defined identically to that for lithium-ion batteries, but it is a separate class to prevent clashes with unavailable options. The model can be called as `pybamm.sodium_ion.BasicDFN()`. It comes with the parameter set presented in the article by [Chayambuka et al (2022)](https://www.sciencedirect.com/science/article/pii/S0013468621020478). For more details please see the [example notebook](https://docs.pybamm.org/en/stable/source/examples/notebooks/models/sodium-ion.html).

## Sensitivity analysis is available for experiments
_Implemented by [Martin Robinson (Oxford RSE)](https://github.com/martinjrobins)_

The `Simulation` class now supports sensitivity calculation, including when running experiments. This means that the sensitivity of the output variables with respect to the parameters can be calculated when running experiments that switch operating modes (e.g. CCCV). For example, to calculate the sensitivity of the voltage with respect to the initial concentration of lithium in the negative electrode, we can run:

```python3
    model = pybamm.lithium_ion.SPM()

    parameter_values = model.default_parameter_values

    input_param_name = "Negative electrode active material volume fraction"
    input_param_value = param[input_param_name]
    parameter_values.update({input_param_name: "[input]"})

    solver = pybamm.IDAKLUSolver()

    experiment = pybamm.Experiment(
        [
            (
                "Charge at 1C until 4.2 V",
                "Hold at 4.2 V until C/50",
                "Rest for 1 hour",
            )
        ]
    )

    sim = pybamm.Simulation(
        model,
        experiment=experiment,
        solver=solver,
        parameter_values=parameter_values,
    )
    solution = sim.solve(
        inputs={input_param_name: input_param_value},
        calculate_sensitivities=calculate_sensitivities,
    )

    sensitivity = solution["Voltage [V]].sensitivities[input_param_name]
```

## Breaking change in parameter functions dependency
_Implemented by [Robert Timms (Ionworks)](https://github.com/rtimms)_

The parameters `... electrode OCP entropic change [V.K-1]` and `... electrode volume change` are now dependent on stoichiometry only (as opposed to stoichiometry and maximum concentration as they used to be). This means that, when defining custom parameter values, these functions need to be defined as

```python3
def your_entropic_change_function(sto):
    return your_entropic_change_value
```

and

```python3
def your_volume_change_function(sto):
    return your_volume_change_value
```
