# 15. Hybrid AI and numerical solvers

[← Back to the main list](../README.md#contents)

Here machine learning works with a classical solver: it speeds up a solve, supplies part of the model, shares the domain or shapes the discretization. This topic also has the tools that connect the two.

Models that mostly replace the solver are under [surrogates](surrogates-and-reduced-order-models.md), networks trained on governing equations under [physics-informed learning](physics-informed-learning-and-energy-methods.md) and standalone material models under [constitutive modeling](constitutive-modeling-and-material-identification.md).

Check where the network acts. If it only preconditions or provides an initial guess, the solver's residual can still control the algebraic error. If it changes the equations, the material law or the solution space, it changes the answer, so validate it outside the training data.

For fluids, see [hybrid AI and CFD](hybrid-ai-and-computational-fluid-dynamics.md).

- [15.1 Learned preconditioners and iterative solvers](#learned-preconditioners-and-iterative-solvers) (5)
- [15.2 Finite element and neural network hybrids](#finite-element-and-neural-network-hybrids) (7)
- [15.3 Connecting machine learning to solvers](#connecting-machine-learning-to-solvers) (8)
- [15.4 Neural subspaces inside simulators](#neural-subspaces-inside-simulators) (4)
- [15.5 Learned physics inside simulators](#learned-physics-inside-simulators) (4)
- [15.6 Learned meshing and coarsening](#learned-meshing-and-coarsening) (2)

## <a id="learned-preconditioners-and-iterative-solvers"></a>15.1 Learned preconditioners and iterative solvers

| Name, language and license | Description | Note |
| --- | --- | --- |
| [DataAnalytics<br>Engineering/<br>UNOCG](https://github.com/DataAnalyticsEngineering/UNOCG)<br><sub>Python</sub><br><sub>MIT</sub> | Neural operator preconditioner for conjugate gradients in thermal and mechanical homogenization. |  |
| [ilayluz/<br>learning-amg](https://github.com/ilayluz/learning-amg)<br><sub>Python</sub><br><sub>none found</sub> | Graph networks that learn prolongation operators for algebraic multigrid. | Requires MATLAB and TensorFlow. |
| [jiechenjiechen/<br>GNP](https://github.com/jiechenjiechen/GNP)<br><sub>Python</sub><br><sub>Apache-2.0</sub> | Graph neural network preconditioner for flexible Krylov methods. | General linear systems, not specific to mechanics. |
| [kopanicakova/<br>HINTS_precond](https://github.com/kopanicakova/HINTS_precond)<br><sub>Python</sub><br><sub>BSD-3-Clause</sub> | Neural operators blended with relaxation and multigrid solvers. | Examples are Poisson and Helmholtz problems, not elasticity. |
| [paulhausner/<br>neural-incomplete-<br>factorization](https://github.com/paulhausner/neural-incomplete-factorization)<br><sub>Python</sub><br><sub>Apache-2.0</sub> | Learned incomplete factorization preconditioners for Krylov solvers. | General linear systems, not specific to mechanics. |

## <a id="finite-element-and-neural-network-hybrids"></a>15.2 Finite element and neural network hybrids

| Name, language and license | Description | Note |
| --- | --- | --- |
| [achraf-15/<br>HiDeNN-FEM](https://github.com/achraf-15/HiDeNN-FEM)<br><sub>Python</sub><br><sub>none found</sub> | Hierarchical neural network finite elements with r-adaptivity, with linear elasticity examples. |  |
| [AlexandreDaby<br>Seesaram/<br>NeuROM](https://github.com/AlexandreDabySeesaram/NeuROM)<br><sub>Python</sub><br><sub>GPL-3.0-or-later (stated in README)</sub> | Reduced-order models that combine finite element interpolation, neural networks and tensor decomposition. | Main branch is being refactored, README recommends a tagged release. |
| [Centrum-Intelli<br>Physics/<br>Time-Marching-<br>Neural-Operator-<br>FE-Coupling](https://github.com/Centrum-IntelliPhysics/Time-Marching-Neural-Operator-FE-Coupling)<br><sub>Python</sub><br><sub>Apache-2.0</sub> | Finite elements coupled to a neural operator by overlapping domain decomposition, for solid mechanics. | Paper code. |
| [Centrum-Intelli<br>Physics/<br>Time-Marching-Non-<br>overlapping-<br>Neural-operator-<br>FE-Coupling](https://github.com/Centrum-IntelliPhysics/Time-Marching-Non-overlapping-Neural-operator-FE-Coupling)<br><sub>Python</sub><br><sub>none found</sub> | Non-overlapping coupling of finite elements and neural operators, including elastodynamics. | Paper code. |
| [Francesco<br>Regazzoni/<br>Neural-DFEM](https://github.com/FrancescoRegazzoni/Neural-DFEM)<br><sub>Python</sub><br><sub>BSD-3-Clause</sub> | Hyperelastic neural models trained through differentiable finite elements. | Paper code; requires FEniCS and dolfin-adjoint. |
| [MiroK/<br>fem-nets](https://github.com/MiroK/fem-nets)<br><sub>Python</sub><br><sub>MIT</sub> | Finite element function spaces represented as PyTorch networks. | Built on legacy FEniCS. |
| [sebastkm/<br>hybrid-fem-nn-<br>examples](https://github.com/sebastkm/hybrid-fem-nn-examples)<br><sub>Python</sub><br><sub>none found</sub> | Examples of neural networks trained inside finite element models. | Paper code; examples include transport, not solid mechanics. |

## <a id="connecting-machine-learning-to-solvers"></a>15.3 Connecting machine learning to solvers

| Name, language and license | Description | Note |
| --- | --- | --- |
| [a-latyshev/<br>dolfinx-external-<br>operator](https://github.com/a-latyshev/dolfinx-external-operator)<br><sub>Python</sub><br><sub>LGPL-3.0-or-later</sub> | External operators in FEniCSx, for constitutive models written in PyTorch, JAX or NumPy. |  |
| [barkm/<br>torch-fenics](https://github.com/barkm/torch-fenics)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | FEniCS models used as differentiable PyTorch modules. | Built on legacy FEniCS. |
| [Cambridge-ICCS/<br>FTorch](https://github.com/Cambridge-ICCS/FTorch)<br><sub>Fortran</sub><br><sub>MIT</sub> | Library for calling PyTorch models from Fortran solvers. | General-purpose, not specific to mechanics. |
| [erc-automatix/<br>jaxmat](https://github.com/erc-automatix/jaxmat)<br><sub>Python</sub><br><sub>LGPL-3.0-or-later</sub> | Material models in JAX that connect machine learning to finite element software. |  |
| [IvanYashchuk/<br>jax-fenics-adjoint](https://github.com/IvanYashchuk/jax-fenics-adjoint)<br><sub>Python</sub><br><sub>MIT</sub> | Differentiable FEniCS and Firedrake solves inside JAX programs. | Built on legacy FEniCS. |
| [marius-duvillard/<br>jax2mfront](https://github.com/marius-duvillard/jax2mfront)<br><sub>Jupyter Notebook</sub><br><sub>none found</sub> | Worked export of neural network material laws from JAX to MFront. |  |
| [nbouziani/<br>physics-driven-ml](https://github.com/nbouziani/physics-driven-ml)<br><sub>Python</sub><br><sub>MIT</sub> | PyTorch models coupled to Firedrake PDE solvers and trained through them. | The included example is heat conduction. |
| [USArmyResearchLab/<br>PyVUMAT](https://github.com/USArmyResearchLab/PyVUMAT)<br><sub>Python</sub><br><sub>CC0-1.0</sub> | Machine learning material models in Python, run as Abaqus VUMAT subroutines. | Examples require Abaqus. |

## <a id="neural-subspaces-inside-simulators"></a>15.4 Neural subspaces inside simulators

| Name, language and license | Description | Note |
| --- | --- | --- |
| [Changy1506/<br>LiCROM_all](https://github.com/Changy1506/LiCROM_all)<br><sub>Python</sub><br><sub>none found, with NVIDIA-restricted files</sub> | Linear-subspace reduced simulation of deformable solids with neural fields. | Some NVIDIA file headers forbid use without a license agreement; README says the code is preliminary. |
| [nmwsharp/<br>neural-physics-<br>subspaces](https://github.com/nmwsharp/neural-physics-subspaces)<br><sub>Python</sub><br><sub>MIT</sub> | Neural subspaces for physical simulation, trained without a dataset. |  |
| [NVIDIAGameWorks/<br>kaolin (Simplicits)](https://github.com/NVIDIAGameWorks/kaolin/tree/master/kaolin/physics/simplicits)<br><sub>Python</sub><br><sub>Apache-2.0</sub> | Simplicits, mesh-free elastic simulation in a learned neural skinning basis. | Other legacy parts of Kaolin are non-commercial. |
| [peterchencyc/<br>CROM_online_<br>deployment](https://github.com/peterchencyc/CROM_online_deployment)<br><sub>Python</sub><br><sub>none found</sub> | Time stepping in a neural latent space, with soft-body elasticity examples. | Online stage of CROM only. |

## <a id="learned-physics-inside-simulators"></a>15.5 Learned physics inside simulators

| Name, language and license | Description | Note |
| --- | --- | --- |
| [erwincoumans/<br>tiny-<br>differentiable-<br>simulator](https://github.com/erwincoumans/tiny-differentiable-simulator)<br><sub>C++</sub><br><sub>Apache-2.0</sub> | Differentiable rigid body simulator that supports neural augmentation of its physics. | Bundled components have their own licenses. |
| [NVlabs/<br>neural-robot-<br>dynamics](https://github.com/NVlabs/neural-robot-dynamics)<br><sub>Python</sub><br><sub>Apache-2.0</sub> | Learned dynamics and contact model that replaces low-level solvers inside NVIDIA Warp. | Articulated rigid bodies only. |
| [PingchuanMa/<br>NCLaw](https://github.com/PingchuanMa/NCLaw)<br><sub>Python</sub><br><sub>none found, with non-commercial bundled Warp</sub> | Neural constitutive laws learned from motion through a material point simulator. | The bundled copy of NVIDIA Warp allows non-commercial use only. |
| [srl-ethz/<br>residual_physics_<br>sim2real](https://github.com/srl-ethz/residual_physics_sim2real)<br><sub>Python and C++</sub><br><sub>MIT</sub> | Learned residual forces that correct a soft-body simulator against real robots. | Paper code; modified from DiffPD. |

## <a id="learned-meshing-and-coarsening"></a>15.6 Learned meshing and coarsening

| Name, language and license | Description | Note |
| --- | --- | --- |
| [farenga/<br>meshGNN](https://github.com/farenga/meshGNN)<br><sub>MATLAB and Python</sub><br><sub>none found</sub> | Graph network agglomeration of polygonal meshes for multigrid solvers. | Experiments require MATLAB; bundled components have their own licenses. |
| [mesh-adaptation/<br>UM2N](https://github.com/mesh-adaptation/UM2N)<br><sub>Python</sub><br><sub>MIT</sub> | Neural mesh movement to improve the accuracy of PDE solvers. | Evaluated on flow, transport and model PDE problems. |

[← Back to the main list](../README.md#contents)
