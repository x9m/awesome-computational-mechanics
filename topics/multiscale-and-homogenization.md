# 10. Multiscale and homogenization

[← Back to the main list](../README.md#contents)

- [10.1 FFT-based homogenization](#fft-based-homogenization) (3)
- [10.2 FE² and computational homogenization](#fe2-and-computational-homogenization) (3)
- [10.3 Inverse homogenization](#inverse-homogenization) (1)
- [10.4 Machine learning for multiscale simulation](#machine-learning-for-multiscale-simulation) (3)
- [10.5 Crystal plasticity](#crystal-plasticity) (5)

## <a id="fft-based-homogenization"></a>10.1 FFT-based homogenization

| Name, language and license | Description | Note |
| --- | --- | --- |
| [DataAnalytics<br>Engineering/<br>FANS](https://github.com/DataAnalyticsEngineering/FANS)<br><sub>C++</sub><br><sub>LGPL-3.0</sub> | Parallel FFT-based homogenization for microscale multiphysics problems. |  |
| [tdegeus/<br>GooseFFT](https://github.com/tdegeus/GooseFFT)<br><sub>Python</sub><br><sub>MIT</sub> | Small teaching scripts for FFT-based micromechanical solvers. |  |
| [vondrejc/<br>FFTHomPy](https://github.com/vondrejc/FFTHomPy)<br><sub>Python</sub><br><sub>MIT</sub> | FFT-based homogenization with guaranteed bounds on effective properties. |  |

## <a id="fe2-and-computational-homogenization"></a>10.2 FE² and computational homogenization

| Name, language and license | Description | Note |
| --- | --- | --- |
| [felipefr/<br>micmacsfenics](https://github.com/felipefr/micmacsfenics)<br><sub>Python</sub><br><sub>MIT</sub> | FE² and computational homogenization in FEniCS. | README points to the legacy branch for working code during a rewrite. |
| [meghbali/<br>MultiScale<br>Plasticity](https://github.com/meghbali/MultiScalePlasticity)<br><sub>MATLAB</sub><br><sub>MIT</sub> | Upscaling of representative volumes with elastoplastic constituents. | Written for MATLAB, Octave support not documented. |
| [MinhNguyenIKM/<br>multiscale-<br>homogenization](https://github.com/MinhNguyenIKM/multiscale-homogenization)<br><sub>MATLAB and Python</sub><br><sub>none found</sub> | FFT microscale and finite element macroscale computational homogenization. | Includes MATLAB code; bundled PyFEM files state all rights reserved. |

## <a id="inverse-homogenization"></a>10.3 Inverse homogenization

| Name, language and license | Description | Note |
| --- | --- | --- |
| [lavenklau/<br>homo3d](https://github.com/lavenklau/homo3d)<br><sub>C++ and CUDA</sub><br><sub>GPL-2.0</sub> | GPU solver for large-scale inverse homogenization. | Requires an NVIDIA GPU; README says the main branch is being refactored. |

## <a id="machine-learning-for-multiscale-simulation"></a>10.4 Machine learning for multiscale simulation

| Name, language and license | Description | Note |
| --- | --- | --- |
| [bessagroup/<br>CRATE](https://github.com/bessagroup/CRATE)<br><sub>Python</sub><br><sub>BSD-3-Clause</sub> | Clustering-based reduced-order homogenization of nonlinear heterogeneous materials. |  |
| [HamidrezaEiv/<br>FE2-Computations-<br>With-Deep-Neural-<br>Networks](https://github.com/HamidrezaEiv/FE2-Computations-With-Deep-Neural-Networks)<br><sub>Fortran and Python</sub><br><sub>none found, with LGPL Forpy files</sub> | Neural network surrogates deployed inside Fortran FE² computations. | Paper code. |
| [SLIMM-Lab/<br>pyprnn](https://github.com/SLIMM-Lab/pyprnn)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Networks with constitutive models embedded for path-dependent homogenization. |  |

## <a id="crystal-plasticity"></a>10.5 Crystal plasticity

| Name, language and license | Description | Note |
| --- | --- | --- |
| [apatra6/<br>rhocp](https://github.com/apatra6/rhocp)<br><sub>C++</sub><br><sub>LGPL-2.1</sub> | Dislocation-density crystal plasticity solver built on MOOSE. |  |
| [damask-<br>multiphysics/<br>DAMASK](https://github.com/damask-multiphysics/DAMASK)<br><sub>Fortran and Python</sub><br><sub>AGPL-3.0-or-later</sub> | Multiscale crystal plasticity simulation kit. | Read-only mirror; development is at git.damask-multiphysics.org. |
| [llnl/<br>ExaConstit](https://github.com/llnl/ExaConstit)<br><sub>C++</sub><br><sub>BSD-3-Clause</sub> | GPU crystal plasticity finite element code with a UMAT interface. |  |
| [prisms-center/<br>plasticity](https://github.com/prisms-center/plasticity)<br><sub>C++</sub><br><sub>LGPL-2.1-or-later</sub> | Crystal and continuum plasticity finite element code built on deal.II. |  |
| [SuperkakaSCU/<br>JAX-CPFEM](https://github.com/SuperkakaSCU/JAX-CPFEM)<br><sub>Python</sub><br><sub>none found</sub> | Differentiable GPU crystal plasticity finite elements built on JAX-FEM. |  |

[← Back to the main list](../README.md#contents)
