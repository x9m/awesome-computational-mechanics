# 3. Virtual element method

[← Back to the main list](../README.md#contents)

The virtual element method (VEM) generalizes finite elements to polygonal and polyhedral elements.

- [3.1 VEM libraries](#vem-libraries) (6)
- [3.2 Elasticity](#elasticity) (9)
- [3.3 Dynamics and fracture](#dynamics-and-fracture) (3)
- [3.4 Coupled fields and electronic packaging](#coupled-fields-and-electronic-packaging) (4)
- [3.5 Topology optimization with VEM](#topology-optimization-with-vem) (2)
- [3.6 Introductory VEM codes](#introductory-vem-codes) (6)

## <a id="vem-libraries"></a>3.1 VEM libraries

| Name, language and license | Description | Note |
| --- | --- | --- |
| [CAMLAB-UChile/<br>vemlab](https://github.com/CAMLAB-UChile/vemlab)<br><sub>MATLAB</sub><br><sub>GPL-3.0</sub> | MATLAB library for linear VEM in 2D elastostatics and Poisson problems. | Runs in MATLAB, or in Octave with small changes described in its README. |
| [cemcen/<br>Veamy](https://github.com/cemcen/Veamy)<br><sub>C++</sub><br><sub>GPL (stated in README), with restricted Triangle code</sub> | Object-oriented C++ library for VEM in 2D elastostatics and Poisson problems. | Bundled Triangle restricts commercial distribution. |
| [dune-fem/<br>dune-vem](https://gitlab.dune-project.org/dune-fem/dune-vem)<br><sub>C++ and Python</sub><br><sub>GPL-2.0-or-later</sub> | DUNE module with a range of virtual element spaces and a Python interface. |  |
| [SINTEF-AppliedComp<br>Sci/<br>MRST](https://github.com/SINTEF-AppliedCompSci/MRST/tree/main/solvers/vemmech)<br><sub>MATLAB</sub><br><sub>GPL-3.0</sub> | VEM mechanics module of the MATLAB Reservoir Simulation Toolbox. | Part of a larger toolbox that runs in MATLAB or Octave; the toolbox bundles Triangle, which restricts commercial distribution. |
| [Terenceyuyue/<br>mVEM](https://github.com/Terenceyuyue/mVEM)<br><sub>MATLAB</sub><br><sub>GPL-3.0</sub> | MATLAB package of virtual element methods published in the literature. | Written for MATLAB, Octave support not documented. |
| [tiagomhrd/<br>ves](https://github.com/tiagomhrd/ves)<br><sub>C++</sub><br><sub>MIT</sub> | Helper library of projectors for several virtual element formulations. |  |

## <a id="elasticity"></a>3.2 Elasticity

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

## <a id="dynamics-and-fracture"></a>3.3 Dynamics and fracture

| Name, language and license | Description | Note |
| --- | --- | --- |
| [MinhNguyenIKM/<br>vem](https://github.com/MinhNguyenIKM/vem)<br><sub>MATLAB</sub><br><sub>none found</sub> | VEM code for 2D linear elastic fracture. | Written for MATLAB, Octave support not documented. |
| [Qinxiaoye/<br>VEM-spcae-time-<br>dynamic](https://github.com/Qinxiaoye/VEM-spcae-time-dynamic)<br><sub>MATLAB</sub><br><sub>none found</sub> | Space-time VEM for elastodynamics. | Written for MATLAB, Octave support not documented; some files are copyright Terence Yu and Long Chen, with no license in this repository. |
| [Qinxiaoye/<br>VEMdynamic_Newmark](https://github.com/Qinxiaoye/VEMdynamic_Newmark)<br><sub>MATLAB</sub><br><sub>none found</sub> | VEM for 2D linear elastodynamics with Newmark time integration. | Written for MATLAB, Octave support not documented; some files are copyright Terence Yu and Long Chen, with no license in this repository. |

## <a id="coupled-fields-and-electronic-packaging"></a>3.4 Coupled fields and electronic packaging

| Name, language and license | Description | Note |
| --- | --- | --- |
| [aerubianoma/<br>vem_stress_<br>assisted_diffusion](https://github.com/aerubianoma/vem_stress_assisted_diffusion)<br><sub>MATLAB</sub><br><sub>GPL-3.0</sub> | Robust VEM experiments for stress-assisted diffusion in elastic materials. | Requires MATLAB, README lists R2023a. |
| [Qinxiaoye/<br>VEMpiezo](https://github.com/Qinxiaoye/VEMpiezo)<br><sub>MATLAB</sub><br><sub>none found</sub> | VEM for 2D piezoelasticity. | Written for MATLAB, Octave support not documented; some files are copyright Terence Yu, with no license in this repository. |
| [yanpeng-gong/<br>FeVeCoupled-<br>Electronic<br>Packaging](https://github.com/yanpeng-gong/FeVeCoupled-ElectronicPackaging)<br><sub>MATLAB</sub><br><sub>MIT</sub> | Coupled finite and virtual element analysis of multiscale electronic packaging structures. | Requires MATLAB. |
| [yanpeng-gong/<br>VEM-electronic-<br>packaging](https://github.com/yanpeng-gong/VEM-electronic-packaging)<br><sub>MATLAB</sub><br><sub>MIT (README badge)</sub> | Standard and stabilization-free VEM for thermomechanical analysis of electronic packaging. | Requires MATLAB; no license file. |

## <a id="topology-optimization-with-vem"></a>3.5 Topology optimization with VEM

| Name, language and license | Description | Note |
| --- | --- | --- |
| [Qinxiaoye/<br>TOPvem](https://github.com/Qinxiaoye/TOPvem)<br><sub>MATLAB</sub><br><sub>none found</sub> | Density-based topology optimization with VEM. | Written for MATLAB, Octave support not documented; some files are copyright Terence Yu, with no license in this repository. |
| [redcican/<br>vem-concurrent-<br>topopt](https://github.com/redcican/vem-concurrent-topopt)<br><sub>Python</sub><br><sub>MIT</sub> | Concurrent multiscale topology optimization with VEM on polygonal and polyhedral meshes. |  |

## <a id="introductory-vem-codes"></a>3.6 Introductory VEM codes

| Name, language and license | Description | Note |
| --- | --- | --- |
| [andrea-borio/<br>vem-<br>implementation-<br>example](https://github.com/andrea-borio/vem-implementation-example)<br><sub>MATLAB</sub><br><sub>GPL-3.0</sub> | Compact example of an optimized VEM implementation. | Written for MATLAB, Octave support not documented; solves the Poisson equation, not elasticity. |
| [deatinor/<br>VEM3D](https://github.com/deatinor/VEM3D)<br><sub>C++</sub><br><sub>none found</sub> | Master's project implementing the virtual element method in three dimensions. | Convergence scripts use MATLAB. |
| [justachetan/<br>VirtualElement<br>Methods](https://github.com/justachetan/VirtualElementMethods)<br><sub>Python</sub><br><sub>MIT</sub> | Python translation of the 50-line introductory VEM code. | Solves the Poisson equation, not elasticity. |
| [oliversutton/<br>50LinesOfVEM](https://github.com/oliversutton/50LinesOfVEM)<br><sub>MATLAB</sub><br><sub>MIT</sub> | Introductory 50-line MATLAB implementation of VEM. | Written for MATLAB, Octave support not documented; solves the Poisson equation, not elasticity. |
| [Qinxiaoye/<br>VEM_Poisson](https://github.com/Qinxiaoye/VEM_Poisson)<br><sub>MATLAB</sub><br><sub>none found</sub> | Introductory 2D VEM code with a theory note. | Written for MATLAB, Octave support not documented; solves the Poisson equation, not elasticity; some files are copyright Terence Yu, with no license in this repository. |
| [Qinxiaoye/<br>VEMbook](https://github.com/Qinxiaoye/VEMbook)<br><sub>MATLAB</sub><br><sub>none found</sub> | VEM teaching scripts, including a 1D truss. | Written for MATLAB, Octave support not documented; sparse documentation. |

[← Back to the main list](../README.md#contents)
