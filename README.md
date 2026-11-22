# Awesome Computational Mechanics

A collection of public repositories for computational mechanics: solid and structural mechanics, soft bodies, biomechanics, particle methods, and machine learning applied to them.

It has 360 entries covering 358 repositories. The list started from the maintainer's GitHub stars and grew through searches for related work and an editorial selection of major projects. Another 6 archived or unmaintained ones are in [archive.md](archive.md).

> **Before you rely on this list:** it is not complete. Descriptions were drafted with AI from README excerpts, file listings and repository metadata. The code was not run or validated, and a listing is not an endorsement. License labels are a convenience, not legal advice. "None found" means no license was found in the places checked, so do not assume you may reuse that code. Public does not always mean open source.

## Contents

- [Finite and boundary element methods](#user-content-open-finite-and-boundary-element-methods) (77)
  - [General-purpose frameworks](#user-content-open-finite-and-boundary-element-methods--general-purpose-frameworks) (20) · [Structural and solid mechanics solvers](#user-content-open-finite-and-boundary-element-methods--structural-and-solid-mechanics-solvers) (16) · [Differentiable and GPU finite elements](#user-content-open-finite-and-boundary-element-methods--differentiable-and-gpu-finite-elements) (7) · [Phase-field fracture](#user-content-open-finite-and-boundary-element-methods--phase-field-fracture) (6) · [Fracture, boundary and scaled boundary methods](#user-content-open-finite-and-boundary-element-methods--fracture-boundary-and-scaled-boundary-methods) (5) · [Unfitted and embedded methods](#user-content-open-finite-and-boundary-element-methods--unfitted-and-embedded-methods) (1) · [Smoothed finite elements](#user-content-open-finite-and-boundary-element-methods--smoothed-finite-elements) (1) · [Beams, rods and shells](#user-content-open-finite-and-boundary-element-methods--beams-rods-and-shells) (3) · [Solver interfaces and utilities](#user-content-open-finite-and-boundary-element-methods--solver-interfaces-and-utilities) (5) · [Teaching and compact codes](#user-content-open-finite-and-boundary-element-methods--teaching-and-compact-codes) (13)
- [Finite volume methods](#user-content-open-finite-volume-methods) (1)
  - [Solid mechanics and fluid-solid interaction](#user-content-open-finite-volume-methods--solid-mechanics-and-fluid-solid-interaction) (1)
- [Virtual element method](#user-content-open-virtual-element-method) (30)
  - [VEM libraries](#user-content-open-virtual-element-method--vem-libraries) (6) · [Elasticity](#user-content-open-virtual-element-method--elasticity) (9) · [Dynamics and fracture](#user-content-open-virtual-element-method--dynamics-and-fracture) (3) · [Coupled fields and electronic packaging](#user-content-open-virtual-element-method--coupled-fields-and-electronic-packaging) (4) · [Topology optimization with VEM](#user-content-open-virtual-element-method--topology-optimization-with-vem) (2) · [Introductory VEM codes](#user-content-open-virtual-element-method--introductory-vem-codes) (6)
- [Contact mechanics](#user-content-open-contact-mechanics) (9)
  - [Contact formulations](#user-content-open-contact-mechanics--contact-formulations) (4) · [Incremental potential contact](#user-content-open-contact-mechanics--incremental-potential-contact) (5)
- [Third medium contact](#user-content-open-third-medium-contact) (13)
  - [Modules and examples in FEM libraries](#user-content-open-third-medium-contact--modules-and-examples-in-fem-libraries) (7) · [Optimization and metamaterials](#user-content-open-third-medium-contact--optimization-and-metamaterials) (4) · [Standalone study codes](#user-content-open-third-medium-contact--standalone-study-codes) (2)
- [Meshfree and particle methods](#user-content-open-meshfree-and-particle-methods) (28)
  - [Material point method](#user-content-open-meshfree-and-particle-methods--material-point-method) (11) · [Smoothed particle hydrodynamics](#user-content-open-meshfree-and-particle-methods--smoothed-particle-hydrodynamics) (4) · [Meshless methods](#user-content-open-meshfree-and-particle-methods--meshless-methods) (5) · [Peridynamics](#user-content-open-meshfree-and-particle-methods--peridynamics) (3) · [Discrete and coarse-grained particle models](#user-content-open-meshfree-and-particle-methods--discrete-and-coarse-grained-particle-models) (5)
- [Soft-body, real-time and differentiable simulation](#user-content-open-soft-body-real-time-and-differentiable-simulation) (26)
  - [Real-time finite elements](#user-content-open-soft-body-real-time-and-differentiable-simulation--real-time-finite-elements) (7) · [Soft robotics](#user-content-open-soft-body-real-time-and-differentiable-simulation--soft-robotics) (6) · [Position-based and implicit dynamics](#user-content-open-soft-body-real-time-and-differentiable-simulation--position-based-and-implicit-dynamics) (4) · [Differentiable simulation](#user-content-open-soft-body-real-time-and-differentiable-simulation--differentiable-simulation) (6) · [Manipulation benchmarks](#user-content-open-soft-body-real-time-and-differentiable-simulation--manipulation-benchmarks) (3)
- [Multibody dynamics and biomechanics](#user-content-open-multibody-dynamics-and-biomechanics) (10)
  - [Physics engines for multibody systems](#user-content-open-multibody-dynamics-and-biomechanics--physics-engines-for-multibody-systems) (6) · [Musculoskeletal biomechanics](#user-content-open-multibody-dynamics-and-biomechanics--musculoskeletal-biomechanics) (2) · [Cardiovascular mechanics](#user-content-open-multibody-dynamics-and-biomechanics--cardiovascular-mechanics) (2)
- [Constitutive modeling and material identification](#user-content-open-constitutive-modeling-and-material-identification) (38)
  - [Neural network constitutive models](#user-content-open-constitutive-modeling-and-material-identification--neural-network-constitutive-models) (15) · [Unsupervised model discovery](#user-content-open-constitutive-modeling-and-material-identification--unsupervised-model-discovery) (7) · [Material subroutines and libraries](#user-content-open-constitutive-modeling-and-material-identification--material-subroutines-and-libraries) (10) · [Experimental parameter identification](#user-content-open-constitutive-modeling-and-material-identification--experimental-parameter-identification) (6)
- [Multiscale and homogenization](#user-content-open-multiscale-and-homogenization) (12)
  - [FFT-based homogenization](#user-content-open-multiscale-and-homogenization--fft-based-homogenization) (3) · [FE² and computational homogenization](#user-content-open-multiscale-and-homogenization--fe2-and-computational-homogenization) (3) · [Inverse homogenization](#user-content-open-multiscale-and-homogenization--inverse-homogenization) (1) · [Crystal plasticity](#user-content-open-multiscale-and-homogenization--crystal-plasticity) (5)
- [Thermal, multiphysics and additive manufacturing](#user-content-open-thermal-multiphysics-and-additive-manufacturing) (11)
  - [Heat transfer and bio-heat](#user-content-open-thermal-multiphysics-and-additive-manufacturing--heat-transfer-and-bio-heat) (5) · [Thermoelasticity](#user-content-open-thermal-multiphysics-and-additive-manufacturing--thermoelasticity) (1) · [Additive manufacturing](#user-content-open-thermal-multiphysics-and-additive-manufacturing--additive-manufacturing) (3) · [Multiphysics coupling](#user-content-open-thermal-multiphysics-and-additive-manufacturing--multiphysics-coupling) (2)
- [Optimization and inverse problems](#user-content-open-optimization-and-inverse-problems) (18)
  - [Topology optimization solvers](#user-content-open-optimization-and-inverse-problems--topology-optimization-solvers) (9) · [Learning-based topology optimization](#user-content-open-optimization-and-inverse-problems--learning-based-topology-optimization) (5) · [Inverse problems](#user-content-open-optimization-and-inverse-problems--inverse-problems) (4)
- [Physics-informed learning and energy methods](#user-content-open-physics-informed-learning-and-energy-methods) (14)
  - [Deep energy methods](#user-content-open-physics-informed-learning-and-energy-methods--deep-energy-methods) (8) · [Residual-based networks](#user-content-open-physics-informed-learning-and-energy-methods--residual-based-networks) (4) · [PINN libraries and examples](#user-content-open-physics-informed-learning-and-energy-methods--pinn-libraries-and-examples) (2)
- [Surrogates and reduced-order models](#user-content-open-surrogates-and-reduced-order-models) (34)
  - [Stress-field prediction](#user-content-open-surrogates-and-reduced-order-models--stress-field-prediction) (7) · [Deformation and reduced dynamics](#user-content-open-surrogates-and-reduced-order-models--deformation-and-reduced-dynamics) (7) · [Projection-based model reduction](#user-content-open-surrogates-and-reduced-order-models--projection-based-model-reduction) (4) · [Graph neural networks](#user-content-open-surrogates-and-reduced-order-models--graph-neural-networks) (4) · [Biomechanical surrogates](#user-content-open-surrogates-and-reduced-order-models--biomechanical-surrogates) (2) · [Response histories and operator learning](#user-content-open-surrogates-and-reduced-order-models--response-histories-and-operator-learning) (6) · [Frameworks and introductory studies](#user-content-open-surrogates-and-reduced-order-models--frameworks-and-introductory-studies) (3) · [Benchmark datasets](#user-content-open-surrogates-and-reduced-order-models--benchmark-datasets) (1)
- [Meshing, pre- and post-processing](#user-content-open-meshing-pre--and-post-processing) (23)
  - [Mesh generation](#user-content-open-meshing-pre--and-post-processing--mesh-generation) (13) · [Mesh processing and formats](#user-content-open-meshing-pre--and-post-processing--mesh-processing-and-formats) (5) · [Visualization and export](#user-content-open-meshing-pre--and-post-processing--visualization-and-export) (5)
- [Courses, references and agents for mechanics](#user-content-open-courses-references-and-agents-for-mechanics) (16)
  - [Courses and tutorials](#user-content-open-courses-references-and-agents-for-mechanics--courses-and-tutorials) (8) · [Curated lists](#user-content-open-courses-references-and-agents-for-mechanics--curated-lists) (5) · [Agents for mechanics](#user-content-open-courses-references-and-agents-for-mechanics--agents-for-mechanics) (3)
- [Contributing](#contributing)

<details>
<summary><h2>Finite and boundary element methods</h2></summary>
<p id="open-finite-and-boundary-element-methods"><sub><b>Finite and boundary element methods</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><h3>General-purpose frameworks</h3></summary>
<p id="open-finite-and-boundary-element-methods--general-purpose-frameworks"><sub>Finite and boundary element methods › <b>General-purpose frameworks</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [dealii/<br>dealii](https://github.com/dealii/dealii) | Library for solving PDEs with adaptive finite elements. | C++ | Apache-2.0 with LLVM exception, or LGPL-2.1-or-later |  |
| [ElmerCSC/<br>elmerfem](https://github.com/ElmerCSC/elmerfem) | Multiphysics finite element suite that includes structural mechanics. | Fortran | GPL-2.0 and LGPL-2.1, by component |  |
| [FEniCS/<br>dolfinx](https://github.com/FEniCS/dolfinx) | Computational environment of FEniCSx for solving PDEs with finite elements in C++ and Python. | C++ | LGPL-3.0 |  |
| [Ferrite-FEM/<br>Ferrite.jl](https://github.com/Ferrite-FEM/Ferrite.jl) | Finite element toolbox for Julia. | Julia | MIT |  |
| [firedrakeproject/<br>firedrake](https://github.com/firedrakeproject/firedrake) | Automated system for solving PDEs with the finite element method. | Python | LGPL-3.0-or-later |  |
| [FreeFem/<br>FreeFem-sources](https://github.com/FreeFem/FreeFem-sources) | Finite element solver for nonlinear multiphysics PDEs in 2D and 3D. | C++ | LGPL-3.0 |  |
| [gridap/<br>Gridap.jl](https://github.com/gridap/Gridap.jl) | Tools for grid-based approximation of linear and nonlinear PDEs. | Julia | MIT |  |
| [idaholab/<br>moose](https://github.com/idaholab/moose) | Finite element and finite volume framework for multiphysics simulation. | C++ | LGPL-2.1 |  |
| [kinnala/<br>scikit-fem](https://github.com/kinnala/scikit-fem) | Lightweight library for finite element assembly. | Python | BSD-3-Clause |  |
| [KratosMultiphysics/<br>Kratos](https://github.com/KratosMultiphysics/Kratos) | Framework for parallel multidisciplinary simulation software. | C++ | BSD-4-Clause (core) | Each application has its own license. |
| [libMesh/<br>libmesh](https://github.com/libMesh/libmesh) | Library for parallel adaptive finite element simulations. | C++ | LGPL-2.1 |  |
| [lyc102/<br>ifem](https://github.com/lyc102/ifem) | Adaptive finite element package for 2D and 3D simplicial grids. | MATLAB | GPL-3.0 | Written for MATLAB, Octave support not documented. |
| [mfem/<br>mfem](https://github.com/mfem/mfem) | Modular parallel library for scalable finite element methods. | C++ | BSD-3-Clause |  |
| [NGSolve/<br>ngsolve](https://github.com/NGSolve/ngsolve) | Multiphysics finite element software with a Python interface. | C++ | LGPL-2.1 |  |
| [polyfem/<br>polyfem](https://github.com/polyfem/polyfem) | General-purpose C++ finite element library. | C++ | MIT |  |
| [sandialabs/<br>Albany](https://github.com/sandialabs/Albany) | Implicit unstructured-grid finite element code for multiphysics problems. | C++ | BSD-3-Clause | Solid mechanics capabilities have moved to [Albany-LCM](https://github.com/sandialabs/LCM). |
| [sfepy/<br>sfepy](https://github.com/sfepy/sfepy) | Finite element solver and library for coupled PDEs in 1D, 2D and 3D. | Python | BSD-3-Clause |  |
| [Terenceyuyue/<br>varFEM](https://github.com/Terenceyuyue/varFEM) | Finite element programming in a variational-form style. | MATLAB | GPL-3.0 | Written for MATLAB, Octave support not documented. |
| [TLCFEM/<br>suanPan](https://github.com/TLCFEM/suanPan) | Parallel and heterogeneous finite element analysis framework. | C++ | GPL-3.0-or-later |  |
| [weihuayi/<br>fealpy](https://github.com/weihuayi/fealpy) | Python finite element library for algorithm research and computer-aided engineering. | Python | GPL-3.0-or-later with added notice | License notice also restricts commercial use. |

</details>

<details>
<summary><h3>Structural and solid mechanics solvers</h3></summary>
<p id="open-finite-and-boundary-element-methods--structural-and-solid-mechanics-solvers"><sub>Finite and boundary element methods › <b>Structural and solid mechanics solvers</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [code_aster](https://gitlab.com/codeaster/src) | Source of code_aster, a finite element solver for structural mechanics. | Python, C++ and Fortran | GPL-3.0 | Some validation and material data are not freely distributed. |
| [Dhondtguido/<br>CalculiX](https://github.com/Dhondtguido/CalculiX) | Three-dimensional structural finite element program. | Fortran | GPL-2.0 |  |
| [dmitryikh/<br>nla3d](https://github.com/dmitryikh/nla3d) | C++ framework for writing nonlinear finite element codes in solid mechanics. | C++ | MIT |  |
| [febiosoftware/<br>FEBio](https://github.com/febiosoftware/FEBio) | Nonlinear finite element solver designed for biomechanics. | C++ | MIT |  |
| [FrontISTR/<br>FrontISTR](https://github.com/FrontISTR/FrontISTR) | Large-scale parallel nonlinear structural analysis with contact and heat conduction. | Fortran and C | MIT | GitHub repository is a mirror; development is on GitLab. |
| [isaar/<br>MSolve](https://github.com/isaar/MSolve) | C# solver for computational mechanics problems. | C# | Apache-2.0 |  |
| [JWock82/<br>Pynite](https://github.com/JWock82/Pynite) | 3D structural analysis library with static, P-Delta, modal and pushover analysis. | Python | MIT |  |
| [llnl/<br>smith](https://github.com/llnl/smith) | 3D implicit nonlinear thermal-structural code built on MFEM. | C++ | BSD-3-Clause | README calls it a pre-alpha release. |
| [MystranSolver/<br>MYSTRANSolver](https://github.com/MystranSolver/MYSTRANSolver) | General-purpose structural finite element analysis solver. | Fortran | MIT |  |
| [nasa/<br>NASTRAN-95](https://github.com/nasa/NASTRAN-95) | NASA's historical structural analysis system for static, dynamic and stability problems. | Fortran | NASA Open Source Agreement 1.3 | No technical support. |
| [oofem/<br>oofem](https://github.com/oofem/oofem) | Object-oriented finite element code for mechanical, transport and fluid problems. | C++ | LGPL-2.1 |  |
| [OpenCourant/<br>OpenCourant](https://github.com/OpenCourant/OpenCourant) | Explicit finite element solver for crash, impact and other dynamic events. | Fortran | AGPL-3.0 | Community fork created after OpenRadioss was withdrawn in October 2026; not affiliated with Siemens or Altair. |
| [OpenSees/<br>OpenSees](https://github.com/OpenSees/OpenSees) | Framework for structural and geotechnical earthquake engineering simulation. | C++ | custom, with commercial restrictions | Commercial distribution requires permission from the University of California. |
| [peer-open-source/<br>xara](https://github.com/peer-open-source/xara) | Python package for nonlinear finite element analysis built on OpenSees. | C++ | BSD-2-Clause, with restricted OpenSees code | Bundled OpenSees files prohibit commercial use without permission from the University of California. |
| [sandialabs/<br>Norma.jl](https://github.com/sandialabs/Norma.jl) | Julia prototype for coupling and multiphysics algorithms in solid mechanics. | Julia | BSD-3-Clause | Research prototype. |
| [sanjayg0/<br>feappv](https://github.com/sanjayg0/feappv) | Free personal version of the FEAP finite element program. | Fortran | BSD-3-Clause | Lacks some FEAP features, including contact and parallel solving. |

</details>

<details>
<summary><h3>Differentiable and GPU finite elements</h3></summary>
<p id="open-finite-and-boundary-element-methods--differentiable-and-gpu-finite-elements"><sub>Finite and boundary element methods › <b>Differentiable and GPU finite elements</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [camlab-ethz/<br>TensorMesh](https://github.com/camlab-ethz/TensorMesh) | Differentiable finite element library built on PyTorch. | Python | Apache-2.0 |  |
| [deepmodeling/<br>jax-fem](https://github.com/deepmodeling/jax-fem) | Differentiable finite element package built on JAX. | Python | GPL-3.0 |  |
| [kailaix/<br>AdFem.jl](https://github.com/kailaix/AdFem.jl) | Differentiable finite element operators for inverse modeling. | Julia and C++ | MIT |  |
| [liangbright/<br>pytorch_fea_paper](https://github.com/liangbright/pytorch_fea_paper) | Differentiable finite element analysis applied to human aorta biomechanics. | Python | none found | Paper code; the author's refactored successor is [pytorch_fea](https://github.com/liangbright/pytorch_fea). |
| [mo-hanxuan/<br>FEMcy](https://github.com/mo-hanxuan/FEMcy) | Taichi-based parallel structural finite element solver with small and large deformation. | Python | MIT |  |
| [sandialabs/<br>optimism](https://github.com/sandialabs/optimism) | JAX finite element library that poses nonlinear solid mechanics as optimization. | Python | MIT |  |
| [zclsjtu/<br>DiffSolid](https://github.com/zclsjtu/DiffSolid) | Differentiable JAX finite element framework for solid mechanics and phase-field fracture. | Python | proprietary | The implementation is not open source; the repository has examples and documentation, and wheels are provided on request. |

</details>

<details>
<summary><h3>Phase-field fracture</h3></summary>
<p id="open-finite-and-boundary-element-methods--phase-field-fracture"><sub>Finite and boundary element methods › <b>Phase-field fracture</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [CastillonMiguel/<br>phasefieldx](https://github.com/CastillonMiguel/phasefieldx) | Phase-field simulation framework built on FEniCSx. | Python | MIT |  |
| [ehsanhaghighat/<br>PhaseField-DSD](https://github.com/ehsanhaghighat/PhaseField-DSD) | Phase-field shear fracture using a deviatoric stress split. | Java | MIT | Requires COMSOL. |
| [hugary1995/<br>raccoon](https://github.com/hugary1995/raccoon) | Massively parallel phase-field fracture code built on MOOSE. | C++ | LGPL-2.1 |  |
| [hyoungsuksuh/<br>micropolar_phasefield](https://github.com/hyoungsuksuh/micropolar_phasefield) | Phase-field cohesive fracture in micropolar continua with FEniCS. | Python | CC-BY-4.0 |  |
| [LuoXueling/<br>deal.II-phase-field-fracture](https://github.com/LuoXueling/deal.II-phase-field-fracture) | Phase-field fracture in deal.II with multiphysics interfaces, adaptive meshes and MPI. | C++ | MIT | Mesh input uses Abaqus input files. |
| [nsundar/<br>PFM_UMAT_ElastoPlastic](https://github.com/nsundar/PFM_UMAT_ElastoPlastic) | Phase-field damage in elastoplastic solids as a UMAT. | Fortran | MIT | Requires Abaqus. |

</details>

<details>
<summary><h3>Fracture, boundary and scaled boundary methods</h3></summary>
<p id="open-finite-and-boundary-element-methods--fracture-boundary-and-scaled-boundary-methods"><sub>Finite and boundary element methods › <b>Fracture, boundary and scaled boundary methods</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [ChongminSong/<br>Platypus](https://github.com/ChongminSong/Platypus) | Code accompanying a textbook on the scaled boundary finite element method. | MATLAB | none found | Written for MATLAB, Octave support not documented. |
| [nsundar/<br>cp-sbfem](https://github.com/nsundar/cp-sbfem) | Scaled boundary finite elements for crystal plasticity as an Abaqus UELMAT. | Fortran and Julia | MIT | Requires Abaqus. |
| [Qinxiaoye/<br>SBFEM2D](https://github.com/Qinxiaoye/SBFEM2D) | Scaled boundary finite element method for 2D linear elasticity. | MATLAB | none found | Written for MATLAB, Octave support not documented; modified from code by Chongmin Song; some files are copyright Terence Yu, with no license in this repository. |
| [ShelvanLee/<br>XFEM](https://github.com/ShelvanLee/XFEM) | Extended finite element program for multiple crack propagation in 2D linear elastic solids. | MATLAB | MIT | Written for MATLAB, Octave support not documented. |
| [Timmmdavis/<br>CutAndDisplace](https://github.com/Timmmdavis/CutAndDisplace) | Boundary element code for faults and deformation. | MATLAB | GPL-3.0 | Runs in MATLAB, also tested in Octave with some issues; README restricts use to academia, although the license is GPL-3.0. |

</details>

<details>
<summary><h3>Unfitted and embedded methods</h3></summary>
<p id="open-finite-and-boundary-element-methods--unfitted-and-embedded-methods"><sub>Finite and boundary element methods › <b>Unfitted and embedded methods</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [gridap/<br>GridapEmbedded.jl](https://github.com/gridap/GridapEmbedded.jl) | Embedded finite element methods, level sets and constructive solid geometry. | Julia | MIT |  |

</details>

<details>
<summary><h3>Smoothed finite elements</h3></summary>
<p id="open-finite-and-boundary-element-methods--smoothed-finite-elements"><sub>Finite and boundary element methods › <b>Smoothed finite elements</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [nsundar/<br>SFEM_in_Abaqus](https://github.com/nsundar/SFEM_in_Abaqus) | Strain smoothing finite elements implemented in Abaqus. | Fortran and MATLAB | GPL-3.0 | Requires Abaqus; includes MATLAB scripts. |

</details>

<details>
<summary><h3>Beams, rods and shells</h3></summary>
<p id="open-finite-and-boundary-element-methods--beams-rods-and-shells"><sub>Finite and boundary element methods › <b>Beams, rods and shells</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [precice/<br>fem-shell](https://github.com/precice/fem-shell) | Flat shell finite element solver for coupled fluid-structure simulation. | C++ | LGPL-3.0 |  |
| [sofa-framework/<br>BeamAdapter](https://github.com/sofa-framework/BeamAdapter) | Adaptive Kirchhoff rod elements for catheters, guidewires and other flexible structures. | C++ | LGPL-2.1 | Requires SOFA. |
| [SofaDefrost/<br>Cosserat](https://github.com/SofaDefrost/Cosserat) | Cosserat beam models of rods, wires and needles. | C++ and Python | LGPL-3.0 | Requires SOFA; source headers state LGPL-2.1-or-later. |

</details>

<details>
<summary><h3>Solver interfaces and utilities</h3></summary>
<p id="open-finite-and-boundary-element-methods--solver-interfaces-and-utilities"><sub>Finite and boundary element methods › <b>Solver interfaces and utilities</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [ansys/<br>pymapdl](https://github.com/ansys/pymapdl) | Python interface to the Ansys MAPDL solver. | Python | MIT | Requires a licensed copy of Ansys. |
| [ansys/<br>pymechanical](https://github.com/ansys/pymechanical) | Python interface to Ansys Mechanical. | Python | MIT | Requires a licensed copy of Ansys Mechanical. |
| [cristobaltapia/<br>pybaqus](https://github.com/cristobaltapia/pybaqus) | Import and post-processing of Abaqus ASCII result files without an Abaqus license. | Python | MIT | README says it is at a very early stage. |
| [febiosoftware/<br>pyfebio](https://github.com/febiosoftware/pyfebio) | Python package for writing FEBio input and converting its results. | Python | MIT |  |
| [lcharleux/<br>abapy](https://github.com/lcharleux/abapy) | Finite element pre- and post-processing in Python. | Python | GPL-2.0 | No README. |

</details>

<details>
<summary><h3>Teaching and compact codes</h3></summary>
<p id="open-finite-and-boundary-element-methods--teaching-and-compact-codes"><sub>Finite and boundary element methods › <b>Teaching and compact codes</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [abuganza/<br>NonlinearFEA](https://github.com/abuganza/NonlinearFEA) | Course notebooks on nonlinear finite element analysis. | Jupyter Notebook | GPL-3.0 |  |
| [AppliedMechanics-EAFIT/<br>Introductory-Finite-Elements](https://github.com/AppliedMechanics-EAFIT/Introductory-Finite-Elements) | Teaching notebooks for an introductory finite element course. | Jupyter Notebook | MIT code, CC-BY-4.0 content (stated in README) |  |
| [AppliedMechanics-EAFIT/<br>SolidsPy](https://github.com/AppliedMechanics-EAFIT/SolidsPy) | Simple finite element code for 2D elasticity. | Python | MIT |  |
| [dilevin/<br>CSC417-a3-finite-elements-3d](https://github.com/dilevin/CSC417-a3-finite-elements-3d) | Course assignment on 3D finite element simulation of elastic objects. | C++ | none found | Starter code for an assignment. |
| [hplgit/<br>fem-book](https://github.com/hplgit/fem-book) | Sources and examples for a book on numerical methods for variational problems. | Python | MIT |  |
| [hplgit/<br>fenics-tutorial](https://github.com/hplgit/fenics-tutorial) | Sources and example programs for the FEniCS Tutorial book. | TeX | none found |  |
| [jjcremmers/<br>PyFEM](https://github.com/jjcremmers/PyFEM) | Educational and research finite element code for nonlinear solid mechanics. | Python | MIT |  |
| [largurajr/<br>FEA-Protus](https://github.com/largurajr/FEA-Protus) | Teaching code for 2D plane stress and plane strain finite element analysis. | Python | none found | Python 2.7. |
| [Qinxiaoye/<br>FEM2D](https://github.com/Qinxiaoye/FEM2D) | MATLAB code for 2D finite element analysis. | MATLAB | none found | Written for MATLAB, Octave support not documented; input scripts use Ansys or Abaqus. |
| [Qinxiaoye/<br>FEM2D_dynamic](https://github.com/Qinxiaoye/FEM2D_dynamic) | Finite element elastodynamics with Newmark time integration. | MATLAB | none found | Written for MATLAB, Octave support not documented; input scripts use Ansys or Abaqus. |
| [Qinxiaoye/<br>FEM3D-C3D8-](https://github.com/Qinxiaoye/FEM3D-C3D8-) | MATLAB finite element code with 3D hexahedral element routines. | MATLAB | none found | Written for MATLAB, Octave support not documented; README calls it 2D; input scripts use Ansys or Abaqus. |
| [Qinxiaoye/<br>xpfem](https://github.com/Qinxiaoye/xpfem) | Linear elastic finite element package with quadrilateral, hexahedral and B-bar elements. | Python | none found |  |
| [tjfulle/<br>fem-with-python](https://github.com/tjfulle/fem-with-python) | Course notes, assignments and code for an introductory finite element course. | Python | MIT (stated in README) |  |

</details>

</details>

<details>
<summary><h2>Finite volume methods</h2></summary>
<p id="open-finite-volume-methods"><sub><b>Finite volume methods</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><h3>Solid mechanics and fluid-solid interaction</h3></summary>
<p id="open-finite-volume-methods--solid-mechanics-and-fluid-solid-interaction"><sub>Finite volume methods › <b>Solid mechanics and fluid-solid interaction</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [solids4foam/<br>solids4foam](https://github.com/solids4foam/solids4foam) | Toolbox for solid mechanics and fluid-solid interaction in OpenFOAM. | C++ | GPL-3.0 | Requires OpenFOAM. |

</details>

</details>

<details>
<summary><h2>Virtual element method</h2></summary>
<p id="open-virtual-element-method"><sub><b>Virtual element method</b> · <a href="#contents">Back to contents</a></sub></p>

The virtual element method (VEM) generalizes finite elements to polygonal and polyhedral elements.

<details>
<summary><h3>VEM libraries</h3></summary>
<p id="open-virtual-element-method--vem-libraries"><sub>Virtual element method › <b>VEM libraries</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [CAMLAB-UChile/<br>vemlab](https://github.com/CAMLAB-UChile/vemlab) | MATLAB library for linear VEM in 2D elastostatics and Poisson problems. | MATLAB | GPL-3.0 | Runs in MATLAB, or in Octave with small changes described in its README. |
| [cemcen/<br>Veamy](https://github.com/cemcen/Veamy) | Object-oriented C++ library for VEM in 2D elastostatics and Poisson problems. | C++ | GPL (stated in README) |  |
| [dune-fem/<br>dune-vem](https://gitlab.dune-project.org/dune-fem/dune-vem) | DUNE module with a range of virtual element spaces and a Python interface. | C++ and Python | GPL-2.0-or-later |  |
| [SINTEF-AppliedCompSci/<br>MRST](https://github.com/SINTEF-AppliedCompSci/MRST/tree/main/solvers/vemmech) | VEM mechanics module of the MATLAB Reservoir Simulation Toolbox. | MATLAB | GPL-3.0 | Part of a larger toolbox that runs in MATLAB or Octave. |
| [Terenceyuyue/<br>mVEM](https://github.com/Terenceyuyue/mVEM) | MATLAB package of virtual element methods published in the literature. | MATLAB | GPL-3.0 | Written for MATLAB, Octave support not documented. |
| [tiagomhrd/<br>ves](https://github.com/tiagomhrd/ves) | Helper library of projectors for several virtual element formulations. | C++ | MIT |  |

</details>

<details>
<summary><h3>Elasticity</h3></summary>
<p id="open-virtual-element-method--elasticity"><sub>Virtual element method › <b>Elasticity</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [chauj96/<br>vem_implementation](https://github.com/chauj96/vem_implementation) | Mixed and hybridized VEM for 3D linear elasticity on polyhedral meshes. | MATLAB | none found | Written for MATLAB, Octave support not documented. |
| [DongxiaoLyu/<br>polymesh](https://github.com/DongxiaoLyu/polymesh) | VEM Studio Online, a browser-based polygonal mesher and VEM solver for 2D elasticity and heat conduction. | JavaScript | MIT |  |
| [Moopz99/<br>VEMK2](https://github.com/Moopz99/VEMK2) | Quadratic VEM for 2D elasticity. | MATLAB | GPL-3.0 | Written for MATLAB, Octave support not documented. |
| [mySimpleProjects/<br>SimpleVEM](https://github.com/mySimpleProjects/SimpleVEM) | Comparison of FEM and VEM for 2D structural analysis. | MATLAB | GPL-3.0 | Requires MATLAB with the Curve Fitting and Optimization toolboxes. |
| [noahherrmann/<br>Comparison-of-the-Virtual-and-Finite-Element-Method](https://github.com/noahherrmann/Comparison-of-the-Virtual-and-Finite-Element-Method) | Bachelor's thesis comparison of VEM and FEM robustness and convergence. | MATLAB | none found | Written for MATLAB, Octave support not documented; bundles SimpleVEM, iFEM and vem2D code. |
| [nsundar/<br>VEM_in_Abaqus](https://github.com/nsundar/VEM_in_Abaqus) | Implementation of the virtual element method as Abaqus subroutines. | Fortran | GPL-3.0 | Requires Abaqus. |
| [Qinxiaoye/<br>VEM_mechanics2D](https://github.com/Qinxiaoye/VEM_mechanics2D) | Teaching code for VEM in 2D linear elasticity, with a theory note. | MATLAB | none found | Written for MATLAB, Octave support not documented; some files are copyright Terence Yu and Long Chen, with no license in this repository. |
| [tytrusty/<br>Shape-Matching-Element-Method](https://github.com/tytrusty/Shape-Matching-Element-Method) | Shape-matching VEM for direct simulation of CAD models. | MATLAB and C++ | none found | Written for MATLAB, Octave support not documented; depends on gptoolbox. |
| [ZhouRuopu/<br>GNE-VEM](https://github.com/ZhouRuopu/GNE-VEM) | Graph neural network approach to VEM stabilization. | Python | none found |  |

</details>

<details>
<summary><h3>Dynamics and fracture</h3></summary>
<p id="open-virtual-element-method--dynamics-and-fracture"><sub>Virtual element method › <b>Dynamics and fracture</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [MinhNguyenIKM/<br>vem](https://github.com/MinhNguyenIKM/vem) | VEM code for 2D linear elastic fracture. | MATLAB | none found | Written for MATLAB, Octave support not documented. |
| [Qinxiaoye/<br>VEM-spcae-time-dynamic](https://github.com/Qinxiaoye/VEM-spcae-time-dynamic) | Space-time VEM for elastodynamics. | MATLAB | none found | Written for MATLAB, Octave support not documented; some files are copyright Terence Yu and Long Chen, with no license in this repository. |
| [Qinxiaoye/<br>VEMdynamic_Newmark](https://github.com/Qinxiaoye/VEMdynamic_Newmark) | VEM for 2D linear elastodynamics with Newmark time integration. | MATLAB | none found | Written for MATLAB, Octave support not documented; some files are copyright Terence Yu and Long Chen, with no license in this repository. |

</details>

<details>
<summary><h3>Coupled fields and electronic packaging</h3></summary>
<p id="open-virtual-element-method--coupled-fields-and-electronic-packaging"><sub>Virtual element method › <b>Coupled fields and electronic packaging</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [aerubianoma/<br>vem_stress_assisted_diffusion](https://github.com/aerubianoma/vem_stress_assisted_diffusion) | Robust VEM experiments for stress-assisted diffusion in elastic materials. | MATLAB | GPL-3.0 | Requires MATLAB, README lists R2023a. |
| [Qinxiaoye/<br>VEMpiezo](https://github.com/Qinxiaoye/VEMpiezo) | VEM for 2D piezoelasticity. | MATLAB | none found | Written for MATLAB, Octave support not documented; some files are copyright Terence Yu, with no license in this repository. |
| [yanpeng-gong/<br>FeVeCoupled-ElectronicPackaging](https://github.com/yanpeng-gong/FeVeCoupled-ElectronicPackaging) | Coupled finite and virtual element analysis of multiscale electronic packaging structures. | MATLAB | MIT | Requires MATLAB. |
| [yanpeng-gong/<br>VEM-electronic-packaging](https://github.com/yanpeng-gong/VEM-electronic-packaging) | Standard and stabilization-free VEM for thermomechanical analysis of electronic packaging. | MATLAB | MIT (README badge) | Requires MATLAB; no license file. |

</details>

<details>
<summary><h3>Topology optimization with VEM</h3></summary>
<p id="open-virtual-element-method--topology-optimization-with-vem"><sub>Virtual element method › <b>Topology optimization with VEM</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [Qinxiaoye/<br>TOPvem](https://github.com/Qinxiaoye/TOPvem) | Density-based topology optimization with VEM. | MATLAB | none found | Written for MATLAB, Octave support not documented; some files are copyright Terence Yu, with no license in this repository. |
| [redcican/<br>vem-concurrent-topopt](https://github.com/redcican/vem-concurrent-topopt) | Concurrent multiscale topology optimization with VEM on polygonal and polyhedral meshes. | Python | MIT |  |

</details>

<details>
<summary><h3>Introductory VEM codes</h3></summary>
<p id="open-virtual-element-method--introductory-vem-codes"><sub>Virtual element method › <b>Introductory VEM codes</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [andrea-borio/<br>vem-implementation-example](https://github.com/andrea-borio/vem-implementation-example) | Compact example of an optimized VEM implementation. | MATLAB | GPL-3.0 | Written for MATLAB, Octave support not documented; solves the Poisson equation, not elasticity. |
| [deatinor/<br>VEM3D](https://github.com/deatinor/VEM3D) | Master's project implementing the virtual element method in three dimensions. | C++ | none found | Convergence scripts use MATLAB. |
| [justachetan/<br>VirtualElementMethods](https://github.com/justachetan/VirtualElementMethods) | Python translation of the 50-line introductory VEM code. | Python | MIT | Solves the Poisson equation, not elasticity. |
| [oliversutton/<br>50LinesOfVEM](https://github.com/oliversutton/50LinesOfVEM) | Introductory 50-line MATLAB implementation of VEM. | MATLAB | MIT | Written for MATLAB, Octave support not documented; solves the Poisson equation, not elasticity. |
| [Qinxiaoye/<br>VEM_Poisson](https://github.com/Qinxiaoye/VEM_Poisson) | Introductory 2D VEM code with a theory note. | MATLAB | none found | Written for MATLAB, Octave support not documented; solves the Poisson equation, not elasticity; some files are copyright Terence Yu, with no license in this repository. |
| [Qinxiaoye/<br>VEMbook](https://github.com/Qinxiaoye/VEMbook) | VEM teaching scripts, including a 1D truss. | MATLAB | none found | Written for MATLAB, Octave support not documented; sparse documentation. |

</details>

</details>

<details>
<summary><h2>Contact mechanics</h2></summary>
<p id="open-contact-mechanics"><sub><b>Contact mechanics</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><h3>Contact formulations</h3></summary>
<p id="open-contact-mechanics--contact-formulations"><sub>Contact mechanics › <b>Contact formulations</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [adtzlr/<br>felupe-contact](https://github.com/adtzlr/felupe-contact) | Large-deformation contact formulations for FElupe. | Python | GPL-3.0-or-later | README says it is at an early stage. |
| [CMSL-HKUST/<br>FMC_contact](https://github.com/CMSL-HKUST/FMC_contact) | Differentiable volume-based contact with Fiber Monte Carlo in finite elements. | Python | GPL-3.0 |  |
| [mimesis-inria/<br>SOFA.NCP](https://github.com/mimesis-inria/SOFA.NCP) | Direct contact solving with the Fischer-Burmeister formulation. | C++ | none found | Requires SOFA; no README. |
| [Wells-Group/<br>asimov-contact](https://github.com/Wells-Group/asimov-contact) | Parallel contact between deforming bodies in FEniCSx. | C++ and Python | MIT | README says it is highly experimental. |

</details>

<details>
<summary><h3>Incremental potential contact</h3></summary>
<p id="open-contact-mechanics--incremental-potential-contact"><sub>Contact mechanics › <b>Incremental potential contact</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [ipc-sim/<br>Codim-IPC](https://github.com/ipc-sim/Codim-IPC) | Incremental potential contact for codimensional objects. | C++ | Apache-2.0 | Paper code; bundled components have their own licenses. |
| [ipc-sim/<br>IPC](https://github.com/ipc-sim/IPC) | Reference implementation of Incremental Potential Contact for large-deformation elastodynamics. | C++ | MIT |  |
| [ipc-sim/<br>ipc-toolkit](https://github.com/ipc-sim/ipc-toolkit) | Reusable functions for adding incremental potential contact to a simulation. | C++ | MIT |  |
| [ipc-sim/<br>rigid-ipc](https://github.com/ipc-sim/rigid-ipc) | Reference implementation of intersection-free rigid body dynamics. | C++ | MIT |  |
| [spiriMirror/<br>libuipc](https://github.com/spiriMirror/libuipc) | GPU library for unified incremental potential contact of rigid and deformable bodies. | C++ and CUDA | Apache-2.0 | The Blender integration includes GPL-3.0 code. |

</details>

</details>

<details>
<summary><h2>Third medium contact</h2></summary>
<p id="open-third-medium-contact"><sub><b>Third medium contact</b> · <a href="#contents">Back to contents</a></sub></p>

Third medium contact (TMC) models contact by meshing the gap with a very compliant fictitious material. Some links open the relevant file inside a larger project. DTU's MATLAB TopTMC code is not in a repository and can be downloaded from the [TopOpt software page](https://www.topopt.mek.dtu.dk/apps-and-software).

<details>
<summary><h3>Modules and examples in FEM libraries</h3></summary>
<p id="open-third-medium-contact--modules-and-examples-in-fem-libraries"><sub>Third medium contact › <b>Modules and examples in FEM libraries</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [adtzlr/<br>felupe](https://github.com/adtzlr/felupe/blob/main/examples/ex20_third-medium-contact.py) | Third medium contact example in the FElupe nonlinear finite element package. | Python | GPL-3.0 |  |
| [deepmodeling/<br>jax-fem](https://github.com/deepmodeling/jax-fem/tree/main/applications/third_medium_contact) | Third medium contact application in JAX-FEM. | Python | GPL-3.0 |  |
| [fenics-dolfiny/<br>dolfiny](https://github.com/fenics-dolfiny/dolfiny/tree/main/demo/tmc) | Third medium contact demo built on FEniCSx. | Python | LGPL-3.0 |  |
| [idaholab/<br>moose](https://github.com/idaholab/moose/blob/next/modules/solid_mechanics/doc/content/source/kernels/SecondDerivativeRegularization.md) | HuHu, LuLu and HuHu-LuLu regularization kernels for solid mechanics. | C++ | LGPL-2.1 | Regularization component, not a complete contact example. |
| [meyer-nils/<br>torch-fem](https://github.com/meyer-nils/torch-fem/blob/main/examples/basic/planar/third_medium_contact.ipynb) | Third medium contact example in a differentiable PyTorch finite element solver. | Python | MIT |  |
| [MultiSimOLab/<br>HyperFEM.jl](https://github.com/MultiSimOLab/HyperFEM.jl/blob/main/test/SimulationsTests/ThirdMediumContactSimulation.jl) | Third medium contact simulation in a hyperelastic multiphysics library. | Julia | MIT | Provided as a test, not a tutorial. |
| [Naruki-Ichihara/<br>feax](https://github.com/Naruki-Ichihara/feax/blob/main/feax/mechanics/tmc.py) | Third medium contact module in a JAX finite element engine, with 2D and 3D examples. | Python | GPL-3.0 |  |

</details>

<details>
<summary><h3>Optimization and metamaterials</h3></summary>
<p id="open-third-medium-contact--optimization-and-metamaterials"><sub>Third medium contact › <b>Optimization and metamaterials</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [charlieaveline/<br>TMC_Firedrake](https://github.com/charlieaveline/TMC_Firedrake) | Minimal unit-cell forward solve with third medium contact and multiscale virtual power. | Python | MIT |  |
| [IMTEK-Simulation/<br>muFFTTO](https://github.com/IMTEK-Simulation/muFFTTO/tree/main/examples/internal_contact) | Internal contact by third medium in an FFT-based microstructure optimization code. | Python | MIT |  |
| [LuoXueling/<br>optimization_of_digital_material_distribution](https://github.com/LuoXueling/optimization_of_digital_material_distribution/blob/main/main_semisphere_dist_opt_tmc.py) | Multimaterial distribution optimization with a third medium contact example. | Python | MIT |  |
| [stefanhiemer/<br>topoptlab](https://github.com/stefanhiemer/topoptlab/tree/main/examples/fem/third_medium_contact) | C-shape contact example in a topology optimization library. | Python | GPL-3.0 |  |

</details>

<details>
<summary><h3>Standalone study codes</h3></summary>
<p id="open-third-medium-contact--standalone-study-codes"><sub>Third medium contact › <b>Standalone study codes</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [chennachaos/<br>FEniCSx-TMC](https://github.com/chennachaos/FEniCSx-TMC) | Attempt at third medium contact in FEniCSx. | Python | GPL-3.0 | Author reports it did not work for the paper's parameters. |
| [MechEngrLorenzoFiore/<br>FEA_studies](https://github.com/MechEngrLorenzoFiore/FEA_studies/tree/main/Third_medium_contact) | Study script based on the 2024 paper by Faltus, Horak, Doskar and Rokos. | Python | MIT | Learning project. |

</details>

</details>

<details>
<summary><h2>Meshfree and particle methods</h2></summary>
<p id="open-meshfree-and-particle-methods"><sub><b>Meshfree and particle methods</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><h3>Material point method</h3></summary>
<p id="open-meshfree-and-particle-methods--material-point-method"><sub>Meshfree and particle methods › <b>Material point method</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [adevaucorbeil/<br>karamelo](https://github.com/adevaucorbeil/karamelo) | Parallel material point method simulator with CPU and GPU support. | C++ | GPL-2.0 | GPU support is on a separate branch. |
| [bcolloran/<br>tlmpm](https://github.com/bcolloran/tlmpm) | Teaching implementation of the total Lagrangian material point method in Taichi. | Python | none found |  |
| [cb-geo/<br>mpm](https://github.com/cb-geo/mpm) | High-performance material point method code for computational geomechanics. | C++ | MIT |  |
| [cb-geo/<br>mpm-benchmarks](https://github.com/cb-geo/mpm-benchmarks) | Benchmark cases for the CB-Geo material point method code. | Jupyter Notebook | CC-BY-4.0 |  |
| [penn-graphics-research/<br>ziran2019](https://github.com/penn-graphics-research/ziran2019) | Implicit material point simulation of viscoelasticity, plasticity and fracture. | C++ | MIT | Paper code. |
| [taichi-dev/<br>mpm_3d_exercise](https://github.com/taichi-dev/mpm_3d_exercise) | Exercise for writing a 3D material point method, with a 2D reference implementation. | Python | MIT | Starter code with the main step left blank. |
| [taichi-dev/<br>taichi_elements](https://github.com/taichi-dev/taichi_elements) | Multi-material MPM engine for elastic solids, water, snow and sand in Taichi. | Python | MIT | README describes it as work in progress. |
| [xzhang66/<br>MPM3D-F90](https://github.com/xzhang66/MPM3D-F90) | Simplified Fortran 90 material point code accompanying two MPM books. | Fortran | none found | Source headers carry a copyright notice without license terms. |
| [Yihao-Shi/<br>GeoTaichi](https://github.com/Yihao-Shi/GeoTaichi) | Coupled material point and discrete element simulation of geophysical problems. | Python | GPL-3.0 | Bundled components have their own licenses. |
| [yuanming-hu/<br>GPUMPM](https://github.com/yuanming-hu/GPUMPM) | GPU-optimized material point method from a SIGGRAPH Asia 2018 paper. | C++ and CUDA | GPL-3.0 | README asks commercial users to contact the authors. |
| [yuanming-hu/<br>taichi_mpm](https://github.com/yuanming-hu/taichi_mpm) | MLS-MPM solver with cutting and two-way rigid body coupling. | C++ | MIT |  |

</details>

<details>
<summary><h3>Smoothed particle hydrodynamics</h3></summary>
<p id="open-meshfree-and-particle-methods--smoothed-particle-hydrodynamics"><sub>Meshfree and particle methods › <b>Smoothed particle hydrodynamics</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [InteractiveComputerGraphics/<br>SPH-Tutorial](https://github.com/InteractiveComputerGraphics/SPH-Tutorial) | Tutorial notes and slides on SPH, including deformable solids. |  | none found | Documents only, no code. |
| [luchete80/<br>WeldForm](https://github.com/luchete80/WeldForm) | SPH solver for elastoplastic and thermally coupled metal forming. | C++ | GPL-3.0-or-later |  |
| [pypr/<br>pysph](https://github.com/pypr/pysph) | Smoothed particle hydrodynamics framework with OpenMP, OpenCL and MPI support. | Python | BSD-3-Clause | Some directories may carry other licenses. |
| [Xiangyu-Hu/<br>SPHinXsys](https://github.com/Xiangyu-Hu/SPHinXsys) | SPH-based multiphysics library for coupled simulation and optimization. | C++ | Apache-2.0 |  |

</details>

<details>
<summary><h3>Meshless methods</h3></summary>
<p id="open-meshfree-and-particle-methods--meshless-methods"><sub>Meshfree and particle methods › <b>Meshless methods</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [iwf-inspire/<br>mfree_iwf](https://github.com/iwf-inspire/mfree_iwf) | Comparison of meshless methods for large-deformation elastodynamics. | C++ | GPL-3.0 | Paper code. |
| [iwf-inspire/<br>mfree_iwf-ul-cut-refine](https://github.com/iwf-inspire/mfree_iwf-ul-cut-refine) | Updated Lagrangian meshfree metal cutting with dynamic refinement. | C++ | GPL-3.0 | Paper code. |
| [JinshuaiBai/<br>RPIM_NNS](https://github.com/JinshuaiBai/RPIM_NNS) | Radial point interpolation meshless method with neural network solvers. | MATLAB | none found | Requires MATLAB. |
| [saullocastro/<br>meshless](https://github.com/saullocastro/meshless) | Meshless methods for computational mechanics, including ES-PIM. | Python | BSD-2-Clause |  |
| [SlicerCBM/<br>SlicerCBM](https://github.com/SlicerCBM/SlicerCBM) | 3D Slicer extension for patient-specific biomechanics, with a meshless TLED (MTLED) simulator. | Python | BSD-3-Clause | Requires 3D Slicer; some external solvers are GPL. |

</details>

<details>
<summary><h3>Peridynamics</h3></summary>
<p id="open-meshfree-and-particle-methods--peridynamics"><sub>Meshfree and particle methods › <b>Peridynamics</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [kaipartmann/<br>Peridynamics.jl](https://github.com/kaipartmann/Peridynamics.jl) | Parallel peridynamics with several formulations and multibody contact. | Julia | MIT |  |
| [peridigm/<br>peridigm](https://github.com/peridigm/peridigm) | Parallel peridynamics code for solid mechanics with material failure. | C++ | BSD-3-Clause |  |
| [PeriHub/<br>PeriLab.jl](https://github.com/PeriHub/PeriLab.jl) | Peridynamics laboratory for a range of material and fracture problems. | Julia | BSD-3-Clause |  |

</details>

<details>
<summary><h3>Discrete and coarse-grained particle models</h3></summary>
<p id="open-meshfree-and-particle-methods--discrete-and-coarse-grained-particle-models"><sub>Meshfree and particle methods › <b>Discrete and coarse-grained particle models</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [idaholab/<br>LIGGGHTS-INL](https://github.com/idaholab/LIGGGHTS-INL) | Extended version of the LIGGGHTS discrete element code. | C++ | GPL-2.0 |  |
| [projectchrono/<br>DEM-Engine](https://github.com/projectchrono/DEM-Engine) | GPU discrete element solver with complex grain geometry. | C++ and CUDA | BSD-3-Clause | Requires an NVIDIA GPU. |
| [YADE](https://gitlab.com/yade-dev/trunk) | Framework for the discrete element method. | C++ and Python | GPL-2.0-or-later |  |
| [yhtang/<br>OpenRBC](https://github.com/yhtang/OpenRBC) | Coarse-grained particle simulator of red blood cells at protein resolution. | C++ | GPL-3.0 |  |
| [yuanming-hu/<br>taichi_dem_mid_autumn](https://github.com/yuanming-hu/taichi_dem_mid_autumn) | Minimal discrete element method demo in Taichi. | Python | MIT |  |

</details>

</details>

<details>
<summary><h2>Soft-body, real-time and differentiable simulation</h2></summary>
<p id="open-soft-body-real-time-and-differentiable-simulation"><sub><b>Soft-body, real-time and differentiable simulation</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><h3>Real-time finite elements</h3></summary>
<p id="open-soft-body-real-time-and-differentiable-simulation--real-time-finite-elements"><sub>Soft-body, real-time and differentiable simulation › <b>Real-time finite elements</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [InteractiveComputerGraphics/<br>FastCorotatedFEM](https://github.com/InteractiveComputerGraphics/FastCorotatedFEM) | Minimal fast corotated finite element method using operator splitting. | C++ | MIT |  |
| [jinaojakezhang/<br>DJTLED](https://github.com/jinaojakezhang/DJTLED) | Direct-Jacobian explicit dynamics finite elements for real-time hyperelastic simulation. | C++ | MIT |  |
| [ltt1598/<br>Quasi-Newton-Methods-for-Real-time-Simulation-of-Hyperelastic-Materials](https://github.com/ltt1598/Quasi-Newton-Methods-for-Real-time-Simulation-of-Hyperelastic-Materials) | Quasi-Newton methods for real-time hyperelastic simulation. | C++ | BSD-3-Clause (stated in source) | Only a Visual Studio build is provided. |
| [sofa-framework/<br>sofa](https://github.com/sofa-framework/sofa) | Interactive finite element physics framework for medical simulation and robotics. | C++ | LGPL-2.1 |  |
| [sofa-framework/<br>SofaPython3](https://github.com/sofa-framework/SofaPython3) | Python interface to the SOFA simulation framework. | C++ and Python | LGPL-2.1 | Requires SOFA; README describes it as work in progress. |
| [x9m/<br>DJTLED_fast](https://github.com/x9m/DJTLED_fast) | Speed-optimized DJ-TLED soft-tissue solver, with Jinao Zhang's original solver for comparison. | C++ | MIT | **By the list maintainer.** Derived from jinaojakezhang/DJTLED; developed and tested on macOS. |
| [x9m/<br>JANP-DJTLED-GPU](https://github.com/x9m/JANP-DJTLED-GPU) | DJTLED with average nodal pressure for nearly incompressible soft tissue, on CPU and GPU. | C++ and CUDA | MIT | **By the list maintainer.** Builds on Jinao Zhang's DJTLED; the GPU solver needs an NVIDIA GPU. |

</details>

<details>
<summary><h3>Soft robotics</h3></summary>
<p id="open-soft-body-real-time-and-differentiable-simulation--soft-robotics"><sub>Soft-body, real-time and differentiable simulation › <b>Soft robotics</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [SofaDefrost/<br>CondensedFEMModel](https://github.com/SofaDefrost/CondensedFEMModel) | Learned condensed finite element models for soft robot control and design. | Python | GPL-3.0 | Requires SOFA. |
| [SofaDefrost/<br>SofaGym](https://github.com/SofaDefrost/SofaGym) | Reinforcement learning environments built from SOFA scenes. | Python | none found | Requires SOFA; source files carry Inria and partner copyright notices. |
| [SofaDefrost/<br>SoftRobots](https://github.com/SofaDefrost/SoftRobots) | SOFA components for modeling, actuating and controlling soft robots. | C++ | LGPL-3.0 | Requires SOFA. |
| [SofaDefrost/<br>SoftRobots.DesignOptimization](https://github.com/SofaDefrost/SoftRobots.DesignOptimization) | Design optimization toolbox for soft robots. | Python | AGPL-3.0 | Requires SOFA. |
| [SofaDefrost/<br>SoftRobots.Inverse](https://github.com/SofaDefrost/SoftRobots.Inverse) | Inverse methods for soft robot control. | C++ | AGPL-3.0 with a patent clause | Requires SOFA; implements a patented Inria method. |
| [StanfordASL/<br>soft-robot-control](https://github.com/StanfordASL/soft-robot-control) | Optimal control of soft robots with reduced-order finite element models. | Python | MIT | Requires SOFA; setup uses a Gurobi license. |

</details>

<details>
<summary><h3>Position-based and implicit dynamics</h3></summary>
<p id="open-soft-body-real-time-and-differentiable-simulation--position-based-and-implicit-dynamics"><sub>Soft-body, real-time and differentiable simulation › <b>Position-based and implicit dynamics</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [InteractiveComputerGraphics/<br>PositionBasedDynamics](https://github.com/InteractiveComputerGraphics/PositionBasedDynamics) | Position-based simulation of rigid bodies, deformable solids and fluids. | C++ | MIT |  |
| [InteractiveComputerGraphics/<br>stark](https://github.com/InteractiveComputerGraphics/stark) | Strongly coupled rigid and deformable bodies with shells, rods and frictional contact. | C++ and Python | Apache-2.0 |  |
| [mattoverby/<br>admm-elastic](https://github.com/mattoverby/admm-elastic) | ADMM generalization of projective dynamics to hyperelastic models. | C++ | MIT |  |
| [Q-Minh/<br>position-based-dynamics](https://github.com/Q-Minh/position-based-dynamics) | Academic prototype of soft-body simulation with extended position-based dynamics. | C++ | BSL-1.0 |  |

</details>

<details>
<summary><h3>Differentiable simulation</h3></summary>
<p id="open-soft-body-real-time-and-differentiable-simulation--differentiable-simulation"><sub>Soft-body, real-time and differentiable simulation › <b>Differentiable simulation</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [NVlabs/<br>DiffRL](https://github.com/NVlabs/DiffRL) | Differentiable simulation and policy learning from the SHAC paper. | Python | NVIDIA Source Code License (non-commercial) | Restricted to non-commercial use. |
| [NVlabs/<br>DiSECt](https://github.com/NVlabs/DiSECt) | Differentiable finite element simulator for robotic cutting of deformable materials. | Python | NVIDIA Source Code License (non-commercial) | Code and dataset are restricted to non-commercial use. |
| [rewarped/<br>rewarped](https://github.com/rewarped/rewarped) | Reinforcement learning with parallel differentiable multiphysics simulation. | Python | Apache-2.0, with NVIDIA-restricted files | Some NVIDIA file headers forbid use without a license agreement. |
| [taichi-dev/<br>difftaichi](https://github.com/taichi-dev/difftaichi) | Examples of differentiable physical simulators written in Taichi. | Python | none found |  |
| [taichi-dev/<br>taichi](https://github.com/taichi-dev/taichi) | Parallel programming language in Python for simulation on CPUs and GPUs. | C++ | Apache-2.0 |  |
| [YilingQiao/<br>diff_fem](https://github.com/YilingQiao/diff_fem) | Differentiable simulation of soft multibody systems. | C++ | Apache-2.0 | Paper code. |

</details>

<details>
<summary><h3>Manipulation benchmarks</h3></summary>
<p id="open-soft-body-real-time-and-differentiable-simulation--manipulation-benchmarks"><sub>Soft-body, real-time and differentiable simulation › <b>Manipulation benchmarks</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [hzaskywalker/<br>PlasticineLab](https://github.com/hzaskywalker/PlasticineLab) | Differentiable physics benchmark for soft-body manipulation. | Python | none found | Only some bundled algorithm folders have license files. |
| [Xingyu-Lin/<br>softagent](https://github.com/Xingyu-Lin/softagent) | Benchmarked learning algorithms for deformable object manipulation in SoftGym. | Python | none found | Some bundled folders have their own licenses. |
| [Xingyu-Lin/<br>softgym](https://github.com/Xingyu-Lin/softgym) | Deformable object manipulation benchmarks for cloth, rope and fluid. | C++ | BSD-3-Clause, with separately licensed NVIDIA FleX | Bundles NVIDIA FleX under the NVIDIA Source Code License (1-Way Commercial); some FleX headers also forbid use without an agreement with NVIDIA. |

</details>

</details>

<details>
<summary><h2>Multibody dynamics and biomechanics</h2></summary>
<p id="open-multibody-dynamics-and-biomechanics"><sub><b>Multibody dynamics and biomechanics</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><h3>Physics engines for multibody systems</h3></summary>
<p id="open-multibody-dynamics-and-biomechanics--physics-engines-for-multibody-systems"><sub>Multibody dynamics and biomechanics › <b>Physics engines for multibody systems</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [dartsim/<br>dart](https://github.com/dartsim/dart) | Kinematics, dynamics and contact of articulated rigid and soft bodies. | C++ | BSD-2-Clause |  |
| [google-deepmind/<br>mujoco](https://github.com/google-deepmind/mujoco) | Multibody dynamics engine with contact and deformable bodies. | C++ | Apache-2.0 |  |
| [jgerstmayr/<br>EXUDYN](https://github.com/jgerstmayr/EXUDYN) | Rigid and flexible multibody dynamics. | C++ and Python | EXUDYN General License (BSD-3-Clause style) |  |
| [newton-physics/<br>newton](https://github.com/newton-physics/newton) | GPU-accelerated physics engine for robotics and simulation research. | Python | Apache-2.0 |  |
| [projectchrono/<br>chrono](https://github.com/projectchrono/chrono) | Multiphysics engine for rigid, deformable and granular system dynamics. | C++ | BSD-3-Clause |  |
| [pydy/<br>pydy](https://github.com/pydy/pydy) | Toolkit for studying multibody dynamics in Python. | Python | BSD-3-Clause |  |

</details>

<details>
<summary><h3>Musculoskeletal biomechanics</h3></summary>
<p id="open-multibody-dynamics-and-biomechanics--musculoskeletal-biomechanics"><sub>Multibody dynamics and biomechanics › <b>Musculoskeletal biomechanics</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [diku-dk/<br>libhip](https://github.com/diku-dk/libhip) | Subject-specific hip joint finite element models and the code to reproduce them. | Python | MIT |  |
| [opensim-org/<br>opensim-core](https://github.com/opensim-org/opensim-core) | Musculoskeletal modeling and dynamic simulation of movement. | C++ | Apache-2.0 |  |

</details>

<details>
<summary><h3>Cardiovascular mechanics</h3></summary>
<p id="open-multibody-dynamics-and-biomechanics--cardiovascular-mechanics"><sub>Multibody dynamics and biomechanics › <b>Cardiovascular mechanics</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [KIT-IBT/<br>CardioMechanics](https://github.com/KIT-IBT/CardioMechanics) | Finite element simulation of cardiac electromechanics. | C++ | GPL-3.0 |  |
| [SimVascular/<br>svMultiPhysics](https://github.com/SimVascular/svMultiPhysics) | Parallel finite element multiphysics solver for cardiovascular simulation. | C++ | BSD-3-Clause, with restricted bundled components | Bundled ParMETIS code is limited to non-profit, government or evaluation use; bundled TetGen is AGPL-3.0. |

</details>

</details>

<details>
<summary><h2>Constitutive modeling and material identification</h2></summary>
<p id="open-constitutive-modeling-and-material-identification"><sub><b>Constitutive modeling and material identification</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><h3>Neural network constitutive models</h3></summary>
<p id="open-constitutive-modeling-and-material-identification--neural-network-constitutive-models"><sub>Constitutive modeling and material identification › <b>Neural network constitutive models</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [abuganza/<br>NN_aniso_UMAT](https://github.com/abuganza/NN_aniso_UMAT) | Neural network models of anisotropic hyperelastic materials, with a UMAT. | Jupyter Notebook | GPL-3.0 | Requires Abaqus for the UMAT. |
| [filippo-masi/<br>Thermodynamics-Neural-Networks](https://github.com/filippo-masi/Thermodynamics-Neural-Networks) | Thermodynamics-based neural networks for inelastic constitutive modeling. | Jupyter Notebook and Python | MIT |  |
| [FuhgJan/<br>ExtremeSparsificationConstitutiveLaws](https://github.com/FuhgJan/ExtremeSparsificationConstitutiveLaws) | Sparse physics-augmented neural networks for interpretable constitutive laws. | Python | GPL (stated in README) |  |
| [FuhgJan/<br>invariant_DD_CM](https://github.com/FuhgJan/invariant_DD_CM) | Space-filling sampling of invariant space for data-driven constitutive models. | MATLAB | conflicting statements | Requires MATLAB R2017a or later; README states both GPL-3.0 and a non-commercial Creative Commons license. |
| [FuhgJan/<br>modelDataDriven_YieldFunction](https://github.com/FuhgJan/modelDataDriven_YieldFunction) | Hybrid model-data-driven yield functions. | Python | conflicting statements | README states both GPL-3.0 and a non-commercial Creative Commons license. |
| [hyoungsuksuh/<br>ABAQUS_NN](https://github.com/hyoungsuksuh/ABAQUS_NN) | PyTorch-to-UMAT framework for deep-learning level-set plasticity. | Python | none found | Requires Abaqus. |
| [LivingMatterLab/<br>CANN](https://github.com/LivingMatterLab/CANN) | Constitutive artificial neural networks for automated material model discovery. | Jupyter Notebook | none found |  |
| [meghbali/<br>ANNElastoplasticity](https://github.com/meghbali/ANNElastoplasticity) | Neural network approach to elastoplastic constitutive modeling. | Python | MIT |  |
| [pantale/<br>Algorithms-2023](https://github.com/pantale/Algorithms-2023) | Activation function comparison for neural flow laws in thermomechanical forming. | Fortran and Jupyter Notebook | GPL-3.0 | Requires Abaqus for the subroutines. |
| [pantale/<br>ANN-ConstitutiveLaw](https://github.com/pantale/ANN-ConstitutiveLaw) | Neural network flow laws for metals, implemented as VUHARD subroutines. | Jupyter Notebook | none found | Requires Abaqus/Explicit for the subroutines. |
| [tajtac/<br>Anisotropic_NN_UMAT](https://github.com/tajtac/Anisotropic_NN_UMAT) | Neural network model of anisotropic soft tissue with a UMAT. | Jupyter Notebook and Fortran | none found | Requires Abaqus for the UMAT. |
| [tajtac/<br>hypermodelcomp](https://github.com/tajtac/hypermodelcomp) | Comparison of CANN, input-convex network and neural ODE models of hyperelasticity. | Jupyter Notebook | none found |  |
| [tajtac/<br>node_diffusion](https://github.com/tajtac/node_diffusion) | Research notebooks combining neural ODE hyperelastic models with diffusion models. | Jupyter Notebook | none found | No README. |
| [tajtac/<br>NODE_v2](https://github.com/tajtac/NODE_v2) | Polyconvex strain energy functions from neural ODEs, with finite element examples. | Jupyter Notebook and Fortran | none found | LICENSE file is empty; finite element examples use Abaqus. |
| [tgulikers/<br>ABAQUS_ANN_constitutive_model](https://github.com/tgulikers/ABAQUS_ANN_constitutive_model) | Thesis code that trains neural network constitutive models and generates a UMAT. | Fortran | none found | Requires Abaqus for the UMAT. |

</details>

<details>
<summary><h3>Unsupervised model discovery</h3></summary>
<p id="open-constitutive-modeling-and-material-identification--unsupervised-model-discovery"><sub>Constitutive modeling and material identification › <b>Unsupervised model discovery</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [EUCLID-code/<br>EUCLID-hyperelasticity](https://github.com/EUCLID-code/EUCLID-hyperelasticity) | Unsupervised discovery of hyperelastic strain energy functions from full-field displacement data. | Python | GPL-3.0 |  |
| [EUCLID-code/<br>EUCLID-hyperelasticity-bayesian](https://github.com/EUCLID-code/EUCLID-hyperelasticity-bayesian) | Bayesian discovery of hyperelastic laws with uncertainty. | Python | GPL-3.0 |  |
| [EUCLID-code/<br>EUCLID-hyperelasticity-NN](https://github.com/EUCLID-code/EUCLID-hyperelasticity-NN) | Neural network hyperelasticity learned without stress data. | Python | GPL-3.0 |  |
| [EUCLID-code/<br>EUCLID-hyperelasticity-PlaneStress-ExperimentalData](https://github.com/EUCLID-code/EUCLID-hyperelasticity-PlaneStress-ExperimentalData) | Discovery of plane-stress hyperelastic laws from experimental data. | Python | none found |  |
| [EUCLID-code/<br>EUCLID-plasticity](https://github.com/EUCLID-code/EUCLID-plasticity) | Discovery of plasticity and generalized standard material models without stress data. | MATLAB | GPL-3.0 | Written for MATLAB, Octave support not documented. |
| [EUCLID-code/<br>EUCLID-plasticity-pressure-sensitive-non-associated](https://github.com/EUCLID-code/EUCLID-plasticity-pressure-sensitive-non-associated) | Discovery of non-associated pressure-sensitive plasticity models. | MATLAB | none found | Written for MATLAB, Octave support not documented. |
| [EUCLID-code/<br>EUCLID-viscoelasticity](https://github.com/EUCLID-code/EUCLID-viscoelasticity) | Automated identification of linear viscoelastic laws. | MATLAB | GPL-3.0 | Written for MATLAB, Octave support not documented. |

</details>

<details>
<summary><h3>Material subroutines and libraries</h3></summary>
<p id="open-constitutive-modeling-and-material-identification--material-subroutines-and-libraries"><sub>Constitutive modeling and material identification › <b>Material subroutines and libraries</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [abuganza/<br>UMAT_anisotropic_damage](https://github.com/abuganza/UMAT_anisotropic_damage) | Anisotropic damage subroutines for collagenous tissue fracture and needle insertion. | Fortran | GPL-3.0, with BSD-style file headers | Requires Abaqus. |
| [adtzlr/<br>hyperelastic](https://github.com/adtzlr/hyperelastic) | Building blocks for hyperelastic material formulations in FElupe. | Python | GPL-3.0 |  |
| [adtzlr/<br>matadi](https://github.com/adtzlr/matadi) | Hyperelastic material definitions with automatic differentiation. | Python | GPL-3.0 |  |
| [bleyerj/<br>dolfinx_materials](https://github.com/bleyerj/dolfinx_materials) | Complex constitutive behaviors for FEniCSx. | Python | CC-BY-SA-4.0 | MFront behaviors require TFEL. |
| [jgomezc1/<br>ABAQUS-US](https://github.com/jgomezc1/ABAQUS-US) | User element and user material subroutines, including classical and Cosserat elements. | Fortran | MIT | Requires Abaqus. |
| [jpsferreira/<br>abaqus-material-lab](https://github.com/jpsferreira/abaqus-material-lab) | Composable UMAT and UEL framework for soft tissues and filament networks. | Fortran | GPL-3.0 (stated in README) | Requires Abaqus; no license file. |
| [jpsferreira/<br>UMAT-ABAQUS](https://github.com/jpsferreira/UMAT-ABAQUS) | Fortran framework for large-deformation material models, aimed at soft tissues and cells. | Fortran | GPL-3.0 | README invites non-commercial use, although the license is GPL-3.0. |
| [pantale/<br>abaqusVumat](https://github.com/pantale/abaqusVumat) | Johnson-Cook VUMAT subroutines. | Fortran | BSD-3-Clause | Requires Abaqus/Explicit. |
| [SofaDefrost/<br>SofaViscoElastic](https://github.com/SofaDefrost/SofaViscoElastic) | SOFA plugin for linear viscoelastic and visco-hyperelastic laws on tetrahedral meshes. | C++ | LGPL-2.1 | Requires SOFA. |
| [thelfer/<br>tfel](https://github.com/thelfer/tfel) | TFEL and MFront, a code generator for material knowledge and behavior laws. | C++ | GPL with linking exception, or CeCILL-A |  |

</details>

<details>
<summary><h3>Experimental parameter identification</h3></summary>
<p id="open-constitutive-modeling-and-material-identification--experimental-parameter-identification"><sub>Constitutive modeling and material identification › <b>Experimental parameter identification</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [BinChenOPEN/<br>FEMU-DIC](https://github.com/BinChenOPEN/FEMU-DIC) | Digital image correlation and finite element model updating for strain measurement and parameter identification. | MATLAB | GPL-3.0 | Requires MATLAB and COMSOL. |
| [dicengine/<br>dice](https://github.com/dicengine/dice) | Stereo digital image correlation engine for full-field displacements and strains. | C++ | BSD-3-Clause |  |
| [lululxvi/<br>deep-learning-for-indentation](https://github.com/lululxvi/deep-learning-for-indentation) | Extraction of material properties from instrumented indentation with deep learning. | Python | Apache-2.0 | Depends on DeepXDE. |
| [MultiDIC/<br>MultiDIC](https://github.com/MultiDIC/MultiDIC) | Multi-view 3D digital image correlation toolbox. | MATLAB | Apache-2.0 | Requires MATLAB with the Image Processing, Computer Vision and Statistics toolboxes. |
| [PolymerGuy/<br>muDIC](https://github.com/PolymerGuy/muDIC) | Python toolkit for digital image correlation and virtual experiments. | Python | MIT |  |
| [vincentjzy/<br>OpenCorr](https://github.com/vincentjzy/OpenCorr) | Library for 2D, stereo and volumetric digital image correlation. | C++ | MPL-2.0 |  |

</details>

</details>

<details>
<summary><h2>Multiscale and homogenization</h2></summary>
<p id="open-multiscale-and-homogenization"><sub><b>Multiscale and homogenization</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><h3>FFT-based homogenization</h3></summary>
<p id="open-multiscale-and-homogenization--fft-based-homogenization"><sub>Multiscale and homogenization › <b>FFT-based homogenization</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [DataAnalyticsEngineering/<br>FANS](https://github.com/DataAnalyticsEngineering/FANS) | Parallel FFT-based homogenization for microscale multiphysics problems. | C++ | LGPL-3.0 |  |
| [tdegeus/<br>GooseFFT](https://github.com/tdegeus/GooseFFT) | Small teaching scripts for FFT-based micromechanical solvers. | Python | MIT |  |
| [vondrejc/<br>FFTHomPy](https://github.com/vondrejc/FFTHomPy) | FFT-based homogenization with guaranteed bounds on effective properties. | Python | MIT |  |

</details>

<details>
<summary><h3>FE² and computational homogenization</h3></summary>
<p id="open-multiscale-and-homogenization--fe2-and-computational-homogenization"><sub>Multiscale and homogenization › <b>FE² and computational homogenization</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [felipefr/<br>micmacsfenics](https://github.com/felipefr/micmacsfenics) | FE² and computational homogenization in FEniCS. | Python | MIT | README points to the legacy branch for working code during a rewrite. |
| [meghbali/<br>MultiScalePlasticity](https://github.com/meghbali/MultiScalePlasticity) | Upscaling of representative volumes with elastoplastic constituents. | MATLAB | MIT | Written for MATLAB, Octave support not documented. |
| [MinhNguyenIKM/<br>multiscale-homogenization](https://github.com/MinhNguyenIKM/multiscale-homogenization) | FFT microscale and finite element macroscale computational homogenization. | MATLAB and Python | none found | Includes MATLAB code; bundled PyFEM files state all rights reserved. |

</details>

<details>
<summary><h3>Inverse homogenization</h3></summary>
<p id="open-multiscale-and-homogenization--inverse-homogenization"><sub>Multiscale and homogenization › <b>Inverse homogenization</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [lavenklau/<br>homo3d](https://github.com/lavenklau/homo3d) | GPU solver for large-scale inverse homogenization. | C++ and CUDA | GPL-2.0 | Requires an NVIDIA GPU; README says the main branch is being refactored. |

</details>

<details>
<summary><h3>Crystal plasticity</h3></summary>
<p id="open-multiscale-and-homogenization--crystal-plasticity"><sub>Multiscale and homogenization › <b>Crystal plasticity</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [apatra6/<br>rhocp](https://github.com/apatra6/rhocp) | Dislocation-density crystal plasticity solver built on MOOSE. | C++ | LGPL-2.1 |  |
| [damask-multiphysics/<br>DAMASK](https://github.com/damask-multiphysics/DAMASK) | Multiscale crystal plasticity simulation kit. | Fortran and Python | AGPL-3.0-or-later | Read-only mirror; development is at git.damask-multiphysics.org. |
| [llnl/<br>ExaConstit](https://github.com/llnl/ExaConstit) | GPU crystal plasticity finite element code with a UMAT interface. | C++ | BSD-3-Clause |  |
| [prisms-center/<br>plasticity](https://github.com/prisms-center/plasticity) | Crystal and continuum plasticity finite element code built on deal.II. | C++ | LGPL-2.1-or-later |  |
| [SuperkakaSCU/<br>JAX-CPFEM](https://github.com/SuperkakaSCU/JAX-CPFEM) | Differentiable GPU crystal plasticity finite elements built on JAX-FEM. | Python | none found |  |

</details>

</details>

<details>
<summary><h2>Thermal, multiphysics and additive manufacturing</h2></summary>
<p id="open-thermal-multiphysics-and-additive-manufacturing"><sub><b>Thermal, multiphysics and additive manufacturing</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><h3>Heat transfer and bio-heat</h3></summary>
<p id="open-thermal-multiphysics-and-additive-manufacturing--heat-transfer-and-bio-heat"><sub>Thermal, multiphysics and additive manufacturing › <b>Heat transfer and bio-heat</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [jinaojakezhang/<br>FEDFEM](https://github.com/jinaojakezhang/FEDFEM) | Fast explicit dynamics finite elements for transient heat transfer. | C++ | MIT |  |
| [jinaojakezhang/<br>FEDFEMBioheat](https://github.com/jinaojakezhang/FEDFEMBioheat) | Real-time bio-heat transfer with fast explicit dynamics finite elements. | C++ | MIT |  |
| [jinaojakezhang/<br>FEDFEMBioheatDamage](https://github.com/jinaojakezhang/FEDFEMBioheatDamage) | CEM43 thermal damage added to real-time bio-heat simulation. | C++ | MIT |  |
| [jinaojakezhang/<br>FEDFEMBioheatDeform](https://github.com/jinaojakezhang/FEDFEMBioheatDeform) | Soft tissue thermal response under deformation for surgical simulation. | C++ | MIT |  |
| [jinaojakezhang/<br>FEDFEMBioheatExpan](https://github.com/jinaojakezhang/FEDFEMBioheatExpan) | Anisotropic thermo-visco-elastodynamics of soft tissue for ablation therapy. | C++ | MIT |  |

</details>

<details>
<summary><h3>Thermoelasticity</h3></summary>
<p id="open-thermal-multiphysics-and-additive-manufacturing--thermoelasticity"><sub>Thermal, multiphysics and additive manufacturing › <b>Thermoelasticity</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [rcapillon/<br>thermoelasticity_fem](https://github.com/rcapillon/thermoelasticity_fem) | Finite element solver for linear thermoelasticity. | Python | MIT | README warns of incomplete documentation and possible bugs. |

</details>

<details>
<summary><h3>Additive manufacturing</h3></summary>
<p id="open-thermal-multiphysics-and-additive-manufacturing--additive-manufacturing"><sub>Thermal, multiphysics and additive manufacturing › <b>Additive manufacturing</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [CMSL-HKUST/<br>jax-am](https://github.com/CMSL-HKUST/jax-am) | Differentiable GPU toolbox for additive manufacturing process, structure and property simulation. | Jupyter Notebook | GPL-3.0 |  |
| [CMSL-HKUST/<br>Opt-IS](https://github.com/CMSL-HKUST/Opt-IS) | Inherent strain calibration for residual stress and distortion in additive manufacturing. | Python | none found |  |
| [JLnorthwestern/<br>GO-MELT](https://github.com/JLnorthwestern/GO-MELT) | GPU multilevel thermal simulation of laser powder bed fusion. | Python | MIT |  |

</details>

<details>
<summary><h3>Multiphysics coupling</h3></summary>
<p id="open-thermal-multiphysics-and-additive-manufacturing--multiphysics-coupling"><sub>Thermal, multiphysics and additive manufacturing › <b>Multiphysics coupling</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [precice/<br>dealii-adapter](https://github.com/precice/dealii-adapter) | Coupled linear and nonlinear elastic solvers connecting deal.II to preCICE. | C++ | LGPL-3.0 |  |
| [precice/<br>precice](https://github.com/precice/precice) | Coupling library for partitioned multiphysics and multiscale simulation. | C++ | LGPL-3.0 |  |

</details>

</details>

<details>
<summary><h2>Optimization and inverse problems</h2></summary>
<p id="open-optimization-and-inverse-problems"><sub><b>Optimization and inverse problems</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><h3>Topology optimization solvers</h3></summary>
<p id="open-optimization-and-inverse-problems--topology-optimization-solvers"><sub>Optimization and inverse problems › <b>Topology optimization solvers</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [calculix/<br>beso](https://github.com/calculix/beso) | Evolutionary topology optimization using the CalculiX solver. | Python | LGPL-3.0 | Requires CalculiX and FreeCAD. |
| [Jasiuk-Research-Group/<br>LatticeOPT](https://github.com/Jasiuk-Research-Group/LatticeOPT) | Heuristic topology optimization of thin-walled lattice structures. | Python | MIT | Requires Abaqus/Explicit. |
| [JuliaTopOpt/<br>TopOpt.jl](https://github.com/JuliaTopOpt/TopOpt.jl) | Truss and continuum topology optimization with automatic differentiation. | Julia | MIT |  |
| [topopt/<br>TopOpt-in-OpenMP-GPU](https://github.com/topopt/TopOpt-in-OpenMP-GPU) | GPU topology optimization with OpenMP target offloading. | C | none found |  |
| [topopt/<br>TopOpt_in_PETSc](https://github.com/topopt/TopOpt_in_PETSc) | Parallel large-scale 3D topology optimization with PETSc. | C++ | unclear | Includes the LGPL text, but source headers say all rights reserved. |
| [topopt/<br>TopOpt_in_PETSc_Transient](https://github.com/topopt/TopOpt_in_PETSc_Transient) | Large-scale transient 3D topology optimization with PETSc. | C++ | unclear | Includes the LGPL text, but source headers say all rights reserved. |
| [williamhunter/<br>topy](https://github.com/williamhunter/topy) | Lightweight 2D and 3D topology optimization framework. | Python | MIT |  |
| [yuanming-hu/<br>spgrid_topo_opt](https://github.com/yuanming-hu/spgrid_topo_opt) | Narrow-band topology optimization on sparsely populated grids. | C++ | MIT and BSD, by component |  |
| [zfergus/<br>topopt](https://github.com/zfergus/topopt) | Python library for topology optimization. | Python | MIT | README says it is at an early stage. |

</details>

<details>
<summary><h3>Learning-based topology optimization</h3></summary>
<p id="open-optimization-and-inverse-problems--learning-based-topology-optimization"><sub>Optimization and inverse problems › <b>Learning-based topology optimization</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [deng-cy/<br>deep_learning_topology_opt](https://github.com/deng-cy/deep_learning_topology_opt) | Self-directed online learning for topology optimization. | MATLAB | MIT | Most examples need MATLAB and COMSOL. |
| [dl4to/<br>dl4to](https://github.com/dl4to/dl4to) | PyTorch library for 3D topology optimization with neural networks. | Python and Jupyter Notebook | Apache-2.0 |  |
| [gigatskhondia/<br>gigala](https://github.com/gigatskhondia/gigala) | Structural topology optimization with reinforcement learning, genetic algorithms and finite elements. | Jupyter Notebook | MIT |  |
| [Jasiuk-Research-Group/<br>DeepEnergy-TopOpt](https://github.com/Jasiuk-Research-Group/DeepEnergy-TopOpt) | Density-based topology optimization with the deep energy method. | Python | none found |  |
| [zhenguonie/<br>2020_TopologyGAN](https://github.com/zhenguonie/2020_TopologyGAN) | Generative adversarial networks for topology optimization from physical fields. | Python | none found | Dataset is downloaded separately. |

</details>

<details>
<summary><h3>Inverse problems</h3></summary>
<p id="open-optimization-and-inverse-problems--inverse-problems"><sub>Optimization and inverse problems › <b>Inverse problems</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [idaholab/<br>isopod](https://github.com/idaholab/isopod) | MOOSE application for PDE-constrained multiphysics optimization. | C++ | LGPL-2.1 |  |
| [kailaix/<br>PhysGNN](https://github.com/kailaix/PhysGNN) | Physics-constrained generative networks, including a stochastic elasticity example. | Julia | none found |  |
| [lu-group/<br>pinn-material-identification](https://github.com/lu-group/pinn-material-identification) | Physics-informed networks for identifying material properties in solid mechanics. | Python | Apache-2.0 | Paper code. |
| [nandakishorebm1995/<br>FOR3022_Code](https://github.com/nandakishorebm1995/FOR3022_Code) | Bayesian damage identification in fiber metal laminates with model order reduction. | MATLAB | none found | Requires MATLAB and COMSOL. |

</details>

</details>

<details>
<summary><h2>Physics-informed learning and energy methods</h2></summary>
<p id="open-physics-informed-learning-and-energy-methods"><sub><b>Physics-informed learning and energy methods</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><h3>Deep energy methods</h3></summary>
<p id="open-physics-informed-learning-and-energy-methods--deep-energy-methods"><sub>Physics-informed learning and energy methods › <b>Deep energy methods</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [FuhgJan/<br>mixedDEM](https://github.com/FuhgJan/mixedDEM) | Mixed deep energy method for stress concentrations in finite-strain hyperelasticity. | Python | conflicting statements | README states both GPL-3.0 and a non-commercial Creative Commons license. |
| [ISM-Weimar/<br>DeepEnergyMethods](https://github.com/ISM-Weimar/DeepEnergyMethods) | Companion code for energy-based deep learning solutions of PDEs in mechanics. | Python | MIT |  |
| [Jasiuk-Research-Group/<br>DEM_for_J2_plasticity](https://github.com/Jasiuk-Research-Group/DEM_for_J2_plasticity) | Deep energy method for 3D J2 elastoplasticity. | Python | MIT |  |
| [Jasiuk-Research-Group/<br>Graph_DEM](https://github.com/Jasiuk-Research-Group/Graph_DEM) | Comparison of graph convolution and MLP deep energy methods for elastic solids. | Python | none found |  |
| [JinshuaiBai/<br>energy_PINN_Contact](https://github.com/JinshuaiBai/energy_PINN_Contact) | Energy-based PINN for frictionless large-deformation contact. | Python | none found |  |
| [MinhNguyenIKM/<br>dem_hyperelasticity](https://github.com/MinhNguyenIKM/dem_hyperelasticity) | Deep energy method for finite-deformation hyperelasticity. | Python | none found |  |
| [somdattagoswami/<br>DEM-PhaseField](https://github.com/somdattagoswami/DEM-PhaseField) | Adaptive phase-field fracture with deep energy minimization. | Python | none found | Requires TensorFlow 1.15. |
| [yizheng-wang/<br>Research-on-Solving-Partial-Differential-Equations-of-Solid-Mechanics-Based-on-PINN](https://github.com/yizheng-wang/Research-on-Solving-Partial-Differential-Equations-of-Solid-Mechanics-Based-on-PINN) | Thesis code for solid mechanics with deep energy, CENN, DCEM and KINN methods. | Python | none found |  |

</details>

<details>
<summary><h3>Residual-based networks</h3></summary>
<p id="open-physics-informed-learning-and-energy-methods--residual-based-networks"><sub>Physics-informed learning and energy methods › <b>Residual-based networks</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [JinshuaiBai/<br>LSWR_loss_function_PINN](https://github.com/JinshuaiBai/LSWR_loss_function_PINN) | Least squares weighted residual loss for PINN solid mechanics. | Python | none found |  |
| [JinshuaiBai/<br>PINN_Comp_Mech](https://github.com/JinshuaiBai/PINN_Comp_Mech) | Introductory PINN examples in solid mechanics with collocation and energy losses. | Python | none found |  |
| [JinshuaiBai/<br>PIRBN](https://github.com/JinshuaiBai/PIRBN) | Physics-informed radial basis networks with spring, wave and viscoelastic flow examples. | Python | none found |  |
| [Raocp/<br>PINN-elastodynamics](https://github.com/Raocp/PINN-elastodynamics) | Physics-informed networks for elastodynamics without labeled data. | Python | none found |  |

</details>

<details>
<summary><h3>PINN libraries and examples</h3></summary>
<p id="open-physics-informed-learning-and-energy-methods--pinn-libraries-and-examples"><sub>Physics-informed learning and energy methods › <b>PINN libraries and examples</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [ehsanhaghighat/<br>sciann-applications](https://github.com/ehsanhaghighat/sciann-applications) | SciANN examples, including elasticity, elastoplasticity, vibration and poroelasticity. | Jupyter Notebook | MIT | SciANN itself is unmaintained. |
| [lululxvi/<br>deepxde](https://github.com/lululxvi/deepxde) | Library for physics-informed learning of forward and inverse differential equation problems. | Python | LGPL-2.1 |  |

</details>

</details>

<details>
<summary><h2>Surrogates and reduced-order models</h2></summary>
<p id="open-surrogates-and-reduced-order-models"><sub><b>Surrogates and reduced-order models</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><h3>Stress-field prediction</h3></summary>
<p id="open-surrogates-and-reduced-order-models--stress-field-prediction"><sub>Surrogates and reduced-order models › <b>Stress-field prediction</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [farazarbabi/<br>CNN_FEM](https://github.com/farazarbabi/CNN_FEM) | Convolutional network prediction of stress fields in solids from simulation data. | Python | all rights reserved | Stated in source file headers. |
| [federicosanna/<br>UNet-for-FEM-and-Stress-Distribution-Inference](https://github.com/federicosanna/UNet-for-FEM-and-Stress-Distribution-Inference) | U-Net inference of stress distributions from finite element data. | Python | none found | Some trained models are not included. |
| [Jasiuk-Research-Group/<br>ResUNet-DeepONet-Plasticity](https://github.com/Jasiuk-Research-Group/ResUNet-DeepONet-Plasticity) | Operator network prediction of plastic stress fields on varying geometries. | Python | MIT |  |
| [lamm-mit/<br>FieldPredictorGAN](https://github.com/lamm-mit/FieldPredictorGAN) | Adversarial network prediction of stress and strain fields in composites. | Python | MIT |  |
| [TML-Gatech/<br>DL_Stress_TAA](https://github.com/TML-Gatech/DL_Stress_TAA) | Deep learning surrogate of finite element stress analysis. |  | all rights reserved | Source files are supplied as PDFs. |
| [zhenguonie/<br>2020_StressGAN](https://github.com/zhenguonie/2020_StressGAN) | Generative model for 2D stress distribution prediction. | Python | none found |  |
| [zhenguonie/<br>stress_net](https://github.com/zhenguonie/stress_net) | Convolutional prediction of stress fields in cantilevered structures. | Python | none found |  |

</details>

<details>
<summary><h3>Deformation and reduced dynamics</h3></summary>
<p id="open-surrogates-and-reduced-order-models--deformation-and-reduced-dynamics"><sub>Surrogates and reduced-order models › <b>Deformation and reduced dynamics</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [AlbanOdot/<br>DeepPhysics-article](https://github.com/AlbanOdot/DeepPhysics-article) | Paper code for physics-aware deep learning in real-time simulation. | Python | CC0-1.0 |  |
| [haller-group/<br>SSMLearn](https://github.com/haller-group/SSMLearn) | Data-driven reduced models of nonlinear dynamics on spectral submanifolds. | MATLAB | AGPL-3.0 | Written for MATLAB, Octave support not documented; requires SSMTool. |
| [lawsonfulton/<br>AutoDef](https://github.com/lawsonfulton/AutoDef) | Latent-space dynamics for reduced deformable simulation. | C++ | MIT | Install script can overwrite your Keras configuration. |
| [lrquad/<br>NNWarp](https://github.com/lrquad/NNWarp) | Neural network-based nonlinear deformable simulator. | C++ | MIT |  |
| [saurabhdeshpande93/<br>convolution-aggregation-attention](https://github.com/saurabhdeshpande93/convolution-aggregation-attention) | CNN, graph and attention surrogates for nonlinear finite element simulations. | Python and Mathematica | MIT | Data generation uses AceFEM. |
| [stefaniafresca/<br>POD-DL-ROM](https://github.com/stefaniafresca/POD-DL-ROM) | Deep learning reduced-order models enhanced by proper orthogonal decomposition. | Python | none found | README reports nonlinear elastodynamics tests; the example scripts are templates with blank settings. |
| [vividda/<br>3D-PhysNet](https://github.com/vividda/3D-PhysNet) | Learned prediction of non-rigid 3D object deformation. | Python | none found | Python 2.7. |

</details>

<details>
<summary><h3>Projection-based model reduction</h3></summary>
<p id="open-surrogates-and-reduced-order-models--projection-based-model-reduction"><sub>Surrogates and reduced-order models › <b>Projection-based model reduction</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [llnl/<br>libROM](https://github.com/llnl/libROM) | Parallel library for intrusive and non-intrusive reduced-order models. | C++ | MIT or Apache-2.0 |  |
| [pymor/<br>pymor](https://github.com/pymor/pymor) | Model order reduction library that works with external PDE solvers. | Python | BSD-2-Clause |  |
| [RBniCS/<br>RBniCS](https://github.com/RBniCS/RBniCS) | Reduced-order modeling techniques implemented in FEniCS. | Python | LGPL-3.0-or-later | Built on legacy FEniCS. |
| [SofaDefrost/<br>ModelOrderReduction](https://github.com/SofaDefrost/ModelOrderReduction) | Model reduction plugin for faster SOFA scenes. | C++ and Python | GPL-2.0 | Requires SOFA. |

</details>

<details>
<summary><h3>Graph neural networks</h3></summary>
<p id="open-surrogates-and-reduced-order-models--graph-neural-networks"><sub>Surrogates and reduced-order models › <b>Graph neural networks</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [Jianxun-Wang/<br>graphGalerkin](https://github.com/Jianxun-Wang/graphGalerkin) | Physics-informed graph neural Galerkin networks for forward and inverse PDE problems. | Python | GPL-3.0 | Requires pyCaMOtk. |
| [m-ulmestrand/<br>gcn-collisions](https://github.com/m-ulmestrand/gcn-collisions) | Graph convolutional network that learns particle collision responses. | Python | Apache-2.0 |  |
| [wwMark/<br>meshgraphnets](https://github.com/wwMark/meshgraphnets) | PyTorch port of MeshGraphNets with cloth simulation. | Python | Apache-2.0 in some files | Author says results do not fully match the original; files without an Apache header state no license. |
| [YasminSalehi/<br>PhysGNN](https://github.com/YasminSalehi/PhysGNN) | Graph neural network prediction of soft tissue deformation in neurosurgery. | Python | BSD-4-Clause |  |

</details>

<details>
<summary><h3>Biomechanical surrogates</h3></summary>
<p id="open-surrogates-and-reduced-order-models--biomechanical-surrogates"><sub>Surrogates and reduced-order models › <b>Biomechanical surrogates</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [dabiriyaghoub/<br>Ventricular_ML_DecisionTrees](https://github.com/dabiriyaghoub/Ventricular_ML_DecisionTrees) | Machine learning prediction of left ventricular mechanics. | Python | all rights reserved |  |
| [michetonu/<br>MALTIDEM--Machine-Learning-for-Tissue-Deformation-Modelling](https://github.com/michetonu/MALTIDEM--Machine-Learning-for-Tissue-Deformation-Modelling) | Data-driven real-time model of brain tumor deformation for neurosurgery. | MATLAB | none found | Workflow uses MATLAB and FEBio. |

</details>

<details>
<summary><h3>Response histories and operator learning</h3></summary>
<p id="open-surrogates-and-reduced-order-models--response-histories-and-operator-learning"><sub>Surrogates and reduced-order models › <b>Response histories and operator learning</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [Jasiuk-Research-Group/<br>Bio-inspired-low-porosity-structures-using-Neural-Networks-GRU-Implemenation](https://github.com/Jasiuk-Research-Group/Bio-inspired-low-porosity-structures-using-Neural-Networks-GRU-Implemenation) | Recurrent network prediction of stress-strain response and energy absorption in bio-inspired structures. | Python | MIT |  |
| [Jasiuk-Research-Group/<br>CMDS-14-impact-resistantance-NN-prediction-](https://github.com/Jasiuk-Research-Group/CMDS-14-impact-resistantance-NN-prediction-) | Neural networks for structure-property relations in impact-resistant structures. | Python | none found |  |
| [Jasiuk-Research-Group/<br>LatticeResponse_NN_Prediction](https://github.com/Jasiuk-Research-Group/LatticeResponse_NN_Prediction) | Recurrent network prediction of lattice stress-strain curves and energy absorption. | Python | none found |  |
| [Jasiuk-Research-Group/<br>S-DeepONet](https://github.com/Jasiuk-Research-Group/S-DeepONet) | Sequential operator network with plasticity and heat transfer examples. | Python | none found |  |
| [Jasiuk-Research-Group/<br>S-DeepONet-transient-predictions](https://github.com/Jasiuk-Research-Group/S-DeepONet-transient-predictions) | Sequential operator network for transient full-field predictions, including plasticity. | Python | none found |  |
| [JinshuaiBai/<br>Discrete-Solution-Operator-Learning-DiSOL](https://github.com/JinshuaiBai/Discrete-Solution-Operator-Learning-DiSOL) | Discrete solution operator learning for geometry-dependent PDEs, including linear elasticity. | Python and MATLAB | MIT | Training datasets are downloaded from Zenodo; MATLAB is used for data generation. |

</details>

<details>
<summary><h3>Frameworks and introductory studies</h3></summary>
<p id="open-surrogates-and-reduced-order-models--frameworks-and-introductory-studies"><sub>Surrogates and reduced-order models › <b>Frameworks and introductory studies</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [hmjeon/<br>FEM-ML](https://github.com/hmjeon/FEM-ML) | Experiments in finite element analysis with machine learning. | Jupyter Notebook | GPL-3.0 | Sparse documentation. |
| [mimesis-inria/<br>DeepPhysX](https://github.com/mimesis-inria/DeepPhysX) | Interface between numerical simulations and learning algorithms for training and prediction. | Python | AGPL-3.0 |  |
| [oleksiyskononenko/<br>mlfem](https://github.com/oleksiyskononenko/mlfem) | Notebook and report on deep learning with finite element models of physical systems. | Jupyter Notebook | none found |  |

</details>

<details>
<summary><h3>Benchmark datasets</h3></summary>
<p id="open-surrogates-and-reduced-order-models--benchmark-datasets"><sub>Surrogates and reduced-order models › <b>Benchmark datasets</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [elejeune11/<br>Mechanical-MNIST](https://github.com/elejeune11/Mechanical-MNIST) | Benchmark of 70,000 large-deformation finite element simulations for surrogate models. | Python | MIT code, CC-BY-SA-3.0 data |  |

</details>

</details>

<details>
<summary><h2>Meshing, pre- and post-processing</h2></summary>
<p id="open-meshing-pre--and-post-processing"><sub><b>Meshing, pre- and post-processing</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><h3>Mesh generation</h3></summary>
<p id="open-meshing-pre--and-post-processing--mesh-generation"><sub>Meshing, pre- and post-processing › <b>Mesh generation</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [fangq/<br>iso2mesh](https://github.com/fangq/iso2mesh) | Surface and volumetric mesh generation from 3D images. | MATLAB | GPL-2.0-or-later, excluding bundled binaries | Runs in MATLAB or Octave; bundled binaries have their own licenses. |
| [gmsh/<br>gmsh](https://gitlab.onelab.info/gmsh/gmsh) | 3D finite element mesh generator with pre- and post-processing. | C++ | GPL-2.0-or-later with linking exception |  |
| [inducer/<br>meshpy](https://github.com/inducer/meshpy) | Python interfaces to the Triangle and TetGen mesh generators. | C++ | MIT wrapper, with Triangle and AGPL-3.0 components | Triangle restricts commercial distribution. |
| [meshpro/<br>dmsh](https://github.com/meshpro/dmsh) | Simple 2D mesh generator inspired by distmesh. |  | unclear | No source in the repository; GitHub reports GPL-3.0, but there is no license file. |
| [meshpro/<br>meshzoo](https://github.com/meshpro/meshzoo) | Generators of meshes for simple canonical domains. |  | none found | No source in the repository. |
| [meshpro/<br>pygalmesh](https://github.com/meshpro/pygalmesh) | Python front end to CGAL's 2D and 3D mesh generators. | C++ | GPL-3.0 | Commercial license offered separately. |
| [NGSolve/<br>netgen](https://github.com/NGSolve/netgen) | Automatic 3D tetrahedral mesh generator. | C++ | LGPL-2.1 |  |
| [nschloe/<br>pygmsh](https://github.com/nschloe/pygmsh) | Python abstractions for building geometries and meshes with Gmsh. | Python | GPL-3.0 |  |
| [pyvista/<br>scikit-gmsh](https://github.com/pyvista/scikit-gmsh) | Python interface to Gmsh for finite element meshes. | Python | GPL-3.0 |  |
| [pyvista/<br>tetgen](https://github.com/pyvista/tetgen) | Python interface to the TetGen tetrahedral mesh generator. | C++ and Python | MIT wrapper, with AGPL-3.0 TetGen |  |
| [sandialabs/<br>vorocrust-meshing](https://github.com/sandialabs/vorocrust-meshing) | Conforming Voronoi meshing of non-convex and non-manifold domains. | C++ | BSD-3-Clause |  |
| [wildmeshing/<br>fTetWild](https://github.com/wildmeshing/fTetWild) | Fast and robust tetrahedral meshing of imperfect input geometry. | C++ | MPL-2.0 |  |
| [wildmeshing/<br>TriWild](https://github.com/wildmeshing/TriWild) | Robust triangulation with curve constraints. | C++ | MPL-2.0 | README requires citation. |

</details>

<details>
<summary><h3>Mesh processing and formats</h3></summary>
<p id="open-meshing-pre--and-post-processing--mesh-processing-and-formats"><sub>Meshing, pre- and post-processing › <b>Mesh processing and formats</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [meshpro/<br>meshplex](https://github.com/meshpro/meshplex) | Geometric quantities such as areas and volumes for simplex meshes. |  | proprietary | No source in the repository; full use requires a paid license. |
| [mikedh/<br>trimesh](https://github.com/mikedh/trimesh) | Python library for loading, editing and analyzing triangular meshes. | Python | MIT |  |
| [nschloe/<br>meshio](https://github.com/nschloe/meshio) | Reader, writer and converter for many mesh file formats. | Python | MIT |  |
| [sandialabs/<br>seacas](https://github.com/sandialabs/seacas) | Suite for finite element pre-processing, post-processing and translation. | C, Fortran and C++ | BSD-3-Clause |  |
| [wildmeshing/<br>wildmeshing-toolkit](https://github.com/wildmeshing/wildmeshing-toolkit) | Parallel triangle and tetrahedral mesh generation and editing. | C++ | MIT |  |

</details>

<details>
<summary><h3>Visualization and export</h3></summary>
<p id="open-meshing-pre--and-post-processing--visualization-and-export"><sub>Meshing, pre- and post-processing › <b>Visualization and export</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [GLVis/<br>glvis](https://github.com/GLVis/glvis) | OpenGL visualization of finite element meshes and functions. | C++ | BSD-3-Clause |  |
| [Kitware/<br>ParaView](https://github.com/Kitware/ParaView) | Parallel data analysis and visualization application built on VTK. | C++ | BSD-3-Clause |  |
| [Liujie-SYSU/<br>odb2vtk](https://github.com/Liujie-SYSU/odb2vtk) | Converter from Abaqus ODB results to VTK for ParaView. | Python | none found | Input is Abaqus output. |
| [paulo-herrera/<br>PyEVTK](https://github.com/paulo-herrera/PyEVTK) | Pure-Python export of data to binary VTK files. | Python | MIT (stated in source) |  |
| [pyvista/<br>pyvista](https://github.com/pyvista/pyvista) | 3D visualization and mesh analysis with a NumPy-based interface. | Python | MIT |  |

</details>

</details>

<details>
<summary><h2>Courses, references and agents for mechanics</h2></summary>
<p id="open-courses-references-and-agents-for-mechanics"><sub><b>Courses, references and agents for mechanics</b> · <a href="#contents">Back to contents</a></sub></p>

<details>
<summary><h3>Courses and tutorials</h3></summary>
<p id="open-courses-references-and-agents-for-mechanics--courses-and-tutorials"><sub>Courses, references and agents for mechanics › <b>Courses and tutorials</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [Ceyron/<br>machine-learning-and-simulation](https://github.com/Ceyron/machine-learning-and-simulation) | Notes and code for a video course on simulation and machine learning, including continuum mechanics and FEniCS. | Jupyter Notebook | MIT |  |
| [cooperrc/<br>computational-mechanics](https://github.com/cooperrc/computational-mechanics) | Open course materials on computational mechanics. | MATLAB | CC-BY-4.0 content, BSD-3-Clause code (stated in README) | Includes code written for MATLAB, Octave support not documented. |
| [dilevin/<br>CSC417-a4-cloth-simulation](https://github.com/dilevin/CSC417-a4-cloth-simulation) | Course assignment on finite element cloth simulation with contact. | C++ | none found | Starter code for an assignment. |
| [InteractiveComputerGraphics/<br>physics-simulation](https://github.com/InteractiveComputerGraphics/physics-simulation) | Introduction to simulation of rigid bodies, deformable solids and fluids. |  | MIT | Documents only, no code. |
| [jomorlier/<br>feacourse](https://github.com/jomorlier/feacourse) | Materials for a computational solid mechanics course. | MATLAB | none found | Tutorials are written for MATLAB; assignments also use commercial solvers. |
| [ltt1598/<br>GAMES_Xi-an_forward_physics](https://github.com/ltt1598/GAMES_Xi-an_forward_physics) | Notes and Taichi sample code from a physically based simulation course. | Python | none found |  |
| [matthias-research/<br>pages](https://github.com/matthias-research/pages/tree/master/tenMinutePhysics) | Ten Minute Physics tutorials on soft bodies, cloth, collisions and other simulation methods. | JavaScript | MIT (stated in source) |  |
| [phys-sim-book/<br>solid-sim-tutorial](https://github.com/phys-sim-book/solid-sim-tutorial) | Readable examples of optimization-based solid simulation. | Python | Apache-2.0 |  |

</details>

<details>
<summary><h3>Curated lists</h3></summary>
<p id="open-courses-references-and-agents-for-mechanics--curated-lists"><sub>Courses, references and agents for mechanics › <b>Curated lists</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [kimimgo/<br>awesome-ai-cae](https://github.com/kimimgo/awesome-ai-cae) | Curated list of engineering simulation tools that software agents can drive. |  | CC0-1.0 |  |
| [modenaxe/<br>awesome-biomechanics](https://github.com/modenaxe/awesome-biomechanics) | Curated resources for biomechanics and human motion analysis. |  | CC0-1.0 (stated in README) |  |
| [nschloe/<br>awesome-scientific-computing](https://github.com/nschloe/awesome-scientific-computing) | Curated list of scientific computing tools, including finite element and meshing software. | Python | CC0-1.0 |  |
| [thunil/<br>Physics-Based-Deep-Learning](https://github.com/thunil/Physics-Based-Deep-Learning) | Curated list of research on physics-based deep learning. |  | none found |  |
| [tkoyama010/<br>awesome-finite-elements](https://github.com/tkoyama010/awesome-finite-elements) | Curated list of finite element software. |  | CC0-1.0 |  |

</details>

<details>
<summary><h3>Agents for mechanics</h3></summary>
<p id="open-courses-references-and-agents-for-mechanics--agents-for-mechanics"><sub>Courses, references and agents for mechanics › <b>Agents for mechanics</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [Farhad-Davaripour/<br>FEA_Assisted_Agent](https://github.com/Farhad-Davaripour/FEA_Assisted_Agent) | Language model agent that automates Abaqus simulations. | Python | MIT | Requires Abaqus and OpenAI models. |
| [lamm-mit/<br>MechAgents](https://github.com/lamm-mit/MechAgents) | Multi-agent language model workflows for solving mechanics problems numerically. | Jupyter Notebook | Apache-2.0 |  |
| [LuoXueling/<br>MechFoundry](https://github.com/LuoXueling/MechFoundry) | Agent-driven shape generation, meshing and finite element analysis. | Python | Apache-2.0, with non-commercial dependencies | README says some dependencies are restricted to non-commercial use. |

</details>

</details>

## Contributing

Corrections and additions are welcome. See [contributing.md](contributing.md).
