# 6. Meshfree and particle methods

[← Back to the main list](../README.md#contents)

- [6.1 Material point method](#material-point-method) (12)
- [6.2 Smoothed particle hydrodynamics](#smoothed-particle-hydrodynamics) (4)
- [6.3 Meshless methods](#meshless-methods) (6)
- [6.4 Peridynamics](#peridynamics) (3)
- [6.5 Discrete and coarse-grained particle models](#discrete-and-coarse-grained-particle-models) (5)

## <a id="material-point-method"></a>6.1 Material point method

| Name, language and license | Description | Note |
| --- | --- | --- |
| [adevaucorbeil/<br>karamelo](https://github.com/adevaucorbeil/karamelo)<br><sub>C++</sub><br><sub>GPL-2.0</sub> | Parallel material point method simulator with CPU and GPU support. | GPU support is on a separate branch. |
| [bcolloran/<br>tlmpm](https://github.com/bcolloran/tlmpm)<br><sub>Python</sub><br><sub>none found</sub> | Teaching implementation of the total Lagrangian material point method in Taichi. |  |
| [cb-geo/<br>mpm](https://github.com/cb-geo/mpm)<br><sub>C++</sub><br><sub>MIT</sub> | High-performance material point method code for computational geomechanics. |  |
| [cb-geo/<br>mpm-benchmarks](https://github.com/cb-geo/mpm-benchmarks)<br><sub>Jupyter Notebook</sub><br><sub>CC-BY-4.0</sub> | Benchmark cases for the CB-Geo material point method code. |  |
| [ethz-pbs21/<br>SandyFluid](https://github.com/ethz-pbs21/SandyFluid)<br><sub>Python</sub><br><sub>none found</sub> | Course project that simulates water and sand with PIC, FLIP and APIC particle-grid transfers in Taichi. | A particle-in-cell solver with a frictional yield model for sand, not a material point code; requires Taichi 0.9.0. |
| [penn-graphics-<br>research/<br>ziran2019](https://github.com/penn-graphics-research/ziran2019)<br><sub>C++</sub><br><sub>MIT</sub> | Implicit material point simulation of viscoelasticity, plasticity and fracture. | Paper code. |
| [taichi-dev/<br>mpm_3d_exercise](https://github.com/taichi-dev/mpm_3d_exercise)<br><sub>Python</sub><br><sub>MIT</sub> | Exercise for writing a 3D material point method, with a 2D reference implementation. | Starter code with the main step left blank. |
| [taichi-dev/<br>taichi_elements](https://github.com/taichi-dev/taichi_elements)<br><sub>Python</sub><br><sub>MIT</sub> | Multi-material MPM engine for elastic solids, water, snow and sand in Taichi. | README describes it as work in progress. |
| [xzhang66/<br>MPM3D-F90](https://github.com/xzhang66/MPM3D-F90)<br><sub>Fortran</sub><br><sub>none found</sub> | Simplified Fortran 90 material point code accompanying two MPM books. | Source headers carry a copyright notice without license terms. |
| [Yihao-Shi/<br>GeoTaichi](https://github.com/Yihao-Shi/GeoTaichi)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Coupled material point and discrete element simulation of geophysical problems. | Bundled components have their own licenses. |
| [yuanming-hu/<br>GPUMPM](https://github.com/yuanming-hu/GPUMPM)<br><sub>C++ and CUDA</sub><br><sub>GPL-3.0</sub> | GPU-optimized material point method from a SIGGRAPH Asia 2018 paper. | README asks commercial users to contact the authors. |
| [yuanming-hu/<br>taichi_mpm](https://github.com/yuanming-hu/taichi_mpm)<br><sub>C++</sub><br><sub>MIT</sub> | MLS-MPM solver with cutting and two-way rigid body coupling. |  |

## <a id="smoothed-particle-hydrodynamics"></a>6.2 Smoothed particle hydrodynamics

| Name, language and license | Description | Note |
| --- | --- | --- |
| [Interactive<br>ComputerGraphics/<br>SPH-Tutorial](https://github.com/InteractiveComputerGraphics/SPH-Tutorial)<br><sub>none found</sub> | Tutorial notes and slides on SPH, including deformable solids. | Documents only, no code. |
| [luchete80/<br>WeldForm](https://github.com/luchete80/WeldForm)<br><sub>C++</sub><br><sub>GPL-3.0-or-later</sub> | SPH solver for elastoplastic and thermally coupled metal forming. |  |
| [pypr/<br>pysph](https://github.com/pypr/pysph)<br><sub>Python</sub><br><sub>BSD-3-Clause</sub> | Smoothed particle hydrodynamics framework with OpenMP, OpenCL and MPI support. | Some directories may carry other licenses. |
| [Xiangyu-Hu/<br>SPHinXsys](https://github.com/Xiangyu-Hu/SPHinXsys)<br><sub>C++</sub><br><sub>Apache-2.0</sub> | SPH-based multiphysics library for coupled simulation and optimization. |  |

## <a id="meshless-methods"></a>6.3 Meshless methods

| Name, language and license | Description | Note |
| --- | --- | --- |
| [iwf-inspire/<br>mfree_iwf](https://github.com/iwf-inspire/mfree_iwf)<br><sub>C++</sub><br><sub>GPL-3.0</sub> | Comparison of meshless methods for large-deformation elastodynamics. | Paper code. |
| [iwf-inspire/<br>mfree_iwf-ul-cut-<br>refine](https://github.com/iwf-inspire/mfree_iwf-ul-cut-refine)<br><sub>C++</sub><br><sub>GPL-3.0</sub> | Updated Lagrangian meshfree metal cutting with dynamic refinement. | Paper code. |
| [JinshuaiBai/<br>RPIM_NNS](https://github.com/JinshuaiBai/RPIM_NNS)<br><sub>MATLAB</sub><br><sub>none found</sub> | Radial point interpolation meshless method with neural network solvers. | Requires MATLAB. |
| [saullocastro/<br>meshless](https://github.com/saullocastro/meshless)<br><sub>Python</sub><br><sub>BSD-2-Clause</sub> | Meshless methods for computational mechanics, including ES-PIM. |  |
| [SlicerCBM/<br>SlicerCBM](https://github.com/SlicerCBM/SlicerCBM)<br><sub>Python</sub><br><sub>BSD-3-Clause</sub> | 3D Slicer extension for patient-specific biomechanics, with a meshless TLED (MTLED) simulator. | Requires 3D Slicer; some external solvers are GPL. |
| [treverhines/<br>RBF](https://github.com/treverhines/RBF)<br><sub>Python and Cython</sub><br><sub>MIT</sub> | Radial basis function tools for scattered-data interpolation and RBF-FD solution of PDEs on irregular domains, with elasticity examples. |  |

## <a id="peridynamics"></a>6.4 Peridynamics

| Name, language and license | Description | Note |
| --- | --- | --- |
| [kaipartmann/<br>Peridynamics.jl](https://github.com/kaipartmann/Peridynamics.jl)<br><sub>Julia</sub><br><sub>MIT</sub> | Parallel peridynamics with several formulations and multibody contact. |  |
| [peridigm/<br>peridigm](https://github.com/peridigm/peridigm)<br><sub>C++</sub><br><sub>BSD-3-Clause</sub> | Parallel peridynamics code for solid mechanics with material failure. |  |
| [PeriHub/<br>PeriLab.jl](https://github.com/PeriHub/PeriLab.jl)<br><sub>Julia</sub><br><sub>BSD-3-Clause</sub> | Peridynamics laboratory for a range of material and fracture problems. |  |

## <a id="discrete-and-coarse-grained-particle-models"></a>6.5 Discrete and coarse-grained particle models

| Name, language and license | Description | Note |
| --- | --- | --- |
| [idaholab/<br>LIGGGHTS-INL](https://github.com/idaholab/LIGGGHTS-INL)<br><sub>C++</sub><br><sub>GPL-2.0</sub> | Extended version of the LIGGGHTS discrete element code. |  |
| [projectchrono/<br>DEM-Engine](https://github.com/projectchrono/DEM-Engine)<br><sub>C++ and CUDA</sub><br><sub>BSD-3-Clause</sub> | GPU discrete element solver with complex grain geometry. | Requires an NVIDIA GPU. |
| [YADE](https://gitlab.com/yade-dev/trunk)<br><sub>C++ and Python</sub><br><sub>GPL-2.0-or-later</sub> | Framework for the discrete element method. |  |
| [yhtang/<br>OpenRBC](https://github.com/yhtang/OpenRBC)<br><sub>C++</sub><br><sub>GPL-3.0</sub> | Coarse-grained particle simulator of red blood cells at protein resolution. |  |
| [yuanming-hu/<br>taichi_dem_mid_<br>autumn](https://github.com/yuanming-hu/taichi_dem_mid_autumn)<br><sub>Python</sub><br><sub>MIT</sub> | Minimal discrete element method demo in Taichi. |  |

[← Back to the main list](../README.md#contents)
