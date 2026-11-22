# 5. Third medium contact

[← Back to the main list](../README.md#contents)

Third medium contact (TMC) models contact by meshing the gap with a very compliant fictitious material. Some links open the relevant file inside a larger project. DTU's MATLAB TopTMC code is not in a repository and can be downloaded from the [TopOpt software page](https://www.topopt.mek.dtu.dk/apps-and-software).

- [5.1 Modules and examples in FEM libraries](#modules-and-examples-in-fem-libraries) (7)
- [5.2 Optimization and metamaterials](#optimization-and-metamaterials) (4)
- [5.3 Standalone study codes](#standalone-study-codes) (1)

## <a id="modules-and-examples-in-fem-libraries"></a>5.1 Modules and examples in FEM libraries

| Name, language and license | Description | Note |
| --- | --- | --- |
| [adtzlr/<br>felupe](https://github.com/adtzlr/felupe/blob/main/examples/ex20_third-medium-contact.py)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Third medium contact example in the FElupe nonlinear finite element package. |  |
| [deepmodeling/<br>jax-fem](https://github.com/deepmodeling/jax-fem/tree/main/applications/third_medium_contact)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Third medium contact application in JAX-FEM. | README asks commercial users to contact the author. |
| [fenics-dolfiny/<br>dolfiny](https://github.com/fenics-dolfiny/dolfiny/tree/main/demo/tmc)<br><sub>Python</sub><br><sub>LGPL-3.0</sub> | Third medium contact demo built on FEniCSx. |  |
| [idaholab/<br>moose](https://github.com/idaholab/moose/blob/next/modules/solid_mechanics/doc/content/source/kernels/SecondDerivativeRegularization.md)<br><sub>C++</sub><br><sub>LGPL-2.1</sub> | HuHu, LuLu and HuHu-LuLu regularization kernels for solid mechanics. | Regularization component, not a complete contact example. |
| [meyer-nils/<br>torch-fem](https://github.com/meyer-nils/torch-fem/blob/main/examples/basic/planar/third_medium_contact.ipynb)<br><sub>Python</sub><br><sub>MIT</sub> | Third medium contact example in a differentiable PyTorch finite element solver. |  |
| [MultiSimOLab/<br>HyperFEM.jl](https://github.com/MultiSimOLab/HyperFEM.jl/blob/main/test/SimulationsTests/ThirdMediumContactSimulation.jl)<br><sub>Julia</sub><br><sub>MIT</sub> | Third medium contact simulation in a hyperelastic multiphysics library. | Provided as a test, not a tutorial. |
| [Naruki-Ichihara/<br>feax](https://github.com/Naruki-Ichihara/feax/blob/main/feax/mechanics/tmc.py)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Third medium contact module in a JAX finite element engine, with 2D and 3D examples. |  |

## <a id="optimization-and-metamaterials"></a>5.2 Optimization and metamaterials

| Name, language and license | Description | Note |
| --- | --- | --- |
| [charlieaveline/<br>TMC_Firedrake](https://github.com/charlieaveline/TMC_Firedrake)<br><sub>Python</sub><br><sub>MIT</sub> | Minimal unit-cell forward solve with third medium contact and multiscale virtual power. |  |
| [IMTEK-Simulation/<br>muFFTTO](https://github.com/IMTEK-Simulation/muFFTTO/tree/main/examples/internal_contact)<br><sub>Python</sub><br><sub>MIT</sub> | Internal contact by third medium in an FFT-based microstructure optimization code. |  |
| [LuoXueling/<br>optimization_of_<br>digital_material_<br>distribution](https://github.com/LuoXueling/optimization_of_digital_material_distribution/blob/main/main_semisphere_dist_opt_tmc.py)<br><sub>Python</sub><br><sub>MIT</sub> | Multimaterial distribution optimization with a third medium contact example. |  |
| [stefanhiemer/<br>topoptlab](https://github.com/stefanhiemer/topoptlab/tree/main/examples/fem/third_medium_contact)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | C-shape contact example in a topology optimization library. |  |

## <a id="standalone-study-codes"></a>5.3 Standalone study codes

| Name, language and license | Description | Note |
| --- | --- | --- |
| [MechEngrLorenzo<br>Fiore/<br>FEA_studies](https://github.com/MechEngrLorenzoFiore/FEA_studies/tree/main/Third_medium_contact)<br><sub>Python</sub><br><sub>MIT</sub> | Study script based on the 2024 paper by Faltus, Horak, Doskar and Rokos. | Learning project. |

[← Back to the main list](../README.md#contents)
