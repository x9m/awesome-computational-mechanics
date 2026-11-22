# 1. Finite and boundary element methods

[← Back to the main list](../README.md#contents)

- [1.1 General-purpose frameworks](#general-purpose-frameworks) (20)
- [1.2 Structural and solid mechanics solvers](#structural-and-solid-mechanics-solvers) (16)
- [1.3 Differentiable and GPU finite elements](#differentiable-and-gpu-finite-elements) (6)
- [1.4 Phase-field fracture](#phase-field-fracture) (6)
- [1.5 Fracture, boundary and scaled boundary methods](#fracture-boundary-and-scaled-boundary-methods) (5)
- [1.6 Unfitted and embedded methods](#unfitted-and-embedded-methods) (1)
- [1.7 Smoothed finite elements](#smoothed-finite-elements) (1)
- [1.8 Beams, rods and shells](#beams-rods-and-shells) (3)
- [1.9 Solver interfaces and utilities](#solver-interfaces-and-utilities) (5)
- [1.10 Teaching and compact codes](#teaching-and-compact-codes) (13)

## <a id="general-purpose-frameworks"></a>1.1 General-purpose frameworks

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

## <a id="structural-and-solid-mechanics-solvers"></a>1.2 Structural and solid mechanics solvers

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

## <a id="differentiable-and-gpu-finite-elements"></a>1.3 Differentiable and GPU finite elements

| Name, language and license | Description | Note |
| --- | --- | --- |
| [camlab-ethz/<br>TensorMesh](https://github.com/camlab-ethz/TensorMesh)<br><sub>Python</sub><br><sub>Apache-2.0</sub> | Differentiable finite element library built on PyTorch. |  |
| [deepmodeling/<br>jax-fem](https://github.com/deepmodeling/jax-fem)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Differentiable finite element package built on JAX. | README asks commercial users to contact the author. |
| [kailaix/<br>AdFem.jl](https://github.com/kailaix/AdFem.jl)<br><sub>Julia and C++</sub><br><sub>MIT</sub> | Differentiable finite element operators for inverse modeling. |  |
| [liangbright/<br>pytorch_fea_paper](https://github.com/liangbright/pytorch_fea_paper)<br><sub>Python</sub><br><sub>none found</sub> | Differentiable finite element analysis applied to human aorta biomechanics. | Paper code; the author's refactored successor is [pytorch_fea](https://github.com/liangbright/pytorch_fea). |
| [mo-hanxuan/<br>FEMcy](https://github.com/mo-hanxuan/FEMcy)<br><sub>Python</sub><br><sub>MIT</sub> | Taichi-based parallel structural finite element solver with small and large deformation. |  |
| [sandialabs/<br>optimism](https://github.com/sandialabs/optimism)<br><sub>Python</sub><br><sub>MIT</sub> | JAX finite element library that poses nonlinear solid mechanics as optimization. |  |

## <a id="phase-field-fracture"></a>1.4 Phase-field fracture

| Name, language and license | Description | Note |
| --- | --- | --- |
| [CastillonMiguel/<br>phasefieldx](https://github.com/CastillonMiguel/phasefieldx)<br><sub>Python</sub><br><sub>MIT</sub> | Phase-field simulation framework built on FEniCSx. |  |
| [ehsanhaghighat/<br>PhaseField-DSD](https://github.com/ehsanhaghighat/PhaseField-DSD)<br><sub>Java</sub><br><sub>MIT</sub> | Phase-field shear fracture using a deviatoric stress split. | Requires COMSOL. |
| [hugary1995/<br>raccoon](https://github.com/hugary1995/raccoon)<br><sub>C++</sub><br><sub>LGPL-2.1</sub> | Massively parallel phase-field fracture code built on MOOSE. |  |
| [hyoungsuksuh/<br>micropolar_<br>phasefield](https://github.com/hyoungsuksuh/micropolar_phasefield)<br><sub>Python</sub><br><sub>CC-BY-4.0</sub> | Phase-field cohesive fracture in micropolar continua with FEniCS. |  |
| [LuoXueling/<br>deal.II-phase-<br>field-fracture](https://github.com/LuoXueling/deal.II-phase-field-fracture)<br><sub>C++</sub><br><sub>MIT</sub> | Phase-field fracture in deal.II with multiphysics interfaces, adaptive meshes and MPI. | Mesh input uses Abaqus input files. |
| [nsundar/<br>PFM_UMAT_Elasto<br>Plastic](https://github.com/nsundar/PFM_UMAT_ElastoPlastic)<br><sub>Fortran</sub><br><sub>MIT</sub> | Phase-field damage in elastoplastic solids as a UMAT. | Requires Abaqus. |

## <a id="fracture-boundary-and-scaled-boundary-methods"></a>1.5 Fracture, boundary and scaled boundary methods

| Name, language and license | Description | Note |
| --- | --- | --- |
| [ChongminSong/<br>Platypus](https://github.com/ChongminSong/Platypus)<br><sub>MATLAB</sub><br><sub>none found</sub> | Code accompanying a textbook on the scaled boundary finite element method. | Written for MATLAB, Octave support not documented. |
| [nsundar/<br>cp-sbfem](https://github.com/nsundar/cp-sbfem)<br><sub>Fortran and Julia</sub><br><sub>MIT</sub> | Scaled boundary finite elements for crystal plasticity as an Abaqus UELMAT. | Requires Abaqus. |
| [Qinxiaoye/<br>SBFEM2D](https://github.com/Qinxiaoye/SBFEM2D)<br><sub>MATLAB</sub><br><sub>none found</sub> | Scaled boundary finite element method for 2D linear elasticity. | Written for MATLAB, Octave support not documented; modified from code by Chongmin Song; some files are copyright Terence Yu, with no license in this repository. |
| [ShelvanLee/<br>XFEM](https://github.com/ShelvanLee/XFEM)<br><sub>MATLAB</sub><br><sub>MIT</sub> | Extended finite element program for multiple crack propagation in 2D linear elastic solids. | Written for MATLAB, Octave support not documented. |
| [Timmmdavis/<br>CutAndDisplace](https://github.com/Timmmdavis/CutAndDisplace)<br><sub>MATLAB</sub><br><sub>GPL-3.0</sub> | Boundary element code for faults and deformation. | Runs in MATLAB, also tested in Octave with some issues; README restricts use to academia, although the license is GPL-3.0. |

## <a id="unfitted-and-embedded-methods"></a>1.6 Unfitted and embedded methods

| Name, language and license | Description | Note |
| --- | --- | --- |
| [gridap/<br>GridapEmbedded.jl](https://github.com/gridap/GridapEmbedded.jl)<br><sub>Julia</sub><br><sub>MIT</sub> | Embedded finite element methods, level sets and constructive solid geometry. |  |

## <a id="smoothed-finite-elements"></a>1.7 Smoothed finite elements

| Name, language and license | Description | Note |
| --- | --- | --- |
| [nsundar/<br>SFEM_in_Abaqus](https://github.com/nsundar/SFEM_in_Abaqus)<br><sub>Fortran and MATLAB</sub><br><sub>GPL-3.0</sub> | Strain smoothing finite elements implemented in Abaqus. | Requires Abaqus; includes MATLAB scripts. |

## <a id="beams-rods-and-shells"></a>1.8 Beams, rods and shells

| Name, language and license | Description | Note |
| --- | --- | --- |
| [precice/<br>fem-shell](https://github.com/precice/fem-shell)<br><sub>C++</sub><br><sub>LGPL-3.0</sub> | Flat shell finite element solver for coupled fluid-structure simulation. |  |
| [sofa-framework/<br>BeamAdapter](https://github.com/sofa-framework/BeamAdapter)<br><sub>C++</sub><br><sub>LGPL-2.1</sub> | Adaptive Kirchhoff rod elements for catheters, guidewires and other flexible structures. | Requires SOFA. |
| [SofaDefrost/<br>Cosserat](https://github.com/SofaDefrost/Cosserat)<br><sub>C++ and Python</sub><br><sub>LGPL-3.0</sub> | Cosserat beam models of rods, wires and needles. | Requires SOFA; source headers state LGPL-2.1-or-later. |

## <a id="solver-interfaces-and-utilities"></a>1.9 Solver interfaces and utilities

| Name, language and license | Description | Note |
| --- | --- | --- |
| [ansys/<br>pymapdl](https://github.com/ansys/pymapdl)<br><sub>Python</sub><br><sub>MIT</sub> | Python interface to the Ansys MAPDL solver. | Requires a licensed copy of Ansys. |
| [ansys/<br>pymechanical](https://github.com/ansys/pymechanical)<br><sub>Python</sub><br><sub>MIT</sub> | Python interface to Ansys Mechanical. | Requires a licensed copy of Ansys Mechanical. |
| [cristobaltapia/<br>pybaqus](https://github.com/cristobaltapia/pybaqus)<br><sub>Python</sub><br><sub>MIT</sub> | Import and post-processing of Abaqus ASCII result files without an Abaqus license. | README says it is at a very early stage. |
| [febiosoftware/<br>pyfebio](https://github.com/febiosoftware/pyfebio)<br><sub>Python</sub><br><sub>MIT</sub> | Python package for writing FEBio input and converting its results. |  |
| [lcharleux/<br>abapy](https://github.com/lcharleux/abapy)<br><sub>Python</sub><br><sub>GPL-2.0</sub> | Finite element pre- and post-processing in Python. | No README. |

## <a id="teaching-and-compact-codes"></a>1.10 Teaching and compact codes

| Name, language and license | Description | Note |
| --- | --- | --- |
| [abuganza/<br>NonlinearFEA](https://github.com/abuganza/NonlinearFEA)<br><sub>Jupyter Notebook</sub><br><sub>GPL-3.0</sub> | Course notebooks on nonlinear finite element analysis. |  |
| [AppliedMechanics-<br>EAFIT/<br>Introductory-<br>Finite-Elements](https://github.com/AppliedMechanics-EAFIT/Introductory-Finite-Elements)<br><sub>Jupyter Notebook</sub><br><sub>MIT code, CC-BY-4.0 content (stated in README)</sub> | Teaching notebooks for an introductory finite element course. |  |
| [AppliedMechanics-<br>EAFIT/<br>SolidsPy](https://github.com/AppliedMechanics-EAFIT/SolidsPy)<br><sub>Python</sub><br><sub>MIT</sub> | Simple finite element code for 2D elasticity. |  |
| [dilevin/<br>CSC417-a3-finite-<br>elements-3d](https://github.com/dilevin/CSC417-a3-finite-elements-3d)<br><sub>C++</sub><br><sub>none found</sub> | Course assignment on 3D finite element simulation of elastic objects. | Starter code for an assignment. |
| [hplgit/<br>fem-book](https://github.com/hplgit/fem-book)<br><sub>Python</sub><br><sub>MIT</sub> | Sources and examples for a book on numerical methods for variational problems. |  |
| [hplgit/<br>fenics-tutorial](https://github.com/hplgit/fenics-tutorial)<br><sub>TeX and Python</sub><br><sub>none found</sub> | Sources and example programs for the FEniCS Tutorial book. | Bundled Triangle restricts commercial distribution. |
| [jjcremmers/<br>PyFEM](https://github.com/jjcremmers/PyFEM)<br><sub>Python</sub><br><sub>MIT</sub> | Educational and research finite element code for nonlinear solid mechanics. |  |
| [largurajr/<br>FEA-Protus](https://github.com/largurajr/FEA-Protus)<br><sub>Python</sub><br><sub>none found</sub> | Teaching code for 2D plane stress and plane strain finite element analysis. | Python 2.7. |
| [Qinxiaoye/<br>FEM2D](https://github.com/Qinxiaoye/FEM2D)<br><sub>MATLAB</sub><br><sub>none found</sub> | MATLAB code for 2D finite element analysis. | Written for MATLAB, Octave support not documented; input scripts use Ansys or Abaqus. |
| [Qinxiaoye/<br>FEM2D_dynamic](https://github.com/Qinxiaoye/FEM2D_dynamic)<br><sub>MATLAB</sub><br><sub>none found</sub> | Finite element elastodynamics with Newmark time integration. | Written for MATLAB, Octave support not documented; input scripts use Ansys or Abaqus. |
| [Qinxiaoye/<br>FEM3D-C3D8-](https://github.com/Qinxiaoye/FEM3D-C3D8-)<br><sub>MATLAB</sub><br><sub>none found</sub> | MATLAB finite element code with 3D hexahedral element routines. | Written for MATLAB, Octave support not documented; README calls it 2D; input scripts use Ansys or Abaqus. |
| [Qinxiaoye/<br>xpfem](https://github.com/Qinxiaoye/xpfem)<br><sub>Python</sub><br><sub>none found</sub> | Linear elastic finite element package with quadrilateral, hexahedral and B-bar elements. |  |
| [tjfulle/<br>fem-with-python](https://github.com/tjfulle/fem-with-python)<br><sub>Python</sub><br><sub>MIT (stated in README)</sub> | Course notes, assignments and code for an introductory finite element course. |  |

[← Back to the main list](../README.md#contents)
