# 20. Verification, validation and uncertainty

[← Back to the main list](../README.md#contents)

These answer different questions, and passing one does not imply passing the others.

- **Code verification**: are the equations implemented correctly? Compare observed and expected convergence rates on exact or manufactured solutions ([Roache, 2002](https://doi.org/10.1115/1.1436090)).
- **Solution verification**: how large is the numerical error in this result? Study mesh, time step and solver tolerances ([Roy, 2005](https://doi.org/10.1016/j.jcp.2004.10.036)). Make sure the quantity can converge: stresses at singular points do not, and nor do results that depend on localized softening without regularization.
- **Validation**: does the model represent reality for its intended use? Compare with experiments relevant to that use that were not used for calibration, allow for their measurement uncertainty and state the range they cover. Agreement with another simulation does not by itself show agreement with reality. If a higher-fidelity model is the reference, as NASA-STD-7009B allows for surrogates, say so.
- **Uncertainty quantification**: how much do uncertain inputs, model form and numerical error affect the prediction ([Roy and Oberkampf, 2011](https://doi.org/10.1016/j.cma.2011.03.016))?

Guidance: [ASME V&V 10](https://webstore.ansi.org/standards/asme/asme102019r2025) for solid mechanics (paid), [ASME V&V 20 and V&V 40](https://www.asme.org/codes-standards/publications-information/verification-validation-uncertainty) for fluids and heat transfer and for medical devices (paid), [NASA-STD-7009B](https://standards.nasa.gov/sites/default/files/standards/NASA/B/1/NASA-STD-7009B-Final-3-5-2024.pdf) for models and simulations, [ten rules for credible simulation in healthcare](https://doi.org/10.1186/s12967-020-02540-4) and the book by [Oberkampf and Roy (2010)](https://doi.org/10.1017/CBO9780511760396). Cardiac benchmarks that compare codes, which is not validation against experiments: [Land et al. (2015)](https://doi.org/10.1098/rspa.2015.0641) and [Aróstica et al. (2025)](https://doi.org/10.1016/j.cma.2024.117485).

- [20.1 Code and solution verification](#code-and-solution-verification) (4)
- [20.2 Benchmarks and reference solutions](#benchmarks-and-reference-solutions) (8)
- [20.3 Experimental data for validation](#experimental-data-for-validation) (4)
- [20.4 Calibration and Bayesian inference](#calibration-and-bayesian-inference) (4)
- [20.5 Uncertainty and sensitivity analysis](#uncertainty-and-sensitivity-analysis) (13)

## <a id="code-and-solution-verification"></a>20.1 Code and solution verification

| Name, language and license | Description | Note |
| --- | --- | --- |
| [lanl/<br>ExactPack](https://github.com/lanl/ExactPack)<br><sub>Python</sub><br><sub>BSD-3-Clause</sub> | Exact solutions of verification problems in solids, heat conduction and hydrodynamics. | Solid mechanics covers the Blake and elastic-plastic piston problems. |
| [manufactured-<br>solutions/<br>MASA](https://github.com/manufactured-solutions/MASA)<br><sub>C++</sub><br><sub>LGPL-2.1</sub> | Library of manufactured solutions for verifying PDE solvers. | Examples are mainly heat transfer and fluid flow. |
| [OSEL-DAM/<br>SimEval](https://github.com/OSEL-DAM/SimEval)<br><sub>Python and Jupyter Notebook</sub><br><sub>CC0-1.0</sub> | Notebooks on code and calculation verification, including for physics-informed networks. |  |
| [tomrobin-teschner/<br>pyGCS](https://github.com/tomrobin-teschner/pyGCS)<br><sub>Python</sub><br><sub>MIT</sub> | Grid convergence index calculations for estimating discretization error. |  |

## <a id="benchmarks-and-reference-solutions"></a>20.2 Benchmarks and reference solutions

| Name, language and license | Description | Note |
| --- | --- | --- |
| [febiosoftware/<br>TestSuite](https://github.com/febiosoftware/TestSuite)<br><sub>Python</sub><br><sub>none found</sub> | FEBio test problems with stored results for regression testing. | Regression results are not independent reference solutions; no README. |
| [finsberg/<br>cardiac_benchmark](https://github.com/finsberg/cardiac_benchmark)<br><sub>Python</sub><br><sub>MIT (stated in README)</sub> | Simula's implementation of a published cardiac elastodynamics benchmark. |  |
| [javijv4/<br>arostica-benchmark](https://github.com/javijv4/arostica-benchmark)<br><sub>Python</sub><br><sub>none found</sub> | Cardiac elastodynamics test against the envelope of ten published solutions. | Requires svMultiPhysics. |
| [Kratos<br>Multiphysics/<br>Examples (contact)](https://github.com/KratosMultiphysics/Examples/tree/master/contact_structural_mechanics/validation)<br><sub>Python</sub><br><sub>none found</sub> | Kratos contact benchmarks, including Hertz, press-fit and ironing cases. |  |
| [Kratos<br>Multiphysics/<br>Examples (structural)](https://github.com/KratosMultiphysics/Examples/tree/master/structural_mechanics/validation)<br><sub>Python</sub><br><sub>none found</sub> | Kratos benchmarks for beams, trusses and membranes, including large deflection and snap-through. |  |
| [Simulation-<br>Benchmarks/<br>linear-elastic-<br>plate-with-hole](https://github.com/Simulation-Benchmarks/linear-elastic-plate-with-hole)<br><sub>Python</sub><br><sub>MIT code, CC-BY-4.0 docs, CC0-1.0 data</sub> | Plate-with-hole benchmark comparing finite element codes with the Kirsch solution. |  |
| [Simulation-<br>Benchmarks/<br>NFDI4IngModel<br>ValidationPlatform](https://github.com/Simulation-Benchmarks/NFDI4IngModelValidationPlatform)<br><sub>Python and Jupyter Notebook</sub><br><sub>MIT</sub> | Registry and shared workflows for reproducible simulation benchmarks. |  |
| [TadeasSvetlik/<br>Elastoplastic-<br>contact-2D-<br>benchmarks](https://github.com/TadeasSvetlik/Elastoplastic-contact-2D-benchmarks)<br><sub>MATLAB</sub><br><sub>none found</sub> | Inputs and reference results for 2D elastic and elastoplastic contact benchmarks. | Written for MATLAB, Octave support not documented; no README. |

## <a id="experimental-data-for-validation"></a>20.3 Experimental data for validation

| Name, language and license | Description | Note |
| --- | --- | --- |
| [dlr-wf/<br>crackmnist](https://github.com/dlr-wf/crackmnist)<br><sub>Python</sub><br><sub>MIT code, CC-BY-4.0 data (stated in README)</sub> | Annotated displacement fields measured by image correlation in fatigue crack growth tests. |  |
| [llamm-de/<br>thermalCANN](https://github.com/llamm-de/thermalCANN/tree/main/data/Treloar)<br><sub>Python</sub><br><sub>MIT</sub> | Treloar's rubber data for uniaxial, equibiaxial and pure shear loading, as republished in 2012. | The Arruda-Boyce file is a model fit, not measured data. |
| [sanjayg0/<br>epcms](https://github.com/sanjayg0/epcms)<br><sub>MATLAB</sub><br><sub>MIT</sub> | Continuum mechanics example codes with tension test data for steel and aluminum. | Written for MATLAB, Octave support not documented. |
| [Simulation-<br>Benchmarks/<br>four-point-<br>bending-test](https://github.com/Simulation-Benchmarks/four-point-bending-test)<br><sub>Python</sub><br><sub>none found</sub> | Reinforced concrete beam benchmark with deflections and strains from a 1963 experiment. | The finite element models require Ansys. |

## <a id="calibration-and-bayesian-inference"></a>20.4 Calibration and Bayesian inference

| Name, language and license | Description | Note |
| --- | --- | --- |
| [BAMresearch/<br>probeye](https://github.com/BAMresearch/probeye)<br><sub>Python</sub><br><sub>MIT</sub> | Solver-independent definition of parameter estimation problems, mainly solved by sampling. |  |
| [CUQI-DTU/<br>CUQIpy](https://github.com/CUQI-DTU/CUQIpy)<br><sub>Python</sub><br><sub>Apache-2.0</sub> | Bayesian modeling and uncertainty quantification for inverse problems. |  |
| [hippylib/<br>hippylib](https://github.com/hippylib/hippylib)<br><sub>Python</sub><br><sub>GPL-2.0</sub> | Deterministic and Bayesian inversion for models governed by PDEs. |  |
| [sandialabs/<br>matcal](https://github.com/sandialabs/matcal)<br><sub>Python</sub><br><sub>BSD-3-Clause</sub> | Calibration of material models to experimental data. | Built-in characterization test models are for SierraSM. |

## <a id="uncertainty-and-sensitivity-analysis"></a>20.5 Uncertainty and sensitivity analysis

| Name, language and license | Description | Note |
| --- | --- | --- |
| [damar-wicaksono/<br>uqtestfuns](https://github.com/damar-wicaksono/uqtestfuns)<br><sub>Python</sub><br><sub>MIT</sub> | Test functions for benchmarking uncertainty quantification methods. |  |
| [febiosoftware/<br>FEBioUncertainSCI](https://github.com/febiosoftware/FEBioUncertainSCI)<br><sub>Python</sub><br><sub>MIT</sub> | Uncertainty and sensitivity analysis of FEBio models with UncertainSCI. |  |
| [idaholab/<br>raven](https://github.com/idaholab/raven)<br><sub>Python</sub><br><sub>Apache-2.0</sub> | Sampling-based risk, validation and uncertainty analysis of complex system codes. |  |
| [jonathf/<br>chaospy](https://github.com/jonathf/chaospy)<br><sub>Python</sub><br><sub>MIT</sub> | Uncertainty propagation with polynomial chaos expansions and quasi-Monte Carlo sampling. |  |
| [openturns/<br>openturns](https://github.com/openturns/openturns)<br><sub>C++</sub><br><sub>LGPL-3.0-or-later</sub> | Probabilistic modeling, reliability and uncertainty propagation. |  |
| [SALib/<br>SALib](https://github.com/SALib/SALib)<br><sub>Python</sub><br><sub>MIT</sub> | Global sensitivity analysis with Sobol, Morris, FAST and other methods. |  |
| [sandialabs/<br>pyapprox](https://github.com/sandialabs/pyapprox)<br><sub>Python</sub><br><sub>MIT</sub> | Surrogate, multifidelity and uncertainty methods for expensive simulations. |  |
| [SCIInstitute/<br>UncertainSCI](https://github.com/SCIInstitute/UncertainSCI)<br><sub>Python</sub><br><sub>MIT</sub> | Non-intrusive parametric uncertainty analysis for biomedical simulations. |  |
| [snl-dakota/<br>dakota](https://github.com/snl-dakota/dakota)<br><sub>C++</sub><br><sub>LGPL-2.1-or-later</sub> | Toolkit for uncertainty, sensitivity, calibration and design studies around existing solvers. |  |
| [SURGroup/<br>UQpy](https://github.com/SURGroup/UQpy)<br><sub>Python</sub><br><sub>MIT</sub> | Toolbox for modeling uncertainty in physical and mathematical systems. |  |
| [UCL-CCS/<br>EasyVVUQ](https://github.com/UCL-CCS/EasyVVUQ)<br><sub>Python</sub><br><sub>LGPL-3.0-or-later or GPL-3.0-or-later</sub> | Workflow manager for verification, validation and uncertainty studies of costly simulations. |  |
| [UM-Bridge/<br>benchmarks](https://github.com/UM-Bridge/benchmarks)<br><sub>Python</sub><br><sub>GPL-3.0-or-later in some files</sub> | Containerized models and reference problems for testing uncertainty algorithms. |  |
| [UM-Bridge/<br>umbridge](https://github.com/UM-Bridge/umbridge)<br><sub>C++</sub><br><sub>MIT</sub> | Language-independent interface between simulation models and uncertainty software. |  |

[← Back to the main list](../README.md#contents)
