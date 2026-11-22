# Awesome Computational Mechanics

**443 entries for computational mechanics, from finite elements and soft tissue to solvers and validation**, with licenses, commercial-software requirements and known usage restrictions noted.

<p align="center">
<img src="assets/banner.png" width="420" alt="A soft cube with circular cuts at 0, 25 and 50 mm of stretch, colored by displacement">
<br>
<sub>Soft-tissue cube simulated with <a href="https://github.com/x9m/JANP-DJTLED-GPU">JANP-DJTLED</a> (<a href="assets/LICENSE">MIT</a>)</sub>
</p>

## Start here

| I want to | Start with | Then browse |
| --- | --- | --- |
| Learn finite elements | [Imperial College course](https://github.com/finite-element/finite-element-course) | [Teaching and compact codes](#user-content-open-finite-and-boundary-element-methods--teaching-and-compact-codes) |
| Write a solver in Python | [scikit-fem](https://github.com/kinnala/scikit-fem) | [General-purpose frameworks](#user-content-open-finite-and-boundary-element-methods--general-purpose-frameworks) |
| Simulate soft tissue | [FEBio](https://github.com/febiosoftware/FEBio) | [Real-time finite elements](#user-content-open-soft-body-real-time-and-differentiable-simulation--real-time-finite-elements) |
| Model contact | [IPC Toolkit](https://github.com/ipc-sim/ipc-toolkit) | [Contact mechanics](#user-content-open-contact-mechanics) |
| Learn material laws from data | [EUCLID](https://github.com/EUCLID-code/EUCLID-hyperelasticity) | [Unsupervised model discovery](#user-content-open-constitutive-modeling-and-material-identification--unsupervised-model-discovery) |
| Try virtual elements | [50 lines of VEM](https://github.com/oliversutton/50LinesOfVEM) | [Virtual element method](#user-content-open-virtual-element-method) |
| Solve large systems | [PETSc](https://gitlab.com/petsc/petsc) | [Linear, eigenvalue and nonlinear solvers](#user-content-open-linear-eigenvalue-and-nonlinear-solvers) |
| Verify and validate a model | [SimEval](https://github.com/OSEL-DAM/SimEval) | [Verification, validation and uncertainty](#user-content-open-verification-validation-and-uncertainty) |

## Contents

1. [Finite and boundary element methods](#user-content-open-finite-and-boundary-element-methods) (77)
2. [Finite volume methods](#user-content-open-finite-volume-methods) (1)
3. [Virtual element method](#user-content-open-virtual-element-method) (30)
4. [Contact mechanics](#user-content-open-contact-mechanics) (9)
5. [Third medium contact](#user-content-open-third-medium-contact) (13)
6. [Meshfree and particle methods](#user-content-open-meshfree-and-particle-methods) (28)
7. [Soft-body, real-time and differentiable simulation](#user-content-open-soft-body-real-time-and-differentiable-simulation) (26)
8. [Multibody dynamics and biomechanics](#user-content-open-multibody-dynamics-and-biomechanics) (10)
9. [Constitutive modeling and material identification](#user-content-open-constitutive-modeling-and-material-identification) (38)
10. [Multiscale and homogenization](#user-content-open-multiscale-and-homogenization) (12)
11. [Thermal, multiphysics and additive manufacturing](#user-content-open-thermal-multiphysics-and-additive-manufacturing) (11)
12. [Optimization and inverse problems](#user-content-open-optimization-and-inverse-problems) (18)
13. [Physics-informed learning and energy methods](#user-content-open-physics-informed-learning-and-energy-methods) (14)
14. [Surrogates and reduced-order models](#user-content-open-surrogates-and-reduced-order-models) (34)
15. [Meshing, pre- and post-processing](#user-content-open-meshing-pre--and-post-processing) (23)
16. [Linear, eigenvalue and nonlinear solvers](#user-content-open-linear-eigenvalue-and-nonlinear-solvers) (35)
17. [Verification, validation and uncertainty](#user-content-open-verification-validation-and-uncertainty) (33)
18. [Courses, references and agents for mechanics](#user-content-open-courses-references-and-agents-for-mechanics) (31)

<details>
<summary>All 81 sub-topics</summary>

1. [Finite and boundary element methods](#user-content-open-finite-and-boundary-element-methods) (77)<br>
   1.1 [General-purpose frameworks](#user-content-open-finite-and-boundary-element-methods--general-purpose-frameworks) (20)<br>
   1.2 [Structural and solid mechanics solvers](#user-content-open-finite-and-boundary-element-methods--structural-and-solid-mechanics-solvers) (16)<br>
   1.3 [Differentiable and GPU finite elements](#user-content-open-finite-and-boundary-element-methods--differentiable-and-gpu-finite-elements) (7)<br>
   1.4 [Phase-field fracture](#user-content-open-finite-and-boundary-element-methods--phase-field-fracture) (6)<br>
   1.5 [Fracture, boundary and scaled boundary methods](#user-content-open-finite-and-boundary-element-methods--fracture-boundary-and-scaled-boundary-methods) (5)<br>
   1.6 [Unfitted and embedded methods](#user-content-open-finite-and-boundary-element-methods--unfitted-and-embedded-methods) (1)<br>
   1.7 [Smoothed finite elements](#user-content-open-finite-and-boundary-element-methods--smoothed-finite-elements) (1)<br>
   1.8 [Beams, rods and shells](#user-content-open-finite-and-boundary-element-methods--beams-rods-and-shells) (3)<br>
   1.9 [Solver interfaces and utilities](#user-content-open-finite-and-boundary-element-methods--solver-interfaces-and-utilities) (5)<br>
   1.10 [Teaching and compact codes](#user-content-open-finite-and-boundary-element-methods--teaching-and-compact-codes) (13)
2. [Finite volume methods](#user-content-open-finite-volume-methods) (1)<br>
   2.1 [Solid mechanics and fluid-solid interaction](#user-content-open-finite-volume-methods--solid-mechanics-and-fluid-solid-interaction) (1)
3. [Virtual element method](#user-content-open-virtual-element-method) (30)<br>
   3.1 [VEM libraries](#user-content-open-virtual-element-method--vem-libraries) (6)<br>
   3.2 [Elasticity](#user-content-open-virtual-element-method--elasticity) (9)<br>
   3.3 [Dynamics and fracture](#user-content-open-virtual-element-method--dynamics-and-fracture) (3)<br>
   3.4 [Coupled fields and electronic packaging](#user-content-open-virtual-element-method--coupled-fields-and-electronic-packaging) (4)<br>
   3.5 [Topology optimization with VEM](#user-content-open-virtual-element-method--topology-optimization-with-vem) (2)<br>
   3.6 [Introductory VEM codes](#user-content-open-virtual-element-method--introductory-vem-codes) (6)
4. [Contact mechanics](#user-content-open-contact-mechanics) (9)<br>
   4.1 [Contact formulations](#user-content-open-contact-mechanics--contact-formulations) (4)<br>
   4.2 [Incremental potential contact](#user-content-open-contact-mechanics--incremental-potential-contact) (5)
5. [Third medium contact](#user-content-open-third-medium-contact) (13)<br>
   5.1 [Modules and examples in FEM libraries](#user-content-open-third-medium-contact--modules-and-examples-in-fem-libraries) (7)<br>
   5.2 [Optimization and metamaterials](#user-content-open-third-medium-contact--optimization-and-metamaterials) (4)<br>
   5.3 [Standalone study codes](#user-content-open-third-medium-contact--standalone-study-codes) (2)
6. [Meshfree and particle methods](#user-content-open-meshfree-and-particle-methods) (28)<br>
   6.1 [Material point method](#user-content-open-meshfree-and-particle-methods--material-point-method) (11)<br>
   6.2 [Smoothed particle hydrodynamics](#user-content-open-meshfree-and-particle-methods--smoothed-particle-hydrodynamics) (4)<br>
   6.3 [Meshless methods](#user-content-open-meshfree-and-particle-methods--meshless-methods) (5)<br>
   6.4 [Peridynamics](#user-content-open-meshfree-and-particle-methods--peridynamics) (3)<br>
   6.5 [Discrete and coarse-grained particle models](#user-content-open-meshfree-and-particle-methods--discrete-and-coarse-grained-particle-models) (5)
7. [Soft-body, real-time and differentiable simulation](#user-content-open-soft-body-real-time-and-differentiable-simulation) (26)<br>
   7.1 [Real-time finite elements](#user-content-open-soft-body-real-time-and-differentiable-simulation--real-time-finite-elements) (7)<br>
   7.2 [Soft robotics](#user-content-open-soft-body-real-time-and-differentiable-simulation--soft-robotics) (6)<br>
   7.3 [Position-based and implicit dynamics](#user-content-open-soft-body-real-time-and-differentiable-simulation--position-based-and-implicit-dynamics) (4)<br>
   7.4 [Differentiable simulation](#user-content-open-soft-body-real-time-and-differentiable-simulation--differentiable-simulation) (6)<br>
   7.5 [Manipulation benchmarks](#user-content-open-soft-body-real-time-and-differentiable-simulation--manipulation-benchmarks) (3)
8. [Multibody dynamics and biomechanics](#user-content-open-multibody-dynamics-and-biomechanics) (10)<br>
   8.1 [Physics engines for multibody systems](#user-content-open-multibody-dynamics-and-biomechanics--physics-engines-for-multibody-systems) (6)<br>
   8.2 [Musculoskeletal biomechanics](#user-content-open-multibody-dynamics-and-biomechanics--musculoskeletal-biomechanics) (2)<br>
   8.3 [Cardiovascular mechanics](#user-content-open-multibody-dynamics-and-biomechanics--cardiovascular-mechanics) (2)
9. [Constitutive modeling and material identification](#user-content-open-constitutive-modeling-and-material-identification) (38)<br>
   9.1 [Neural network constitutive models](#user-content-open-constitutive-modeling-and-material-identification--neural-network-constitutive-models) (15)<br>
   9.2 [Unsupervised model discovery](#user-content-open-constitutive-modeling-and-material-identification--unsupervised-model-discovery) (7)<br>
   9.3 [Material subroutines and libraries](#user-content-open-constitutive-modeling-and-material-identification--material-subroutines-and-libraries) (10)<br>
   9.4 [Experimental parameter identification](#user-content-open-constitutive-modeling-and-material-identification--experimental-parameter-identification) (6)
10. [Multiscale and homogenization](#user-content-open-multiscale-and-homogenization) (12)<br>
    10.1 [FFT-based homogenization](#user-content-open-multiscale-and-homogenization--fft-based-homogenization) (3)<br>
    10.2 [FE² and computational homogenization](#user-content-open-multiscale-and-homogenization--fe2-and-computational-homogenization) (3)<br>
    10.3 [Inverse homogenization](#user-content-open-multiscale-and-homogenization--inverse-homogenization) (1)<br>
    10.4 [Crystal plasticity](#user-content-open-multiscale-and-homogenization--crystal-plasticity) (5)
11. [Thermal, multiphysics and additive manufacturing](#user-content-open-thermal-multiphysics-and-additive-manufacturing) (11)<br>
    11.1 [Heat transfer and bio-heat](#user-content-open-thermal-multiphysics-and-additive-manufacturing--heat-transfer-and-bio-heat) (5)<br>
    11.2 [Thermoelasticity](#user-content-open-thermal-multiphysics-and-additive-manufacturing--thermoelasticity) (1)<br>
    11.3 [Additive manufacturing](#user-content-open-thermal-multiphysics-and-additive-manufacturing--additive-manufacturing) (3)<br>
    11.4 [Multiphysics coupling](#user-content-open-thermal-multiphysics-and-additive-manufacturing--multiphysics-coupling) (2)
12. [Optimization and inverse problems](#user-content-open-optimization-and-inverse-problems) (18)<br>
    12.1 [Topology optimization solvers](#user-content-open-optimization-and-inverse-problems--topology-optimization-solvers) (9)<br>
    12.2 [Learning-based topology optimization](#user-content-open-optimization-and-inverse-problems--learning-based-topology-optimization) (5)<br>
    12.3 [Inverse problems](#user-content-open-optimization-and-inverse-problems--inverse-problems) (4)
13. [Physics-informed learning and energy methods](#user-content-open-physics-informed-learning-and-energy-methods) (14)<br>
    13.1 [Deep energy methods](#user-content-open-physics-informed-learning-and-energy-methods--deep-energy-methods) (8)<br>
    13.2 [Residual-based networks](#user-content-open-physics-informed-learning-and-energy-methods--residual-based-networks) (4)<br>
    13.3 [PINN libraries and examples](#user-content-open-physics-informed-learning-and-energy-methods--pinn-libraries-and-examples) (2)
14. [Surrogates and reduced-order models](#user-content-open-surrogates-and-reduced-order-models) (34)<br>
    14.1 [Stress-field prediction](#user-content-open-surrogates-and-reduced-order-models--stress-field-prediction) (7)<br>
    14.2 [Deformation and reduced dynamics](#user-content-open-surrogates-and-reduced-order-models--deformation-and-reduced-dynamics) (7)<br>
    14.3 [Projection-based model reduction](#user-content-open-surrogates-and-reduced-order-models--projection-based-model-reduction) (4)<br>
    14.4 [Graph neural networks](#user-content-open-surrogates-and-reduced-order-models--graph-neural-networks) (4)<br>
    14.5 [Biomechanical surrogates](#user-content-open-surrogates-and-reduced-order-models--biomechanical-surrogates) (2)<br>
    14.6 [Response histories and operator learning](#user-content-open-surrogates-and-reduced-order-models--response-histories-and-operator-learning) (6)<br>
    14.7 [Frameworks and introductory studies](#user-content-open-surrogates-and-reduced-order-models--frameworks-and-introductory-studies) (3)<br>
    14.8 [Benchmark datasets](#user-content-open-surrogates-and-reduced-order-models--benchmark-datasets) (1)
15. [Meshing, pre- and post-processing](#user-content-open-meshing-pre--and-post-processing) (23)<br>
    15.1 [Mesh generation](#user-content-open-meshing-pre--and-post-processing--mesh-generation) (13)<br>
    15.2 [Mesh processing and formats](#user-content-open-meshing-pre--and-post-processing--mesh-processing-and-formats) (5)<br>
    15.3 [Visualization and export](#user-content-open-meshing-pre--and-post-processing--visualization-and-export) (5)
16. [Linear, eigenvalue and nonlinear solvers](#user-content-open-linear-eigenvalue-and-nonlinear-solvers) (35)<br>
    16.1 [Solver toolkits](#user-content-open-linear-eigenvalue-and-nonlinear-solvers--solver-toolkits) (4)<br>
    16.2 [Dense linear algebra](#user-content-open-linear-eigenvalue-and-nonlinear-solvers--dense-linear-algebra) (4)<br>
    16.3 [Sparse direct solvers](#user-content-open-linear-eigenvalue-and-nonlinear-solvers--sparse-direct-solvers) (6)<br>
    16.4 [Iterative solvers and preconditioners](#user-content-open-linear-eigenvalue-and-nonlinear-solvers--iterative-solvers-and-preconditioners) (8)<br>
    16.5 [Nonlinear solvers, time integration and continuation](#user-content-open-linear-eigenvalue-and-nonlinear-solvers--nonlinear-solvers-time-integration-and-continuation) (5)<br>
    16.6 [Eigenvalue solvers](#user-content-open-linear-eigenvalue-and-nonlinear-solvers--eigenvalue-solvers) (4)<br>
    16.7 [Matrix-free operators and partitioning](#user-content-open-linear-eigenvalue-and-nonlinear-solvers--matrix-free-operators-and-partitioning) (4)
17. [Verification, validation and uncertainty](#user-content-open-verification-validation-and-uncertainty) (33)<br>
    17.1 [Code and solution verification](#user-content-open-verification-validation-and-uncertainty--code-and-solution-verification) (4)<br>
    17.2 [Benchmarks and reference solutions](#user-content-open-verification-validation-and-uncertainty--benchmarks-and-reference-solutions) (8)<br>
    17.3 [Experimental data for validation](#user-content-open-verification-validation-and-uncertainty--experimental-data-for-validation) (4)<br>
    17.4 [Calibration and Bayesian inference](#user-content-open-verification-validation-and-uncertainty--calibration-and-bayesian-inference) (4)<br>
    17.5 [Uncertainty and sensitivity analysis](#user-content-open-verification-validation-and-uncertainty--uncertainty-and-sensitivity-analysis) (13)
18. [Courses, references and agents for mechanics](#user-content-open-courses-references-and-agents-for-mechanics) (31)<br>
    18.1 [Courses and tutorials](#user-content-open-courses-references-and-agents-for-mechanics--courses-and-tutorials) (16)<br>
    18.2 [Element definitions and form languages](#user-content-open-courses-references-and-agents-for-mechanics--element-definitions-and-form-languages) (5)<br>
    18.3 [Reproducible research software](#user-content-open-courses-references-and-agents-for-mechanics--reproducible-research-software) (2)<br>
    18.4 [Curated lists](#user-content-open-courses-references-and-agents-for-mechanics--curated-lists) (5)<br>
    18.5 [Agents for mechanics](#user-content-open-courses-references-and-agents-for-mechanics--agents-for-mechanics) (3)

</details>

[Archived and unmaintained projects](archive.md) (6)

[Contributing](#contributing)

<details>
<summary><a id="finite-and-boundary-element-methods"></a><h2>1. Finite and boundary element methods</h2></summary>
<p id="open-finite-and-boundary-element-methods"><sub><b>1. Finite and boundary element methods</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><a id="general-purpose-frameworks"></a><h3>1.1 General-purpose frameworks</h3></summary>
<p id="open-finite-and-boundary-element-methods--general-purpose-frameworks"><sub>Finite and boundary element methods › <b>1.1 General-purpose frameworks</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [dealii/<br>dealii](https://github.com/dealii/dealii)<br><sub>C++</sub><br><sub>Apache-2.0 with LLVM exception, or LGPL-2.1-or-later</sub> | Library for solving PDEs with adaptive finite elements. |  |
| [ElmerCSC/<br>elmerfem](https://github.com/ElmerCSC/elmerfem)<br><sub>Fortran</sub><br><sub>GPL-2.0 and LGPL-2.1, by component</sub> | Multiphysics finite element suite that includes structural mechanics. | The bundled TetGen plugin is AGPL-3.0. |
| [FEniCS/<br>dolfinx](https://github.com/FEniCS/dolfinx)<br><sub>C++</sub><br><sub>LGPL-3.0</sub> | Computational environment of FEniCSx for solving PDEs with finite elements in C++ and Python. |  |
| [Ferrite-FEM/<br>Ferrite.jl](https://github.com/Ferrite-FEM/Ferrite.jl)<br><sub>Julia</sub><br><sub>MIT</sub> | Finite element toolbox for Julia. |  |
| [firedrakeproject/<br>firedrake](https://github.com/firedrakeproject/firedrake)<br><sub>Python</sub><br><sub>LGPL-3.0-or-later</sub> | Automated system for solving PDEs with the finite element method. |  |
| [FreeFem/<br>FreeFem-sources](https://github.com/FreeFem/FreeFem-sources)<br><sub>C++</sub><br><sub>LGPL-3.0</sub> | Finite element solver for nonlinear multiphysics PDEs in 2D and 3D. |  |
| [gridap/<br>Gridap.jl](https://github.com/gridap/Gridap.jl)<br><sub>Julia</sub><br><sub>MIT</sub> | Tools for grid-based approximation of linear and nonlinear PDEs. |  |
| [idaholab/<br>moose](https://github.com/idaholab/moose)<br><sub>C++</sub><br><sub>LGPL-2.1</sub> | Finite element and finite volume framework for multiphysics simulation. |  |
| [kinnala/<br>scikit-fem](https://github.com/kinnala/scikit-fem)<br><sub>Python</sub><br><sub>BSD-3-Clause</sub> | Lightweight library for finite element assembly. |  |
| [Kratos<br>Multiphysics/<br>Kratos](https://github.com/KratosMultiphysics/Kratos)<br><sub>C++</sub><br><sub>BSD-4-Clause (core), with restricted Triangle code</sub> | Framework for parallel multidisciplinary simulation software. | Each application has its own license; bundled Triangle restricts commercial distribution. |
| [libMesh/<br>libmesh](https://github.com/libMesh/libmesh)<br><sub>C++</sub><br><sub>LGPL-2.1, with restricted bundled components</sub> | Library for parallel adaptive finite element simulations. | Bundled Triangle restricts commercial distribution; bundled TetGen is AGPL-3.0; bundled ParMETIS has only an emailed permission, not a license. |
| [lyc102/<br>ifem](https://github.com/lyc102/ifem)<br><sub>MATLAB</sub><br><sub>GPL-3.0</sub> | Adaptive finite element package for 2D and 3D simplicial grids. | Written for MATLAB, Octave support not documented. |
| [mfem/<br>mfem](https://github.com/mfem/mfem)<br><sub>C++</sub><br><sub>BSD-3-Clause</sub> | Modular parallel library for scalable finite element methods. |  |
| [NGSolve/<br>ngsolve](https://github.com/NGSolve/ngsolve)<br><sub>C++</sub><br><sub>LGPL-2.1</sub> | Multiphysics finite element software with a Python interface. |  |
| [polyfem/<br>polyfem](https://github.com/polyfem/polyfem)<br><sub>C++</sub><br><sub>MIT</sub> | General-purpose C++ finite element library. |  |
| [sandialabs/<br>Albany](https://github.com/sandialabs/Albany)<br><sub>C++</sub><br><sub>BSD-3-Clause</sub> | Implicit unstructured-grid finite element code for multiphysics problems. | Solid mechanics capabilities have moved to [Albany-LCM](https://github.com/sandialabs/LCM). |
| [sfepy/<br>sfepy](https://github.com/sfepy/sfepy)<br><sub>Python</sub><br><sub>BSD-3-Clause</sub> | Finite element solver and library for coupled PDEs in 1D, 2D and 3D. |  |
| [Terenceyuyue/<br>varFEM](https://github.com/Terenceyuyue/varFEM)<br><sub>MATLAB</sub><br><sub>GPL-3.0</sub> | Finite element programming in a variational-form style. | Written for MATLAB, Octave support not documented. |
| [TLCFEM/<br>suanPan](https://github.com/TLCFEM/suanPan)<br><sub>C++</sub><br><sub>GPL-3.0-or-later, with restricted MC64 code</sub> | Parallel and heterogeneous finite element analysis framework. | Bundled MC64 may not be passed to third parties without its authors' consent. |
| [weihuayi/<br>fealpy](https://github.com/weihuayi/fealpy)<br><sub>Python</sub><br><sub>GPL-3.0-or-later with added notice</sub> | Python finite element library for algorithm research and computer-aided engineering. | License notice also restricts commercial use; bundled TetGen is AGPL-3.0. |

</details>

<details>
<summary><a id="structural-and-solid-mechanics-solvers"></a><h3>1.2 Structural and solid mechanics solvers</h3></summary>
<p id="open-finite-and-boundary-element-methods--structural-and-solid-mechanics-solvers"><sub>Finite and boundary element methods › <b>1.2 Structural and solid mechanics solvers</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [code_aster](https://gitlab.com/codeaster/src)<br><sub>Python, C++ and Fortran</sub><br><sub>GPL-3.0</sub> | Source of code_aster, a finite element solver for structural mechanics. | Some validation and material data are not freely distributed. |
| [Dhondtguido/<br>CalculiX](https://github.com/Dhondtguido/CalculiX)<br><sub>Fortran</sub><br><sub>GPL-2.0</sub> | Three-dimensional structural finite element program. |  |
| [dmitryikh/<br>nla3d](https://github.com/dmitryikh/nla3d)<br><sub>C++</sub><br><sub>MIT</sub> | C++ framework for writing nonlinear finite element codes in solid mechanics. |  |
| [febiosoftware/<br>FEBio](https://github.com/febiosoftware/FEBio)<br><sub>C++</sub><br><sub>MIT</sub> | Nonlinear finite element solver designed for biomechanics. |  |
| [FrontISTR/<br>FrontISTR](https://github.com/FrontISTR/FrontISTR)<br><sub>Fortran and C</sub><br><sub>MIT</sub> | Large-scale parallel nonlinear structural analysis with contact and heat conduction. | GitHub repository is a mirror; development is on GitLab. |
| [isaar/<br>MSolve](https://github.com/isaar/MSolve)<br><sub>C#</sub><br><sub>Apache-2.0</sub> | C# solver for computational mechanics problems. |  |
| [JWock82/<br>Pynite](https://github.com/JWock82/Pynite)<br><sub>Python</sub><br><sub>MIT</sub> | 3D structural analysis library with static, P-Delta, modal and pushover analysis. |  |
| [llnl/<br>smith](https://github.com/llnl/smith)<br><sub>C++</sub><br><sub>BSD-3-Clause</sub> | 3D implicit nonlinear thermal-structural code built on MFEM. | README calls it a pre-alpha release. |
| [MystranSolver/<br>MYSTRANSolver](https://github.com/MystranSolver/MYSTRANSolver)<br><sub>Fortran</sub><br><sub>MIT</sub> | General-purpose structural finite element analysis solver. |  |
| [nasa/<br>NASTRAN-95](https://github.com/nasa/NASTRAN-95)<br><sub>Fortran</sub><br><sub>NASA Open Source Agreement 1.3</sub> | NASA's historical structural analysis system for static, dynamic and stability problems. | No technical support. |
| [oofem/<br>oofem](https://github.com/oofem/oofem)<br><sub>C++</sub><br><sub>LGPL-2.1</sub> | Object-oriented finite element code for mechanical, transport and fluid problems. |  |
| [OpenCourant/<br>OpenCourant](https://github.com/OpenCourant/OpenCourant)<br><sub>Fortran</sub><br><sub>AGPL-3.0</sub> | Explicit finite element solver for crash, impact and other dynamic events. | Community fork created after OpenRadioss was withdrawn in October 2026; not affiliated with Siemens or Altair. |
| [OpenSees/<br>OpenSees](https://github.com/OpenSees/OpenSees)<br><sub>C++</sub><br><sub>custom, with commercial restrictions</sub> | Framework for structural and geotechnical earthquake engineering simulation. | Commercial distribution requires permission from the University of California; bundled MC64, Triangle and TetGen have their own restrictions. |
| [peer-open-source/<br>xara](https://github.com/peer-open-source/xara)<br><sub>C++</sub><br><sub>BSD-2-Clause, with restricted OpenSees code</sub> | Python package for nonlinear finite element analysis built on OpenSees. | Bundled OpenSees files prohibit commercial use without permission from the University of California; bundled MC64, Triangle and TetGen have their own restrictions. |
| [sandialabs/<br>Norma.jl](https://github.com/sandialabs/Norma.jl)<br><sub>Julia</sub><br><sub>BSD-3-Clause</sub> | Julia prototype for coupling and multiphysics algorithms in solid mechanics. | Research prototype. |
| [sanjayg0/<br>feappv](https://github.com/sanjayg0/feappv)<br><sub>Fortran</sub><br><sub>BSD-3-Clause</sub> | Free personal version of the FEAP finite element program. | Lacks some FEAP features, including contact and parallel solving. |

</details>

<details>
<summary><a id="differentiable-and-gpu-finite-elements"></a><h3>1.3 Differentiable and GPU finite elements</h3></summary>
<p id="open-finite-and-boundary-element-methods--differentiable-and-gpu-finite-elements"><sub>Finite and boundary element methods › <b>1.3 Differentiable and GPU finite elements</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [camlab-ethz/<br>TensorMesh](https://github.com/camlab-ethz/TensorMesh)<br><sub>Python</sub><br><sub>Apache-2.0</sub> | Differentiable finite element library built on PyTorch. |  |
| [deepmodeling/<br>jax-fem](https://github.com/deepmodeling/jax-fem)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Differentiable finite element package built on JAX. |  |
| [kailaix/<br>AdFem.jl](https://github.com/kailaix/AdFem.jl)<br><sub>Julia and C++</sub><br><sub>MIT</sub> | Differentiable finite element operators for inverse modeling. |  |
| [liangbright/<br>pytorch_fea_paper](https://github.com/liangbright/pytorch_fea_paper)<br><sub>Python</sub><br><sub>none found</sub> | Differentiable finite element analysis applied to human aorta biomechanics. | Paper code; the author's refactored successor is [pytorch_fea](https://github.com/liangbright/pytorch_fea). |
| [mo-hanxuan/<br>FEMcy](https://github.com/mo-hanxuan/FEMcy)<br><sub>Python</sub><br><sub>MIT</sub> | Taichi-based parallel structural finite element solver with small and large deformation. |  |
| [sandialabs/<br>optimism](https://github.com/sandialabs/optimism)<br><sub>Python</sub><br><sub>MIT</sub> | JAX finite element library that poses nonlinear solid mechanics as optimization. |  |
| [zclsjtu/<br>DiffSolid](https://github.com/zclsjtu/DiffSolid)<br><sub>Python</sub><br><sub>proprietary</sub> | Differentiable JAX finite element framework for solid mechanics and phase-field fracture. | The implementation is not open source; the repository has examples and documentation, and wheels are provided on request. |

</details>

<details>
<summary><a id="phase-field-fracture"></a><h3>1.4 Phase-field fracture</h3></summary>
<p id="open-finite-and-boundary-element-methods--phase-field-fracture"><sub>Finite and boundary element methods › <b>1.4 Phase-field fracture</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [CastillonMiguel/<br>phasefieldx](https://github.com/CastillonMiguel/phasefieldx)<br><sub>Python</sub><br><sub>MIT</sub> | Phase-field simulation framework built on FEniCSx. |  |
| [ehsanhaghighat/<br>PhaseField-DSD](https://github.com/ehsanhaghighat/PhaseField-DSD)<br><sub>Java</sub><br><sub>MIT</sub> | Phase-field shear fracture using a deviatoric stress split. | Requires COMSOL. |
| [hugary1995/<br>raccoon](https://github.com/hugary1995/raccoon)<br><sub>C++</sub><br><sub>LGPL-2.1</sub> | Massively parallel phase-field fracture code built on MOOSE. |  |
| [hyoungsuksuh/<br>micropolar_<br>phasefield](https://github.com/hyoungsuksuh/micropolar_phasefield)<br><sub>Python</sub><br><sub>CC-BY-4.0</sub> | Phase-field cohesive fracture in micropolar continua with FEniCS. |  |
| [LuoXueling/<br>deal.II-phase-<br>field-fracture](https://github.com/LuoXueling/deal.II-phase-field-fracture)<br><sub>C++</sub><br><sub>MIT</sub> | Phase-field fracture in deal.II with multiphysics interfaces, adaptive meshes and MPI. | Mesh input uses Abaqus input files. |
| [nsundar/<br>PFM_UMAT_Elasto<br>Plastic](https://github.com/nsundar/PFM_UMAT_ElastoPlastic)<br><sub>Fortran</sub><br><sub>MIT</sub> | Phase-field damage in elastoplastic solids as a UMAT. | Requires Abaqus. |

</details>

<details>
<summary><a id="fracture-boundary-and-scaled-boundary-methods"></a><h3>1.5 Fracture, boundary and scaled boundary methods</h3></summary>
<p id="open-finite-and-boundary-element-methods--fracture-boundary-and-scaled-boundary-methods"><sub>Finite and boundary element methods › <b>1.5 Fracture, boundary and scaled boundary methods</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [ChongminSong/<br>Platypus](https://github.com/ChongminSong/Platypus)<br><sub>MATLAB</sub><br><sub>none found</sub> | Code accompanying a textbook on the scaled boundary finite element method. | Written for MATLAB, Octave support not documented. |
| [nsundar/<br>cp-sbfem](https://github.com/nsundar/cp-sbfem)<br><sub>Fortran and Julia</sub><br><sub>MIT</sub> | Scaled boundary finite elements for crystal plasticity as an Abaqus UELMAT. | Requires Abaqus. |
| [Qinxiaoye/<br>SBFEM2D](https://github.com/Qinxiaoye/SBFEM2D)<br><sub>MATLAB</sub><br><sub>none found</sub> | Scaled boundary finite element method for 2D linear elasticity. | Written for MATLAB, Octave support not documented; modified from code by Chongmin Song; some files are copyright Terence Yu, with no license in this repository. |
| [ShelvanLee/<br>XFEM](https://github.com/ShelvanLee/XFEM)<br><sub>MATLAB</sub><br><sub>MIT</sub> | Extended finite element program for multiple crack propagation in 2D linear elastic solids. | Written for MATLAB, Octave support not documented. |
| [Timmmdavis/<br>CutAndDisplace](https://github.com/Timmmdavis/CutAndDisplace)<br><sub>MATLAB</sub><br><sub>GPL-3.0</sub> | Boundary element code for faults and deformation. | Runs in MATLAB, also tested in Octave with some issues; README restricts use to academia, although the license is GPL-3.0. |

</details>

<details>
<summary><a id="unfitted-and-embedded-methods"></a><h3>1.6 Unfitted and embedded methods</h3></summary>
<p id="open-finite-and-boundary-element-methods--unfitted-and-embedded-methods"><sub>Finite and boundary element methods › <b>1.6 Unfitted and embedded methods</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [gridap/<br>GridapEmbedded.jl](https://github.com/gridap/GridapEmbedded.jl)<br><sub>Julia</sub><br><sub>MIT</sub> | Embedded finite element methods, level sets and constructive solid geometry. |  |

</details>

<details>
<summary><a id="smoothed-finite-elements"></a><h3>1.7 Smoothed finite elements</h3></summary>
<p id="open-finite-and-boundary-element-methods--smoothed-finite-elements"><sub>Finite and boundary element methods › <b>1.7 Smoothed finite elements</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [nsundar/<br>SFEM_in_Abaqus](https://github.com/nsundar/SFEM_in_Abaqus)<br><sub>Fortran and MATLAB</sub><br><sub>GPL-3.0</sub> | Strain smoothing finite elements implemented in Abaqus. | Requires Abaqus; includes MATLAB scripts. |

</details>

<details>
<summary><a id="beams-rods-and-shells"></a><h3>1.8 Beams, rods and shells</h3></summary>
<p id="open-finite-and-boundary-element-methods--beams-rods-and-shells"><sub>Finite and boundary element methods › <b>1.8 Beams, rods and shells</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [precice/<br>fem-shell](https://github.com/precice/fem-shell)<br><sub>C++</sub><br><sub>LGPL-3.0</sub> | Flat shell finite element solver for coupled fluid-structure simulation. |  |
| [sofa-framework/<br>BeamAdapter](https://github.com/sofa-framework/BeamAdapter)<br><sub>C++</sub><br><sub>LGPL-2.1</sub> | Adaptive Kirchhoff rod elements for catheters, guidewires and other flexible structures. | Requires SOFA. |
| [SofaDefrost/<br>Cosserat](https://github.com/SofaDefrost/Cosserat)<br><sub>C++ and Python</sub><br><sub>LGPL-3.0</sub> | Cosserat beam models of rods, wires and needles. | Requires SOFA; source headers state LGPL-2.1-or-later. |

</details>

<details>
<summary><a id="solver-interfaces-and-utilities"></a><h3>1.9 Solver interfaces and utilities</h3></summary>
<p id="open-finite-and-boundary-element-methods--solver-interfaces-and-utilities"><sub>Finite and boundary element methods › <b>1.9 Solver interfaces and utilities</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [ansys/<br>pymapdl](https://github.com/ansys/pymapdl)<br><sub>Python</sub><br><sub>MIT</sub> | Python interface to the Ansys MAPDL solver. | Requires a licensed copy of Ansys. |
| [ansys/<br>pymechanical](https://github.com/ansys/pymechanical)<br><sub>Python</sub><br><sub>MIT</sub> | Python interface to Ansys Mechanical. | Requires a licensed copy of Ansys Mechanical. |
| [cristobaltapia/<br>pybaqus](https://github.com/cristobaltapia/pybaqus)<br><sub>Python</sub><br><sub>MIT</sub> | Import and post-processing of Abaqus ASCII result files without an Abaqus license. | README says it is at a very early stage. |
| [febiosoftware/<br>pyfebio](https://github.com/febiosoftware/pyfebio)<br><sub>Python</sub><br><sub>MIT</sub> | Python package for writing FEBio input and converting its results. |  |
| [lcharleux/<br>abapy](https://github.com/lcharleux/abapy)<br><sub>Python</sub><br><sub>GPL-2.0</sub> | Finite element pre- and post-processing in Python. | No README. |

</details>

<details>
<summary><a id="teaching-and-compact-codes"></a><h3>1.10 Teaching and compact codes</h3></summary>
<p id="open-finite-and-boundary-element-methods--teaching-and-compact-codes"><sub>Finite and boundary element methods › <b>1.10 Teaching and compact codes</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [abuganza/<br>NonlinearFEA](https://github.com/abuganza/NonlinearFEA)<br><sub>Jupyter Notebook</sub><br><sub>GPL-3.0</sub> | Course notebooks on nonlinear finite element analysis. |  |
| [AppliedMechanics-<br>EAFIT/<br>Introductory-<br>Finite-Elements](https://github.com/AppliedMechanics-EAFIT/Introductory-Finite-Elements)<br><sub>Jupyter Notebook</sub><br><sub>MIT code, CC-BY-4.0 content (stated in README)</sub> | Teaching notebooks for an introductory finite element course. |  |
| [AppliedMechanics-<br>EAFIT/<br>SolidsPy](https://github.com/AppliedMechanics-EAFIT/SolidsPy)<br><sub>Python</sub><br><sub>MIT</sub> | Simple finite element code for 2D elasticity. |  |
| [dilevin/<br>CSC417-a3-finite-<br>elements-3d](https://github.com/dilevin/CSC417-a3-finite-elements-3d)<br><sub>C++</sub><br><sub>none found</sub> | Course assignment on 3D finite element simulation of elastic objects. | Starter code for an assignment. |
| [hplgit/<br>fem-book](https://github.com/hplgit/fem-book)<br><sub>Python</sub><br><sub>MIT</sub> | Sources and examples for a book on numerical methods for variational problems. |  |
| [hplgit/<br>fenics-tutorial](https://github.com/hplgit/fenics-tutorial)<br><sub>TeX</sub><br><sub>none found</sub> | Sources and example programs for the FEniCS Tutorial book. | Bundled Triangle restricts commercial distribution. |
| [jjcremmers/<br>PyFEM](https://github.com/jjcremmers/PyFEM)<br><sub>Python</sub><br><sub>MIT</sub> | Educational and research finite element code for nonlinear solid mechanics. |  |
| [largurajr/<br>FEA-Protus](https://github.com/largurajr/FEA-Protus)<br><sub>Python</sub><br><sub>none found</sub> | Teaching code for 2D plane stress and plane strain finite element analysis. | Python 2.7. |
| [Qinxiaoye/<br>FEM2D](https://github.com/Qinxiaoye/FEM2D)<br><sub>MATLAB</sub><br><sub>none found</sub> | MATLAB code for 2D finite element analysis. | Written for MATLAB, Octave support not documented; input scripts use Ansys or Abaqus. |
| [Qinxiaoye/<br>FEM2D_dynamic](https://github.com/Qinxiaoye/FEM2D_dynamic)<br><sub>MATLAB</sub><br><sub>none found</sub> | Finite element elastodynamics with Newmark time integration. | Written for MATLAB, Octave support not documented; input scripts use Ansys or Abaqus. |
| [Qinxiaoye/<br>FEM3D-C3D8-](https://github.com/Qinxiaoye/FEM3D-C3D8-)<br><sub>MATLAB</sub><br><sub>none found</sub> | MATLAB finite element code with 3D hexahedral element routines. | Written for MATLAB, Octave support not documented; README calls it 2D; input scripts use Ansys or Abaqus. |
| [Qinxiaoye/<br>xpfem](https://github.com/Qinxiaoye/xpfem)<br><sub>Python</sub><br><sub>none found</sub> | Linear elastic finite element package with quadrilateral, hexahedral and B-bar elements. |  |
| [tjfulle/<br>fem-with-python](https://github.com/tjfulle/fem-with-python)<br><sub>Python</sub><br><sub>MIT (stated in README)</sub> | Course notes, assignments and code for an introductory finite element course. |  |

</details>

</details>

<details>
<summary><a id="finite-volume-methods"></a><h2>2. Finite volume methods</h2></summary>
<p id="open-finite-volume-methods"><sub><b>2. Finite volume methods</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><a id="solid-mechanics-and-fluid-solid-interaction"></a><h3>2.1 Solid mechanics and fluid-solid interaction</h3></summary>
<p id="open-finite-volume-methods--solid-mechanics-and-fluid-solid-interaction"><sub>Finite volume methods › <b>2.1 Solid mechanics and fluid-solid interaction</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [solids4foam/<br>solids4foam](https://github.com/solids4foam/solids4foam)<br><sub>C++</sub><br><sub>GPL-3.0</sub> | Toolbox for solid mechanics and fluid-solid interaction in OpenFOAM. | Requires OpenFOAM. |

</details>

</details>

<details>
<summary><a id="virtual-element-method"></a><h2>3. Virtual element method</h2></summary>
<p id="open-virtual-element-method"><sub><b>3. Virtual element method</b> · <a href="#contents">Back to contents</a></sub></p>

The virtual element method (VEM) generalizes finite elements to polygonal and polyhedral elements.

<details>
<summary><a id="vem-libraries"></a><h3>3.1 VEM libraries</h3></summary>
<p id="open-virtual-element-method--vem-libraries"><sub>Virtual element method › <b>3.1 VEM libraries</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [CAMLAB-UChile/<br>vemlab](https://github.com/CAMLAB-UChile/vemlab)<br><sub>MATLAB</sub><br><sub>GPL-3.0</sub> | MATLAB library for linear VEM in 2D elastostatics and Poisson problems. | Runs in MATLAB, or in Octave with small changes described in its README. |
| [cemcen/<br>Veamy](https://github.com/cemcen/Veamy)<br><sub>C++</sub><br><sub>GPL (stated in README), with restricted Triangle code</sub> | Object-oriented C++ library for VEM in 2D elastostatics and Poisson problems. | Bundled Triangle restricts commercial distribution. |
| [dune-fem/<br>dune-vem](https://gitlab.dune-project.org/dune-fem/dune-vem)<br><sub>C++ and Python</sub><br><sub>GPL-2.0-or-later</sub> | DUNE module with a range of virtual element spaces and a Python interface. |  |
| [SINTEF-AppliedComp<br>Sci/<br>MRST](https://github.com/SINTEF-AppliedCompSci/MRST/tree/main/solvers/vemmech)<br><sub>MATLAB</sub><br><sub>GPL-3.0</sub> | VEM mechanics module of the MATLAB Reservoir Simulation Toolbox. | Part of a larger toolbox that runs in MATLAB or Octave; the toolbox bundles Triangle, which restricts commercial distribution. |
| [Terenceyuyue/<br>mVEM](https://github.com/Terenceyuyue/mVEM)<br><sub>MATLAB</sub><br><sub>GPL-3.0</sub> | MATLAB package of virtual element methods published in the literature. | Written for MATLAB, Octave support not documented. |
| [tiagomhrd/<br>ves](https://github.com/tiagomhrd/ves)<br><sub>C++</sub><br><sub>MIT</sub> | Helper library of projectors for several virtual element formulations. |  |

</details>

<details>
<summary><a id="elasticity"></a><h3>3.2 Elasticity</h3></summary>
<p id="open-virtual-element-method--elasticity"><sub>Virtual element method › <b>3.2 Elasticity</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [chauj96/<br>vem_implementation](https://github.com/chauj96/vem_implementation)<br><sub>MATLAB</sub><br><sub>none found</sub> | Mixed and hybridized VEM for 3D linear elasticity on polyhedral meshes. | Written for MATLAB, Octave support not documented; bundled METIS 4 has a copyright notice but no license terms. |
| [DongxiaoLyu/<br>polymesh](https://github.com/DongxiaoLyu/polymesh)<br><sub>JavaScript</sub><br><sub>MIT</sub> | VEM Studio Online, a browser-based polygonal mesher and VEM solver for 2D elasticity and heat conduction. |  |
| [Moopz99/<br>VEMK2](https://github.com/Moopz99/VEMK2)<br><sub>MATLAB</sub><br><sub>GPL-3.0</sub> | Quadratic VEM for 2D elasticity. | Written for MATLAB, Octave support not documented. |
| [mySimpleProjects/<br>SimpleVEM](https://github.com/mySimpleProjects/SimpleVEM)<br><sub>MATLAB</sub><br><sub>GPL-3.0</sub> | Comparison of FEM and VEM for 2D structural analysis. | Requires MATLAB with the Curve Fitting and Optimization toolboxes. |
| [noahherrmann/<br>Comparison-of-the-<br>Virtual-and-<br>Finite-Element-<br>Method](https://github.com/noahherrmann/Comparison-of-the-Virtual-and-Finite-Element-Method)<br><sub>MATLAB</sub><br><sub>none found</sub> | Bachelor's thesis comparison of VEM and FEM robustness and convergence. | Written for MATLAB, Octave support not documented; bundles SimpleVEM, iFEM and vem2D code. |
| [nsundar/<br>VEM_in_Abaqus](https://github.com/nsundar/VEM_in_Abaqus)<br><sub>Fortran</sub><br><sub>GPL-3.0</sub> | Implementation of the virtual element method as Abaqus subroutines. | Requires Abaqus. |
| [Qinxiaoye/<br>VEM_mechanics2D](https://github.com/Qinxiaoye/VEM_mechanics2D)<br><sub>MATLAB</sub><br><sub>none found</sub> | Teaching code for VEM in 2D linear elasticity, with a theory note. | Written for MATLAB, Octave support not documented; some files are copyright Terence Yu and Long Chen, with no license in this repository. |
| [tytrusty/<br>Shape-Matching-<br>Element-Method](https://github.com/tytrusty/Shape-Matching-Element-Method)<br><sub>MATLAB and C++</sub><br><sub>none found</sub> | Shape-matching VEM for direct simulation of CAD models. | Written for MATLAB, Octave support not documented; depends on gptoolbox. |
| [ZhouRuopu/<br>GNE-VEM](https://github.com/ZhouRuopu/GNE-VEM)<br><sub>Python</sub><br><sub>none found</sub> | Graph neural network approach to VEM stabilization. |  |

</details>

<details>
<summary><a id="dynamics-and-fracture"></a><h3>3.3 Dynamics and fracture</h3></summary>
<p id="open-virtual-element-method--dynamics-and-fracture"><sub>Virtual element method › <b>3.3 Dynamics and fracture</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [MinhNguyenIKM/<br>vem](https://github.com/MinhNguyenIKM/vem)<br><sub>MATLAB</sub><br><sub>none found</sub> | VEM code for 2D linear elastic fracture. | Written for MATLAB, Octave support not documented. |
| [Qinxiaoye/<br>VEM-spcae-time-<br>dynamic](https://github.com/Qinxiaoye/VEM-spcae-time-dynamic)<br><sub>MATLAB</sub><br><sub>none found</sub> | Space-time VEM for elastodynamics. | Written for MATLAB, Octave support not documented; some files are copyright Terence Yu and Long Chen, with no license in this repository. |
| [Qinxiaoye/<br>VEMdynamic_Newmark](https://github.com/Qinxiaoye/VEMdynamic_Newmark)<br><sub>MATLAB</sub><br><sub>none found</sub> | VEM for 2D linear elastodynamics with Newmark time integration. | Written for MATLAB, Octave support not documented; some files are copyright Terence Yu and Long Chen, with no license in this repository. |

</details>

<details>
<summary><a id="coupled-fields-and-electronic-packaging"></a><h3>3.4 Coupled fields and electronic packaging</h3></summary>
<p id="open-virtual-element-method--coupled-fields-and-electronic-packaging"><sub>Virtual element method › <b>3.4 Coupled fields and electronic packaging</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [aerubianoma/<br>vem_stress_<br>assisted_diffusion](https://github.com/aerubianoma/vem_stress_assisted_diffusion)<br><sub>MATLAB</sub><br><sub>GPL-3.0</sub> | Robust VEM experiments for stress-assisted diffusion in elastic materials. | Requires MATLAB, README lists R2023a. |
| [Qinxiaoye/<br>VEMpiezo](https://github.com/Qinxiaoye/VEMpiezo)<br><sub>MATLAB</sub><br><sub>none found</sub> | VEM for 2D piezoelasticity. | Written for MATLAB, Octave support not documented; some files are copyright Terence Yu, with no license in this repository. |
| [yanpeng-gong/<br>FeVeCoupled-<br>Electronic<br>Packaging](https://github.com/yanpeng-gong/FeVeCoupled-ElectronicPackaging)<br><sub>MATLAB</sub><br><sub>MIT</sub> | Coupled finite and virtual element analysis of multiscale electronic packaging structures. | Requires MATLAB. |
| [yanpeng-gong/<br>VEM-electronic-<br>packaging](https://github.com/yanpeng-gong/VEM-electronic-packaging)<br><sub>MATLAB</sub><br><sub>MIT (README badge)</sub> | Standard and stabilization-free VEM for thermomechanical analysis of electronic packaging. | Requires MATLAB; no license file. |

</details>

<details>
<summary><a id="topology-optimization-with-vem"></a><h3>3.5 Topology optimization with VEM</h3></summary>
<p id="open-virtual-element-method--topology-optimization-with-vem"><sub>Virtual element method › <b>3.5 Topology optimization with VEM</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [Qinxiaoye/<br>TOPvem](https://github.com/Qinxiaoye/TOPvem)<br><sub>MATLAB</sub><br><sub>none found</sub> | Density-based topology optimization with VEM. | Written for MATLAB, Octave support not documented; some files are copyright Terence Yu, with no license in this repository. |
| [redcican/<br>vem-concurrent-<br>topopt](https://github.com/redcican/vem-concurrent-topopt)<br><sub>Python</sub><br><sub>MIT</sub> | Concurrent multiscale topology optimization with VEM on polygonal and polyhedral meshes. |  |

</details>

<details>
<summary><a id="introductory-vem-codes"></a><h3>3.6 Introductory VEM codes</h3></summary>
<p id="open-virtual-element-method--introductory-vem-codes"><sub>Virtual element method › <b>3.6 Introductory VEM codes</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [andrea-borio/<br>vem-<br>implementation-<br>example](https://github.com/andrea-borio/vem-implementation-example)<br><sub>MATLAB</sub><br><sub>GPL-3.0</sub> | Compact example of an optimized VEM implementation. | Written for MATLAB, Octave support not documented; solves the Poisson equation, not elasticity. |
| [deatinor/<br>VEM3D](https://github.com/deatinor/VEM3D)<br><sub>C++</sub><br><sub>none found</sub> | Master's project implementing the virtual element method in three dimensions. | Convergence scripts use MATLAB. |
| [justachetan/<br>VirtualElement<br>Methods](https://github.com/justachetan/VirtualElementMethods)<br><sub>Python</sub><br><sub>MIT</sub> | Python translation of the 50-line introductory VEM code. | Solves the Poisson equation, not elasticity. |
| [oliversutton/<br>50LinesOfVEM](https://github.com/oliversutton/50LinesOfVEM)<br><sub>MATLAB</sub><br><sub>MIT</sub> | Introductory 50-line MATLAB implementation of VEM. | Written for MATLAB, Octave support not documented; solves the Poisson equation, not elasticity. |
| [Qinxiaoye/<br>VEM_Poisson](https://github.com/Qinxiaoye/VEM_Poisson)<br><sub>MATLAB</sub><br><sub>none found</sub> | Introductory 2D VEM code with a theory note. | Written for MATLAB, Octave support not documented; solves the Poisson equation, not elasticity; some files are copyright Terence Yu, with no license in this repository. |
| [Qinxiaoye/<br>VEMbook](https://github.com/Qinxiaoye/VEMbook)<br><sub>MATLAB</sub><br><sub>none found</sub> | VEM teaching scripts, including a 1D truss. | Written for MATLAB, Octave support not documented; sparse documentation. |

</details>

</details>

<details>
<summary><a id="contact-mechanics"></a><h2>4. Contact mechanics</h2></summary>
<p id="open-contact-mechanics"><sub><b>4. Contact mechanics</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><a id="contact-formulations"></a><h3>4.1 Contact formulations</h3></summary>
<p id="open-contact-mechanics--contact-formulations"><sub>Contact mechanics › <b>4.1 Contact formulations</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [adtzlr/<br>felupe-contact](https://github.com/adtzlr/felupe-contact)<br><sub>Python</sub><br><sub>GPL-3.0-or-later</sub> | Large-deformation contact formulations for FElupe. | README says it is at an early stage. |
| [CMSL-HKUST/<br>FMC_contact](https://github.com/CMSL-HKUST/FMC_contact)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Differentiable volume-based contact with Fiber Monte Carlo in finite elements. |  |
| [mimesis-inria/<br>SOFA.NCP](https://github.com/mimesis-inria/SOFA.NCP)<br><sub>C++</sub><br><sub>none found</sub> | Direct contact solving with the Fischer-Burmeister formulation. | Requires SOFA; no README. |
| [Wells-Group/<br>asimov-contact](https://github.com/Wells-Group/asimov-contact)<br><sub>C++ and Python</sub><br><sub>MIT</sub> | Parallel contact between deforming bodies in FEniCSx. | README says it is highly experimental. |

</details>

<details>
<summary><a id="incremental-potential-contact"></a><h3>4.2 Incremental potential contact</h3></summary>
<p id="open-contact-mechanics--incremental-potential-contact"><sub>Contact mechanics › <b>4.2 Incremental potential contact</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [ipc-sim/<br>Codim-IPC](https://github.com/ipc-sim/Codim-IPC)<br><sub>C++</sub><br><sub>Apache-2.0</sub> | Incremental potential contact for codimensional objects. | Paper code; bundled components have their own licenses. |
| [ipc-sim/<br>IPC](https://github.com/ipc-sim/IPC)<br><sub>C++</sub><br><sub>MIT</sub> | Reference implementation of Incremental Potential Contact for large-deformation elastodynamics. |  |
| [ipc-sim/<br>ipc-toolkit](https://github.com/ipc-sim/ipc-toolkit)<br><sub>C++</sub><br><sub>MIT</sub> | Reusable functions for adding incremental potential contact to a simulation. |  |
| [ipc-sim/<br>rigid-ipc](https://github.com/ipc-sim/rigid-ipc)<br><sub>C++</sub><br><sub>MIT</sub> | Reference implementation of intersection-free rigid body dynamics. |  |
| [spiriMirror/<br>libuipc](https://github.com/spiriMirror/libuipc)<br><sub>C++ and CUDA</sub><br><sub>Apache-2.0</sub> | GPU library for unified incremental potential contact of rigid and deformable bodies. | The Blender integration includes GPL-3.0 code. |

</details>

</details>

<details>
<summary><a id="third-medium-contact"></a><h2>5. Third medium contact</h2></summary>
<p id="open-third-medium-contact"><sub><b>5. Third medium contact</b> · <a href="#contents">Back to contents</a></sub></p>

Third medium contact (TMC) models contact by meshing the gap with a very compliant fictitious material. Some links open the relevant file inside a larger project. DTU's MATLAB TopTMC code is not in a repository and can be downloaded from the [TopOpt software page](https://www.topopt.mek.dtu.dk/apps-and-software).

<details>
<summary><a id="modules-and-examples-in-fem-libraries"></a><h3>5.1 Modules and examples in FEM libraries</h3></summary>
<p id="open-third-medium-contact--modules-and-examples-in-fem-libraries"><sub>Third medium contact › <b>5.1 Modules and examples in FEM libraries</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [adtzlr/<br>felupe](https://github.com/adtzlr/felupe/blob/main/examples/ex20_third-medium-contact.py)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Third medium contact example in the FElupe nonlinear finite element package. |  |
| [deepmodeling/<br>jax-fem](https://github.com/deepmodeling/jax-fem/tree/main/applications/third_medium_contact)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Third medium contact application in JAX-FEM. |  |
| [fenics-dolfiny/<br>dolfiny](https://github.com/fenics-dolfiny/dolfiny/tree/main/demo/tmc)<br><sub>Python</sub><br><sub>LGPL-3.0</sub> | Third medium contact demo built on FEniCSx. |  |
| [idaholab/<br>moose](https://github.com/idaholab/moose/blob/next/modules/solid_mechanics/doc/content/source/kernels/SecondDerivativeRegularization.md)<br><sub>C++</sub><br><sub>LGPL-2.1</sub> | HuHu, LuLu and HuHu-LuLu regularization kernels for solid mechanics. | Regularization component, not a complete contact example. |
| [meyer-nils/<br>torch-fem](https://github.com/meyer-nils/torch-fem/blob/main/examples/basic/planar/third_medium_contact.ipynb)<br><sub>Python</sub><br><sub>MIT</sub> | Third medium contact example in a differentiable PyTorch finite element solver. |  |
| [MultiSimOLab/<br>HyperFEM.jl](https://github.com/MultiSimOLab/HyperFEM.jl/blob/main/test/SimulationsTests/ThirdMediumContactSimulation.jl)<br><sub>Julia</sub><br><sub>MIT</sub> | Third medium contact simulation in a hyperelastic multiphysics library. | Provided as a test, not a tutorial. |
| [Naruki-Ichihara/<br>feax](https://github.com/Naruki-Ichihara/feax/blob/main/feax/mechanics/tmc.py)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Third medium contact module in a JAX finite element engine, with 2D and 3D examples. |  |

</details>

<details>
<summary><a id="optimization-and-metamaterials"></a><h3>5.2 Optimization and metamaterials</h3></summary>
<p id="open-third-medium-contact--optimization-and-metamaterials"><sub>Third medium contact › <b>5.2 Optimization and metamaterials</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [charlieaveline/<br>TMC_Firedrake](https://github.com/charlieaveline/TMC_Firedrake)<br><sub>Python</sub><br><sub>MIT</sub> | Minimal unit-cell forward solve with third medium contact and multiscale virtual power. |  |
| [IMTEK-Simulation/<br>muFFTTO](https://github.com/IMTEK-Simulation/muFFTTO/tree/main/examples/internal_contact)<br><sub>Python</sub><br><sub>MIT</sub> | Internal contact by third medium in an FFT-based microstructure optimization code. |  |
| [LuoXueling/<br>optimization_of_<br>digital_material_<br>distribution](https://github.com/LuoXueling/optimization_of_digital_material_distribution/blob/main/main_semisphere_dist_opt_tmc.py)<br><sub>Python</sub><br><sub>MIT</sub> | Multimaterial distribution optimization with a third medium contact example. |  |
| [stefanhiemer/<br>topoptlab](https://github.com/stefanhiemer/topoptlab/tree/main/examples/fem/third_medium_contact)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | C-shape contact example in a topology optimization library. |  |

</details>

<details>
<summary><a id="standalone-study-codes"></a><h3>5.3 Standalone study codes</h3></summary>
<p id="open-third-medium-contact--standalone-study-codes"><sub>Third medium contact › <b>5.3 Standalone study codes</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [chennachaos/<br>FEniCSx-TMC](https://github.com/chennachaos/FEniCSx-TMC)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Attempt at third medium contact in FEniCSx. | Author reports it did not work for the paper's parameters. |
| [MechEngrLorenzo<br>Fiore/<br>FEA_studies](https://github.com/MechEngrLorenzoFiore/FEA_studies/tree/main/Third_medium_contact)<br><sub>Python</sub><br><sub>MIT</sub> | Study script based on the 2024 paper by Faltus, Horak, Doskar and Rokos. | Learning project. |

</details>

</details>

<details>
<summary><a id="meshfree-and-particle-methods"></a><h2>6. Meshfree and particle methods</h2></summary>
<p id="open-meshfree-and-particle-methods"><sub><b>6. Meshfree and particle methods</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><a id="material-point-method"></a><h3>6.1 Material point method</h3></summary>
<p id="open-meshfree-and-particle-methods--material-point-method"><sub>Meshfree and particle methods › <b>6.1 Material point method</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [adevaucorbeil/<br>karamelo](https://github.com/adevaucorbeil/karamelo)<br><sub>C++</sub><br><sub>GPL-2.0</sub> | Parallel material point method simulator with CPU and GPU support. | GPU support is on a separate branch. |
| [bcolloran/<br>tlmpm](https://github.com/bcolloran/tlmpm)<br><sub>Python</sub><br><sub>none found</sub> | Teaching implementation of the total Lagrangian material point method in Taichi. |  |
| [cb-geo/<br>mpm](https://github.com/cb-geo/mpm)<br><sub>C++</sub><br><sub>MIT</sub> | High-performance material point method code for computational geomechanics. |  |
| [cb-geo/<br>mpm-benchmarks](https://github.com/cb-geo/mpm-benchmarks)<br><sub>Jupyter Notebook</sub><br><sub>CC-BY-4.0</sub> | Benchmark cases for the CB-Geo material point method code. |  |
| [penn-graphics-<br>research/<br>ziran2019](https://github.com/penn-graphics-research/ziran2019)<br><sub>C++</sub><br><sub>MIT</sub> | Implicit material point simulation of viscoelasticity, plasticity and fracture. | Paper code. |
| [taichi-dev/<br>mpm_3d_exercise](https://github.com/taichi-dev/mpm_3d_exercise)<br><sub>Python</sub><br><sub>MIT</sub> | Exercise for writing a 3D material point method, with a 2D reference implementation. | Starter code with the main step left blank. |
| [taichi-dev/<br>taichi_elements](https://github.com/taichi-dev/taichi_elements)<br><sub>Python</sub><br><sub>MIT</sub> | Multi-material MPM engine for elastic solids, water, snow and sand in Taichi. | README describes it as work in progress. |
| [xzhang66/<br>MPM3D-F90](https://github.com/xzhang66/MPM3D-F90)<br><sub>Fortran</sub><br><sub>none found</sub> | Simplified Fortran 90 material point code accompanying two MPM books. | Source headers carry a copyright notice without license terms. |
| [Yihao-Shi/<br>GeoTaichi](https://github.com/Yihao-Shi/GeoTaichi)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Coupled material point and discrete element simulation of geophysical problems. | Bundled components have their own licenses. |
| [yuanming-hu/<br>GPUMPM](https://github.com/yuanming-hu/GPUMPM)<br><sub>C++ and CUDA</sub><br><sub>GPL-3.0</sub> | GPU-optimized material point method from a SIGGRAPH Asia 2018 paper. | README asks commercial users to contact the authors. |
| [yuanming-hu/<br>taichi_mpm](https://github.com/yuanming-hu/taichi_mpm)<br><sub>C++</sub><br><sub>MIT</sub> | MLS-MPM solver with cutting and two-way rigid body coupling. |  |

</details>

<details>
<summary><a id="smoothed-particle-hydrodynamics"></a><h3>6.2 Smoothed particle hydrodynamics</h3></summary>
<p id="open-meshfree-and-particle-methods--smoothed-particle-hydrodynamics"><sub>Meshfree and particle methods › <b>6.2 Smoothed particle hydrodynamics</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [Interactive<br>ComputerGraphics/<br>SPH-Tutorial](https://github.com/InteractiveComputerGraphics/SPH-Tutorial)<br><sub>none found</sub> | Tutorial notes and slides on SPH, including deformable solids. | Documents only, no code. |
| [luchete80/<br>WeldForm](https://github.com/luchete80/WeldForm)<br><sub>C++</sub><br><sub>GPL-3.0-or-later</sub> | SPH solver for elastoplastic and thermally coupled metal forming. |  |
| [pypr/<br>pysph](https://github.com/pypr/pysph)<br><sub>Python</sub><br><sub>BSD-3-Clause</sub> | Smoothed particle hydrodynamics framework with OpenMP, OpenCL and MPI support. | Some directories may carry other licenses. |
| [Xiangyu-Hu/<br>SPHinXsys](https://github.com/Xiangyu-Hu/SPHinXsys)<br><sub>C++</sub><br><sub>Apache-2.0</sub> | SPH-based multiphysics library for coupled simulation and optimization. |  |

</details>

<details>
<summary><a id="meshless-methods"></a><h3>6.3 Meshless methods</h3></summary>
<p id="open-meshfree-and-particle-methods--meshless-methods"><sub>Meshfree and particle methods › <b>6.3 Meshless methods</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [iwf-inspire/<br>mfree_iwf](https://github.com/iwf-inspire/mfree_iwf)<br><sub>C++</sub><br><sub>GPL-3.0</sub> | Comparison of meshless methods for large-deformation elastodynamics. | Paper code. |
| [iwf-inspire/<br>mfree_iwf-ul-cut-<br>refine](https://github.com/iwf-inspire/mfree_iwf-ul-cut-refine)<br><sub>C++</sub><br><sub>GPL-3.0</sub> | Updated Lagrangian meshfree metal cutting with dynamic refinement. | Paper code. |
| [JinshuaiBai/<br>RPIM_NNS](https://github.com/JinshuaiBai/RPIM_NNS)<br><sub>MATLAB</sub><br><sub>none found</sub> | Radial point interpolation meshless method with neural network solvers. | Requires MATLAB. |
| [saullocastro/<br>meshless](https://github.com/saullocastro/meshless)<br><sub>Python</sub><br><sub>BSD-2-Clause</sub> | Meshless methods for computational mechanics, including ES-PIM. |  |
| [SlicerCBM/<br>SlicerCBM](https://github.com/SlicerCBM/SlicerCBM)<br><sub>Python</sub><br><sub>BSD-3-Clause</sub> | 3D Slicer extension for patient-specific biomechanics, with a meshless TLED (MTLED) simulator. | Requires 3D Slicer; some external solvers are GPL. |

</details>

<details>
<summary><a id="peridynamics"></a><h3>6.4 Peridynamics</h3></summary>
<p id="open-meshfree-and-particle-methods--peridynamics"><sub>Meshfree and particle methods › <b>6.4 Peridynamics</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [kaipartmann/<br>Peridynamics.jl](https://github.com/kaipartmann/Peridynamics.jl)<br><sub>Julia</sub><br><sub>MIT</sub> | Parallel peridynamics with several formulations and multibody contact. |  |
| [peridigm/<br>peridigm](https://github.com/peridigm/peridigm)<br><sub>C++</sub><br><sub>BSD-3-Clause</sub> | Parallel peridynamics code for solid mechanics with material failure. |  |
| [PeriHub/<br>PeriLab.jl](https://github.com/PeriHub/PeriLab.jl)<br><sub>Julia</sub><br><sub>BSD-3-Clause</sub> | Peridynamics laboratory for a range of material and fracture problems. |  |

</details>

<details>
<summary><a id="discrete-and-coarse-grained-particle-models"></a><h3>6.5 Discrete and coarse-grained particle models</h3></summary>
<p id="open-meshfree-and-particle-methods--discrete-and-coarse-grained-particle-models"><sub>Meshfree and particle methods › <b>6.5 Discrete and coarse-grained particle models</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [idaholab/<br>LIGGGHTS-INL](https://github.com/idaholab/LIGGGHTS-INL)<br><sub>C++</sub><br><sub>GPL-2.0</sub> | Extended version of the LIGGGHTS discrete element code. |  |
| [projectchrono/<br>DEM-Engine](https://github.com/projectchrono/DEM-Engine)<br><sub>C++ and CUDA</sub><br><sub>BSD-3-Clause</sub> | GPU discrete element solver with complex grain geometry. | Requires an NVIDIA GPU. |
| [YADE](https://gitlab.com/yade-dev/trunk)<br><sub>C++ and Python</sub><br><sub>GPL-2.0-or-later</sub> | Framework for the discrete element method. |  |
| [yhtang/<br>OpenRBC](https://github.com/yhtang/OpenRBC)<br><sub>C++</sub><br><sub>GPL-3.0</sub> | Coarse-grained particle simulator of red blood cells at protein resolution. |  |
| [yuanming-hu/<br>taichi_dem_mid_<br>autumn](https://github.com/yuanming-hu/taichi_dem_mid_autumn)<br><sub>Python</sub><br><sub>MIT</sub> | Minimal discrete element method demo in Taichi. |  |

</details>

</details>

<details>
<summary><a id="soft-body-real-time-and-differentiable-simulation"></a><h2>7. Soft-body, real-time and differentiable simulation</h2></summary>
<p id="open-soft-body-real-time-and-differentiable-simulation"><sub><b>7. Soft-body, real-time and differentiable simulation</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><a id="real-time-finite-elements"></a><h3>7.1 Real-time finite elements</h3></summary>
<p id="open-soft-body-real-time-and-differentiable-simulation--real-time-finite-elements"><sub>Soft-body, real-time and differentiable simulation › <b>7.1 Real-time finite elements</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [Interactive<br>ComputerGraphics/<br>FastCorotatedFEM](https://github.com/InteractiveComputerGraphics/FastCorotatedFEM)<br><sub>C++</sub><br><sub>MIT</sub> | Minimal fast corotated finite element method using operator splitting. |  |
| [jinaojakezhang/<br>DJTLED](https://github.com/jinaojakezhang/DJTLED)<br><sub>C++</sub><br><sub>MIT</sub> | Direct-Jacobian explicit dynamics finite elements for real-time hyperelastic simulation. |  |
| [ltt1598/<br>Quasi-Newton-<br>Methods-for-Real-<br>time-Simulation-<br>of-Hyperelastic-<br>Materials](https://github.com/ltt1598/Quasi-Newton-Methods-for-Real-time-Simulation-of-Hyperelastic-Materials)<br><sub>C++</sub><br><sub>BSD-3-Clause (stated in source)</sub> | Quasi-Newton methods for real-time hyperelastic simulation. | Only a Visual Studio build is provided. |
| [sofa-framework/<br>sofa](https://github.com/sofa-framework/sofa)<br><sub>C++</sub><br><sub>LGPL-2.1</sub> | Interactive finite element physics framework for medical simulation and robotics. |  |
| [sofa-framework/<br>SofaPython3](https://github.com/sofa-framework/SofaPython3)<br><sub>C++ and Python</sub><br><sub>LGPL-2.1</sub> | Python interface to the SOFA simulation framework. | Requires SOFA; README describes it as work in progress. |
| [x9m/<br>DJTLED_fast](https://github.com/x9m/DJTLED_fast)<br><sub>C++</sub><br><sub>MIT</sub> | Speed-optimized DJ-TLED soft-tissue solver, with Jinao Zhang's original solver for comparison. | **By the list maintainer.** Derived from Jinao Zhang's DJTLED; developed and tested on macOS. |
| [x9m/<br>JANP-DJTLED-GPU](https://github.com/x9m/JANP-DJTLED-GPU)<br><sub>C++ and CUDA</sub><br><sub>MIT</sub> | DJTLED with average nodal pressure for nearly incompressible soft tissue, on CPU and GPU. | **By the list maintainer.** Builds on Jinao Zhang's DJTLED; the GPU solver needs an NVIDIA GPU. |

</details>

<details>
<summary><a id="soft-robotics"></a><h3>7.2 Soft robotics</h3></summary>
<p id="open-soft-body-real-time-and-differentiable-simulation--soft-robotics"><sub>Soft-body, real-time and differentiable simulation › <b>7.2 Soft robotics</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [SofaDefrost/<br>CondensedFEMModel](https://github.com/SofaDefrost/CondensedFEMModel)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Learned condensed finite element models for soft robot control and design. | Requires SOFA. |
| [SofaDefrost/<br>SofaGym](https://github.com/SofaDefrost/SofaGym)<br><sub>Python</sub><br><sub>none found</sub> | Reinforcement learning environments built from SOFA scenes. | Requires SOFA; source files carry Inria and partner copyright notices. |
| [SofaDefrost/<br>SoftRobots](https://github.com/SofaDefrost/SoftRobots)<br><sub>C++</sub><br><sub>LGPL-3.0</sub> | SOFA components for modeling, actuating and controlling soft robots. | Requires SOFA. |
| [SofaDefrost/<br>SoftRobots.Design<br>Optimization](https://github.com/SofaDefrost/SoftRobots.DesignOptimization)<br><sub>Python</sub><br><sub>AGPL-3.0</sub> | Design optimization toolbox for soft robots. | Requires SOFA. |
| [SofaDefrost/<br>SoftRobots.Inverse](https://github.com/SofaDefrost/SoftRobots.Inverse)<br><sub>C++</sub><br><sub>AGPL-3.0 with a patent clause</sub> | Inverse methods for soft robot control. | Requires SOFA; implements a patented Inria method. |
| [StanfordASL/<br>soft-robot-control](https://github.com/StanfordASL/soft-robot-control)<br><sub>Python</sub><br><sub>MIT</sub> | Optimal control of soft robots with reduced-order finite element models. | Requires SOFA; setup uses a Gurobi license. |

</details>

<details>
<summary><a id="position-based-and-implicit-dynamics"></a><h3>7.3 Position-based and implicit dynamics</h3></summary>
<p id="open-soft-body-real-time-and-differentiable-simulation--position-based-and-implicit-dynamics"><sub>Soft-body, real-time and differentiable simulation › <b>7.3 Position-based and implicit dynamics</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [Interactive<br>ComputerGraphics/<br>PositionBased<br>Dynamics](https://github.com/InteractiveComputerGraphics/PositionBasedDynamics)<br><sub>C++</sub><br><sub>MIT</sub> | Position-based simulation of rigid bodies, deformable solids and fluids. |  |
| [Interactive<br>ComputerGraphics/<br>stark](https://github.com/InteractiveComputerGraphics/stark)<br><sub>C++ and Python</sub><br><sub>Apache-2.0</sub> | Strongly coupled rigid and deformable bodies with shells, rods and frictional contact. |  |
| [mattoverby/<br>admm-elastic](https://github.com/mattoverby/admm-elastic)<br><sub>C++</sub><br><sub>MIT</sub> | ADMM generalization of projective dynamics to hyperelastic models. |  |
| [Q-Minh/<br>position-based-<br>dynamics](https://github.com/Q-Minh/position-based-dynamics)<br><sub>C++</sub><br><sub>BSL-1.0</sub> | Academic prototype of soft-body simulation with extended position-based dynamics. |  |

</details>

<details>
<summary><a id="differentiable-simulation"></a><h3>7.4 Differentiable simulation</h3></summary>
<p id="open-soft-body-real-time-and-differentiable-simulation--differentiable-simulation"><sub>Soft-body, real-time and differentiable simulation › <b>7.4 Differentiable simulation</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [NVlabs/<br>DiffRL](https://github.com/NVlabs/DiffRL)<br><sub>Python</sub><br><sub>NVIDIA Source Code License (non-commercial)</sub> | Differentiable simulation and policy learning from the SHAC paper. | Restricted to non-commercial use. |
| [NVlabs/<br>DiSECt](https://github.com/NVlabs/DiSECt)<br><sub>Python</sub><br><sub>NVIDIA Source Code License (non-commercial)</sub> | Differentiable finite element simulator for robotic cutting of deformable materials. | Code and dataset are restricted to non-commercial use. |
| [rewarped/<br>rewarped](https://github.com/rewarped/rewarped)<br><sub>Python</sub><br><sub>Apache-2.0, with NVIDIA-restricted files</sub> | Reinforcement learning with parallel differentiable multiphysics simulation. | Some NVIDIA file headers forbid use without a license agreement. |
| [taichi-dev/<br>difftaichi](https://github.com/taichi-dev/difftaichi)<br><sub>Python</sub><br><sub>none found</sub> | Examples of differentiable physical simulators written in Taichi. |  |
| [taichi-dev/<br>taichi](https://github.com/taichi-dev/taichi)<br><sub>C++</sub><br><sub>Apache-2.0</sub> | Parallel programming language in Python for simulation on CPUs and GPUs. |  |
| [YilingQiao/<br>diff_fem](https://github.com/YilingQiao/diff_fem)<br><sub>C++</sub><br><sub>Apache-2.0</sub> | Differentiable simulation of soft multibody systems. | Paper code. |

</details>

<details>
<summary><a id="manipulation-benchmarks"></a><h3>7.5 Manipulation benchmarks</h3></summary>
<p id="open-soft-body-real-time-and-differentiable-simulation--manipulation-benchmarks"><sub>Soft-body, real-time and differentiable simulation › <b>7.5 Manipulation benchmarks</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [hzaskywalker/<br>PlasticineLab](https://github.com/hzaskywalker/PlasticineLab)<br><sub>Python</sub><br><sub>none found</sub> | Differentiable physics benchmark for soft-body manipulation. | Only some bundled algorithm folders have license files. |
| [Xingyu-Lin/<br>softagent](https://github.com/Xingyu-Lin/softagent)<br><sub>Python</sub><br><sub>none found</sub> | Benchmarked learning algorithms for deformable object manipulation in SoftGym. | Some bundled folders have their own licenses. |
| [Xingyu-Lin/<br>softgym](https://github.com/Xingyu-Lin/softgym)<br><sub>C++</sub><br><sub>BSD-3-Clause, with separately licensed NVIDIA FleX</sub> | Deformable object manipulation benchmarks for cloth, rope and fluid. | Bundles NVIDIA FleX under the NVIDIA Source Code License (1-Way Commercial); some FleX headers also forbid use without an agreement with NVIDIA. |

</details>

</details>

<details>
<summary><a id="multibody-dynamics-and-biomechanics"></a><h2>8. Multibody dynamics and biomechanics</h2></summary>
<p id="open-multibody-dynamics-and-biomechanics"><sub><b>8. Multibody dynamics and biomechanics</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><a id="physics-engines-for-multibody-systems"></a><h3>8.1 Physics engines for multibody systems</h3></summary>
<p id="open-multibody-dynamics-and-biomechanics--physics-engines-for-multibody-systems"><sub>Multibody dynamics and biomechanics › <b>8.1 Physics engines for multibody systems</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [dartsim/<br>dart](https://github.com/dartsim/dart)<br><sub>C++</sub><br><sub>BSD-2-Clause</sub> | Kinematics, dynamics and contact of articulated rigid and soft bodies. |  |
| [google-deepmind/<br>mujoco](https://github.com/google-deepmind/mujoco)<br><sub>C++</sub><br><sub>Apache-2.0</sub> | Multibody dynamics engine with contact and deformable bodies. |  |
| [jgerstmayr/<br>EXUDYN](https://github.com/jgerstmayr/EXUDYN)<br><sub>C++ and Python</sub><br><sub>EXUDYN General License (BSD-3-Clause style)</sub> | Rigid and flexible multibody dynamics. |  |
| [newton-physics/<br>newton](https://github.com/newton-physics/newton)<br><sub>Python</sub><br><sub>Apache-2.0</sub> | GPU-accelerated physics engine for robotics and simulation research. |  |
| [projectchrono/<br>chrono](https://github.com/projectchrono/chrono)<br><sub>C++</sub><br><sub>BSD-3-Clause</sub> | Multiphysics engine for rigid, deformable and granular system dynamics. |  |
| [pydy/<br>pydy](https://github.com/pydy/pydy)<br><sub>Python</sub><br><sub>BSD-3-Clause</sub> | Toolkit for studying multibody dynamics in Python. |  |

</details>

<details>
<summary><a id="musculoskeletal-biomechanics"></a><h3>8.2 Musculoskeletal biomechanics</h3></summary>
<p id="open-multibody-dynamics-and-biomechanics--musculoskeletal-biomechanics"><sub>Multibody dynamics and biomechanics › <b>8.2 Musculoskeletal biomechanics</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [diku-dk/<br>libhip](https://github.com/diku-dk/libhip)<br><sub>Python</sub><br><sub>MIT</sub> | Subject-specific hip joint finite element models and the code to reproduce them. |  |
| [opensim-org/<br>opensim-core](https://github.com/opensim-org/opensim-core)<br><sub>C++</sub><br><sub>Apache-2.0</sub> | Musculoskeletal modeling and dynamic simulation of movement. |  |

</details>

<details>
<summary><a id="cardiovascular-mechanics"></a><h3>8.3 Cardiovascular mechanics</h3></summary>
<p id="open-multibody-dynamics-and-biomechanics--cardiovascular-mechanics"><sub>Multibody dynamics and biomechanics › <b>8.3 Cardiovascular mechanics</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [KIT-IBT/<br>CardioMechanics](https://github.com/KIT-IBT/CardioMechanics)<br><sub>C++</sub><br><sub>GPL-3.0</sub> | Finite element simulation of cardiac electromechanics. |  |
| [SimVascular/<br>svMultiPhysics](https://github.com/SimVascular/svMultiPhysics)<br><sub>C++</sub><br><sub>BSD-3-Clause, with restricted bundled components</sub> | Parallel finite element multiphysics solver for cardiovascular simulation. | Bundled ParMETIS code is limited to non-profit, government or evaluation use; bundled TetGen is AGPL-3.0. |

</details>

</details>

<details>
<summary><a id="constitutive-modeling-and-material-identification"></a><h2>9. Constitutive modeling and material identification</h2></summary>
<p id="open-constitutive-modeling-and-material-identification"><sub><b>9. Constitutive modeling and material identification</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><a id="neural-network-constitutive-models"></a><h3>9.1 Neural network constitutive models</h3></summary>
<p id="open-constitutive-modeling-and-material-identification--neural-network-constitutive-models"><sub>Constitutive modeling and material identification › <b>9.1 Neural network constitutive models</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [abuganza/<br>NN_aniso_UMAT](https://github.com/abuganza/NN_aniso_UMAT)<br><sub>Jupyter Notebook</sub><br><sub>GPL-3.0</sub> | Neural network models of anisotropic hyperelastic materials, with a UMAT. | Requires Abaqus for the UMAT. |
| [filippo-masi/<br>Thermodynamics-<br>Neural-Networks](https://github.com/filippo-masi/Thermodynamics-Neural-Networks)<br><sub>Jupyter Notebook and Python</sub><br><sub>MIT</sub> | Thermodynamics-based neural networks for inelastic constitutive modeling. |  |
| [FuhgJan/<br>Extreme<br>Sparsification<br>ConstitutiveLaws](https://github.com/FuhgJan/ExtremeSparsificationConstitutiveLaws)<br><sub>Python</sub><br><sub>GPL (stated in README)</sub> | Sparse physics-augmented neural networks for interpretable constitutive laws. |  |
| [FuhgJan/<br>invariant_DD_CM](https://github.com/FuhgJan/invariant_DD_CM)<br><sub>MATLAB</sub><br><sub>conflicting statements</sub> | Space-filling sampling of invariant space for data-driven constitutive models. | Requires MATLAB R2017a or later; README states both GPL-3.0 and a non-commercial Creative Commons license. |
| [FuhgJan/<br>modelDataDriven_<br>YieldFunction](https://github.com/FuhgJan/modelDataDriven_YieldFunction)<br><sub>Python</sub><br><sub>conflicting statements</sub> | Hybrid model-data-driven yield functions. | README states both GPL-3.0 and a non-commercial Creative Commons license. |
| [hyoungsuksuh/<br>ABAQUS_NN](https://github.com/hyoungsuksuh/ABAQUS_NN)<br><sub>Python</sub><br><sub>none found</sub> | PyTorch-to-UMAT framework for deep-learning level-set plasticity. | Requires Abaqus. |
| [LivingMatterLab/<br>CANN](https://github.com/LivingMatterLab/CANN)<br><sub>Jupyter Notebook</sub><br><sub>none found</sub> | Constitutive artificial neural networks for automated material model discovery. |  |
| [meghbali/<br>ANNElastoplasticity](https://github.com/meghbali/ANNElastoplasticity)<br><sub>Python</sub><br><sub>MIT</sub> | Neural network approach to elastoplastic constitutive modeling. |  |
| [pantale/<br>Algorithms-2023](https://github.com/pantale/Algorithms-2023)<br><sub>Fortran and Jupyter Notebook</sub><br><sub>GPL-3.0</sub> | Activation function comparison for neural flow laws in thermomechanical forming. | Requires Abaqus for the subroutines. |
| [pantale/<br>ANN-Constitutive<br>Law](https://github.com/pantale/ANN-ConstitutiveLaw)<br><sub>Jupyter Notebook</sub><br><sub>none found</sub> | Neural network flow laws for metals, implemented as VUHARD subroutines. | Requires Abaqus/Explicit for the subroutines. |
| [tajtac/<br>Anisotropic_NN_<br>UMAT](https://github.com/tajtac/Anisotropic_NN_UMAT)<br><sub>Jupyter Notebook and Fortran</sub><br><sub>none found</sub> | Neural network model of anisotropic soft tissue with a UMAT. | Requires Abaqus for the UMAT. |
| [tajtac/<br>hypermodelcomp](https://github.com/tajtac/hypermodelcomp)<br><sub>Jupyter Notebook</sub><br><sub>none found</sub> | Comparison of CANN, input-convex network and neural ODE models of hyperelasticity. |  |
| [tajtac/<br>node_diffusion](https://github.com/tajtac/node_diffusion)<br><sub>Jupyter Notebook</sub><br><sub>none found</sub> | Research notebooks combining neural ODE hyperelastic models with diffusion models. | No README. |
| [tajtac/<br>NODE_v2](https://github.com/tajtac/NODE_v2)<br><sub>Jupyter Notebook and Fortran</sub><br><sub>none found</sub> | Polyconvex strain energy functions from neural ODEs, with finite element examples. | LICENSE file is empty; finite element examples use Abaqus. |
| [tgulikers/<br>ABAQUS_ANN_<br>constitutive_model](https://github.com/tgulikers/ABAQUS_ANN_constitutive_model)<br><sub>Fortran</sub><br><sub>none found</sub> | Thesis code that trains neural network constitutive models and generates a UMAT. | Requires Abaqus for the UMAT. |

</details>

<details>
<summary><a id="unsupervised-model-discovery"></a><h3>9.2 Unsupervised model discovery</h3></summary>
<p id="open-constitutive-modeling-and-material-identification--unsupervised-model-discovery"><sub>Constitutive modeling and material identification › <b>9.2 Unsupervised model discovery</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [EUCLID-code/<br>EUCLID-<br>hyperelasticity](https://github.com/EUCLID-code/EUCLID-hyperelasticity)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Unsupervised discovery of hyperelastic strain energy functions from full-field displacement data. |  |
| [EUCLID-code/<br>EUCLID-<br>hyperelasticity-<br>bayesian](https://github.com/EUCLID-code/EUCLID-hyperelasticity-bayesian)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Bayesian discovery of hyperelastic laws with uncertainty. |  |
| [EUCLID-code/<br>EUCLID-<br>hyperelasticity-NN](https://github.com/EUCLID-code/EUCLID-hyperelasticity-NN)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Neural network hyperelasticity learned without stress data. |  |
| [EUCLID-code/<br>EUCLID-<br>hyperelasticity-<br>PlaneStress-<br>ExperimentalData](https://github.com/EUCLID-code/EUCLID-hyperelasticity-PlaneStress-ExperimentalData)<br><sub>Python</sub><br><sub>none found</sub> | Discovery of plane-stress hyperelastic laws from experimental data. |  |
| [EUCLID-code/<br>EUCLID-plasticity](https://github.com/EUCLID-code/EUCLID-plasticity)<br><sub>MATLAB</sub><br><sub>GPL-3.0</sub> | Discovery of plasticity and generalized standard material models without stress data. | Written for MATLAB, Octave support not documented. |
| [EUCLID-code/<br>EUCLID-plasticity-<br>pressure-<br>sensitive-non-<br>associated](https://github.com/EUCLID-code/EUCLID-plasticity-pressure-sensitive-non-associated)<br><sub>MATLAB</sub><br><sub>none found</sub> | Discovery of non-associated pressure-sensitive plasticity models. | Written for MATLAB, Octave support not documented. |
| [EUCLID-code/<br>EUCLID-<br>viscoelasticity](https://github.com/EUCLID-code/EUCLID-viscoelasticity)<br><sub>MATLAB</sub><br><sub>GPL-3.0</sub> | Automated identification of linear viscoelastic laws. | Written for MATLAB, Octave support not documented. |

</details>

<details>
<summary><a id="material-subroutines-and-libraries"></a><h3>9.3 Material subroutines and libraries</h3></summary>
<p id="open-constitutive-modeling-and-material-identification--material-subroutines-and-libraries"><sub>Constitutive modeling and material identification › <b>9.3 Material subroutines and libraries</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [abuganza/<br>UMAT_anisotropic_<br>damage](https://github.com/abuganza/UMAT_anisotropic_damage)<br><sub>Fortran</sub><br><sub>GPL-3.0, with BSD-style file headers</sub> | Anisotropic damage subroutines for collagenous tissue fracture and needle insertion. | Requires Abaqus; no README. |
| [adtzlr/<br>hyperelastic](https://github.com/adtzlr/hyperelastic)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Building blocks for hyperelastic material formulations in FElupe. |  |
| [adtzlr/<br>matadi](https://github.com/adtzlr/matadi)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Hyperelastic material definitions with automatic differentiation. |  |
| [bleyerj/<br>dolfinx_materials](https://github.com/bleyerj/dolfinx_materials)<br><sub>Python</sub><br><sub>CC-BY-SA-4.0</sub> | Complex constitutive behaviors for FEniCSx. | MFront behaviors require TFEL. |
| [jgomezc1/<br>ABAQUS-US](https://github.com/jgomezc1/ABAQUS-US)<br><sub>Fortran</sub><br><sub>MIT</sub> | User element and user material subroutines, including classical and Cosserat elements. | Requires Abaqus. |
| [jpsferreira/<br>abaqus-material-<br>lab](https://github.com/jpsferreira/abaqus-material-lab)<br><sub>Fortran</sub><br><sub>GPL-3.0 (stated in README)</sub> | Composable UMAT and UEL framework for soft tissues and filament networks. | Requires Abaqus; no license file. |
| [jpsferreira/<br>UMAT-ABAQUS](https://github.com/jpsferreira/UMAT-ABAQUS)<br><sub>Fortran</sub><br><sub>GPL-3.0</sub> | Fortran framework for large-deformation material models, aimed at soft tissues and cells. | README invites non-commercial use, although the license is GPL-3.0. |
| [pantale/<br>abaqusVumat](https://github.com/pantale/abaqusVumat)<br><sub>Fortran</sub><br><sub>BSD-3-Clause</sub> | Johnson-Cook VUMAT subroutines. | Requires Abaqus/Explicit. |
| [SofaDefrost/<br>SofaViscoElastic](https://github.com/SofaDefrost/SofaViscoElastic)<br><sub>C++</sub><br><sub>LGPL-2.1</sub> | SOFA plugin for linear viscoelastic and visco-hyperelastic laws on tetrahedral meshes. | Requires SOFA. |
| [thelfer/<br>tfel](https://github.com/thelfer/tfel)<br><sub>C++</sub><br><sub>GPL with linking exception, or CeCILL-A</sub> | TFEL and MFront, a code generator for material knowledge and behavior laws. |  |

</details>

<details>
<summary><a id="experimental-parameter-identification"></a><h3>9.4 Experimental parameter identification</h3></summary>
<p id="open-constitutive-modeling-and-material-identification--experimental-parameter-identification"><sub>Constitutive modeling and material identification › <b>9.4 Experimental parameter identification</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [BinChenOPEN/<br>FEMU-DIC](https://github.com/BinChenOPEN/FEMU-DIC)<br><sub>MATLAB</sub><br><sub>GPL-3.0</sub> | Digital image correlation and finite element model updating for strain measurement and parameter identification. | Requires MATLAB and COMSOL. |
| [dicengine/<br>dice](https://github.com/dicengine/dice)<br><sub>C++</sub><br><sub>BSD-3-Clause, with restricted Triangle code</sub> | Stereo digital image correlation engine for full-field displacements and strains. | Bundled Triangle restricts commercial distribution. |
| [lululxvi/<br>deep-learning-for-<br>indentation](https://github.com/lululxvi/deep-learning-for-indentation)<br><sub>Python</sub><br><sub>Apache-2.0</sub> | Extraction of material properties from instrumented indentation with deep learning. | Depends on DeepXDE. |
| [MultiDIC/<br>MultiDIC](https://github.com/MultiDIC/MultiDIC)<br><sub>MATLAB</sub><br><sub>Apache-2.0</sub> | Multi-view 3D digital image correlation toolbox. | Requires MATLAB with the Image Processing, Computer Vision and Statistics toolboxes. |
| [PolymerGuy/<br>muDIC](https://github.com/PolymerGuy/muDIC)<br><sub>Python</sub><br><sub>MIT</sub> | Python toolkit for digital image correlation and virtual experiments. |  |
| [vincentjzy/<br>OpenCorr](https://github.com/vincentjzy/OpenCorr)<br><sub>C++</sub><br><sub>MPL-2.0</sub> | Library for 2D, stereo and volumetric digital image correlation. |  |

</details>

</details>

<details>
<summary><a id="multiscale-and-homogenization"></a><h2>10. Multiscale and homogenization</h2></summary>
<p id="open-multiscale-and-homogenization"><sub><b>10. Multiscale and homogenization</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><a id="fft-based-homogenization"></a><h3>10.1 FFT-based homogenization</h3></summary>
<p id="open-multiscale-and-homogenization--fft-based-homogenization"><sub>Multiscale and homogenization › <b>10.1 FFT-based homogenization</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [DataAnalytics<br>Engineering/<br>FANS](https://github.com/DataAnalyticsEngineering/FANS)<br><sub>C++</sub><br><sub>LGPL-3.0</sub> | Parallel FFT-based homogenization for microscale multiphysics problems. |  |
| [tdegeus/<br>GooseFFT](https://github.com/tdegeus/GooseFFT)<br><sub>Python</sub><br><sub>MIT</sub> | Small teaching scripts for FFT-based micromechanical solvers. |  |
| [vondrejc/<br>FFTHomPy](https://github.com/vondrejc/FFTHomPy)<br><sub>Python</sub><br><sub>MIT</sub> | FFT-based homogenization with guaranteed bounds on effective properties. |  |

</details>

<details>
<summary><a id="fe-and-computational-homogenization"></a><h3>10.2 FE² and computational homogenization</h3></summary>
<p id="open-multiscale-and-homogenization--fe2-and-computational-homogenization"><sub>Multiscale and homogenization › <b>10.2 FE² and computational homogenization</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [felipefr/<br>micmacsfenics](https://github.com/felipefr/micmacsfenics)<br><sub>Python</sub><br><sub>MIT</sub> | FE² and computational homogenization in FEniCS. | README points to the legacy branch for working code during a rewrite. |
| [meghbali/<br>MultiScale<br>Plasticity](https://github.com/meghbali/MultiScalePlasticity)<br><sub>MATLAB</sub><br><sub>MIT</sub> | Upscaling of representative volumes with elastoplastic constituents. | Written for MATLAB, Octave support not documented. |
| [MinhNguyenIKM/<br>multiscale-<br>homogenization](https://github.com/MinhNguyenIKM/multiscale-homogenization)<br><sub>MATLAB and Python</sub><br><sub>none found</sub> | FFT microscale and finite element macroscale computational homogenization. | Includes MATLAB code; bundled PyFEM files state all rights reserved. |

</details>

<details>
<summary><a id="inverse-homogenization"></a><h3>10.3 Inverse homogenization</h3></summary>
<p id="open-multiscale-and-homogenization--inverse-homogenization"><sub>Multiscale and homogenization › <b>10.3 Inverse homogenization</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [lavenklau/<br>homo3d](https://github.com/lavenklau/homo3d)<br><sub>C++ and CUDA</sub><br><sub>GPL-2.0</sub> | GPU solver for large-scale inverse homogenization. | Requires an NVIDIA GPU; README says the main branch is being refactored. |

</details>

<details>
<summary><a id="crystal-plasticity"></a><h3>10.4 Crystal plasticity</h3></summary>
<p id="open-multiscale-and-homogenization--crystal-plasticity"><sub>Multiscale and homogenization › <b>10.4 Crystal plasticity</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [apatra6/<br>rhocp](https://github.com/apatra6/rhocp)<br><sub>C++</sub><br><sub>LGPL-2.1</sub> | Dislocation-density crystal plasticity solver built on MOOSE. |  |
| [damask-<br>multiphysics/<br>DAMASK](https://github.com/damask-multiphysics/DAMASK)<br><sub>Fortran and Python</sub><br><sub>AGPL-3.0-or-later</sub> | Multiscale crystal plasticity simulation kit. | Read-only mirror; development is at git.damask-multiphysics.org. |
| [llnl/<br>ExaConstit](https://github.com/llnl/ExaConstit)<br><sub>C++</sub><br><sub>BSD-3-Clause</sub> | GPU crystal plasticity finite element code with a UMAT interface. |  |
| [prisms-center/<br>plasticity](https://github.com/prisms-center/plasticity)<br><sub>C++</sub><br><sub>LGPL-2.1-or-later</sub> | Crystal and continuum plasticity finite element code built on deal.II. |  |
| [SuperkakaSCU/<br>JAX-CPFEM](https://github.com/SuperkakaSCU/JAX-CPFEM)<br><sub>Python</sub><br><sub>none found</sub> | Differentiable GPU crystal plasticity finite elements built on JAX-FEM. |  |

</details>

</details>

<details>
<summary><a id="thermal-multiphysics-and-additive-manufacturing"></a><h2>11. Thermal, multiphysics and additive manufacturing</h2></summary>
<p id="open-thermal-multiphysics-and-additive-manufacturing"><sub><b>11. Thermal, multiphysics and additive manufacturing</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><a id="heat-transfer-and-bio-heat"></a><h3>11.1 Heat transfer and bio-heat</h3></summary>
<p id="open-thermal-multiphysics-and-additive-manufacturing--heat-transfer-and-bio-heat"><sub>Thermal, multiphysics and additive manufacturing › <b>11.1 Heat transfer and bio-heat</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [jinaojakezhang/<br>FEDFEM](https://github.com/jinaojakezhang/FEDFEM)<br><sub>C++</sub><br><sub>MIT</sub> | Fast explicit dynamics finite elements for transient heat transfer. |  |
| [jinaojakezhang/<br>FEDFEMBioheat](https://github.com/jinaojakezhang/FEDFEMBioheat)<br><sub>C++</sub><br><sub>MIT</sub> | Real-time bio-heat transfer with fast explicit dynamics finite elements. |  |
| [jinaojakezhang/<br>FEDFEMBioheat<br>Damage](https://github.com/jinaojakezhang/FEDFEMBioheatDamage)<br><sub>C++</sub><br><sub>MIT</sub> | CEM43 thermal damage added to real-time bio-heat simulation. |  |
| [jinaojakezhang/<br>FEDFEMBioheat<br>Deform](https://github.com/jinaojakezhang/FEDFEMBioheatDeform)<br><sub>C++</sub><br><sub>MIT</sub> | Soft tissue thermal response under deformation for surgical simulation. |  |
| [jinaojakezhang/<br>FEDFEMBioheatExpan](https://github.com/jinaojakezhang/FEDFEMBioheatExpan)<br><sub>C++</sub><br><sub>MIT</sub> | Anisotropic thermo-visco-elastodynamics of soft tissue for ablation therapy. |  |

</details>

<details>
<summary><a id="thermoelasticity"></a><h3>11.2 Thermoelasticity</h3></summary>
<p id="open-thermal-multiphysics-and-additive-manufacturing--thermoelasticity"><sub>Thermal, multiphysics and additive manufacturing › <b>11.2 Thermoelasticity</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [rcapillon/<br>thermoelasticity_<br>fem](https://github.com/rcapillon/thermoelasticity_fem)<br><sub>Python</sub><br><sub>MIT</sub> | Finite element solver for linear thermoelasticity. | README warns of incomplete documentation and possible bugs. |

</details>

<details>
<summary><a id="additive-manufacturing"></a><h3>11.3 Additive manufacturing</h3></summary>
<p id="open-thermal-multiphysics-and-additive-manufacturing--additive-manufacturing"><sub>Thermal, multiphysics and additive manufacturing › <b>11.3 Additive manufacturing</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [CMSL-HKUST/<br>jax-am](https://github.com/CMSL-HKUST/jax-am)<br><sub>Jupyter Notebook</sub><br><sub>GPL-3.0</sub> | Differentiable GPU toolbox for additive manufacturing process, structure and property simulation. |  |
| [CMSL-HKUST/<br>Opt-IS](https://github.com/CMSL-HKUST/Opt-IS)<br><sub>Python</sub><br><sub>none found</sub> | Inherent strain calibration for residual stress and distortion in additive manufacturing. |  |
| [JLnorthwestern/<br>GO-MELT](https://github.com/JLnorthwestern/GO-MELT)<br><sub>Python</sub><br><sub>MIT</sub> | GPU multilevel thermal simulation of laser powder bed fusion. |  |

</details>

<details>
<summary><a id="multiphysics-coupling"></a><h3>11.4 Multiphysics coupling</h3></summary>
<p id="open-thermal-multiphysics-and-additive-manufacturing--multiphysics-coupling"><sub>Thermal, multiphysics and additive manufacturing › <b>11.4 Multiphysics coupling</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [precice/<br>dealii-adapter](https://github.com/precice/dealii-adapter)<br><sub>C++</sub><br><sub>LGPL-3.0</sub> | Coupled linear and nonlinear elastic solvers connecting deal.II to preCICE. |  |
| [precice/<br>precice](https://github.com/precice/precice)<br><sub>C++</sub><br><sub>LGPL-3.0</sub> | Coupling library for partitioned multiphysics and multiscale simulation. |  |

</details>

</details>

<details>
<summary><a id="optimization-and-inverse-problems"></a><h2>12. Optimization and inverse problems</h2></summary>
<p id="open-optimization-and-inverse-problems"><sub><b>12. Optimization and inverse problems</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><a id="topology-optimization-solvers"></a><h3>12.1 Topology optimization solvers</h3></summary>
<p id="open-optimization-and-inverse-problems--topology-optimization-solvers"><sub>Optimization and inverse problems › <b>12.1 Topology optimization solvers</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [calculix/<br>beso](https://github.com/calculix/beso)<br><sub>Python</sub><br><sub>LGPL-3.0</sub> | Evolutionary topology optimization using the CalculiX solver. | Requires CalculiX and FreeCAD. |
| [Jasiuk-Research-<br>Group/<br>LatticeOPT](https://github.com/Jasiuk-Research-Group/LatticeOPT)<br><sub>Python</sub><br><sub>MIT</sub> | Heuristic topology optimization of thin-walled lattice structures. | Requires Abaqus/Explicit. |
| [JuliaTopOpt/<br>TopOpt.jl](https://github.com/JuliaTopOpt/TopOpt.jl)<br><sub>Julia</sub><br><sub>MIT</sub> | Truss and continuum topology optimization with automatic differentiation. |  |
| [topopt/<br>TopOpt-in-OpenMP-<br>GPU](https://github.com/topopt/TopOpt-in-OpenMP-GPU)<br><sub>C</sub><br><sub>none found</sub> | GPU topology optimization with OpenMP target offloading. |  |
| [topopt/<br>TopOpt_in_PETSc](https://github.com/topopt/TopOpt_in_PETSc)<br><sub>C++</sub><br><sub>unclear</sub> | Parallel large-scale 3D topology optimization with PETSc. | Includes the LGPL text, but source headers say all rights reserved. |
| [topopt/<br>TopOpt_in_PETSc_<br>Transient](https://github.com/topopt/TopOpt_in_PETSc_Transient)<br><sub>C++</sub><br><sub>unclear</sub> | Large-scale transient 3D topology optimization with PETSc. | Includes the LGPL text, but source headers say all rights reserved. |
| [williamhunter/<br>topy](https://github.com/williamhunter/topy)<br><sub>Python</sub><br><sub>MIT</sub> | Lightweight 2D and 3D topology optimization framework. |  |
| [yuanming-hu/<br>spgrid_topo_opt](https://github.com/yuanming-hu/spgrid_topo_opt)<br><sub>C++</sub><br><sub>MIT and BSD, by component</sub> | Narrow-band topology optimization on sparsely populated grids. |  |
| [zfergus/<br>topopt](https://github.com/zfergus/topopt)<br><sub>Python</sub><br><sub>MIT</sub> | Python library for topology optimization. | README says it is at an early stage. |

</details>

<details>
<summary><a id="learning-based-topology-optimization"></a><h3>12.2 Learning-based topology optimization</h3></summary>
<p id="open-optimization-and-inverse-problems--learning-based-topology-optimization"><sub>Optimization and inverse problems › <b>12.2 Learning-based topology optimization</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [deng-cy/<br>deep_learning_<br>topology_opt](https://github.com/deng-cy/deep_learning_topology_opt)<br><sub>MATLAB</sub><br><sub>MIT</sub> | Self-directed online learning for topology optimization. | Most examples need MATLAB and COMSOL. |
| [dl4to/<br>dl4to](https://github.com/dl4to/dl4to)<br><sub>Python and Jupyter Notebook</sub><br><sub>Apache-2.0</sub> | PyTorch library for 3D topology optimization with neural networks. |  |
| [gigatskhondia/<br>gigala](https://github.com/gigatskhondia/gigala)<br><sub>Jupyter Notebook</sub><br><sub>MIT</sub> | Structural topology optimization with reinforcement learning, genetic algorithms and finite elements. |  |
| [Jasiuk-Research-<br>Group/<br>DeepEnergy-TopOpt](https://github.com/Jasiuk-Research-Group/DeepEnergy-TopOpt)<br><sub>Python</sub><br><sub>none found</sub> | Density-based topology optimization with the deep energy method. |  |
| [zhenguonie/<br>2020_TopologyGAN](https://github.com/zhenguonie/2020_TopologyGAN)<br><sub>Python</sub><br><sub>none found</sub> | Generative adversarial networks for topology optimization from physical fields. | Dataset is downloaded separately. |

</details>

<details>
<summary><a id="inverse-problems"></a><h3>12.3 Inverse problems</h3></summary>
<p id="open-optimization-and-inverse-problems--inverse-problems"><sub>Optimization and inverse problems › <b>12.3 Inverse problems</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [idaholab/<br>isopod](https://github.com/idaholab/isopod)<br><sub>C++</sub><br><sub>LGPL-2.1</sub> | MOOSE application for PDE-constrained multiphysics optimization. |  |
| [kailaix/<br>PhysGNN](https://github.com/kailaix/PhysGNN)<br><sub>Julia</sub><br><sub>none found</sub> | Physics-constrained generative networks, including a stochastic elasticity example. |  |
| [lu-group/<br>pinn-material-<br>identification](https://github.com/lu-group/pinn-material-identification)<br><sub>Python</sub><br><sub>Apache-2.0</sub> | Physics-informed networks for identifying material properties in solid mechanics. | Paper code. |
| [nandakishorebm1995/<br>FOR3022_Code](https://github.com/nandakishorebm1995/FOR3022_Code)<br><sub>MATLAB</sub><br><sub>none found</sub> | Bayesian damage identification in fiber metal laminates with model order reduction. | Requires MATLAB and COMSOL. |

</details>

</details>

<details>
<summary><a id="physics-informed-learning-and-energy-methods"></a><h2>13. Physics-informed learning and energy methods</h2></summary>
<p id="open-physics-informed-learning-and-energy-methods"><sub><b>13. Physics-informed learning and energy methods</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><a id="deep-energy-methods"></a><h3>13.1 Deep energy methods</h3></summary>
<p id="open-physics-informed-learning-and-energy-methods--deep-energy-methods"><sub>Physics-informed learning and energy methods › <b>13.1 Deep energy methods</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [FuhgJan/<br>mixedDEM](https://github.com/FuhgJan/mixedDEM)<br><sub>Python</sub><br><sub>conflicting statements</sub> | Mixed deep energy method for stress concentrations in finite-strain hyperelasticity. | README states both GPL-3.0 and a non-commercial Creative Commons license. |
| [ISM-Weimar/<br>DeepEnergyMethods](https://github.com/ISM-Weimar/DeepEnergyMethods)<br><sub>Python</sub><br><sub>MIT</sub> | Companion code for energy-based deep learning solutions of PDEs in mechanics. |  |
| [Jasiuk-Research-<br>Group/<br>DEM_for_J2_<br>plasticity](https://github.com/Jasiuk-Research-Group/DEM_for_J2_plasticity)<br><sub>Python</sub><br><sub>MIT</sub> | Deep energy method for 3D J2 elastoplasticity. |  |
| [Jasiuk-Research-<br>Group/<br>Graph_DEM](https://github.com/Jasiuk-Research-Group/Graph_DEM)<br><sub>Python</sub><br><sub>none found</sub> | Comparison of graph convolution and MLP deep energy methods for elastic solids. |  |
| [JinshuaiBai/<br>energy_PINN_<br>Contact](https://github.com/JinshuaiBai/energy_PINN_Contact)<br><sub>Python</sub><br><sub>none found</sub> | Energy-based PINN for frictionless large-deformation contact. |  |
| [MinhNguyenIKM/<br>dem_<br>hyperelasticity](https://github.com/MinhNguyenIKM/dem_hyperelasticity)<br><sub>Python</sub><br><sub>none found</sub> | Deep energy method for finite-deformation hyperelasticity. |  |
| [somdattagoswami/<br>DEM-PhaseField](https://github.com/somdattagoswami/DEM-PhaseField)<br><sub>Python</sub><br><sub>none found</sub> | Adaptive phase-field fracture with deep energy minimization. | Requires TensorFlow 1.15. |
| [yizheng-wang/<br>Research-on-<br>Solving-Partial-<br>Differential-<br>Equations-of-<br>Solid-Mechanics-<br>Based-on-PINN](https://github.com/yizheng-wang/Research-on-Solving-Partial-Differential-Equations-of-Solid-Mechanics-Based-on-PINN)<br><sub>Python</sub><br><sub>none found</sub> | Thesis code for solid mechanics with deep energy, CENN, DCEM and KINN methods. |  |

</details>

<details>
<summary><a id="residual-based-networks"></a><h3>13.2 Residual-based networks</h3></summary>
<p id="open-physics-informed-learning-and-energy-methods--residual-based-networks"><sub>Physics-informed learning and energy methods › <b>13.2 Residual-based networks</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [JinshuaiBai/<br>LSWR_loss_<br>function_PINN](https://github.com/JinshuaiBai/LSWR_loss_function_PINN)<br><sub>Python</sub><br><sub>none found</sub> | Least squares weighted residual loss for PINN solid mechanics. |  |
| [JinshuaiBai/<br>PINN_Comp_Mech](https://github.com/JinshuaiBai/PINN_Comp_Mech)<br><sub>Python</sub><br><sub>none found</sub> | Introductory PINN examples in solid mechanics with collocation and energy losses. |  |
| [JinshuaiBai/<br>PIRBN](https://github.com/JinshuaiBai/PIRBN)<br><sub>Python</sub><br><sub>none found</sub> | Physics-informed radial basis networks with spring, wave and viscoelastic flow examples. |  |
| [Raocp/<br>PINN-<br>elastodynamics](https://github.com/Raocp/PINN-elastodynamics)<br><sub>Python</sub><br><sub>none found</sub> | Physics-informed networks for elastodynamics without labeled data. |  |

</details>

<details>
<summary><a id="pinn-libraries-and-examples"></a><h3>13.3 PINN libraries and examples</h3></summary>
<p id="open-physics-informed-learning-and-energy-methods--pinn-libraries-and-examples"><sub>Physics-informed learning and energy methods › <b>13.3 PINN libraries and examples</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [ehsanhaghighat/<br>sciann-<br>applications](https://github.com/ehsanhaghighat/sciann-applications)<br><sub>Jupyter Notebook</sub><br><sub>MIT</sub> | SciANN examples, including elasticity, elastoplasticity, vibration and poroelasticity. | SciANN itself is unmaintained. |
| [lululxvi/<br>deepxde](https://github.com/lululxvi/deepxde)<br><sub>Python</sub><br><sub>LGPL-2.1</sub> | Library for physics-informed learning of forward and inverse differential equation problems. |  |

</details>

</details>

<details>
<summary><a id="surrogates-and-reduced-order-models"></a><h2>14. Surrogates and reduced-order models</h2></summary>
<p id="open-surrogates-and-reduced-order-models"><sub><b>14. Surrogates and reduced-order models</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><a id="stress-field-prediction"></a><h3>14.1 Stress-field prediction</h3></summary>
<p id="open-surrogates-and-reduced-order-models--stress-field-prediction"><sub>Surrogates and reduced-order models › <b>14.1 Stress-field prediction</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [farazarbabi/<br>CNN_FEM](https://github.com/farazarbabi/CNN_FEM)<br><sub>Python</sub><br><sub>all rights reserved</sub> | Convolutional network prediction of stress fields in solids from simulation data. | Stated in source file headers. |
| [federicosanna/<br>UNet-for-FEM-and-<br>Stress-<br>Distribution-<br>Inference](https://github.com/federicosanna/UNet-for-FEM-and-Stress-Distribution-Inference)<br><sub>Python</sub><br><sub>none found</sub> | U-Net inference of stress distributions from finite element data. | Some trained models are not included. |
| [Jasiuk-Research-<br>Group/<br>ResUNet-DeepONet-<br>Plasticity](https://github.com/Jasiuk-Research-Group/ResUNet-DeepONet-Plasticity)<br><sub>Python</sub><br><sub>MIT</sub> | Operator network prediction of plastic stress fields on varying geometries. |  |
| [lamm-mit/<br>FieldPredictorGAN](https://github.com/lamm-mit/FieldPredictorGAN)<br><sub>Python</sub><br><sub>MIT</sub> | Adversarial network prediction of stress and strain fields in composites. |  |
| [TML-Gatech/<br>DL_Stress_TAA](https://github.com/TML-Gatech/DL_Stress_TAA)<br><sub>all rights reserved</sub> | Deep learning surrogate of finite element stress analysis. | Source files are supplied as PDFs. |
| [zhenguonie/<br>2020_StressGAN](https://github.com/zhenguonie/2020_StressGAN)<br><sub>Python</sub><br><sub>none found</sub> | Generative model for 2D stress distribution prediction. |  |
| [zhenguonie/<br>stress_net](https://github.com/zhenguonie/stress_net)<br><sub>Python</sub><br><sub>none found</sub> | Convolutional prediction of stress fields in cantilevered structures. |  |

</details>

<details>
<summary><a id="deformation-and-reduced-dynamics"></a><h3>14.2 Deformation and reduced dynamics</h3></summary>
<p id="open-surrogates-and-reduced-order-models--deformation-and-reduced-dynamics"><sub>Surrogates and reduced-order models › <b>14.2 Deformation and reduced dynamics</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [AlbanOdot/<br>DeepPhysics-<br>article](https://github.com/AlbanOdot/DeepPhysics-article)<br><sub>Python</sub><br><sub>CC0-1.0</sub> | Paper code for physics-aware deep learning in real-time simulation. |  |
| [haller-group/<br>SSMLearn](https://github.com/haller-group/SSMLearn)<br><sub>MATLAB</sub><br><sub>AGPL-3.0</sub> | Data-driven reduced models of nonlinear dynamics on spectral submanifolds. | Written for MATLAB, Octave support not documented; requires SSMTool. |
| [lawsonfulton/<br>AutoDef](https://github.com/lawsonfulton/AutoDef)<br><sub>C++</sub><br><sub>MIT</sub> | Latent-space dynamics for reduced deformable simulation. | Install script can overwrite your Keras configuration. |
| [lrquad/<br>NNWarp](https://github.com/lrquad/NNWarp)<br><sub>C++</sub><br><sub>MIT</sub> | Neural network-based nonlinear deformable simulator. |  |
| [saurabhdeshpande93/<br>convolution-<br>aggregation-<br>attention](https://github.com/saurabhdeshpande93/convolution-aggregation-attention)<br><sub>Python and Mathematica</sub><br><sub>MIT</sub> | CNN, graph and attention surrogates for nonlinear finite element simulations. | Data generation uses AceFEM. |
| [stefaniafresca/<br>POD-DL-ROM](https://github.com/stefaniafresca/POD-DL-ROM)<br><sub>Python</sub><br><sub>none found</sub> | Deep learning reduced-order models enhanced by proper orthogonal decomposition. | README reports nonlinear elastodynamics tests; the example scripts are templates with blank settings. |
| [vividda/<br>3D-PhysNet](https://github.com/vividda/3D-PhysNet)<br><sub>Python</sub><br><sub>none found</sub> | Learned prediction of non-rigid 3D object deformation. | Python 2.7. |

</details>

<details>
<summary><a id="projection-based-model-reduction"></a><h3>14.3 Projection-based model reduction</h3></summary>
<p id="open-surrogates-and-reduced-order-models--projection-based-model-reduction"><sub>Surrogates and reduced-order models › <b>14.3 Projection-based model reduction</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [llnl/<br>libROM](https://github.com/llnl/libROM)<br><sub>C++</sub><br><sub>MIT or Apache-2.0, with restricted ParMETIS archive</sub> | Parallel library for intrusive and non-intrusive reduced-order models. | Bundled ParMETIS archive may not be redistributed without approval. |
| [pymor/<br>pymor](https://github.com/pymor/pymor)<br><sub>Python</sub><br><sub>BSD-2-Clause</sub> | Model order reduction library that works with external PDE solvers. |  |
| [RBniCS/<br>RBniCS](https://github.com/RBniCS/RBniCS)<br><sub>Python</sub><br><sub>LGPL-3.0-or-later</sub> | Reduced-order modeling techniques implemented in FEniCS. | Built on legacy FEniCS. |
| [SofaDefrost/<br>ModelOrder<br>Reduction](https://github.com/SofaDefrost/ModelOrderReduction)<br><sub>C++ and Python</sub><br><sub>GPL-2.0</sub> | Model reduction plugin for faster SOFA scenes. | Requires SOFA. |

</details>

<details>
<summary><a id="graph-neural-networks"></a><h3>14.4 Graph neural networks</h3></summary>
<p id="open-surrogates-and-reduced-order-models--graph-neural-networks"><sub>Surrogates and reduced-order models › <b>14.4 Graph neural networks</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [Jianxun-Wang/<br>graphGalerkin](https://github.com/Jianxun-Wang/graphGalerkin)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Physics-informed graph neural Galerkin networks for forward and inverse PDE problems. | Requires pyCaMOtk. |
| [m-ulmestrand/<br>gcn-collisions](https://github.com/m-ulmestrand/gcn-collisions)<br><sub>Python</sub><br><sub>Apache-2.0</sub> | Graph convolutional network that learns particle collision responses. |  |
| [wwMark/<br>meshgraphnets](https://github.com/wwMark/meshgraphnets)<br><sub>Python</sub><br><sub>Apache-2.0 in some files</sub> | PyTorch port of MeshGraphNets with cloth simulation. | Author says results do not fully match the original; files without an Apache header state no license. |
| [YasminSalehi/<br>PhysGNN](https://github.com/YasminSalehi/PhysGNN)<br><sub>Python</sub><br><sub>BSD-4-Clause</sub> | Graph neural network prediction of soft tissue deformation in neurosurgery. |  |

</details>

<details>
<summary><a id="biomechanical-surrogates"></a><h3>14.5 Biomechanical surrogates</h3></summary>
<p id="open-surrogates-and-reduced-order-models--biomechanical-surrogates"><sub>Surrogates and reduced-order models › <b>14.5 Biomechanical surrogates</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [dabiriyaghoub/<br>Ventricular_ML_<br>DecisionTrees](https://github.com/dabiriyaghoub/Ventricular_ML_DecisionTrees)<br><sub>Python</sub><br><sub>all rights reserved</sub> | Machine learning prediction of left ventricular mechanics. |  |
| [michetonu/<br>MALTIDEM--Machine-<br>Learning-for-<br>Tissue-<br>Deformation-<br>Modelling](https://github.com/michetonu/MALTIDEM--Machine-Learning-for-Tissue-Deformation-Modelling)<br><sub>MATLAB</sub><br><sub>none found</sub> | Data-driven real-time model of brain tumor deformation for neurosurgery. | Workflow uses MATLAB and FEBio. |

</details>

<details>
<summary><a id="response-histories-and-operator-learning"></a><h3>14.6 Response histories and operator learning</h3></summary>
<p id="open-surrogates-and-reduced-order-models--response-histories-and-operator-learning"><sub>Surrogates and reduced-order models › <b>14.6 Response histories and operator learning</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [Jasiuk-Research-<br>Group/<br>Bio-inspired-low-<br>porosity-<br>structures-using-<br>Neural-Networks-<br>GRU-Implemenation](https://github.com/Jasiuk-Research-Group/Bio-inspired-low-porosity-structures-using-Neural-Networks-GRU-Implemenation)<br><sub>Python</sub><br><sub>MIT</sub> | Recurrent network prediction of stress-strain response and energy absorption in bio-inspired structures. |  |
| [Jasiuk-Research-<br>Group/<br>CMDS-14-impact-<br>resistantance-NN-<br>prediction-](https://github.com/Jasiuk-Research-Group/CMDS-14-impact-resistantance-NN-prediction-)<br><sub>Python</sub><br><sub>none found</sub> | Neural networks for structure-property relations in impact-resistant structures. |  |
| [Jasiuk-Research-<br>Group/<br>LatticeResponse_<br>NN_Prediction](https://github.com/Jasiuk-Research-Group/LatticeResponse_NN_Prediction)<br><sub>Python</sub><br><sub>none found</sub> | Recurrent network prediction of lattice stress-strain curves and energy absorption. |  |
| [Jasiuk-Research-<br>Group/<br>S-DeepONet](https://github.com/Jasiuk-Research-Group/S-DeepONet)<br><sub>Python</sub><br><sub>none found</sub> | Sequential operator network with plasticity and heat transfer examples. |  |
| [Jasiuk-Research-<br>Group/<br>S-DeepONet-<br>transient-<br>predictions](https://github.com/Jasiuk-Research-Group/S-DeepONet-transient-predictions)<br><sub>Python</sub><br><sub>none found</sub> | Sequential operator network for transient full-field predictions, including plasticity. |  |
| [JinshuaiBai/<br>Discrete-Solution-<br>Operator-Learning-<br>DiSOL](https://github.com/JinshuaiBai/Discrete-Solution-Operator-Learning-DiSOL)<br><sub>Python and MATLAB</sub><br><sub>MIT</sub> | Discrete solution operator learning for geometry-dependent PDEs, including linear elasticity. | Training datasets are downloaded from Zenodo; MATLAB is used for data generation. |

</details>

<details>
<summary><a id="frameworks-and-introductory-studies"></a><h3>14.7 Frameworks and introductory studies</h3></summary>
<p id="open-surrogates-and-reduced-order-models--frameworks-and-introductory-studies"><sub>Surrogates and reduced-order models › <b>14.7 Frameworks and introductory studies</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [hmjeon/<br>FEM-ML](https://github.com/hmjeon/FEM-ML)<br><sub>Jupyter Notebook</sub><br><sub>GPL-3.0</sub> | Experiments in finite element analysis with machine learning. | Sparse documentation. |
| [mimesis-inria/<br>DeepPhysX](https://github.com/mimesis-inria/DeepPhysX)<br><sub>Python</sub><br><sub>AGPL-3.0</sub> | Interface between numerical simulations and learning algorithms for training and prediction. |  |
| [oleksiyskononenko/<br>mlfem](https://github.com/oleksiyskononenko/mlfem)<br><sub>Jupyter Notebook</sub><br><sub>none found</sub> | Notebook and report on deep learning with finite element models of physical systems. |  |

</details>

<details>
<summary><a id="benchmark-datasets"></a><h3>14.8 Benchmark datasets</h3></summary>
<p id="open-surrogates-and-reduced-order-models--benchmark-datasets"><sub>Surrogates and reduced-order models › <b>14.8 Benchmark datasets</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [elejeune11/<br>Mechanical-MNIST](https://github.com/elejeune11/Mechanical-MNIST)<br><sub>Python</sub><br><sub>MIT code, CC-BY-SA-3.0 data</sub> | Benchmark of 70,000 large-deformation finite element simulations for surrogate models. |  |

</details>

</details>

<details>
<summary><a id="meshing-pre--and-post-processing"></a><h2>15. Meshing, pre- and post-processing</h2></summary>
<p id="open-meshing-pre--and-post-processing"><sub><b>15. Meshing, pre- and post-processing</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><a id="mesh-generation"></a><h3>15.1 Mesh generation</h3></summary>
<p id="open-meshing-pre--and-post-processing--mesh-generation"><sub>Meshing, pre- and post-processing › <b>15.1 Mesh generation</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [fangq/<br>iso2mesh](https://github.com/fangq/iso2mesh)<br><sub>MATLAB</sub><br><sub>GPL-2.0-or-later, excluding bundled binaries</sub> | Surface and volumetric mesh generation from 3D images. | Runs in MATLAB or Octave; bundled binaries have their own licenses. |
| [gmsh/<br>gmsh](https://gitlab.onelab.info/gmsh/gmsh)<br><sub>C++</sub><br><sub>GPL-2.0-or-later with linking exception</sub> | 3D finite element mesh generator with pre- and post-processing. |  |
| [inducer/<br>meshpy](https://github.com/inducer/meshpy)<br><sub>C++</sub><br><sub>MIT wrapper, with Triangle and AGPL-3.0 components</sub> | Python interfaces to the Triangle and TetGen mesh generators. | Triangle restricts commercial distribution. |
| [meshpro/<br>dmsh](https://github.com/meshpro/dmsh)<br><sub>unclear</sub> | Simple 2D mesh generator inspired by distmesh. | No source in the repository; GitHub reports GPL-3.0, but there is no license file. |
| [meshpro/<br>meshzoo](https://github.com/meshpro/meshzoo)<br><sub>none found</sub> | Generators of meshes for simple canonical domains. | No source in the repository. |
| [meshpro/<br>pygalmesh](https://github.com/meshpro/pygalmesh)<br><sub>C++</sub><br><sub>GPL-3.0</sub> | Python front end to CGAL's 2D and 3D mesh generators. | Commercial license offered separately. |
| [NGSolve/<br>netgen](https://github.com/NGSolve/netgen)<br><sub>C++</sub><br><sub>LGPL-2.1</sub> | Automatic 3D tetrahedral mesh generator. |  |
| [nschloe/<br>pygmsh](https://github.com/nschloe/pygmsh)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Python abstractions for building geometries and meshes with Gmsh. |  |
| [pyvista/<br>scikit-gmsh](https://github.com/pyvista/scikit-gmsh)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Python interface to Gmsh for finite element meshes. |  |
| [pyvista/<br>tetgen](https://github.com/pyvista/tetgen)<br><sub>C++ and Python</sub><br><sub>MIT wrapper, with AGPL-3.0 TetGen</sub> | Python interface to the TetGen tetrahedral mesh generator. |  |
| [sandialabs/<br>vorocrust-meshing](https://github.com/sandialabs/vorocrust-meshing)<br><sub>C++</sub><br><sub>BSD-3-Clause</sub> | Conforming Voronoi meshing of non-convex and non-manifold domains. |  |
| [wildmeshing/<br>fTetWild](https://github.com/wildmeshing/fTetWild)<br><sub>C++</sub><br><sub>MPL-2.0</sub> | Fast and robust tetrahedral meshing of imperfect input geometry. |  |
| [wildmeshing/<br>TriWild](https://github.com/wildmeshing/TriWild)<br><sub>C++</sub><br><sub>MPL-2.0</sub> | Robust triangulation with curve constraints. | README requires citation. |

</details>

<details>
<summary><a id="mesh-processing-and-formats"></a><h3>15.2 Mesh processing and formats</h3></summary>
<p id="open-meshing-pre--and-post-processing--mesh-processing-and-formats"><sub>Meshing, pre- and post-processing › <b>15.2 Mesh processing and formats</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [meshpro/<br>meshplex](https://github.com/meshpro/meshplex)<br><sub>proprietary</sub> | Geometric quantities such as areas and volumes for simplex meshes. | No source in the repository; full use requires a paid license. |
| [mikedh/<br>trimesh](https://github.com/mikedh/trimesh)<br><sub>Python</sub><br><sub>MIT</sub> | Python library for loading, editing and analyzing triangular meshes. |  |
| [nschloe/<br>meshio](https://github.com/nschloe/meshio)<br><sub>Python</sub><br><sub>MIT</sub> | Reader, writer and converter for many mesh file formats. |  |
| [sandialabs/<br>seacas](https://github.com/sandialabs/seacas)<br><sub>C, Fortran and C++</sub><br><sub>BSD-3-Clause</sub> | Suite for finite element pre-processing, post-processing and translation. |  |
| [wildmeshing/<br>wildmeshing-<br>toolkit](https://github.com/wildmeshing/wildmeshing-toolkit)<br><sub>C++</sub><br><sub>MIT</sub> | Parallel triangle and tetrahedral mesh generation and editing. |  |

</details>

<details>
<summary><a id="visualization-and-export"></a><h3>15.3 Visualization and export</h3></summary>
<p id="open-meshing-pre--and-post-processing--visualization-and-export"><sub>Meshing, pre- and post-processing › <b>15.3 Visualization and export</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [GLVis/<br>glvis](https://github.com/GLVis/glvis)<br><sub>C++</sub><br><sub>BSD-3-Clause</sub> | OpenGL visualization of finite element meshes and functions. |  |
| [Kitware/<br>ParaView](https://github.com/Kitware/ParaView)<br><sub>C++</sub><br><sub>BSD-3-Clause</sub> | Parallel data analysis and visualization application built on VTK. |  |
| [Liujie-SYSU/<br>odb2vtk](https://github.com/Liujie-SYSU/odb2vtk)<br><sub>Python</sub><br><sub>none found</sub> | Converter from Abaqus ODB results to VTK for ParaView. | Input is Abaqus output. |
| [paulo-herrera/<br>PyEVTK](https://github.com/paulo-herrera/PyEVTK)<br><sub>Python</sub><br><sub>MIT (stated in source)</sub> | Pure-Python export of data to binary VTK files. |  |
| [pyvista/<br>pyvista](https://github.com/pyvista/pyvista)<br><sub>Python</sub><br><sub>MIT</sub> | 3D visualization and mesh analysis with a NumPy-based interface. |  |

</details>

</details>

<details>
<summary><a id="linear-eigenvalue-and-nonlinear-solvers"></a><h2>16. Linear, eigenvalue and nonlinear solvers</h2></summary>
<p id="open-linear-eigenvalue-and-nonlinear-solvers"><sub><b>16. Linear, eigenvalue and nonlinear solvers</b> · <a href="#contents">Back to contents</a></sub></p>

The right solver depends on the structure of the discrete problem.

- **Symmetric positive definite**, as in many compressible elasticity problems: use Cholesky, or conjugate gradients with a preconditioner. For smoothed-aggregation multigrid, supply the rigid body modes.
- **Symmetric indefinite**, as in mixed formulations and frictionless Lagrange multiplier contact: use an LDLᵀ factorization, MINRES with a positive definite preconditioner, or GMRES with a block preconditioner.
- **Nonsymmetric**, as with friction or non-associated plasticity: use LU, or GMRES or BiCGSTAB with a preconditioner.
- **Snap-through and buckling**: the tangent becomes singular. Arc-length continuation can pass a limit point, where load-controlled Newton fails. Following a buckled branch from a bifurcation also needs an imperfection or branch switching.
- **Any system**: a small residual does not guarantee a small error when the matrix is ill-conditioned.

Further reading: [Davis et al. (2016)](https://doi.org/10.1017/S0962492916000076) on direct methods, [Saad (2003)](https://doi.org/10.1137/1.9780898718003) on iterative methods, [Benzi et al. (2005)](https://doi.org/10.1017/S0962492904000212) on saddle point problems and [Higham (2002)](https://doi.org/10.1137/1.9780898718027) on accuracy and stability.

<details>
<summary><a id="solver-toolkits"></a><h3>16.1 Solver toolkits</h3></summary>
<p id="open-linear-eigenvalue-and-nonlinear-solvers--solver-toolkits"><sub>Linear, eigenvalue and nonlinear solvers › <b>16.1 Solver toolkits</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [ginkgo-project/<br>ginkgo](https://github.com/ginkgo-project/ginkgo)<br><sub>C++</sub><br><sub>BSD-3-Clause</sub> | Sparse linear algebra library for multicore processors and GPUs. |  |
| [petsc/<br>petsc](https://gitlab.com/petsc/petsc)<br><sub>C</sub><br><sub>BSD-2-Clause</sub> | Parallel toolkit of linear, nonlinear and time-stepping solvers for PDE-based models. |  |
| [polyfem/<br>polysolve](https://github.com/polyfem/polysolve)<br><sub>C++</sub><br><sub>MIT</sub> | Common interface to external linear solvers, with its own nonlinear solvers. |  |
| [trilinos/<br>Trilinos](https://github.com/trilinos/Trilinos)<br><sub>C++</sub><br><sub>BSD and (L)GPL, by package</sub> | Collection of packages for large-scale solvers, discretization and optimization. |  |

</details>

<details>
<summary><a id="dense-linear-algebra"></a><h3>16.2 Dense linear algebra</h3></summary>
<p id="open-linear-eigenvalue-and-nonlinear-solvers--dense-linear-algebra"><sub>Linear, eigenvalue and nonlinear solvers › <b>16.2 Dense linear algebra</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [flame/<br>blis](https://github.com/flame/blis)<br><sub>C</sub><br><sub>BSD-3-Clause</sub> | Framework for building BLAS-like dense linear algebra libraries. |  |
| [libeigen/<br>eigen](https://gitlab.com/libeigen/eigen)<br><sub>C++</sub><br><sub>MPL-2.0, with permissive third-party files</sub> | C++ template library for dense and sparse linear algebra. |  |
| [OpenMathLib/<br>OpenBLAS](https://github.com/OpenMathLib/OpenBLAS)<br><sub>C</sub><br><sub>BSD-3-Clause</sub> | Optimized implementation of the BLAS kernels used by many solvers. |  |
| [Reference-LAPACK/<br>lapack](https://github.com/Reference-LAPACK/lapack)<br><sub>Fortran</sub><br><sub>BSD-3-Clause</sub> | Reference routines for linear systems, least squares and eigenvalue problems. |  |

</details>

<details>
<summary><a id="sparse-direct-solvers"></a><h3>16.3 Sparse direct solvers</h3></summary>
<p id="open-linear-eigenvalue-and-nonlinear-solvers--sparse-direct-solvers"><sub>Linear, eigenvalue and nonlinear solvers › <b>16.3 Sparse direct solvers</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [DrTimothyAlden<br>Davis/<br>SuiteSparse](https://github.com/DrTimothyAldenDavis/SuiteSparse)<br><sub>C</sub><br><sub>BSD, Apache-2.0, LGPL and GPL, by package</sub> | Sparse matrix packages, including the CHOLMOD, UMFPACK and KLU factorizations. | Some packages, including UMFPACK, are GPL. |
| [pghysels/<br>STRUMPACK](https://github.com/pghysels/STRUMPACK)<br><sub>C++</sub><br><sub>BSD-3-Clause, with restricted MC64 code</sub> | Sparse direct solvers and preconditioners that use rank-structured compression. | Bundled MC64 may not be passed to third parties without its authors' consent. |
| [ralna/<br>spral](https://github.com/ralna/spral)<br><sub>Fortran</sub><br><sub>BSD-3-Clause</sub> | Sparse algorithms, including factorizations for symmetric systems. |  |
| [scivision/<br>mumps-superbuild](https://github.com/scivision/mumps-superbuild)<br><sub>CMake</sub><br><sub>MIT build scripts, CeCILL-C MUMPS</sub> | CMake build of the MUMPS parallel multifrontal solver and its dependencies. | Build scripts, not the official MUMPS repository. |
| [xiaoyeli/<br>superlu](https://github.com/xiaoyeli/superlu)<br><sub>C</sub><br><sub>BSD-3-Clause, with restricted MC64 code</sub> | Sequential supernodal LU factorization for sparse nonsymmetric systems. | Bundled MC64 may not be passed to third parties without its authors' consent. |
| [xiaoyeli/<br>superlu_dist](https://github.com/xiaoyeli/superlu_dist)<br><sub>C</sub><br><sub>BSD-3-Clause, with restricted MC64 code</sub> | Distributed-memory sparse LU factorization with static pivoting. | Bundled MC64 may not be passed to third parties without its authors' consent. |

</details>

<details>
<summary><a id="iterative-solvers-and-preconditioners"></a><h3>16.4 Iterative solvers and preconditioners</h3></summary>
<p id="open-linear-eigenvalue-and-nonlinear-solvers--iterative-solvers-and-preconditioners"><sub>Linear, eigenvalue and nonlinear solvers › <b>16.4 Iterative solvers and preconditioners</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [anishida/<br>lis](https://github.com/anishida/lis)<br><sub>C</sub><br><sub>BSD-3-Clause</sub> | Parallel iterative solvers for linear systems and eigenvalue problems. |  |
| [ddemidov/<br>amgcl](https://github.com/ddemidov/amgcl)<br><sub>C++</sub><br><sub>MIT</sub> | Header-only algebraic multigrid for large sparse linear systems. |  |
| [gridap/<br>GridapSolvers.jl](https://github.com/gridap/GridapSolvers.jl)<br><sub>Julia</sub><br><sub>MIT</sub> | Block, multigrid and other physics-tailored solvers for Gridap. |  |
| [hpddm/<br>hpddm](https://github.com/hpddm/hpddm)<br><sub>C++</sub><br><sub>LGPL-3.0</sub> | Domain decomposition methods, including overlapping Schwarz, FETI and BDD. |  |
| [hypre-space/<br>hypre](https://github.com/hypre-space/hypre)<br><sub>C</sub><br><sub>MIT or Apache-2.0</sub> | Parallel preconditioners and solvers with algebraic and structured multigrid. |  |
| [JuliaSmooth<br>Optimizers/<br>Krylov.jl](https://github.com/JuliaSmoothOptimizers/Krylov.jl)<br><sub>Julia</sub><br><sub>MPL-2.0</sub> | Collection of Krylov methods for linear and least-squares problems. |  |
| [NVIDIA/<br>AMGX](https://github.com/NVIDIA/AMGX)<br><sub>C++ and CUDA</sub><br><sub>BSD-3-Clause, with Apache-2.0 CUSP</sub> | Distributed algebraic multigrid and Krylov solvers for GPUs. | Requires CUDA. |
| [pyamg/<br>pyamg](https://github.com/pyamg/pyamg)<br><sub>Python</sub><br><sub>MIT</sub> | Algebraic multigrid solvers in Python. |  |

</details>

<details>
<summary><a id="nonlinear-solvers-time-integration-and-continuation"></a><h3>16.5 Nonlinear solvers, time integration and continuation</h3></summary>
<p id="open-linear-eigenvalue-and-nonlinear-solvers--nonlinear-solvers-time-integration-and-continuation"><sub>Linear, eigenvalue and nonlinear solvers › <b>16.5 Nonlinear solvers, time integration and continuation</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [bifurcationkit/<br>BifurcationKit.jl](https://github.com/bifurcationkit/BifurcationKit.jl)<br><sub>Julia</sub><br><sub>MIT</sub> | Continuation and bifurcation analysis, for tracing instabilities and solution branches. |  |
| [coin-or/<br>Ipopt](https://github.com/coin-or/Ipopt)<br><sub>C++</sub><br><sub>EPL-2.0</sub> | Interior point solver for large constrained nonlinear optimization. | Optional HSL and Pardiso solvers have separate licenses. |
| [llnl/<br>sundials](https://github.com/llnl/sundials)<br><sub>C</sub><br><sub>BSD-3-Clause</sub> | Time integrators and nonlinear solvers for ODE and differential-algebraic systems. |  |
| [pprachas/<br>fenics_arclength](https://github.com/pprachas/fenics_arclength)<br><sub>Python</sub><br><sub>MIT</sub> | Riks arc-length solver for tracing unstable equilibrium paths in FEniCS. | Requires legacy FEniCS 2019.1, not FEniCSx. |
| [SciML/<br>NonlinearSolve.jl](https://github.com/SciML/NonlinearSolve.jl)<br><sub>Julia</sub><br><sub>MIT</sub> | Newton-type and other root-finding methods for nonlinear systems. |  |

</details>

<details>
<summary><a id="eigenvalue-solvers"></a><h3>16.6 Eigenvalue solvers</h3></summary>
<p id="open-linear-eigenvalue-and-nonlinear-solvers--eigenvalue-solvers"><sub>Linear, eigenvalue and nonlinear solvers › <b>16.6 Eigenvalue solvers</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [opencollab/<br>arpack-ng](https://github.com/opencollab/arpack-ng)<br><sub>Fortran</sub><br><sub>BSD-3-Clause</sub> | Community-maintained ARPACK routines for large eigenvalue problems. |  |
| [primme/<br>primme](https://github.com/primme/primme)<br><sub>C</sub><br><sub>BSD-3-Clause, with LGPL test files</sub> | Preconditioned eigenvalue and singular value solvers for large problems. |  |
| [slepc/<br>slepc](https://gitlab.com/slepc/slepc)<br><sub>C</sub><br><sub>BSD-2-Clause</sub> | Parallel solvers for large sparse eigenvalue problems, built on PETSc. |  |
| [yixuan/<br>spectra](https://github.com/yixuan/spectra)<br><sub>C++</sub><br><sub>MPL-2.0</sub> | Header-only C++ library for computing a few eigenvalues of large matrices. |  |

</details>

<details>
<summary><a id="matrix-free-operators-and-partitioning"></a><h3>16.7 Matrix-free operators and partitioning</h3></summary>
<p id="open-linear-eigenvalue-and-nonlinear-solvers--matrix-free-operators-and-partitioning"><sub>Linear, eigenvalue and nonlinear solvers › <b>16.7 Matrix-free operators and partitioning</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [CEED/<br>libCEED](https://github.com/CEED/libCEED)<br><sub>C</sub><br><sub>BSD-2-Clause, with LGPL deal.II examples</sub> | Matrix-free evaluation of finite element operators on CPUs and GPUs. |  |
| [KaHIP/<br>KaHIP](https://github.com/KaHIP/KaHIP)<br><sub>C++</sub><br><sub>MIT</sub> | Multilevel graph partitioning and node ordering. |  |
| [KarypisLab/<br>METIS](https://github.com/KarypisLab/METIS)<br><sub>C</sub><br><sub>Apache-2.0</sub> | Graph and mesh partitioning, and fill-reducing orderings for sparse matrices. |  |
| [KarypisLab/<br>ParMETIS](https://github.com/KarypisLab/ParMETIS)<br><sub>C</sub><br><sub>custom, with non-commercial restrictions</sub> | MPI library for parallel partitioning and fill-reducing ordering. | Free only for non-profit and US government education and research; others need approval for anything beyond evaluation; redistribution also needs approval. |

</details>

</details>

<details>
<summary><a id="verification-validation-and-uncertainty"></a><h2>17. Verification, validation and uncertainty</h2></summary>
<p id="open-verification-validation-and-uncertainty"><sub><b>17. Verification, validation and uncertainty</b> · <a href="#contents">Back to contents</a></sub></p>

These answer different questions, and passing one does not imply passing the others.

- **Code verification**: are the equations implemented correctly? Compare observed and expected convergence rates on exact or manufactured solutions ([Roache, 2002](https://doi.org/10.1115/1.1436090)).
- **Solution verification**: how large is the numerical error in this result? Study mesh, time step and solver tolerances ([Roy, 2005](https://doi.org/10.1016/j.jcp.2004.10.036)).
- **Validation**: does the model represent reality for its intended use? Compare with experiments that were not used for calibration. Agreement with another simulation is not validation.
- **Uncertainty quantification**: how much do uncertain inputs, model form and numerical error affect the prediction ([Roy and Oberkampf, 2011](https://doi.org/10.1016/j.cma.2011.03.016))?

Guidance: [ASME V&V 10](https://webstore.ansi.org/standards/asme/asme102019r2025) for solid mechanics (paid), [NASA-STD-7009B](https://standards.nasa.gov/sites/default/files/standards/NASA/B/1/NASA-STD-7009B-Final-3-5-2024.pdf) for models and simulations, [ten rules for credible simulation in healthcare](https://doi.org/10.1186/s12967-020-02540-4) and the book by [Oberkampf and Roy (2010)](https://doi.org/10.1017/CBO9780511760396). Published cardiac benchmarks: [Land et al. (2015)](https://doi.org/10.1098/rspa.2015.0641) and [Aróstica et al. (2025)](https://doi.org/10.1016/j.cma.2024.117485).

<details>
<summary><a id="code-and-solution-verification"></a><h3>17.1 Code and solution verification</h3></summary>
<p id="open-verification-validation-and-uncertainty--code-and-solution-verification"><sub>Verification, validation and uncertainty › <b>17.1 Code and solution verification</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [lanl/<br>ExactPack](https://github.com/lanl/ExactPack)<br><sub>Python</sub><br><sub>BSD-3-Clause</sub> | Exact solutions of verification problems in solids, heat conduction and hydrodynamics. | Solid mechanics covers the Blake and elastic-plastic piston problems. |
| [manufactured-<br>solutions/<br>MASA](https://github.com/manufactured-solutions/MASA)<br><sub>C++</sub><br><sub>LGPL-2.1</sub> | Library of manufactured solutions for verifying PDE solvers. | Examples are mainly heat transfer and fluid flow. |
| [OSEL-DAM/<br>SimEval](https://github.com/OSEL-DAM/SimEval)<br><sub>Python and Jupyter Notebook</sub><br><sub>CC0-1.0</sub> | Notebooks on code and calculation verification, including for physics-informed networks. |  |
| [tomrobin-teschner/<br>pyGCS](https://github.com/tomrobin-teschner/pyGCS)<br><sub>Python</sub><br><sub>MIT</sub> | Grid convergence index calculations for estimating discretization error. |  |

</details>

<details>
<summary><a id="benchmarks-and-reference-solutions"></a><h3>17.2 Benchmarks and reference solutions</h3></summary>
<p id="open-verification-validation-and-uncertainty--benchmarks-and-reference-solutions"><sub>Verification, validation and uncertainty › <b>17.2 Benchmarks and reference solutions</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [febiosoftware/<br>TestSuite](https://github.com/febiosoftware/TestSuite)<br><sub>Python</sub><br><sub>none found</sub> | FEBio test problems with stored results for regression testing. | Regression results are not independent reference solutions; no README. |
| [finsberg/<br>cardiac_benchmark](https://github.com/finsberg/cardiac_benchmark)<br><sub>Python</sub><br><sub>MIT (stated in README)</sub> | Simula's implementation of a published cardiac elastodynamics benchmark. |  |
| [javijv4/<br>arostica-benchmark](https://github.com/javijv4/arostica-benchmark)<br><sub>Python</sub><br><sub>none found</sub> | Cardiac elastodynamics test against the envelope of ten published solutions. | Requires svMultiPhysics. |
| [Kratos<br>Multiphysics/<br>Examples (contact)](https://github.com/KratosMultiphysics/Examples/tree/master/contact_structural_mechanics/validation)<br><sub>Python</sub><br><sub>none found</sub> | Kratos contact benchmarks, including Hertz, press-fit and ironing cases. |  |
| [Kratos<br>Multiphysics/<br>Examples (structural)](https://github.com/KratosMultiphysics/Examples/tree/master/structural_mechanics/validation)<br><sub>Python</sub><br><sub>none found</sub> | Kratos benchmarks for beams, trusses and membranes, including large deflection and snap-through. |  |
| [Simulation-<br>Benchmarks/<br>linear-elastic-<br>plate-with-hole](https://github.com/Simulation-Benchmarks/linear-elastic-plate-with-hole)<br><sub>Python</sub><br><sub>MIT code, CC-BY-4.0 docs, CC0-1.0 data</sub> | Plate-with-hole benchmark comparing finite element codes with the Kirsch solution. |  |
| [Simulation-<br>Benchmarks/<br>NFDI4IngModel<br>ValidationPlatform](https://github.com/Simulation-Benchmarks/NFDI4IngModelValidationPlatform)<br><sub>Jupyter Notebook</sub><br><sub>MIT</sub> | Registry and shared workflows for reproducible simulation benchmarks. |  |
| [TadeasSvetlik/<br>Elastoplastic-<br>contact-2D-<br>benchmarks](https://github.com/TadeasSvetlik/Elastoplastic-contact-2D-benchmarks)<br><sub>MATLAB</sub><br><sub>none found</sub> | Inputs and reference results for 2D elastic and elastoplastic contact benchmarks. | No README. |

</details>

<details>
<summary><a id="experimental-data-for-validation"></a><h3>17.3 Experimental data for validation</h3></summary>
<p id="open-verification-validation-and-uncertainty--experimental-data-for-validation"><sub>Verification, validation and uncertainty › <b>17.3 Experimental data for validation</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [dlr-wf/<br>crackmnist](https://github.com/dlr-wf/crackmnist)<br><sub>Python</sub><br><sub>MIT code, CC-BY-4.0 data (stated in README)</sub> | Annotated displacement fields measured by image correlation in fatigue crack growth tests. |  |
| [llamm-de/<br>thermalCANN](https://github.com/llamm-de/thermalCANN/tree/main/data/Treloar)<br><sub>Python</sub><br><sub>MIT</sub> | Treloar's rubber data for uniaxial, equibiaxial and pure shear loading, as republished in 2012. | The Arruda-Boyce file is a model fit, not measured data. |
| [sanjayg0/<br>epcms](https://github.com/sanjayg0/epcms)<br><sub>MATLAB</sub><br><sub>MIT</sub> | Continuum mechanics example codes with tension test data for steel and aluminum. |  |
| [Simulation-<br>Benchmarks/<br>four-point-<br>bending-test](https://github.com/Simulation-Benchmarks/four-point-bending-test)<br><sub>Python</sub><br><sub>none found</sub> | Reinforced concrete beam benchmark with deflections and strains from a 1963 experiment. | The finite element models require Ansys. |

</details>

<details>
<summary><a id="calibration-and-bayesian-inference"></a><h3>17.4 Calibration and Bayesian inference</h3></summary>
<p id="open-verification-validation-and-uncertainty--calibration-and-bayesian-inference"><sub>Verification, validation and uncertainty › <b>17.4 Calibration and Bayesian inference</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [BAMresearch/<br>probeye](https://github.com/BAMresearch/probeye)<br><sub>Python</sub><br><sub>MIT</sub> | Solver-independent definition of parameter estimation problems, mainly solved by sampling. |  |
| [CUQI-DTU/<br>CUQIpy](https://github.com/CUQI-DTU/CUQIpy)<br><sub>Python</sub><br><sub>Apache-2.0</sub> | Bayesian modeling and uncertainty quantification for inverse problems. |  |
| [hippylib/<br>hippylib](https://github.com/hippylib/hippylib)<br><sub>Python</sub><br><sub>GPL-2.0</sub> | Deterministic and Bayesian inversion for models governed by PDEs. |  |
| [sandialabs/<br>matcal](https://github.com/sandialabs/matcal)<br><sub>Python</sub><br><sub>BSD-3-Clause</sub> | Calibration of material models to experimental data. | Built-in characterization test models are for SierraSM. |

</details>

<details>
<summary><a id="uncertainty-and-sensitivity-analysis"></a><h3>17.5 Uncertainty and sensitivity analysis</h3></summary>
<p id="open-verification-validation-and-uncertainty--uncertainty-and-sensitivity-analysis"><sub>Verification, validation and uncertainty › <b>17.5 Uncertainty and sensitivity analysis</b> · <a href="#contents">Back to contents</a></sub></p>

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

</details>

</details>

<details>
<summary><a id="courses-references-and-agents-for-mechanics"></a><h2>18. Courses, references and agents for mechanics</h2></summary>
<p id="open-courses-references-and-agents-for-mechanics"><sub><b>18. Courses, references and agents for mechanics</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><a id="courses-and-tutorials"></a><h3>18.1 Courses and tutorials</h3></summary>
<p id="open-courses-references-and-agents-for-mechanics--courses-and-tutorials"><a id="textbooks-and-numerical-tutorials"></a><a id="open-courses-references-and-agents-for-mechanics--textbooks-and-numerical-tutorials"></a><sub>Courses, references and agents for mechanics › <b>18.1 Courses and tutorials</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [albower/<br>Applied_Mechanics_<br>of_Solids](https://github.com/albower/Applied_Mechanics_of_Solids)<br><sub>MATLAB</sub><br><sub>none found</sub> | Problem sets and finite element codes for Bower's Applied Mechanics of Solids. | Requires MATLAB. |
| [bleyerj/<br>comet-fenicsx](https://github.com/bleyerj/comet-fenicsx)<br><sub>Python</sub><br><sub>CC-BY-SA-4.0</sub> | Numerical tours of computational mechanics with FEniCSx. |  |
| [bueler/<br>p4pdes](https://github.com/bueler/p4pdes)<br><sub>C</sub><br><sub>MIT</sub> | Example programs from a book on solving PDEs with PETSc and Firedrake. |  |
| [Ceyron/<br>machine-learning-<br>and-simulation](https://github.com/Ceyron/machine-learning-and-simulation)<br><sub>Jupyter Notebook</sub><br><sub>MIT</sub> | Notes and code for a video course on simulation and machine learning, including continuum mechanics and FEniCS. |  |
| [cooperrc/<br>computational-<br>mechanics](https://github.com/cooperrc/computational-mechanics)<br><sub>MATLAB</sub><br><sub>CC-BY-4.0 content, BSD-3-Clause code (stated in README)</sub> | Open course materials on computational mechanics. | Includes code written for MATLAB, Octave support not documented. |
| [dilevin/<br>CSC417-a4-cloth-<br>simulation](https://github.com/dilevin/CSC417-a4-cloth-simulation)<br><sub>C++</sub><br><sub>none found</sub> | Course assignment on finite element cloth simulation with contact. | Starter code for an assignment. |
| [finite-element/<br>finite-element-<br>course](https://github.com/finite-element/finite-element-course)<br><sub>Python</sub><br><sub>MIT (stated in pyproject.toml)</sub> | Imperial College course on finite element analysis and implementation. | No README. |
| [gridap/<br>Tutorials](https://github.com/gridap/Tutorials)<br><sub>Julia</sub><br><sub>MIT</sub> | Worked tutorials on solving PDEs with Gridap. |  |
| [Interactive<br>ComputerGraphics/<br>physics-simulation](https://github.com/InteractiveComputerGraphics/physics-simulation)<br><sub>MIT</sub> | Introduction to simulation of rigid bodies, deformable solids and fluids. | Documents only, no code. |
| [jomorlier/<br>feacourse](https://github.com/jomorlier/feacourse)<br><sub>MATLAB</sub><br><sub>none found</sub> | Materials for a computational solid mechanics course. | Tutorials are written for MATLAB; assignments also use commercial solvers. |
| [jorgensd/<br>dolfinx-tutorial](https://github.com/jorgensd/dolfinx-tutorial)<br><sub>Jupyter Notebook</sub><br><sub>CC-BY-4.0 content, MIT in some files</sub> | Tutorial book on solving PDEs with FEniCSx, including elasticity and hyperelasticity. |  |
| [Kevin-Mattheus-<br>Moerman/<br>NonlinearContinuum<br>Mechanics](https://github.com/Kevin-Mattheus-Moerman/NonlinearContinuumMechanics)<br><sub>Jupyter Notebook</sub><br><sub>MIT</sub> | Notebooks deriving stresses in Ogden hyperelasticity. |  |
| [ltt1598/<br>GAMES_Xi-an_<br>forward_physics](https://github.com/ltt1598/GAMES_Xi-an_forward_physics)<br><sub>Python</sub><br><sub>none found</sub> | Notes and Taichi sample code from a physically based simulation course. |  |
| [matthias-research/<br>pages](https://github.com/matthias-research/pages/tree/master/tenMinutePhysics)<br><sub>JavaScript</sub><br><sub>MIT (stated in source)</sub> | Ten Minute Physics tutorials on soft bodies, cloth, collisions and other simulation methods. |  |
| [mitmath/<br>18335](https://github.com/mitmath/18335)<br><sub>Jupyter Notebook</sub><br><sub>none found</sub> | MIT course notes on numerical linear algebra, stability and iterative methods. |  |
| [phys-sim-book/<br>solid-sim-tutorial](https://github.com/phys-sim-book/solid-sim-tutorial)<br><sub>Python</sub><br><sub>Apache-2.0</sub> | Readable examples of optimization-based solid simulation. |  |

</details>

<details>
<summary><a id="element-definitions-and-form-languages"></a><h3>18.2 Element definitions and form languages</h3></summary>
<p id="open-courses-references-and-agents-for-mechanics--element-definitions-and-form-languages"><sub>Courses, references and agents for mechanics › <b>18.2 Element definitions and form languages</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [DefElement/<br>DefElement](https://github.com/DefElement/DefElement)<br><sub>Python</sub><br><sub>MIT code, CC-BY-4.0 content</sub> | Source of DefElement, an encyclopedia of finite element definitions. |  |
| [FEniCS/<br>basix](https://github.com/FEniCS/basix)<br><sub>C++</sub><br><sub>MIT</sub> | Runtime tabulation of finite element basis functions, quadrature and mappings. |  |
| [FEniCS/<br>ufl](https://github.com/FEniCS/ufl)<br><sub>Python</sub><br><sub>LGPL-3.0-or-later</sub> | Language for writing variational forms in notation close to the mathematics. |  |
| [firedrakeproject/<br>fiat](https://github.com/firedrakeproject/fiat)<br><sub>Python</sub><br><sub>LGPL-3.0-or-later</sub> | Tabulation of arbitrary-order finite elements and quadrature rules. |  |
| [mscroggs/<br>symfem](https://github.com/mscroggs/symfem)<br><sub>Python</sub><br><sub>MIT</sub> | Symbolic definitions of finite elements and their basis functions. |  |

</details>

<details>
<summary><a id="reproducible-research-software"></a><h3>18.3 Reproducible research software</h3></summary>
<p id="open-courses-references-and-agents-for-mechanics--reproducible-research-software"><sub>Courses, references and agents for mechanics › <b>18.3 Reproducible research software</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [betterscientificsoftware/<br>bssw.io](https://github.com/betterscientificsoftware/bssw.io)<br><sub>MIT</sub> | Articles on testing, sustaining and improving scientific software. |  |
| [the-turing-way/<br>the-turing-way](https://github.com/the-turing-way/the-turing-way)<br><sub>MIT code, CC-BY-4.0 content</sub> | Handbook on reproducible, ethical and collaborative research. |  |

</details>

<details>
<summary><a id="curated-lists"></a><h3>18.4 Curated lists</h3></summary>
<p id="open-courses-references-and-agents-for-mechanics--curated-lists"><sub>Courses, references and agents for mechanics › <b>18.4 Curated lists</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [kimimgo/<br>awesome-ai-cae](https://github.com/kimimgo/awesome-ai-cae)<br><sub>CC0-1.0</sub> | Curated list of engineering simulation tools that software agents can drive. |  |
| [modenaxe/<br>awesome-<br>biomechanics](https://github.com/modenaxe/awesome-biomechanics)<br><sub>CC0-1.0 (stated in README)</sub> | Curated resources for biomechanics and human motion analysis. |  |
| [nschloe/<br>awesome-<br>scientific-<br>computing](https://github.com/nschloe/awesome-scientific-computing)<br><sub>CC0-1.0</sub> | Curated list of scientific computing tools, including finite element and meshing software. |  |
| [thunil/<br>Physics-Based-<br>Deep-Learning](https://github.com/thunil/Physics-Based-Deep-Learning)<br><sub>none found</sub> | Curated list of research on physics-based deep learning. |  |
| [tkoyama010/<br>awesome-finite-<br>elements](https://github.com/tkoyama010/awesome-finite-elements)<br><sub>CC0-1.0</sub> | Curated list of finite element software. |  |

</details>

<details>
<summary><a id="agents-for-mechanics"></a><h3>18.5 Agents for mechanics</h3></summary>
<p id="open-courses-references-and-agents-for-mechanics--agents-for-mechanics"><sub>Courses, references and agents for mechanics › <b>18.5 Agents for mechanics</b> · <a href="#contents">Back to contents</a></sub></p>

| Name, language and license | Description | Note |
| --- | --- | --- |
| [Farhad-Davaripour/<br>FEA_Assisted_Agent](https://github.com/Farhad-Davaripour/FEA_Assisted_Agent)<br><sub>Python</sub><br><sub>MIT</sub> | Language model agent that automates Abaqus simulations. | Requires Abaqus and OpenAI models. |
| [lamm-mit/<br>MechAgents](https://github.com/lamm-mit/MechAgents)<br><sub>Jupyter Notebook</sub><br><sub>Apache-2.0</sub> | Multi-agent language model workflows for solving mechanics problems numerically. |  |
| [LuoXueling/<br>MechFoundry](https://github.com/LuoXueling/MechFoundry)<br><sub>Python</sub><br><sub>Apache-2.0, with non-commercial dependencies</sub> | Agent-driven shape generation, meshing and finite element analysis. | README says some dependencies are restricted to non-commercial use. |

</details>

</details>

## Contributing

Corrections and additions are welcome. See [contributing.md](contributing.md).

## Acknowledgements

Thanks to the authors and maintainers of the listed projects, and to those of the [curated lists](#user-content-open-courses-references-and-agents-for-mechanics--curated-lists) that helped shape this collection. Descriptions and guides were drafted with the help of AI.
