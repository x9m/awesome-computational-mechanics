# 14. Surrogates and reduced-order models

[← Back to the main list](../README.md#contents)

- [14.1 Stress-field prediction](#stress-field-prediction) (7)
- [14.2 Flow-field prediction](#flow-field-prediction) (5)
- [14.3 Deformation and reduced dynamics](#deformation-and-reduced-dynamics) (9)
- [14.4 Classical machine learning and equation discovery](#classical-machine-learning-and-equation-discovery) (13)
- [14.5 Projection-based model reduction](#projection-based-model-reduction) (4)
- [14.6 Graph neural networks](#graph-neural-networks) (4)
- [14.7 Biomechanical surrogates](#biomechanical-surrogates) (2)
- [14.8 Response histories and operator learning](#response-histories-and-operator-learning) (7)
- [14.9 Frameworks and introductory studies](#frameworks-and-introductory-studies) (4)
- [14.10 Benchmark datasets](#benchmark-datasets) (6)

## <a id="stress-field-prediction"></a>14.1 Stress-field prediction

| Name, language and license | Description | Note |
| --- | --- | --- |
| [farazarbabi/<br>CNN_FEM](https://github.com/farazarbabi/CNN_FEM)<br><sub>Python</sub><br><sub>all rights reserved</sub> | Convolutional network prediction of stress fields in solids from simulation data. | Stated in source file headers. |
| [federicosanna/<br>UNet-for-FEM-and-<br>Stress-<br>Distribution-<br>Inference](https://github.com/federicosanna/UNet-for-FEM-and-Stress-Distribution-Inference)<br><sub>Python</sub><br><sub>none found</sub> | U-Net inference of stress distributions from finite element data. | Some trained models are not included. |
| [Jasiuk-Research-<br>Group/<br>ResUNet-DeepONet-<br>Plasticity](https://github.com/Jasiuk-Research-Group/ResUNet-DeepONet-Plasticity)<br><sub>Python</sub><br><sub>MIT</sub> | Operator network prediction of plastic stress fields on varying geometries. |  |
| [lamm-mit/<br>FieldPredictorGAN](https://github.com/lamm-mit/FieldPredictorGAN)<br><sub>Python</sub><br><sub>MIT</sub> | Adversarial network prediction of stress and strain fields in composites. |  |
| [TML-Gatech/<br>DL_Stress_TAA](https://github.com/TML-Gatech/DL_Stress_TAA)<br><sub>all rights reserved</sub> | Deep learning surrogate of finite element stress analysis. | Source files are supplied as PDFs. |
| [zhenguonie/<br>2020_StressGAN](https://github.com/zhenguonie/2020_StressGAN)<br><sub>Python</sub><br><sub>none found</sub> | Generative model for 2D stress distribution prediction. |  |
| [zhenguonie/<br>stress_net](https://github.com/zhenguonie/stress_net)<br><sub>Python</sub><br><sub>none found</sub> | Convolutional prediction of stress fields in cantilevered structures. |  |

## <a id="flow-field-prediction"></a>14.2 Flow-field prediction

| Name, language and license | Description | Note |
| --- | --- | --- |
| [byungsook/<br>deep-fluids](https://github.com/byungsook/deep-fluids)<br><sub>Python</sub><br><sub>none found</sub> | Generative network that synthesizes velocity fields of parameterized smoke and liquid simulations. | Requires mantaflow and TensorFlow 1.15. |
| [maxjiang93/<br>space_time_pde](https://github.com/maxjiang93/space_time_pde)<br><sub>Python</sub><br><sub>MIT</sub> | MeshfreeFlowNet, space-time super-resolution of flow simulations trained with PDE constraints. | Example is Rayleigh-Bénard convection. |
| [pranshupant/<br>DL-ROM](https://github.com/pranshupant/DL-ROM)<br><sub>Python and Jupyter Notebook</sub><br><sub>MIT</sub> | Autoencoder reduced-order model that predicts future time steps of fluid simulations. | Datasets are downloaded from Google Drive. |
| [wiewel/<br>LatentSpacePhysics](https://github.com/wiewel/LatentSpacePhysics)<br><sub>Python and C++</sub><br><sub>GPL-3.0, with Apache-2.0 mantaflow</sub> | Autoencoder and LSTM networks that predict the time evolution of fluid pressure fields in a latent space. | Bundles a copy of mantaflow; tested with TensorFlow 1.7. |
| [wiewel/<br>LatentSpace<br>Subdivision](https://github.com/wiewel/LatentSpaceSubdivision)<br><sub>Python</sub><br><sub>MIT</sub> | Latent-space prediction of smoke flows, with a subdivided latent space for stable and controllable long rollouts. | Requires mantaflow and TensorFlow 1.11. |

## <a id="deformation-and-reduced-dynamics"></a>14.3 Deformation and reduced dynamics

| Name, language and license | Description | Note |
| --- | --- | --- |
| [AlbanOdot/<br>DeepPhysics-<br>article](https://github.com/AlbanOdot/DeepPhysics-article)<br><sub>Python</sub><br><sub>CC0-1.0</sub> | Paper code for physics-aware deep learning in real-time simulation. |  |
| [haller-group/<br>SSMLearn](https://github.com/haller-group/SSMLearn)<br><sub>MATLAB</sub><br><sub>AGPL-3.0</sub> | Data-driven reduced models of nonlinear dynamics on spectral submanifolds. | Written for MATLAB, Octave support not documented; requires SSMTool. |
| [lawsonfulton/<br>AutoDef](https://github.com/lawsonfulton/AutoDef)<br><sub>C++</sub><br><sub>MIT</sub> | Latent-space dynamics for reduced deformable simulation. | Install script can overwrite your Keras configuration. |
| [llnl/<br>GPLaSDI](https://github.com/llnl/GPLaSDI)<br><sub>Python</sub><br><sub>MIT</sub> | Autoencoders and Gaussian processes that learn latent dynamics of simulations. | Not specific to solid mechanics. |
| [lrquad/<br>NNWarp](https://github.com/lrquad/NNWarp)<br><sub>C++</sub><br><sub>MIT, excluding bundled binaries</sub> | Neural network-based nonlinear deformable simulator. | Bundled Windows binaries, including Intel and EASendMail libraries, have their own licenses. |
| [saurabhdeshpande93/<br>convolution-<br>aggregation-<br>attention](https://github.com/saurabhdeshpande93/convolution-aggregation-attention)<br><sub>Python and Mathematica</sub><br><sub>MIT</sub> | CNN, graph and attention surrogates for nonlinear finite element simulations. | Data generation uses AceFEM. |
| [stefaniafresca/<br>DL-ROM-Meth](https://github.com/stefaniafresca/DL-ROM-Meth)<br><sub>Python and MATLAB</sub><br><sub>none found</sub> | Deep learning reduced-order models for nonlinear time-dependent parametrized PDEs. | README says the full network implementation is available on request; MATLAB is used for data generation. |
| [stefaniafresca/<br>POD-DL-ROM](https://github.com/stefaniafresca/POD-DL-ROM)<br><sub>Python</sub><br><sub>none found</sub> | Deep learning reduced-order models enhanced by proper orthogonal decomposition. | README reports nonlinear elastodynamics tests; the example scripts are templates with blank settings. |
| [vividda/<br>3D-PhysNet](https://github.com/vividda/3D-PhysNet)<br><sub>Python</sub><br><sub>none found</sub> | Learned prediction of non-rigid 3D object deformation. | Python 2.7. |

## <a id="classical-machine-learning-and-equation-discovery"></a>14.4 Classical machine learning and equation discovery

| Name, language and license | Description | Note |
| --- | --- | --- |
| [astroautomata/<br>PySR](https://github.com/astroautomata/PySR)<br><sub>Python</sub><br><sub>Apache-2.0</sub> | Symbolic regression that searches for interpretable equations. | General-purpose. |
| [bessagroup/<br>f3dasm](https://github.com/bessagroup/f3dasm)<br><sub>Python</sub><br><sub>BSD-3-Clause</sub> | Framework for data-driven design and analysis of structures and materials. |  |
| [dynamicslab/<br>pysindy](https://github.com/dynamicslab/pysindy)<br><sub>Python</sub><br><sub>MIT</sub> | Sparse regression that identifies governing equations from data. | General-purpose. |
| [isds-neu/<br>PeRCNN](https://github.com/isds-neu/PeRCNN)<br><sub>Python</sub><br><sub>MIT</sub> | Physics-encoded recurrent convolutional networks for modeling and discovering reaction-diffusion equations. | Paper code; examples are reaction-diffusion and 2D Burgers systems. |
| [kylebeggs/<br>POD-RBF](https://github.com/kylebeggs/POD-RBF)<br><sub>Python</sub><br><sub>conflicting statements</sub> | Reduced-order models from snapshot data by proper orthogonal decomposition and radial basis function interpolation, written in JAX. | LICENSE file is GPL-3.0, but pyproject.toml states MIT. |
| [mathLab/<br>EZyRB](https://github.com/mathLab/EZyRB)<br><sub>Python</sub><br><sub>MIT</sub> | Data-driven reduced-order models of parametrized simulations. |  |
| [maziarraissi/<br>DeepHPMs](https://github.com/maziarraissi/DeepHPMs)<br><sub>Python</sub><br><sub>MIT</sub> | Deep hidden physics models that learn nonlinear PDEs from scattered data, with Burgers, KdV, Kuramoto-Sivashinsky and Navier-Stokes examples. | Paper code; written for TensorFlow 1. |
| [maziarraissi/<br>HPM](https://github.com/maziarraissi/HPM)<br><sub>MATLAB and Mathematica</sub><br><sub>MIT</sub> | Gaussian process models that identify parameters of nonlinear PDEs from data, with Navier-Stokes and other examples. | Written for MATLAB, Octave support not documented. |
| [operator-<br>inference/<br>opinf](https://github.com/operator-inference/opinf)<br><sub>Python</sub><br><sub>MIT</sub> | Non-intrusive reduced-order models learned by operator inference. |  |
| [PyDMD/<br>PyDMD](https://github.com/PyDMD/PyDMD)<br><sub>Python</sub><br><sub>MIT</sub> | Dynamic mode decomposition of time-varying simulation or measured data. |  |
| [SciML/<br>Surrogates.jl](https://github.com/SciML/Surrogates.jl)<br><sub>Julia</sub><br><sub>MIT</sub> | Surrogate modeling and optimization for expensive simulations. | General-purpose. |
| [SMTorg/<br>smt](https://github.com/SMTorg/smt)<br><sub>Python</sub><br><sub>BSD-3-Clause</sub> | Surrogate modeling toolbox with kriging, other regressors and sampling methods. | General-purpose. |
| [ZichaoLong/<br>PDE-Net](https://github.com/ZichaoLong/PDE-Net)<br><sub>Python</sub><br><sub>none found</sub> | PDE-Net and PDE-Net 2.0, networks that learn PDEs and their time stepping from data. | Source code is on the PDE-Net and PDE-Net-2.0 branches, not the default branch; requires the authors' aTEAM library. |

## <a id="projection-based-model-reduction"></a>14.5 Projection-based model reduction

| Name, language and license | Description | Note |
| --- | --- | --- |
| [llnl/<br>libROM](https://github.com/llnl/libROM)<br><sub>C++</sub><br><sub>MIT or Apache-2.0, with restricted ParMETIS archive</sub> | Parallel library for intrusive and non-intrusive reduced-order models. | Bundled ParMETIS archive may not be redistributed without approval. |
| [pymor/<br>pymor](https://github.com/pymor/pymor)<br><sub>Python</sub><br><sub>BSD-2-Clause</sub> | Model order reduction library that works with external PDE solvers. |  |
| [RBniCS/<br>RBniCS](https://github.com/RBniCS/RBniCS)<br><sub>Python</sub><br><sub>LGPL-3.0-or-later</sub> | Reduced-order modeling techniques implemented in FEniCS. | Built on legacy FEniCS. |
| [SofaDefrost/<br>ModelOrder<br>Reduction](https://github.com/SofaDefrost/ModelOrderReduction)<br><sub>C++ and Python</sub><br><sub>GPL-2.0</sub> | Model reduction plugin for faster SOFA scenes. | Requires SOFA. |

## <a id="graph-neural-networks"></a>14.6 Graph neural networks

| Name, language and license | Description | Note |
| --- | --- | --- |
| [Jianxun-Wang/<br>graphGalerkin](https://github.com/Jianxun-Wang/graphGalerkin)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Physics-informed graph neural Galerkin networks for forward and inverse PDE problems. | Requires pyCaMOtk. |
| [sukjulian/<br>coronary-mesh-<br>convolution](https://github.com/sukjulian/coronary-mesh-convolution)<br><sub>Python</sub><br><sub>MIT</sub> | Mesh neural networks that estimate wall shear stress and hemodynamics on the artery wall. | Dataset is downloaded separately. |
| [wwMark/<br>meshgraphnets](https://github.com/wwMark/meshgraphnets)<br><sub>Python</sub><br><sub>Apache-2.0 in some files</sub> | PyTorch port of MeshGraphNets with cloth simulation. | Author says results do not fully match the original; files without an Apache header state no license. |
| [YasminSalehi/<br>PhysGNN](https://github.com/YasminSalehi/PhysGNN)<br><sub>Python</sub><br><sub>BSD-4-Clause</sub> | Graph neural network prediction of soft tissue deformation in neurosurgery. |  |

## <a id="biomechanical-surrogates"></a>14.7 Biomechanical surrogates

| Name, language and license | Description | Note |
| --- | --- | --- |
| [dabiriyaghoub/<br>Ventricular_ML_<br>DecisionTrees](https://github.com/dabiriyaghoub/Ventricular_ML_DecisionTrees)<br><sub>Python</sub><br><sub>all rights reserved</sub> | Machine learning prediction of left ventricular mechanics. |  |
| [michetonu/<br>MALTIDEM--Machine-<br>Learning-for-<br>Tissue-<br>Deformation-<br>Modelling](https://github.com/michetonu/MALTIDEM--Machine-Learning-for-Tissue-Deformation-Modelling)<br><sub>MATLAB</sub><br><sub>none found</sub> | Data-driven real-time model of brain tumor deformation for neurosurgery. | Workflow uses MATLAB and FEBio. |

## <a id="response-histories-and-operator-learning"></a>14.8 Response histories and operator learning

| Name, language and license | Description | Note |
| --- | --- | --- |
| [Jasiuk-Research-<br>Group/<br>Bio-inspired-low-<br>porosity-<br>structures-using-<br>Neural-Networks-<br>GRU-Implemenation](https://github.com/Jasiuk-Research-Group/Bio-inspired-low-porosity-structures-using-Neural-Networks-GRU-Implemenation)<br><sub>Python</sub><br><sub>MIT</sub> | Recurrent network prediction of stress-strain response and energy absorption in bio-inspired structures. |  |
| [Jasiuk-Research-<br>Group/<br>CMDS-14-impact-<br>resistantance-NN-<br>prediction-](https://github.com/Jasiuk-Research-Group/CMDS-14-impact-resistantance-NN-prediction-)<br><sub>Python</sub><br><sub>none found</sub> | Neural networks for structure-property relations in impact-resistant structures. |  |
| [Jasiuk-Research-<br>Group/<br>LatticeResponse_<br>NN_Prediction](https://github.com/Jasiuk-Research-Group/LatticeResponse_NN_Prediction)<br><sub>Python</sub><br><sub>none found</sub> | Recurrent network prediction of lattice stress-strain curves and energy absorption. |  |
| [Jasiuk-Research-<br>Group/<br>S-DeepONet](https://github.com/Jasiuk-Research-Group/S-DeepONet)<br><sub>Python</sub><br><sub>none found</sub> | Sequential operator network with plasticity and heat transfer examples. |  |
| [Jasiuk-Research-<br>Group/<br>S-DeepONet-<br>transient-<br>predictions](https://github.com/Jasiuk-Research-Group/S-DeepONet-transient-predictions)<br><sub>Python</sub><br><sub>none found</sub> | Sequential operator network for transient full-field predictions, including plasticity. |  |
| [JinshuaiBai/<br>Discrete-Solution-<br>Operator-Learning-<br>DiSOL](https://github.com/JinshuaiBai/Discrete-Solution-Operator-Learning-DiSOL)<br><sub>Python and MATLAB</sub><br><sub>MIT</sub> | Discrete solution operator learning for geometry-dependent PDEs, including linear elasticity. | Training datasets are downloaded from Zenodo; MATLAB is used for data generation. |
| [neuraloperator/<br>neuraloperator](https://github.com/neuraloperator/neuraloperator)<br><sub>Python</sub><br><sub>MIT, with Apache-2.0 files</sub> | Library of neural operators that learn maps between functions. | General-purpose. |

## <a id="frameworks-and-introductory-studies"></a>14.9 Frameworks and introductory studies

| Name, language and license | Description | Note |
| --- | --- | --- |
| [hmjeon/<br>FEM-ML](https://github.com/hmjeon/FEM-ML)<br><sub>Python, Fortran and Jupyter Notebook</sub><br><sub>GPL-3.0</sub> | Experiments in finite element analysis with machine learning. | Sparse documentation. |
| [mimesis-inria/<br>DeepPhysX](https://github.com/mimesis-inria/DeepPhysX)<br><sub>Python</sub><br><sub>AGPL-3.0</sub> | Interface between numerical simulations and learning algorithms for training and prediction. |  |
| [NVIDIA/<br>physicsnemo](https://github.com/NVIDIA/physicsnemo)<br><sub>Python</sub><br><sub>Apache-2.0, with MIT files</sub> | Deep learning framework for physics, with CFD and other simulation examples. | Some example datasets restrict commercial use. |
| [oleksiyskononenko/<br>mlfem](https://github.com/oleksiyskononenko/mlfem)<br><sub>Jupyter Notebook</sub><br><sub>none found</sub> | Notebook and report on deep learning with finite element models of physical systems. |  |

## <a id="benchmark-datasets"></a>14.10 Benchmark datasets

| Name, language and license | Description | Note |
| --- | --- | --- |
| [elejeune11/<br>Mechanical-MNIST](https://github.com/elejeune11/Mechanical-MNIST)<br><sub>Python</sub><br><sub>MIT code, CC-BY-SA-3.0 data</sub> | Benchmark of 70,000 large-deformation finite element simulations for surrogate models. |  |
| [Extrality/<br>AirfRANS](https://github.com/Extrality/AirfRANS)<br><sub>Python</sub><br><sub>ODbL-1.0</sub> | Dataset and baselines for learning RANS solutions around airfoils. | Simulated data, not measurements. |
| [Mohamedelrefaie/<br>DrivAerNet](https://github.com/Mohamedelrefaie/DrivAerNet)<br><sub>Python</sub><br><sub>CC-BY-NC-4.0 data, conflicting statements on code</sub> | Car aerodynamics CFD datasets and deep learning benchmarks. | Simulated data, not measurements; data prohibit commercial use; README calls the code MIT, but the LICENSE file is CC-BY-NC-4.0. |
| [pdebench/<br>PDEBench](https://github.com/pdebench/PDEBench)<br><sub>Python</sub><br><sub>MIT, with non-commercial NEC files</sub> | Datasets and baselines for machine learning on PDEs, including fluid flows. | Simulated data, not measurements; some core scripts allow non-commercial research use only. |
| [PolymathicAI/<br>the_well](https://github.com/PolymathicAI/the_well)<br><sub>Python</sub><br><sub>BSD-3-Clause, with CC-BY-4.0 data</sub> | Large collection of physics simulation datasets for machine learning. | Simulated data, not measurements. |
| [tum-pbs/<br>apebench](https://github.com/tum-pbs/apebench)<br><sub>Python</sub><br><sub>MIT</sub> | Benchmark of autoregressive PDE emulators with a differentiable reference solver. | Simulated data, not measurements. |

[← Back to the main list](../README.md#contents)
