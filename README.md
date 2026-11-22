# Awesome Computational Mechanics

A collection of public repositories for computational mechanics: solid and structural mechanics, soft bodies, biomechanics, particle methods, and machine learning applied to them.

It has 220 entries covering 218 repositories: 112 from the maintainer's GitHub stars, 2 by the maintainer, 33 from accounts the maintainer follows, 4 where those accounts are collaborators, 31 found by topic search and 38 major projects chosen editorially. Another 5 archived or unmaintained ones are in [archive.md](archive.md).

> **Before you rely on this list:** it is not complete. Descriptions were drafted with AI from README excerpts, file listings and repository metadata. The code was not run or validated, and a listing is not an endorsement. License labels are a convenience, not legal advice. "None found" means no license was found in the places checked, so do not assume you may reuse that code. Public does not always mean open source.

## Contents

- [Finite and boundary element methods](#user-content-open-finite-and-boundary-element-methods) (47)
- [Virtual element method](#user-content-open-virtual-element-method) (26)
- [Third medium contact](#user-content-open-third-medium-contact) (13)
- [Meshfree and particle methods](#user-content-open-meshfree-and-particle-methods) (16)
- [Soft-body, real-time and differentiable simulation](#user-content-open-soft-body-real-time-and-differentiable-simulation) (14)
- [Multibody dynamics and biomechanics](#user-content-open-multibody-dynamics-and-biomechanics) (4)
- [Constitutive modeling and material identification](#user-content-open-constitutive-modeling-and-material-identification) (24)
- [Multiscale and homogenization](#user-content-open-multiscale-and-homogenization) (3)
- [Thermal, multiphysics and additive manufacturing](#user-content-open-thermal-multiphysics-and-additive-manufacturing) (7)
- [Optimization and inverse problems](#user-content-open-optimization-and-inverse-problems) (8)
- [Physics-informed learning and energy methods](#user-content-open-physics-informed-learning-and-energy-methods) (13)
- [Surrogates and reduced-order models](#user-content-open-surrogates-and-reduced-order-models) (24)
- [Meshing, pre- and post-processing](#user-content-open-meshing-pre--and-post-processing) (15)
- [Courses, references and agents for mechanics](#user-content-open-courses-references-and-agents-for-mechanics) (6)
- [Contributing](#contributing)

<details>
<summary><h2>Finite and boundary element methods</h2></summary>
<p id="open-finite-and-boundary-element-methods"><sub><b>Finite and boundary element methods</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [ansys/<br>pymapdl](https://github.com/ansys/pymapdl) | Python interface to the Ansys MAPDL solver. | Python | MIT | Requires a licensed copy of Ansys. |
| [AppliedMechanics-EAFIT/<br>SolidsPy](https://github.com/AppliedMechanics-EAFIT/SolidsPy) | Simple finite element code for 2D elasticity. | Python | MIT |  |
| [codeaster/<br>src](https://gitlab.com/codeaster/src) | Source of code_aster, a finite element solver for structural mechanics. | Python, C++ and Fortran | GPL-3.0 | Some validation and material data are not freely distributed. |
| [dealii/<br>dealii](https://github.com/dealii/dealii) | Library for solving PDEs with adaptive finite elements. | C++ | Apache-2.0 with LLVM exception, or LGPL-2.1-or-later |  |
| [deepmodeling/<br>jax-fem](https://github.com/deepmodeling/jax-fem) | Differentiable finite element package built on JAX. | Python | GPL-3.0 |  |
| [Dhondtguido/<br>CalculiX](https://github.com/Dhondtguido/CalculiX) | Three-dimensional structural finite element program. | Fortran | GPL-2.0 |  |
| [dilevin/<br>CSC417-a3-finite-elements-3d](https://github.com/dilevin/CSC417-a3-finite-elements-3d) | Course assignment on 3D finite element simulation of elastic objects. | C++ | none found | Starter code for an assignment. |
| [dmitryikh/<br>nla3d](https://github.com/dmitryikh/nla3d) | C++ framework for writing nonlinear finite element codes in solid mechanics. | C++ | MIT |  |
| [ElmerCSC/<br>elmerfem](https://github.com/ElmerCSC/elmerfem) | Multiphysics finite element suite that includes structural mechanics. | Fortran | GPL-2.0 and LGPL-2.1, by component |  |
| [febiosoftware/<br>FEBio](https://github.com/febiosoftware/FEBio) | Nonlinear finite element solver designed for biomechanics. | C++ | MIT |  |
| [FEniCS/<br>dolfinx](https://github.com/FEniCS/dolfinx) | Computational environment of FEniCSx for solving PDEs with finite elements in C++ and Python. | C++ | LGPL-3.0 |  |
| [Ferrite-FEM/<br>Ferrite.jl](https://github.com/Ferrite-FEM/Ferrite.jl) | Finite element toolbox for Julia. | Julia | MIT |  |
| [firedrakeproject/<br>firedrake](https://github.com/firedrakeproject/firedrake) | Automated system for solving PDEs with the finite element method. | Python | LGPL-3.0-or-later |  |
| [FreeFem/<br>FreeFem-sources](https://github.com/FreeFem/FreeFem-sources) | Finite element solver for nonlinear multiphysics PDEs in 2D and 3D. | C++ | LGPL-3.0 |  |
| [gridap/<br>Gridap.jl](https://github.com/gridap/Gridap.jl) | Tools for grid-based approximation of linear and nonlinear PDEs. | Julia | MIT |  |
| [hplgit/<br>fenics-tutorial](https://github.com/hplgit/fenics-tutorial) | Sources and example programs for the FEniCS Tutorial book. | TeX | none found |  |
| [idaholab/<br>moose](https://github.com/idaholab/moose) | Finite element and finite volume framework for multiphysics simulation. | C++ | LGPL-2.1 |  |
| [isaar/<br>MSolve](https://github.com/isaar/MSolve) | C# solver for computational mechanics problems. | C# | Apache-2.0 |  |
| [jjcremmers/<br>PyFEM](https://github.com/jjcremmers/PyFEM) | Educational and research finite element code for nonlinear solid mechanics. | Python | MIT |  |
| [JWock82/<br>Pynite](https://github.com/JWock82/Pynite) | 3D structural analysis library with static, P-Delta, modal and pushover analysis. | Python | MIT |  |
| [kinnala/<br>scikit-fem](https://github.com/kinnala/scikit-fem) | Lightweight library for finite element assembly. | Python | BSD-3-Clause |  |
| [KratosMultiphysics/<br>Kratos](https://github.com/KratosMultiphysics/Kratos) | Framework for parallel multidisciplinary simulation software. | C++ | BSD-4-Clause (core) | Each application has its own license. |
| [largurajr/<br>FEA-Protus](https://github.com/largurajr/FEA-Protus) | Teaching code for 2D plane stress and plane strain finite element analysis. | Python | none found | Python 2.7. |
| [lcharleux/<br>abapy](https://github.com/lcharleux/abapy) | Finite element pre- and post-processing in Python. | Python | GPL-2.0 | No README. |
| [liangbright/<br>pytorch_fea_paper](https://github.com/liangbright/pytorch_fea_paper) | Differentiable finite element analysis applied to human aorta biomechanics. | Python | none found | Paper code. |
| [libMesh/<br>libmesh](https://github.com/libMesh/libmesh) | Library for parallel adaptive finite element simulations. | C++ | LGPL-2.1 |  |
| [lyc102/<br>ifem](https://github.com/lyc102/ifem) | Adaptive finite element package for 2D and 3D simplicial grids. | MATLAB | GPL-3.0 | Requires MATLAB. |
| [mfem/<br>mfem](https://github.com/mfem/mfem) | Modular parallel library for scalable finite element methods. | C++ | BSD-3-Clause |  |
| [mo-hanxuan/<br>FEMcy](https://github.com/mo-hanxuan/FEMcy) | Taichi-based parallel structural finite element solver with small and large deformation. | Python | MIT |  |
| [nasa/<br>NASTRAN-95](https://github.com/nasa/NASTRAN-95) | NASA's historical structural analysis system for static, dynamic and stability problems. | Fortran | NASA Open Source Agreement 1.3 | No technical support. |
| [NGSolve/<br>ngsolve](https://github.com/NGSolve/ngsolve) | Multiphysics finite element software with a Python interface. | C++ | LGPL-2.1 |  |
| [oofem/<br>oofem](https://github.com/oofem/oofem) | Object-oriented finite element code for mechanical, transport and fluid problems. | C++ | LGPL-2.1 |  |
| [OpenCourant/<br>OpenCourant](https://github.com/OpenCourant/OpenCourant) | Explicit finite element solver for crash, impact and other dynamic events. | Fortran | AGPL-3.0 | Community fork created after OpenRadioss was withdrawn in October 2026; not affiliated with Siemens or Altair. |
| [OpenSees/<br>OpenSees](https://github.com/OpenSees/OpenSees) | Framework for structural and geotechnical earthquake engineering simulation. | C++ | custom, with commercial restrictions | Commercial distribution requires permission from the University of California. |
| [polyfem/<br>polyfem](https://github.com/polyfem/polyfem) | General-purpose C++ finite element library. | C++ | MIT |  |
| [Qinxiaoye/<br>FEM2D](https://github.com/Qinxiaoye/FEM2D) | MATLAB code for 2D finite element analysis. | MATLAB | none found | Input scripts use Ansys or Abaqus. |
| [Qinxiaoye/<br>FEM2D_dynamic](https://github.com/Qinxiaoye/FEM2D_dynamic) | Finite element elastodynamics with Newmark time integration. | MATLAB | none found | Input scripts use Ansys or Abaqus. |
| [Qinxiaoye/<br>FEM3D-C3D8-](https://github.com/Qinxiaoye/FEM3D-C3D8-) | MATLAB finite element code with 3D hexahedral element routines. | MATLAB | none found | README calls it 2D; input scripts use Ansys or Abaqus. |
| [Qinxiaoye/<br>SBFEM2D](https://github.com/Qinxiaoye/SBFEM2D) | Scaled boundary finite element method for 2D linear elasticity. | MATLAB | none found | Modified from code by Chongmin Song. |
| [Qinxiaoye/<br>xpfem](https://github.com/Qinxiaoye/xpfem) | Linear elastic finite element package with quadrilateral, hexahedral and B-bar elements. | Python | none found |  |
| [sandialabs/<br>optimism](https://github.com/sandialabs/optimism) | JAX finite element library that poses nonlinear solid mechanics as optimization. | Python | MIT |  |
| [sfepy/<br>sfepy](https://github.com/sfepy/sfepy) | Finite element solver and library for coupled PDEs in 1D, 2D and 3D. | Python | BSD-3-Clause |  |
| [ShelvanLee/<br>XFEM](https://github.com/ShelvanLee/XFEM) | Extended finite element program for multiple crack propagation in 2D linear elastic solids. | MATLAB | MIT | Requires MATLAB. |
| [Terenceyuyue/<br>varFEM](https://github.com/Terenceyuyue/varFEM) | Finite element programming in a variational-form style. | MATLAB | GPL-3.0 | Requires MATLAB. |
| [Timmmdavis/<br>CutAndDisplace](https://github.com/Timmmdavis/CutAndDisplace) | Boundary element code for faults and deformation. | MATLAB | GPL-3.0 | Requires MATLAB; README restricts use to academia, although the license is GPL-3.0. |
| [tjfulle/<br>fem-with-python](https://github.com/tjfulle/fem-with-python) | Course notes, assignments and code for an introductory finite element course. | Python | MIT (stated in README) |  |
| [weihuayi/<br>fealpy](https://github.com/weihuayi/fealpy) | Python finite element library for algorithm research and computer-aided engineering. | Python | GPL-3.0-or-later with added notice | License notice also restricts commercial use. |

</details>

<details>
<summary><h2>Virtual element method</h2></summary>
<p id="open-virtual-element-method"><sub><b>Virtual element method</b> · <a href="#contents">Back to contents</a></sub></p>

The virtual element method (VEM) generalizes finite elements to polygonal and polyhedral elements.

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [aerubianoma/<br>vem_stress_assisted_diffusion](https://github.com/aerubianoma/vem_stress_assisted_diffusion) | Robust VEM experiments for stress-assisted diffusion in elastic materials. | MATLAB | GPL-3.0 |  |
| [CAMLAB-UChile/<br>vemlab](https://github.com/CAMLAB-UChile/vemlab) | MATLAB library for linear VEM in 2D elastostatics and Poisson problems. | MATLAB | GPL-3.0 |  |
| [cemcen/<br>Veamy](https://github.com/cemcen/Veamy) | Object-oriented C++ library for VEM in 2D elastostatics and Poisson problems. | C++ | GPL (stated in README) |  |
| [chauj96/<br>vem_implementation](https://github.com/chauj96/vem_implementation) | Mixed and hybridized VEM for 3D linear elasticity on polyhedral meshes. | MATLAB | none found | Main code is MATLAB. |
| [DongxiaoLyu/<br>polymesh](https://github.com/DongxiaoLyu/polymesh) | VEM Studio Online, a browser-based polygonal mesher and VEM solver for 2D elasticity and heat conduction. | JavaScript | MIT | Qinxiaoye is a collaborator. |
| [dune-fem/<br>dune-vem](https://gitlab.dune-project.org/dune-fem/dune-vem) | DUNE module with a range of virtual element spaces and a Python interface. | C++ and Python | GPL-2.0 |  |
| [justachetan/<br>VirtualElementMethods](https://github.com/justachetan/VirtualElementMethods) | Python translation of the 50-line introductory VEM code. | Jupyter Notebook | MIT | Solves the Poisson equation, not elasticity. |
| [MinhNguyenIKM/<br>vem](https://github.com/MinhNguyenIKM/vem) | VEM code for 2D linear elastic fracture. | MATLAB | none found |  |
| [Moopz99/<br>VEMK2](https://github.com/Moopz99/VEMK2) | Quadratic VEM for 2D elasticity. | MATLAB | GPL-3.0 | Requires MATLAB. |
| [mySimpleProjects/<br>SimpleVEM](https://github.com/mySimpleProjects/SimpleVEM) | Teaching comparison of FEM and VEM for 2D structural analysis. | MATLAB | GPL-3.0 |  |
| [nsundar/<br>VEM_in_Abaqus](https://github.com/nsundar/VEM_in_Abaqus) | Implementation of the virtual element method as Abaqus subroutines. | Fortran | GPL-3.0 | Requires Abaqus. |
| [oliversutton/<br>50LinesOfVEM](https://github.com/oliversutton/50LinesOfVEM) | Introductory 50-line MATLAB implementation of VEM. | MATLAB | MIT | Solves the Poisson equation, not elasticity. |
| [Qinxiaoye/<br>TOPvem](https://github.com/Qinxiaoye/TOPvem) | Density-based topology optimization with VEM. | MATLAB | none found | Requires MATLAB. |
| [Qinxiaoye/<br>VEM-spcae-time-dynamic](https://github.com/Qinxiaoye/VEM-spcae-time-dynamic) | Space-time VEM for elastodynamics. | MATLAB | none found | Requires MATLAB. |
| [Qinxiaoye/<br>VEM_mechanics2D](https://github.com/Qinxiaoye/VEM_mechanics2D) | Teaching code for VEM in 2D linear elasticity, with a theory note. | MATLAB | none found | Requires MATLAB. |
| [Qinxiaoye/<br>VEM_Poisson](https://github.com/Qinxiaoye/VEM_Poisson) | Introductory 2D VEM code with a theory note. | MATLAB | none found | Solves the Poisson equation, not elasticity. |
| [Qinxiaoye/<br>VEMbook](https://github.com/Qinxiaoye/VEMbook) | VEM teaching scripts, including a 1D truss. | MATLAB | none found | Sparse documentation. |
| [Qinxiaoye/<br>VEMdynamic_Newmark](https://github.com/Qinxiaoye/VEMdynamic_Newmark) | VEM for 2D linear elastodynamics with Newmark time integration. | MATLAB | none found | Requires MATLAB. |
| [Qinxiaoye/<br>VEMpiezo](https://github.com/Qinxiaoye/VEMpiezo) | VEM for 2D piezoelasticity. | MATLAB | none found | Requires MATLAB. |
| [redcican/<br>vem-concurrent-topopt](https://github.com/redcican/vem-concurrent-topopt) | Concurrent multiscale topology optimization with VEM on polygonal and polyhedral meshes. | Python | MIT |  |
| [SINTEF-AppliedCompSci/<br>MRST](https://github.com/SINTEF-AppliedCompSci/MRST/tree/main/solvers/vemmech) | VEM mechanics module of the MATLAB Reservoir Simulation Toolbox. | MATLAB | GPL-3.0 | Part of a larger toolbox. |
| [Terenceyuyue/<br>mVEM](https://github.com/Terenceyuyue/mVEM) | MATLAB package of virtual element methods published in the literature. | MATLAB | GPL-3.0 | Requires MATLAB. |
| [tytrusty/<br>Shape-Matching-Element-Method](https://github.com/tytrusty/Shape-Matching-Element-Method) | Shape-matching VEM for direct simulation of CAD models. | C | none found |  |
| [yanpeng-gong/<br>FeVeCoupled-ElectronicPackaging](https://github.com/yanpeng-gong/FeVeCoupled-ElectronicPackaging) | Coupled finite and virtual element analysis of multiscale electronic packaging structures. | MATLAB | MIT | Requires MATLAB. |
| [yanpeng-gong/<br>VEM-electronic-packaging](https://github.com/yanpeng-gong/VEM-electronic-packaging) | Standard and stabilization-free VEM for thermomechanical analysis of electronic packaging. | MATLAB | MIT (README badge) | Requires MATLAB; no license file. |
| [ZhouRuopu/<br>GNE-VEM](https://github.com/ZhouRuopu/GNE-VEM) | Graph neural network approach to VEM stabilization. | Python | none found |  |

</details>

<details>
<summary><h2>Third medium contact</h2></summary>
<p id="open-third-medium-contact"><sub><b>Third medium contact</b> · <a href="#contents">Back to contents</a></sub></p>

Third medium contact (TMC) models contact by meshing the gap with a very compliant fictitious material. Some links open the relevant file inside a larger project. DTU's MATLAB TopTMC code is not in a repository and can be downloaded from the [TopOpt software page](https://www.topopt.mek.dtu.dk/apps-and-software).

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [adtzlr/<br>felupe](https://github.com/adtzlr/felupe/blob/main/examples/ex20_third-medium-contact.py) | Third medium contact example in the FElupe nonlinear finite element package. | Python | GPL-3.0 |  |
| [charlieaveline/<br>TMC_Firedrake](https://github.com/charlieaveline/TMC_Firedrake) | Minimal unit-cell forward solve with third medium contact and multiscale virtual power. | Python | MIT |  |
| [chennachaos/<br>FEniCSx-TMC](https://github.com/chennachaos/FEniCSx-TMC) | Attempt at third medium contact in FEniCSx. | Python | GPL-3.0 | Author reports it did not work for the paper's parameters. |
| [deepmodeling/<br>jax-fem](https://github.com/deepmodeling/jax-fem/tree/main/applications/third_medium_contact) | Third medium contact application in JAX-FEM. | Python | GPL-3.0 |  |
| [fenics-dolfiny/<br>dolfiny](https://github.com/fenics-dolfiny/dolfiny/tree/main/demo/tmc) | Third medium contact demo built on FEniCSx. | Python | LGPL-3.0 |  |
| [idaholab/<br>moose](https://github.com/idaholab/moose/blob/next/modules/solid_mechanics/doc/content/source/kernels/SecondDerivativeRegularization.md) | HuHu, LuLu and HuHu-LuLu regularization kernels for solid mechanics. | C++ | LGPL-2.1 | Regularization component, not a complete contact example. |
| [IMTEK-Simulation/<br>muFFTTO](https://github.com/IMTEK-Simulation/muFFTTO/tree/main/examples/internal_contact) | Internal contact by third medium in an FFT-based microstructure optimization code. | Python | MIT |  |
| [LuoXueling/<br>optimization_of_digital_material_distribution](https://github.com/LuoXueling/optimization_of_digital_material_distribution/blob/main/main_semisphere_dist_opt_tmc.py) | Multimaterial distribution optimization with a third medium contact example. | Python | MIT |  |
| [MechEngrLorenzoFiore/<br>FEA_studies](https://github.com/MechEngrLorenzoFiore/FEA_studies/tree/main/Third_medium_contact) | Study script based on the 2024 paper by Faltus, Horak, Doskar and Rokos. | Python | MIT | Learning project. |
| [meyer-nils/<br>torch-fem](https://github.com/meyer-nils/torch-fem/blob/main/examples/basic/planar/third_medium_contact.ipynb) | Third medium contact example in a differentiable PyTorch finite element solver. | Python | MIT |  |
| [MultiSimOLab/<br>HyperFEM.jl](https://github.com/MultiSimOLab/HyperFEM.jl/blob/main/test/SimulationsTests/ThirdMediumContactSimulation.jl) | Third medium contact simulation in a hyperelastic multiphysics library. | Julia | MIT | Provided as a test, not a tutorial. |
| [Naruki-Ichihara/<br>feax](https://github.com/Naruki-Ichihara/feax/blob/main/feax/mechanics/tmc.py) | Third medium contact module in a JAX finite element engine, with 2D and 3D examples. | Python | GPL-3.0 |  |
| [stefanhiemer/<br>topoptlab](https://github.com/stefanhiemer/topoptlab/tree/main/examples/fem/third_medium_contact) | C-shape contact example in a topology optimization library. | Python | GPL-3.0 |  |

</details>

<details>
<summary><h2>Meshfree and particle methods</h2></summary>
<p id="open-meshfree-and-particle-methods"><sub><b>Meshfree and particle methods</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [adevaucorbeil/<br>karamelo](https://github.com/adevaucorbeil/karamelo) | Parallel material point method simulator with CPU and GPU support. | C++ | GPL-2.0 | GPU support is on a separate branch. |
| [bcolloran/<br>tlmpm](https://github.com/bcolloran/tlmpm) | Teaching implementation of the total Lagrangian material point method in Taichi. | Python | none found |  |
| [cb-geo/<br>mpm](https://github.com/cb-geo/mpm) | High-performance material point method code for computational geomechanics. | C++ | MIT |  |
| [iwf-inspire/<br>mfree_iwf](https://github.com/iwf-inspire/mfree_iwf) | Comparison of meshless methods for large-deformation elastodynamics. | C++ | GPL-3.0 | Paper code. |
| [JinshuaiBai/<br>RPIM_NNS](https://github.com/JinshuaiBai/RPIM_NNS) | Radial point interpolation meshless method with neural network solvers. | MATLAB | none found | Requires MATLAB. |
| [peridigm/<br>peridigm](https://github.com/peridigm/peridigm) | Parallel peridynamics code for solid mechanics with material failure. | C++ | BSD-3-Clause |  |
| [pypr/<br>pysph](https://github.com/pypr/pysph) | Smoothed particle hydrodynamics framework with OpenMP, OpenCL and MPI support. | Python | BSD-3-Clause | Some directories may carry other licenses. |
| [saullocastro/<br>meshless](https://github.com/saullocastro/meshless) | Meshless methods for computational mechanics, including ES-PIM. | Python | BSD-2-Clause |  |
| [taichi-dev/<br>mpm_3d_exercise](https://github.com/taichi-dev/mpm_3d_exercise) | Exercise for writing a 3D material point method, with a 2D reference implementation. | Python | MIT | Starter code with the main step left blank; yuanming-hu is a collaborator. |
| [taichi-dev/<br>taichi_elements](https://github.com/taichi-dev/taichi_elements) | Multi-material MPM engine for elastic solids, water, snow and sand in Taichi. | Python | MIT | README describes it as work in progress; yuanming-hu is a collaborator. |
| [Xiangyu-Hu/<br>SPHinXsys](https://github.com/Xiangyu-Hu/SPHinXsys) | SPH-based multiphysics library for coupled simulation and optimization. | C++ | Apache-2.0 |  |
| [yade-dev/<br>trunk](https://gitlab.com/yade-dev/trunk) | Framework for the discrete element method. | C++ and Python | GPL-2.0-or-later |  |
| [yhtang/<br>OpenRBC](https://github.com/yhtang/OpenRBC) | Coarse-grained particle simulator of red blood cells at protein resolution. | C++ | GPL-3.0 | lululxvi is a collaborator. |
| [yuanming-hu/<br>GPUMPM](https://github.com/yuanming-hu/GPUMPM) | GPU-optimized material point method from a SIGGRAPH Asia 2018 paper. |  | GPL-3.0 | README asks commercial users to contact the authors. |
| [yuanming-hu/<br>taichi_dem_mid_autumn](https://github.com/yuanming-hu/taichi_dem_mid_autumn) | Minimal discrete element method demo in Taichi. | Python | MIT |  |
| [yuanming-hu/<br>taichi_mpm](https://github.com/yuanming-hu/taichi_mpm) | MLS-MPM solver with cutting and two-way rigid body coupling. | C++ | MIT |  |

</details>

<details>
<summary><h2>Soft-body, real-time and differentiable simulation</h2></summary>
<p id="open-soft-body-real-time-and-differentiable-simulation"><sub><b>Soft-body, real-time and differentiable simulation</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [hzaskywalker/<br>PlasticineLab](https://github.com/hzaskywalker/PlasticineLab) | Differentiable physics benchmark for soft-body manipulation. | Python | none found | Only some bundled algorithm folders have license files. |
| [InteractiveComputerGraphics/<br>PositionBasedDynamics](https://github.com/InteractiveComputerGraphics/PositionBasedDynamics) | Position-based simulation of rigid bodies, deformable solids and fluids. | C++ | MIT |  |
| [ipc-sim/<br>IPC](https://github.com/ipc-sim/IPC) | Reference implementation of Incremental Potential Contact for large-deformation elastodynamics. | C++ | MIT |  |
| [jinaojakezhang/<br>DJTLED](https://github.com/jinaojakezhang/DJTLED) | Direct-Jacobian explicit dynamics finite elements for real-time hyperelastic simulation. | C++ | MIT |  |
| [NVlabs/<br>DiSECt](https://github.com/NVlabs/DiSECt) | Differentiable finite element simulator for robotic cutting of deformable materials. | Python | NVIDIA Source Code License (non-commercial) | Code and dataset are restricted to non-commercial use. |
| [Q-Minh/<br>position-based-dynamics](https://github.com/Q-Minh/position-based-dynamics) | Academic prototype of soft-body simulation with extended position-based dynamics. | C++ | BSL-1.0 |  |
| [sofa-framework/<br>sofa](https://github.com/sofa-framework/sofa) | Interactive finite element physics framework for medical simulation and robotics. | C++ | LGPL-2.1 |  |
| [SofaDefrost/<br>CondensedFEMModel](https://github.com/SofaDefrost/CondensedFEMModel) | Learned condensed finite element models for soft robot control and design. | Python | GPL-3.0 | Requires SOFA. |
| [SofaDefrost/<br>SoftRobots](https://github.com/SofaDefrost/SoftRobots) | SOFA components for modeling, actuating and controlling soft robots. | C++ | LGPL-3.0 | Requires SOFA. |
| [taichi-dev/<br>difftaichi](https://github.com/taichi-dev/difftaichi) | Examples of differentiable physical simulators written in Taichi. |  | none found |  |
| [taichi-dev/<br>taichi](https://github.com/taichi-dev/taichi) | Parallel programming language in Python for simulation on CPUs and GPUs. | C++ | Apache-2.0 |  |
| [x9m/<br>DJTLED_fast](https://github.com/x9m/DJTLED_fast) | Speed-optimized DJ-TLED soft-tissue solver, with Jinao Zhang's original solver for comparison. | C++ | MIT | **By the list maintainer.** Derived from jinaojakezhang/DJTLED; developed and tested on macOS. |
| [x9m/<br>JANP-DJTLED-GPU](https://github.com/x9m/JANP-DJTLED-GPU) | DJTLED with average nodal pressure for nearly incompressible soft tissue, on CPU and GPU. | C++ and CUDA | MIT | **By the list maintainer.** Builds on Jinao Zhang's DJTLED; the GPU solver needs an NVIDIA GPU. |
| [Xingyu-Lin/<br>softgym](https://github.com/Xingyu-Lin/softgym) | Deformable object manipulation benchmarks for cloth, rope and fluid. | C++ | BSD-3-Clause | Depends on NVIDIA FleX. |

</details>

<details>
<summary><h2>Multibody dynamics and biomechanics</h2></summary>
<p id="open-multibody-dynamics-and-biomechanics"><sub><b>Multibody dynamics and biomechanics</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [google-deepmind/<br>mujoco](https://github.com/google-deepmind/mujoco) | Multibody dynamics engine with contact and deformable bodies. | C++ | Apache-2.0 |  |
| [newton-physics/<br>newton](https://github.com/newton-physics/newton) | GPU-accelerated physics engine for robotics and simulation research. | Python | Apache-2.0 |  |
| [opensim-org/<br>opensim-core](https://github.com/opensim-org/opensim-core) | Musculoskeletal modeling and dynamic simulation of movement. | C++ | Apache-2.0 |  |
| [projectchrono/<br>chrono](https://github.com/projectchrono/chrono) | Multiphysics engine for rigid, deformable and granular system dynamics. | C++ | BSD-3-Clause |  |

</details>

<details>
<summary><h2>Constitutive modeling and material identification</h2></summary>
<p id="open-constitutive-modeling-and-material-identification"><sub><b>Constitutive modeling and material identification</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [abuganza/<br>NN_aniso_UMAT](https://github.com/abuganza/NN_aniso_UMAT) | Neural network models of anisotropic hyperelastic materials, with a UMAT. | Jupyter Notebook | GPL-3.0 | Abaqus for the UMAT. |
| [BinChenOPEN/<br>FEMU-DIC](https://github.com/BinChenOPEN/FEMU-DIC) | Digital image correlation and finite element model updating for strain measurement and parameter identification. | MATLAB | GPL-3.0 | Requires MATLAB and COMSOL. |
| [EUCLID-code/<br>EUCLID-hyperelasticity](https://github.com/EUCLID-code/EUCLID-hyperelasticity) | Unsupervised discovery of hyperelastic strain energy functions from full-field displacement data. | HTML | GPL-3.0 |  |
| [EUCLID-code/<br>EUCLID-hyperelasticity-bayesian](https://github.com/EUCLID-code/EUCLID-hyperelasticity-bayesian) | Bayesian discovery of hyperelastic laws with uncertainty. | HTML | GPL-3.0 |  |
| [EUCLID-code/<br>EUCLID-hyperelasticity-NN](https://github.com/EUCLID-code/EUCLID-hyperelasticity-NN) | Neural network hyperelasticity learned without stress data. | HTML | GPL-3.0 |  |
| [EUCLID-code/<br>EUCLID-hyperelasticity-PlaneStress-ExperimentalData](https://github.com/EUCLID-code/EUCLID-hyperelasticity-PlaneStress-ExperimentalData) | Discovery of plane-stress hyperelastic laws from experimental data. | Python | none found |  |
| [EUCLID-code/<br>EUCLID-plasticity](https://github.com/EUCLID-code/EUCLID-plasticity) | Discovery of plasticity and generalized standard material models without stress data. | HTML | GPL-3.0 |  |
| [EUCLID-code/<br>EUCLID-plasticity-pressure-sensitive-non-associated](https://github.com/EUCLID-code/EUCLID-plasticity-pressure-sensitive-non-associated) | Discovery of non-associated pressure-sensitive plasticity models. | MATLAB | none found |  |
| [EUCLID-code/<br>EUCLID-viscoelasticity](https://github.com/EUCLID-code/EUCLID-viscoelasticity) | Automated identification of linear viscoelastic laws. | MATLAB | GPL-3.0 |  |
| [FuhgJan/<br>ExtremeSparsificationConstitutiveLaws](https://github.com/FuhgJan/ExtremeSparsificationConstitutiveLaws) | Sparse physics-augmented neural networks for interpretable constitutive laws. | Python | GPL (stated in README) |  |
| [FuhgJan/<br>invariant_DD_CM](https://github.com/FuhgJan/invariant_DD_CM) | Space-filling sampling of invariant space for data-driven constitutive models. | MATLAB | conflicting statements | README states both GPL-3.0 and a non-commercial Creative Commons license. |
| [FuhgJan/<br>modelDataDriven_YieldFunction](https://github.com/FuhgJan/modelDataDriven_YieldFunction) | Hybrid model-data-driven yield functions. | Python | conflicting statements | README states both GPL-3.0 and a non-commercial Creative Commons license. |
| [hyoungsuksuh/<br>ABAQUS_NN](https://github.com/hyoungsuksuh/ABAQUS_NN) | PyTorch-to-UMAT framework for deep-learning level-set plasticity. | Python | none found | Requires Abaqus. |
| [jgomezc1/<br>ABAQUS-US](https://github.com/jgomezc1/ABAQUS-US) | User element and user material subroutines, including classical and Cosserat elements. | Fortran | MIT | Requires Abaqus. |
| [jpsferreira/<br>UMAT-ABAQUS](https://github.com/jpsferreira/UMAT-ABAQUS) | Fortran framework for large-deformation material models, aimed at soft tissues and cells. | Fortran | GPL-3.0 | README invites non-commercial use, although the license is GPL-3.0. |
| [LivingMatterLab/<br>CANN](https://github.com/LivingMatterLab/CANN) | Constitutive artificial neural networks for automated material model discovery. | Jupyter Notebook | none found |  |
| [lululxvi/<br>deep-learning-for-indentation](https://github.com/lululxvi/deep-learning-for-indentation) | Extraction of material properties from instrumented indentation with deep learning. | Python | Apache-2.0 | Depends on DeepXDE. |
| [meghbali/<br>ANNElastoplasticity](https://github.com/meghbali/ANNElastoplasticity) | Neural network approach to elastoplastic constitutive modeling. | Python | MIT |  |
| [pantale/<br>ANN-ConstitutiveLaw](https://github.com/pantale/ANN-ConstitutiveLaw) | Neural network flow laws for metals, implemented as VUHARD subroutines. | Jupyter Notebook | none found | Abaqus/Explicit for the subroutines. |
| [SofaDefrost/<br>SofaViscoElastic](https://github.com/SofaDefrost/SofaViscoElastic) | SOFA plugin for linear viscoelastic and visco-hyperelastic laws on tetrahedral meshes. | C++ | LGPL-2.1 | Requires SOFA. |
| [tajtac/<br>hypermodelcomp](https://github.com/tajtac/hypermodelcomp) | Comparison of CANN, input-convex network and neural ODE models of hyperelasticity. | Jupyter Notebook | none found |  |
| [tajtac/<br>node_diffusion](https://github.com/tajtac/node_diffusion) | Research notebooks combining neural ODE hyperelastic models with diffusion models. | Jupyter Notebook | none found | No README. |
| [tgulikers/<br>ABAQUS_ANN_constitutive_model](https://github.com/tgulikers/ABAQUS_ANN_constitutive_model) | Thesis code that trains neural network constitutive models and generates a UMAT. | Fortran | none found | Abaqus for the UMAT. |
| [thelfer/<br>tfel](https://github.com/thelfer/tfel) | TFEL and MFront, a code generator for material knowledge and behavior laws. | C++ | GPL with linking exception, or CeCILL-A |  |

</details>

<details>
<summary><h2>Multiscale and homogenization</h2></summary>
<p id="open-multiscale-and-homogenization"><sub><b>Multiscale and homogenization</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [damask-multiphysics/<br>DAMASK](https://github.com/damask-multiphysics/DAMASK) | Multiscale crystal plasticity simulation kit. | Fortran and Python | AGPL-3.0-or-later | Read-only mirror; development is at git.damask-multiphysics.org. |
| [tdegeus/<br>GooseFFT](https://github.com/tdegeus/GooseFFT) | Small teaching scripts for FFT-based micromechanical solvers. | Python | MIT |  |
| [vondrejc/<br>FFTHomPy](https://github.com/vondrejc/FFTHomPy) | FFT-based homogenization with guaranteed bounds on effective properties. | Python | MIT |  |

</details>

<details>
<summary><h2>Thermal, multiphysics and additive manufacturing</h2></summary>
<p id="open-thermal-multiphysics-and-additive-manufacturing"><sub><b>Thermal, multiphysics and additive manufacturing</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [CMSL-HKUST/<br>jax-am](https://github.com/CMSL-HKUST/jax-am) | Differentiable GPU toolbox for additive manufacturing process, structure and property simulation. | Jupyter Notebook | GPL-3.0 |  |
| [jinaojakezhang/<br>FEDFEM](https://github.com/jinaojakezhang/FEDFEM) | Fast explicit dynamics finite elements for transient heat transfer. | C++ | MIT |  |
| [jinaojakezhang/<br>FEDFEMBioheat](https://github.com/jinaojakezhang/FEDFEMBioheat) | Real-time bio-heat transfer with fast explicit dynamics finite elements. | C++ | MIT |  |
| [jinaojakezhang/<br>FEDFEMBioheatDamage](https://github.com/jinaojakezhang/FEDFEMBioheatDamage) | CEM43 thermal damage added to real-time bio-heat simulation. | C++ | MIT |  |
| [jinaojakezhang/<br>FEDFEMBioheatDeform](https://github.com/jinaojakezhang/FEDFEMBioheatDeform) | Soft tissue thermal response under deformation for surgical simulation. | C++ | MIT |  |
| [jinaojakezhang/<br>FEDFEMBioheatExpan](https://github.com/jinaojakezhang/FEDFEMBioheatExpan) | Anisotropic thermo-visco-elastodynamics of soft tissue for ablation therapy. | C++ | MIT |  |
| [precice/<br>precice](https://github.com/precice/precice) | Coupling library for partitioned multiphysics and multiscale simulation. | C++ | LGPL-3.0 |  |

</details>

<details>
<summary><h2>Optimization and inverse problems</h2></summary>
<p id="open-optimization-and-inverse-problems"><sub><b>Optimization and inverse problems</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [deng-cy/<br>deep_learning_topology_opt](https://github.com/deng-cy/deep_learning_topology_opt) | Self-directed online learning for topology optimization. | MATLAB | MIT | Most examples need MATLAB and COMSOL. |
| [gigatskhondia/<br>gigala](https://github.com/gigatskhondia/gigala) | Structural topology optimization with reinforcement learning, genetic algorithms and finite elements. | Jupyter Notebook | MIT |  |
| [Jasiuk-Research-Group/<br>DeepEnergy-TopOpt](https://github.com/Jasiuk-Research-Group/DeepEnergy-TopOpt) | Density-based topology optimization with the deep energy method. | Python | none found |  |
| [Jasiuk-Research-Group/<br>LatticeOPT](https://github.com/Jasiuk-Research-Group/LatticeOPT) | Heuristic topology optimization of thin-walled lattice structures. | Python | MIT | Requires Abaqus/Explicit. |
| [kailaix/<br>PhysGNN](https://github.com/kailaix/PhysGNN) | Physics-constrained generative networks, including a stochastic elasticity example. | Julia | none found |  |
| [nandakishorebm1995/<br>FOR3022_Code](https://github.com/nandakishorebm1995/FOR3022_Code) | Bayesian damage identification in fiber metal laminates with model order reduction. | MATLAB | none found | Requires MATLAB and COMSOL. |
| [topopt/<br>TopOpt_in_PETSc](https://github.com/topopt/TopOpt_in_PETSc) | Parallel large-scale 3D topology optimization with PETSc. | C++ | unclear | Includes the LGPL text, but source headers say all rights reserved. |
| [yuanming-hu/<br>spgrid_topo_opt](https://github.com/yuanming-hu/spgrid_topo_opt) | Narrow-band topology optimization on sparsely populated grids. | C++ | MIT and BSD, by component |  |

</details>

<details>
<summary><h2>Physics-informed learning and energy methods</h2></summary>
<p id="open-physics-informed-learning-and-energy-methods"><sub><b>Physics-informed learning and energy methods</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [ehsanhaghighat/<br>sciann-applications](https://github.com/ehsanhaghighat/sciann-applications) | SciANN examples, including elasticity, elastoplasticity, vibration and poroelasticity. | Jupyter Notebook | MIT | SciANN itself is unmaintained. |
| [FuhgJan/<br>mixedDEM](https://github.com/FuhgJan/mixedDEM) | Mixed deep energy method for stress concentrations in finite-strain hyperelasticity. | Python | conflicting statements | README states both GPL-3.0 and a non-commercial Creative Commons license. |
| [ISM-Weimar/<br>DeepEnergyMethods](https://github.com/ISM-Weimar/DeepEnergyMethods) | Companion code for energy-based deep learning solutions of PDEs in mechanics. | Python | MIT |  |
| [Jasiuk-Research-Group/<br>DEM_for_J2_plasticity](https://github.com/Jasiuk-Research-Group/DEM_for_J2_plasticity) | Deep energy method for 3D J2 elastoplasticity. | Python | MIT |  |
| [Jasiuk-Research-Group/<br>Graph_DEM](https://github.com/Jasiuk-Research-Group/Graph_DEM) | Comparison of graph convolution and MLP deep energy methods for elastic solids. | Python | none found |  |
| [JinshuaiBai/<br>energy_PINN_Contact](https://github.com/JinshuaiBai/energy_PINN_Contact) | Energy-based PINN for frictionless large-deformation contact. | Python | none found |  |
| [JinshuaiBai/<br>LSWR_loss_function_PINN](https://github.com/JinshuaiBai/LSWR_loss_function_PINN) | Least squares weighted residual loss for PINN solid mechanics. | Python | none found |  |
| [JinshuaiBai/<br>PINN_Comp_Mech](https://github.com/JinshuaiBai/PINN_Comp_Mech) | Introductory PINN examples in solid mechanics with collocation and energy losses. | Python | none found |  |
| [JinshuaiBai/<br>PIRBN](https://github.com/JinshuaiBai/PIRBN) | Physics-informed radial basis networks with spring, wave and viscoelastic flow examples. | Python | none found |  |
| [lululxvi/<br>deepxde](https://github.com/lululxvi/deepxde) | Library for physics-informed learning of forward and inverse differential equation problems. | Python | LGPL-2.1 |  |
| [MinhNguyenIKM/<br>dem_hyperelasticity](https://github.com/MinhNguyenIKM/dem_hyperelasticity) | Deep energy method for finite-deformation hyperelasticity. | Python | none found |  |
| [Raocp/<br>PINN-elastodynamics](https://github.com/Raocp/PINN-elastodynamics) | Physics-informed networks for elastodynamics without labeled data. | Python | none found |  |
| [yizheng-wang/<br>Research-on-Solving-Partial-Differential-Equations-of-Solid-Mechanics-Based-on-PINN](https://github.com/yizheng-wang/Research-on-Solving-Partial-Differential-Equations-of-Solid-Mechanics-Based-on-PINN) | Thesis code for solid mechanics with deep energy, CENN, DCEM and KINN methods. | Python | none found |  |

</details>

<details>
<summary><h2>Surrogates and reduced-order models</h2></summary>
<p id="open-surrogates-and-reduced-order-models"><sub><b>Surrogates and reduced-order models</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [AlbanOdot/<br>DeepPhysics-article](https://github.com/AlbanOdot/DeepPhysics-article) | Paper code for physics-aware deep learning in real-time simulation. | Python | CC0-1.0 |  |
| [dabiriyaghoub/<br>Ventricular_ML_DecisionTrees](https://github.com/dabiriyaghoub/Ventricular_ML_DecisionTrees) | Machine learning prediction of left ventricular mechanics. | Python | all rights reserved |  |
| [farazarbabi/<br>CNN_FEM](https://github.com/farazarbabi/CNN_FEM) | Convolutional network prediction of stress fields in solids from simulation data. | Python | none found |  |
| [federicosanna/<br>UNet-for-FEM-and-Stress-Distribution-Inference](https://github.com/federicosanna/UNet-for-FEM-and-Stress-Distribution-Inference) | U-Net inference of stress distributions from finite element data. | Python | none found | Some trained models are not included. |
| [hmjeon/<br>FEM-ML](https://github.com/hmjeon/FEM-ML) | Experiments in finite element analysis with machine learning. | Jupyter Notebook | GPL-3.0 | Sparse documentation. |
| [Jasiuk-Research-Group/<br>Bio-inspired-low-porosity-structures-using-Neural-Networks-GRU-Implemenation](https://github.com/Jasiuk-Research-Group/Bio-inspired-low-porosity-structures-using-Neural-Networks-GRU-Implemenation) | Recurrent network prediction of stress-strain response and energy absorption in bio-inspired structures. | Python | MIT |  |
| [Jasiuk-Research-Group/<br>CMDS-14-impact-resistantance-NN-prediction-](https://github.com/Jasiuk-Research-Group/CMDS-14-impact-resistantance-NN-prediction-) | Neural networks for structure-property relations in impact-resistant structures. | PureBasic | none found |  |
| [Jasiuk-Research-Group/<br>LatticeResponse_NN_Prediction](https://github.com/Jasiuk-Research-Group/LatticeResponse_NN_Prediction) | Recurrent network prediction of lattice stress-strain curves and energy absorption. | Python | none found |  |
| [Jasiuk-Research-Group/<br>ResUNet-DeepONet-Plasticity](https://github.com/Jasiuk-Research-Group/ResUNet-DeepONet-Plasticity) | Operator network prediction of plastic stress fields on varying geometries. | Python | MIT |  |
| [Jasiuk-Research-Group/<br>S-DeepONet](https://github.com/Jasiuk-Research-Group/S-DeepONet) | Sequential operator network with plasticity and heat transfer examples. | Python | none found |  |
| [Jasiuk-Research-Group/<br>S-DeepONet-transient-predictions](https://github.com/Jasiuk-Research-Group/S-DeepONet-transient-predictions) | Sequential operator network for transient full-field predictions, including plasticity. | Python | none found |  |
| [Jianxun-Wang/<br>graphGalerkin](https://github.com/Jianxun-Wang/graphGalerkin) | Physics-informed graph neural Galerkin networks for forward and inverse PDE problems. | Python | GPL-3.0 | Requires pyCaMOtk. |
| [lawsonfulton/<br>AutoDef](https://github.com/lawsonfulton/AutoDef) | Latent-space dynamics for reduced deformable simulation. | C++ | MIT | Install script can overwrite your Keras configuration. |
| [lrquad/<br>NNWarp](https://github.com/lrquad/NNWarp) | Neural network-based nonlinear deformable simulator. | C++ | MIT |  |
| [m-ulmestrand/<br>gcn-collisions](https://github.com/m-ulmestrand/gcn-collisions) | Graph convolutional network that learns particle collision responses. | Python | Apache-2.0 |  |
| [michetonu/<br>MALTIDEM--Machine-Learning-for-Tissue-Deformation-Modelling](https://github.com/michetonu/MALTIDEM--Machine-Learning-for-Tissue-Deformation-Modelling) | Data-driven real-time model of brain tumor deformation for neurosurgery. | MATLAB | none found | Workflow uses MATLAB and FEBio. |
| [mimesis-inria/<br>DeepPhysX](https://github.com/mimesis-inria/DeepPhysX) | Interface between numerical simulations and learning algorithms for training and prediction. | Python | AGPL-3.0 |  |
| [oleksiyskononenko/<br>mlfem](https://github.com/oleksiyskononenko/mlfem) | Notebook and report on deep learning with finite element models of physical systems. | Jupyter Notebook | none found |  |
| [saurabhdeshpande93/<br>convolution-aggregation-attention](https://github.com/saurabhdeshpande93/convolution-aggregation-attention) | CNN, graph and attention surrogates for nonlinear finite element simulations. | Mathematica | MIT | Data generation uses AceFEM. |
| [TML-Gatech/<br>DL_Stress_TAA](https://github.com/TML-Gatech/DL_Stress_TAA) | Deep learning surrogate of finite element stress analysis. |  | all rights reserved | Source files are supplied as PDFs. |
| [vividda/<br>3D-PhysNet](https://github.com/vividda/3D-PhysNet) | Learned prediction of non-rigid 3D object deformation. | Python | none found | Python 2.7. |
| [wwMark/<br>meshgraphnets](https://github.com/wwMark/meshgraphnets) | PyTorch port of MeshGraphNets with cloth simulation. | Python | none found | Author says results do not fully match the original. |
| [YasminSalehi/<br>PhysGNN](https://github.com/YasminSalehi/PhysGNN) | Graph neural network prediction of soft tissue deformation in neurosurgery. | Python | BSD-4-Clause |  |
| [zhenguonie/<br>stress_net](https://github.com/zhenguonie/stress_net) | Convolutional prediction of stress fields in cantilevered structures. | Python | none found |  |

</details>

<details>
<summary><h2>Meshing, pre- and post-processing</h2></summary>
<p id="open-meshing-pre--and-post-processing"><sub><b>Meshing, pre- and post-processing</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [gmsh/<br>gmsh](https://gitlab.onelab.info/gmsh/gmsh) | 3D finite element mesh generator with pre- and post-processing. | C++ | GPL-2.0-or-later with linking exception |  |
| [inducer/<br>meshpy](https://github.com/inducer/meshpy) | Python interfaces to the Triangle and TetGen mesh generators. | C++ | mixed, including Triangle and AGPL-3.0 | Triangle restricts commercial distribution. |
| [Kitware/<br>ParaView](https://github.com/Kitware/ParaView) | Parallel data analysis and visualization application built on VTK. | C++ | BSD-3-Clause |  |
| [Liujie-SYSU/<br>odb2vtk](https://github.com/Liujie-SYSU/odb2vtk) | Converter from Abaqus ODB results to VTK for ParaView. | Python | none found | Input is Abaqus output. |
| [meshpro/<br>meshplex](https://github.com/meshpro/meshplex) | Geometric quantities such as areas and volumes for simplex meshes. |  | proprietary | No source in the repository; full use requires a paid license. |
| [meshpro/<br>meshzoo](https://github.com/meshpro/meshzoo) | Generators of meshes for simple canonical domains. |  | none found | No source in the repository. |
| [meshpro/<br>pygalmesh](https://github.com/meshpro/pygalmesh) | Python front end to CGAL's 2D and 3D mesh generators. | C++ | GPL-3.0 | Commercial license offered separately. |
| [mikedh/<br>trimesh](https://github.com/mikedh/trimesh) | Python library for loading, editing and analyzing triangular meshes. | Python | MIT |  |
| [NGSolve/<br>netgen](https://github.com/NGSolve/netgen) | Automatic 3D tetrahedral mesh generator. | C++ | LGPL-2.1 |  |
| [nschloe/<br>meshio](https://github.com/nschloe/meshio) | Reader, writer and converter for many mesh file formats. | Python | MIT |  |
| [nschloe/<br>pygmsh](https://github.com/nschloe/pygmsh) | Python abstractions for building geometries and meshes with Gmsh. | Python | GPL-3.0 |  |
| [paulo-herrera/<br>PyEVTK](https://github.com/paulo-herrera/PyEVTK) | Pure-Python export of data to binary VTK files. | Python | MIT (stated in source) |  |
| [pyvista/<br>pyvista](https://github.com/pyvista/pyvista) | 3D visualization and mesh analysis with a NumPy-based interface. | Python | MIT |  |
| [Qinxiaoye/<br>geometry](https://github.com/Qinxiaoye/geometry) | Sample CAD and surface geometry files, including torsion, hook, bunny and wind turbine models. |  | none found | Geometry only, no code or README; model origins are undocumented. |
| [wildmeshing/<br>fTetWild](https://github.com/wildmeshing/fTetWild) | Fast and robust tetrahedral meshing of imperfect input geometry. | C++ | MPL-2.0 |  |

</details>

<details>
<summary><h2>Courses, references and agents for mechanics</h2></summary>
<p id="open-courses-references-and-agents-for-mechanics"><sub><b>Courses, references and agents for mechanics</b> · <a href="#contents">Back to contents</a></sub></p>

| Name | Descriptions | Languages | License | Note |
| --- | --- | --- | --- | --- |
| [Ceyron/<br>machine-learning-and-simulation](https://github.com/Ceyron/machine-learning-and-simulation) | Notes and code for a video course on simulation and machine learning, including continuum mechanics and FEniCS. | Jupyter Notebook | MIT |  |
| [lamm-mit/<br>MechAgents](https://github.com/lamm-mit/MechAgents) | Multi-agent language model workflows for solving mechanics problems numerically. | Jupyter Notebook | Apache-2.0 |  |
| [ltt1598/<br>GAMES_Xi-an_forward_physics](https://github.com/ltt1598/GAMES_Xi-an_forward_physics) | Notes and Taichi sample code from a physically based simulation course. |  | none found |  |
| [matthias-research/<br>pages](https://github.com/matthias-research/pages/tree/master/tenMinutePhysics) | Ten Minute Physics tutorials on soft bodies, cloth, collisions and other simulation methods. | JavaScript | MIT (stated in source) |  |
| [nschloe/<br>awesome-scientific-computing](https://github.com/nschloe/awesome-scientific-computing) | Curated list of scientific computing tools, including finite element and meshing software. | Python | CC0-1.0 |  |
| [thunil/<br>Physics-Based-Deep-Learning](https://github.com/thunil/Physics-Based-Deep-Learning) | Curated list of research on physics-based deep learning. |  | none found |  |

</details>

## Contributing

Corrections and additions are welcome. See [contributing.md](contributing.md).
