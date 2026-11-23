# 13. Physics-informed learning and energy methods

[← Back to the main list](../README.md#contents)

- [13.1 Deep energy methods](#deep-energy-methods) (10)
- [13.2 Residual-based networks](#residual-based-networks) (11)
- [13.3 PINN libraries and examples](#pinn-libraries-and-examples) (7)

## <a id="deep-energy-methods"></a>13.1 Deep energy methods

| Name, language and license | Description | Note |
| --- | --- | --- |
| [FuhgJan/<br>DCRM](https://github.com/FuhgJan/DCRM)<br><sub>Python</sub><br><sub>GPL-3.0 (stated in README)</sub> | Deep convolutional Ritz method, which trains parametric PDE surrogates by energy minimization without labeled data. | Poisson equation only; datasets are downloaded from Zenodo. |
| [FuhgJan/<br>mixedDEM](https://github.com/FuhgJan/mixedDEM)<br><sub>Python</sub><br><sub>conflicting statements</sub> | Mixed deep energy method for stress concentrations in finite-strain hyperelasticity. | README states both GPL-3.0 and a non-commercial Creative Commons license. |
| [ISM-Weimar/<br>DeepEnergyMethods](https://github.com/ISM-Weimar/DeepEnergyMethods)<br><sub>Python</sub><br><sub>MIT</sub> | Companion code for energy-based deep learning solutions of PDEs in mechanics. |  |
| [Jasiuk-Research-<br>Group/<br>DEM_for_J2_<br>plasticity](https://github.com/Jasiuk-Research-Group/DEM_for_J2_plasticity)<br><sub>Python</sub><br><sub>MIT</sub> | Deep energy method for 3D J2 elastoplasticity. |  |
| [Jasiuk-Research-<br>Group/<br>Graph_DEM](https://github.com/Jasiuk-Research-Group/Graph_DEM)<br><sub>Python</sub><br><sub>none found</sub> | Comparison of graph convolution and MLP deep energy methods for elastic solids. |  |
| [JinshuaiBai/<br>energy_PINN_<br>Contact](https://github.com/JinshuaiBai/energy_PINN_Contact)<br><sub>Python</sub><br><sub>none found</sub> | Energy-based PINN for frictionless large-deformation contact. |  |
| [MinhNguyenIKM/<br>dem_<br>hyperelasticity](https://github.com/MinhNguyenIKM/dem_hyperelasticity)<br><sub>Python</sub><br><sub>none found</sub> | Deep energy method for finite-deformation hyperelasticity. |  |
| [somdattagoswami/<br>DEM-PhaseField](https://github.com/somdattagoswami/DEM-PhaseField)<br><sub>Python</sub><br><sub>none found</sub> | Adaptive phase-field fracture with deep energy minimization. | Requires TensorFlow 1.15. |
| [yizheng-wang/<br>Research-on-<br>Solving-Partial-<br>Differential-<br>Equations-of-<br>Solid-Mechanics-<br>Based-on-PINN](https://github.com/yizheng-wang/Research-on-Solving-Partial-Differential-Equations-of-Solid-Mechanics-Based-on-PINN)<br><sub>Python</sub><br><sub>none found</sub> | Thesis code for solid mechanics with deep energy, CENN, DCEM and KINN methods. |  |
| [ZeyuJia/<br>DeepRitzMethod](https://github.com/ZeyuJia/DeepRitzMethod)<br><sub>Jupyter Notebook</sub><br><sub>none found</sub> | Course project that implements and discusses the deep Ritz method. | Poisson equation only. |

## <a id="residual-based-networks"></a>13.2 Residual-based networks

| Name, language and license | Description | Note |
| --- | --- | --- |
| [AdityaLab/<br>pinnsformer](https://github.com/AdityaLab/pinnsformer)<br><sub>Python and Jupyter Notebook</sub><br><sub>none found</sub> | Transformer-based physics-informed networks, with convection, reaction, wave and Navier-Stokes demos. | Paper code. |
| [jayroxis/<br>PINNs](https://github.com/jayroxis/PINNs)<br><sub>Jupyter Notebook</sub><br><sub>none found</sub> | PyTorch and TensorFlow 1 notebooks that reimplement the Burgers examples of the original PINN code. | Burgers equation only. |
| [Jianxun-Wang/<br>LabelFree-DNN-<br>Surrogate](https://github.com/Jianxun-Wang/LabelFree-DNN-Surrogate)<br><sub>Python and Jupyter Notebook</sub><br><sub>MIT</sub> | Physics-constrained networks trained without simulation data as surrogates of parametric pipe and aneurysm flows. | Paper code. |
| [JinshuaiBai/<br>LSWR_loss_<br>function_PINN](https://github.com/JinshuaiBai/LSWR_loss_function_PINN)<br><sub>Python</sub><br><sub>none found</sub> | Least squares weighted residual loss for PINN solid mechanics. |  |
| [JinshuaiBai/<br>PINN_Comp_Mech](https://github.com/JinshuaiBai/PINN_Comp_Mech)<br><sub>Python</sub><br><sub>none found</sub> | Introductory PINN examples in solid mechanics with collocation and energy losses. |  |
| [JinshuaiBai/<br>PIRBN](https://github.com/JinshuaiBai/PIRBN)<br><sub>Python</sub><br><sub>none found</sub> | Physics-informed radial basis networks with spring, wave and viscoelastic flow examples. |  |
| [Neural-Mechanics-<br>Lab/<br>folax](https://github.com/Neural-Mechanics-Lab/folax)<br><sub>Python</sub><br><sub>BSD-4-Clause, with MIT files</sub> | Finite operator learning trained on discrete residuals from classical discretizations. |  |
| [nn4pde/<br>SPINN](https://github.com/nn4pde/SPINN)<br><sub>Python</sub><br><sub>BSD-3-Clause</sub> | Sparse, physics-based and partially interpretable neural networks for ODEs and PDEs, including a lid-driven cavity flow. | Paper code. |
| [prateekbhustali/<br>Physics-Informed-<br>Neural-Networks](https://github.com/prateekbhustali/Physics-Informed-Neural-Networks)<br><sub>Jupyter Notebook</sub><br><sub>MIT</sub> | TensorFlow 2 and PyTorch notebooks that study PINN training on Burgers, Helmholtz and Poisson problems. | Model equations only. |
| [Raocp/<br>PINN-<br>elastodynamics](https://github.com/Raocp/PINN-elastodynamics)<br><sub>Python</sub><br><sub>none found</sub> | Physics-informed networks for elastodynamics without labeled data. |  |
| [ThangLe-duc/<br>FEINN](https://github.com/ThangLe-duc/FEINN)<br><sub>MATLAB</sub><br><sub>Apache-2.0</sub> | Networks trained with a finite element residual loss for structural statics. | Written for MATLAB, Octave support not documented. |

## <a id="pinn-libraries-and-examples"></a>13.3 PINN libraries and examples

| Name, language and license | Description | Note |
| --- | --- | --- |
| [analysiscenter/<br>pydens](https://github.com/analysiscenter/pydens)<br><sub>Python and Jupyter Notebook</sub><br><sub>Apache-2.0</sub> | Framework for solving ordinary and partial differential equations with neural networks, including parametric families and trainable coefficients. | General-purpose; built on PyTorch and BatchFlow. |
| [ehsanhaghighat/<br>sciann-<br>applications](https://github.com/ehsanhaghighat/sciann-applications)<br><sub>Jupyter Notebook</sub><br><sub>MIT</sub> | SciANN examples, including elasticity, elastoplasticity, vibration and poroelasticity. | SciANN itself is unmaintained. |
| [i207M/<br>PINNacle](https://github.com/i207M/PINNacle)<br><sub>Python</sub><br><sub>MIT</sub> | Benchmark of physics-informed neural network variants on 20 PDE cases, including heat, wave and Navier-Stokes problems. | Bundles copies of DeepXDE (LGPL-2.1 upstream), FBPINNs and hp-VPINNs; reference solutions are simulated, not measured. |
| [lululxvi/<br>deepxde](https://github.com/lululxvi/deepxde)<br><sub>Python</sub><br><sub>LGPL-2.1</sub> | Library for physics-informed learning of forward and inverse differential equation problems. |  |
| [NeuroDiffGym/<br>neurodiffeq](https://github.com/NeuroDiffGym/neurodiffeq)<br><sub>Python</sub><br><sub>MIT</sub> | PyTorch library that solves ordinary and partial differential equations with neural networks. | General-purpose. |
| [PINA-org/<br>PINA](https://github.com/PINA-org/PINA)<br><sub>Python</sub><br><sub>MIT</sub> | Library for physics-informed networks, neural operators and data-driven models. |  |
| [SciML/<br>NeuralPDE.jl](https://github.com/SciML/NeuralPDE.jl)<br><sub>Julia</sub><br><sub>MIT</sub> | Physics-informed neural network solvers for ordinary, stochastic and partial differential equations. | General-purpose. |

[← Back to the main list](../README.md#contents)
