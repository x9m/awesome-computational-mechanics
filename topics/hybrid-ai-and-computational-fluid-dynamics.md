# 16. Hybrid AI and computational fluid dynamics

[← Back to the main list](../README.md#contents)

Here machine learning works with flow solvers: it learns closures and corrections, speeds up solves or controls flows. Differentiable solvers and coupling tools built for this are included. General CFD codes are not. Models that mostly replace the solver, and datasets to train them, are under [surrogates](surrogates-and-reduced-order-models.md).

Test learned closures inside the solver. A model can fit high-fidelity data well and still be inaccurate or unstable once coupled, and may not carry over to other geometries, Reynolds numbers or meshes.

Further reading: [Duraisamy et al. (2019)](https://doi.org/10.1146/annurev-fluid-010518-040547) on turbulence modeling with data, and [Agdestein and Sanderse (2025)](https://doi.org/10.1016/j.jcp.2024.113577) on closures that match the discretization.

- [16.1 Differentiable CFD for machine learning](#differentiable-cfd-for-machine-learning) (8)
- [16.2 Learned turbulence closures](#learned-turbulence-closures) (8)
- [16.3 Learned correction and acceleration](#learned-correction-and-acceleration) (6)
- [16.4 Connecting machine learning to CFD codes](#connecting-machine-learning-to-cfd-codes) (5)
- [16.5 Reinforcement learning with flow solvers](#reinforcement-learning-with-flow-solvers) (4)

## <a id="differentiable-cfd-for-machine-learning"></a>16.1 Differentiable CFD for machine learning

| Name, language and license | Description | Note |
| --- | --- | --- |
| [Autodesk/<br>XLB](https://github.com/Autodesk/XLB)<br><sub>Python</sub><br><sub>Apache-2.0</sub> | Differentiable lattice Boltzmann library for physics-based machine learning. |  |
| [lettucecfd/<br>lettuce](https://github.com/lettucecfd/lettuce)<br><sub>Python</sub><br><sub>MIT</sub> | Lattice Boltzmann framework in PyTorch that integrates neural networks. |  |
| [scaomath/<br>torch-cfd](https://github.com/scaomath/torch-cfd)<br><sub>Python</sub><br><sub>Apache-2.0, with MIT files</sub> | PyTorch flow solvers combined with neural operators. |  |
| [tum-pbs/<br>diffSPH](https://github.com/tum-pbs/diffSPH)<br><sub>Python</sub><br><sub>Apache-2.0</sub> | Differentiable smoothed particle hydrodynamics for adjoints and machine learning. |  |
| [tum-pbs/<br>PhiFlow](https://github.com/tum-pbs/PhiFlow)<br><sub>Python</sub><br><sub>MIT</sub> | Differentiable simulation toolkit that combines fluid solvers with machine learning frameworks. |  |
| [tum-pbs/<br>PICT](https://github.com/tum-pbs/PICT)<br><sub>Python and CUDA</sub><br><sub>Apache-2.0</sub> | Differentiable multi-block PISO solver for learning coupled to simulation. | Requires CUDA. |
| [tumaer/<br>jax-sph](https://github.com/tumaer/jax-sph)<br><sub>Python</sub><br><sub>MIT, with Apache-2.0 JAX MD files</sub> | Differentiable smoothed particle hydrodynamics framework in JAX. |  |
| [tumaer/<br>JAXFLUIDS](https://github.com/tumaer/JAXFLUIDS)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Differentiable compressible single-phase and two-phase flow solver for research on machine learning in CFD. |  |

## <a id="learned-turbulence-closures"></a>16.2 Learned turbulence closures

| Name, language and license | Description | Note |
| --- | --- | --- |
| [agdestein/<br>Divergence<br>Consistency](https://github.com/agdestein/DivergenceConsistency)<br><sub>Julia</sub><br><sub>MIT, by component</sub> | Divergence-consistent neural closures trained inside large-eddy simulations. | Paper code. |
| [agdestein/<br>SymmetryCode.jl](https://github.com/agdestein/SymmetryCode.jl)<br><sub>Julia</sub><br><sub>MIT</sub> | Symmetry-preserving learned closures compared inside a spectral flow solver. | Paper code. |
| [argonne-lcf/<br>TensorFlowFoam](https://github.com/argonne-lcf/TensorFlowFoam)<br><sub>C++</sub><br><sub>MIT, with GPL OpenFOAM files</sub> | Tutorials on neural turbulence models and in-situ training in OpenFOAM. | Requires OpenFOAM 5.0 and TensorFlow 1.15. |
| [mthsmcd/<br>MachineLearning<br>TurbulenceModels](https://github.com/mthsmcd/MachineLearningTurbulenceModels)<br><sub>C++</sub><br><sub>GPL-3.0</sub> | OpenFOAM turbulence models driven by machine learning predictions. | Requires OpenFOAM. |
| [sandialabs/<br>tbnn](https://github.com/sandialabs/tbnn)<br><sub>Python</sub><br><sub>BSD-3-Clause</sub> | Tensor basis neural networks for turbulence and other models with known invariances. | Built on Theano and Lasagne; last commit in 2018. |
| [sayin/<br>Data_Driven_<br>Symbolic_<br>Regression](https://github.com/sayin/Data_Driven_Symbolic_Regression)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Symbolic and sparse regression for equation and subgrid closure discovery. | Paper code; last commit in 2021. |
| [tum-pbs/<br>differentiable-<br>piso](https://github.com/tum-pbs/differentiable-piso)<br><sub>Python</sub><br><sub>MIT</sub> | Turbulence models trained through a differentiable PISO solver. | Paper code; requires TensorFlow 1.14. |
| [xiaoh/<br>DAFI](https://github.com/xiaoh/DAFI)<br><sub>Python and C++</sub><br><sub>Apache-2.0, with GPL OpenFOAM files</sub> | Ensemble data assimilation, including learning turbulence closures from sparse data. |  |

## <a id="learned-correction-and-acceleration"></a>16.3 Learned correction and acceleration

| Name, language and license | Description | Note |
| --- | --- | --- |
| [ayano721/<br>2023_DCDM](https://github.com/ayano721/2023_DCDM)<br><sub>Python</sub><br><sub>none found</sub> | Network that replaces the search direction in iterative pressure solves. | Paper code. |
| [kai-lan/<br>MLPCG](https://github.com/kai-lan/MLPCG)<br><sub>Python and C++</sub><br><sub>none found</sub> | Neural preconditioner for pressure Poisson solves with mixed boundary conditions. | Paper code; requires CUDA. |
| [locuslab/<br>cfd-gcn](https://github.com/locuslab/cfd-gcn)<br><sub>Python</sub><br><sub>none found</sub> | Graph network with a differentiable SU2 solver embedded in it. | Paper code; a Dockerfile builds the dependencies. |
| [tum-pbs/<br>DiffPhys-Cylinder<br>WakeFlow](https://github.com/tum-pbs/DiffPhys-CylinderWakeFlow)<br><sub>Jupyter Notebook</sub><br><sub>MIT</sub> | Coarse differentiable solver with a network that corrects cylinder wake flows. | Paper code. |
| [tum-pbs/<br>Hybrid-Solver-for-<br>Reactive-Flows](https://github.com/tum-pbs/Hybrid-Solver-for-Reactive-Flows)<br><sub>Python</sub><br><sub>MIT</sub> | Networks that supply unknown physics to a reactive flow solver. | Paper code. |
| [tum-pbs/<br>Solver-in-the-Loop](https://github.com/tum-pbs/Solver-in-the-Loop)<br><sub>Python</sub><br><sub>MIT</sub> | Learned corrections trained through iterative PDE solvers, with flow examples. | Paper code; built on older TensorFlow and PhiFlow. |

## <a id="connecting-machine-learning-to-cfd-codes"></a>16.4 Connecting machine learning to CFD codes

| Name, language and license | Description | Note |
| --- | --- | --- |
| [argonne-lcf/<br>PythonFOAM](https://github.com/argonne-lcf/PythonFOAM)<br><sub>C++</sub><br><sub>BSD-3-Clause, with GPL OpenFOAM files</sub> | OpenFOAM solvers that call Python for in-situ analysis and learning. | Requires OpenFOAM. |
| [CrayLabs/<br>SmartSim](https://github.com/CrayLabs/SmartSim)<br><sub>Python</sub><br><sub>BSD-2-Clause</sub> | Workflow library for using machine learning inside high-performance simulations. | General-purpose, not specific to CFD. |
| [deepmodeling/<br>deepflame-dev](https://github.com/deepmodeling/deepflame-dev)<br><sub>C++</sub><br><sub>GPL-3.0</sub> | Reacting flow platform joining OpenFOAM, Cantera and PyTorch. | Requires OpenFOAM and Cantera. |
| [OFDataCommittee/<br>openfoam-smartsim](https://github.com/OFDataCommittee/openfoam-smartsim)<br><sub>C++</sub><br><sub>GPL-3.0-or-later</sub> | OpenFOAM module that embeds SmartSim in simulations. | Requires OpenFOAM. |
| [Weishuo93/<br>NN_Pred](https://github.com/Weishuo93/NN_Pred)<br><sub>C++ and Fortran</sub><br><sub>MIT, with LGPL and Apache-2.0 parts</sub> | Library that deploys trained models inside OpenFOAM and CFL3D. |  |

## <a id="reinforcement-learning-with-flow-solvers"></a>16.5 Reinforcement learning with flow solvers

| Name, language and license | Description | Note |
| --- | --- | --- |
| [dynamicslab/<br>hydrogym](https://github.com/dynamicslab/hydrogym)<br><sub>Python</sub><br><sub>MIT</sub> | Reinforcement learning environments for flow control on several CFD solvers. |  |
| [flexi-framework/<br>relexi](https://github.com/flexi-framework/relexi)<br><sub>Python</sub><br><sub>GPL-3.0-or-later</sub> | Reinforcement learning on HPC systems for the FLEXI flow solver. | Built on TensorFlow and SmartSim. |
| [OFDataCommittee/<br>drlfoam](https://github.com/OFDataCommittee/drlfoam)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Deep reinforcement learning with OpenFOAM simulations. | Requires OpenFOAM. |
| [venturi123/<br>DRLinFluids](https://github.com/venturi123/DRLinFluids)<br><sub>Python</sub><br><sub>Apache-2.0, with GPL OpenFOAM files</sub> | Platform that couples deep reinforcement learning to OpenFOAM. | Requires OpenFOAM. |

[← Back to the main list](../README.md#contents)
