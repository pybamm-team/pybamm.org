---
title: PyBaMM 24.9 has been released!
summary: PyBaMM version 24.9 has now been released with several new features and improvements.
date: 2024-09-03
shortcutDepth: 1
---

PyBaMM 24.9 has now been released! This release continues the previous release schedule conforming to three releases a year and marks the third release of 2024. We would like to thank all the [contributors](https://pybamm.org/teams/) who made this release possible.

The full list of changes can be found in the [CHANGELOG](https://pybamm.org/changelog/) file, but here we provide a deeper overview of the main features of this release.

## IDAKLU solver improvements
_Implemented by [Marc Berliner (Ionworks)](https://github.com/MarcBerliner)_

The `IDAKLUSolver` is now significantly faster thanks to changes in its time-stepping behavior. `solve` now returns the solution results at time points determined by its adaptive time-stepping algorithm. As a low-memory option, the adaptive time results can be disabled by specifying a `t_interp` argument or an experiment `period`. Additionally, the `t_eval` argument has been updated to explicitly stop the integration due to discontinuities in the input function, such as with a drive cycle. For example, the fastest way to use the new `IDAKLUSolver` is:

```python3
solver = pybamm.IDAKLUSolver()
model = pybamm.lithium_ion.DFN()
sim = pybamm.Simulation(model, solver=solver)
t_eval = [0, 3600]
sol = sim.solve(t_eval)
```

This will return the solution at the time steps taken by the solver.

Alternatively, to save specific points in time with the new `t_interp` argument, use:

```python3
solver = pybamm.IDAKLUSolver()
model = pybamm.lithium_ion.DFN()
sim = pybamm.Simulation(model, solver=solver)
t_eval = [0, 3600]
t_interp = np.linspace(0, 3600, 100)
sol = sim.solve(t_eval, t_interp=t_interp)
```

This will return the solution at the times specified in `t_interp`.

## Thevenin ECM model with diffusion
_Implemented by [Mehrdad Babazadeh (WMG, University of Warwick)](https://github.com/MehrdadBabazadeh)_

A diffusion component can now be included in the Thevenin equivalent circuit model, based on the work of [Fan et al (2022)](https://doi.org/10.1016/j.apenergy.2022.119336). The model can be called using

```python3
pybamm.equivalent_circuit.Thevenin(options={"diffusion element": "true"})
```

Note than an additional parameter, the `"Diffusion time constant [s]"`, must be provided for the model to run. A full example is available at [examples/scripts/run_ecmd.py](https://github.com/pybamm-team/PyBaMM/blob/develop/examples/scripts/run_ecmd.py).

## Lumped surface thermal model
_Implemented by [Valentin Sulzer (Ionworks)](https://github.com/valentinsulzer)_

A new lumped thermal model has been included to account for different core and surface temperatures, based on the work of [Lin et al (2014)](https://doi.org/10.1016/j.jpowsour.2014.01.097). The new model option `"surface temperature"` can be set to either `"ambient"` or `"lumped"`. e.g.

```python3
pybamm.lithium_ion.SPMe(
    {"thermal": "lumped", "surface temperature": "ambient"},
    name="ambient surface temperature",
)

pybamm.lithium_ion.SPMe(
    {"thermal": "lumped", "surface temperature": "lumped"},
    name="lumped surface temperature",
)
```

Additional parameters `"Casing heat capacity [J.K-1]"` and `"Environment thermal resistance [K.W-1]"` are needed for the model to run. For a full example please see [examples/scripts/compare_surface_temperature.py](https://github.com/pybamm-team/PyBaMM/blob/develop/examples/scripts/compare_surface_temperature.py).
