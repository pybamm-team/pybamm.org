---
title: PyBaMM Roadmap
summary: This page is a working document of the main features PyBaMM aims to provide
---

This page contains a summary of the main features we are working towards and might provide ideas for funding applications.

The fact that an item is listed in this roadmap does not mean that it will necessarily happen. On the other hand, an item not being listed in the roadmap does not mean it cannot be included in the future. Note that the ideas here correspond to big features, smaller features will still be tracked in the [issue tracker](https://github.com/pybamm-team/PyBaMM/issues).

## Additional battery models

We strive to keep PyBaMM up with the state-of-the-art in battery models, which advances in two different directions:

1. Include additional effects and physics (e.g. thermal, degradation...) for existing battery chemistries (e.g. lithium-ion, lead-acid..).
2. Implement models for new chemistries (e.g. sodium-ion, lithium-air...).

## Integration with other platforms & packages

Currently, PyBaMM runs on Python, though it can generate CasADI code (which runs on C). We would like to extend our capabilities so we can generate code for our models on other platforms, and also make PyBaMM compatible with other packages. Some of the platforms & packages we would like to interface PyBaMM with are

- Julia
- Cantera

## Improve documentation

We would like to improve the content, structure and presentation of the documentation. Some specific goals include:

- Self-hosting (similar to scipy)
- Better design
- Dependency trees
- Link to examples where various functionality is used (similar to scikit-learn)
- Show output and runtime of examples (notebooks and scripts) (similar to scikit-learn)

## Performance

We aim to continuously improve PyBaMM's performance. Performance is monitored via [airspeed velocity](https://asv.readthedocs.io/en/stable/). The work on this area has two main fronts:

1. Improving the benchmark suite (available at https://pybamm.org/benchmarks) to monitor the code better.
2. Reformat the backend of the code to make it more efficient.

## Suggestions

If you have any suggestions for this roadmap, please feel free to open a [discussion](https://github.com/pybamm-team/PyBaMM/discussions).
