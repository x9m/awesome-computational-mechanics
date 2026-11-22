# 14. Surrogates and reduced-order models

[← Back to the main list](../README.md#contents)

- [14.1 Stress-field prediction](#stress-field-prediction) (7)
- [14.2 Deformation and reduced dynamics](#deformation-and-reduced-dynamics) (7)
- [14.3 Projection-based model reduction](#projection-based-model-reduction) (4)
- [14.4 Graph neural networks](#graph-neural-networks) (4)
- [14.5 Biomechanical surrogates](#biomechanical-surrogates) (2)
- [14.6 Response histories and operator learning](#response-histories-and-operator-learning) (6)
- [14.7 Frameworks and introductory studies](#frameworks-and-introductory-studies) (3)
- [14.8 Benchmark datasets](#benchmark-datasets) (1)

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

## <a id="deformation-and-reduced-dynamics"></a>14.2 Deformation and reduced dynamics

| Name, language and license | Description | Note |
| --- | --- | --- |
| [AlbanOdot/<br>DeepPhysics-<br>article](https://github.com/AlbanOdot/DeepPhysics-article)<br><sub>Python</sub><br><sub>CC0-1.0</sub> | Paper code for physics-aware deep learning in real-time simulation. |  |
| [haller-group/<br>SSMLearn](https://github.com/haller-group/SSMLearn)<br><sub>MATLAB</sub><br><sub>AGPL-3.0</sub> | Data-driven reduced models of nonlinear dynamics on spectral submanifolds. | Written for MATLAB, Octave support not documented; requires SSMTool. |
| [lawsonfulton/<br>AutoDef](https://github.com/lawsonfulton/AutoDef)<br><sub>C++</sub><br><sub>MIT</sub> | Latent-space dynamics for reduced deformable simulation. | Install script can overwrite your Keras configuration. |
| [lrquad/<br>NNWarp](https://github.com/lrquad/NNWarp)<br><sub>C++</sub><br><sub>MIT</sub> | Neural network-based nonlinear deformable simulator. |  |
| [saurabhdeshpande93/<br>convolution-<br>aggregation-<br>attention](https://github.com/saurabhdeshpande93/convolution-aggregation-attention)<br><sub>Python and Mathematica</sub><br><sub>MIT</sub> | CNN, graph and attention surrogates for nonlinear finite element simulations. | Data generation uses AceFEM. |
| [stefaniafresca/<br>POD-DL-ROM](https://github.com/stefaniafresca/POD-DL-ROM)<br><sub>Python</sub><br><sub>none found</sub> | Deep learning reduced-order models enhanced by proper orthogonal decomposition. | README reports nonlinear elastodynamics tests; the example scripts are templates with blank settings. |
| [vividda/<br>3D-PhysNet](https://github.com/vividda/3D-PhysNet)<br><sub>Python</sub><br><sub>none found</sub> | Learned prediction of non-rigid 3D object deformation. | Python 2.7. |

## <a id="projection-based-model-reduction"></a>14.3 Projection-based model reduction

| Name, language and license | Description | Note |
| --- | --- | --- |
| [llnl/<br>libROM](https://github.com/llnl/libROM)<br><sub>C++</sub><br><sub>MIT or Apache-2.0, with restricted ParMETIS archive</sub> | Parallel library for intrusive and non-intrusive reduced-order models. | Bundled ParMETIS archive may not be redistributed without approval. |
| [pymor/<br>pymor](https://github.com/pymor/pymor)<br><sub>Python</sub><br><sub>BSD-2-Clause</sub> | Model order reduction library that works with external PDE solvers. |  |
| [RBniCS/<br>RBniCS](https://github.com/RBniCS/RBniCS)<br><sub>Python</sub><br><sub>LGPL-3.0-or-later</sub> | Reduced-order modeling techniques implemented in FEniCS. | Built on legacy FEniCS. |
| [SofaDefrost/<br>ModelOrder<br>Reduction](https://github.com/SofaDefrost/ModelOrderReduction)<br><sub>C++ and Python</sub><br><sub>GPL-2.0</sub> | Model reduction plugin for faster SOFA scenes. | Requires SOFA. |

## <a id="graph-neural-networks"></a>14.4 Graph neural networks

| Name, language and license | Description | Note |
| --- | --- | --- |
| [Jianxun-Wang/<br>graphGalerkin](https://github.com/Jianxun-Wang/graphGalerkin)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Physics-informed graph neural Galerkin networks for forward and inverse PDE problems. | Requires pyCaMOtk. |
| [m-ulmestrand/<br>gcn-collisions](https://github.com/m-ulmestrand/gcn-collisions)<br><sub>Python</sub><br><sub>Apache-2.0</sub> | Graph convolutional network that learns particle collision responses. |  |
| [wwMark/<br>meshgraphnets](https://github.com/wwMark/meshgraphnets)<br><sub>Python</sub><br><sub>Apache-2.0 in some files</sub> | PyTorch port of MeshGraphNets with cloth simulation. | Author says results do not fully match the original; files without an Apache header state no license. |
| [YasminSalehi/<br>PhysGNN](https://github.com/YasminSalehi/PhysGNN)<br><sub>Python</sub><br><sub>BSD-4-Clause</sub> | Graph neural network prediction of soft tissue deformation in neurosurgery. |  |

## <a id="biomechanical-surrogates"></a>14.5 Biomechanical surrogates

| Name, language and license | Description | Note |
| --- | --- | --- |
| [dabiriyaghoub/<br>Ventricular_ML_<br>DecisionTrees](https://github.com/dabiriyaghoub/Ventricular_ML_DecisionTrees)<br><sub>Python</sub><br><sub>all rights reserved</sub> | Machine learning prediction of left ventricular mechanics. |  |
| [michetonu/<br>MALTIDEM--Machine-<br>Learning-for-<br>Tissue-<br>Deformation-<br>Modelling](https://github.com/michetonu/MALTIDEM--Machine-Learning-for-Tissue-Deformation-Modelling)<br><sub>MATLAB</sub><br><sub>none found</sub> | Data-driven real-time model of brain tumor deformation for neurosurgery. | Workflow uses MATLAB and FEBio. |

## <a id="response-histories-and-operator-learning"></a>14.6 Response histories and operator learning

| Name, language and license | Description | Note |
| --- | --- | --- |
| [Jasiuk-Research-<br>Group/<br>Bio-inspired-low-<br>porosity-<br>structures-using-<br>Neural-Networks-<br>GRU-Implemenation](https://github.com/Jasiuk-Research-Group/Bio-inspired-low-porosity-structures-using-Neural-Networks-GRU-Implemenation)<br><sub>Python</sub><br><sub>MIT</sub> | Recurrent network prediction of stress-strain response and energy absorption in bio-inspired structures. |  |
| [Jasiuk-Research-<br>Group/<br>CMDS-14-impact-<br>resistantance-NN-<br>prediction-](https://github.com/Jasiuk-Research-Group/CMDS-14-impact-resistantance-NN-prediction-)<br><sub>Python</sub><br><sub>none found</sub> | Neural networks for structure-property relations in impact-resistant structures. |  |
| [Jasiuk-Research-<br>Group/<br>LatticeResponse_<br>NN_Prediction](https://github.com/Jasiuk-Research-Group/LatticeResponse_NN_Prediction)<br><sub>Python</sub><br><sub>none found</sub> | Recurrent network prediction of lattice stress-strain curves and energy absorption. |  |
| [Jasiuk-Research-<br>Group/<br>S-DeepONet](https://github.com/Jasiuk-Research-Group/S-DeepONet)<br><sub>Python</sub><br><sub>none found</sub> | Sequential operator network with plasticity and heat transfer examples. |  |
| [Jasiuk-Research-<br>Group/<br>S-DeepONet-<br>transient-<br>predictions](https://github.com/Jasiuk-Research-Group/S-DeepONet-transient-predictions)<br><sub>Python</sub><br><sub>none found</sub> | Sequential operator network for transient full-field predictions, including plasticity. |  |
| [JinshuaiBai/<br>Discrete-Solution-<br>Operator-Learning-<br>DiSOL](https://github.com/JinshuaiBai/Discrete-Solution-Operator-Learning-DiSOL)<br><sub>Python and MATLAB</sub><br><sub>MIT</sub> | Discrete solution operator learning for geometry-dependent PDEs, including linear elasticity. | Training datasets are downloaded from Zenodo; MATLAB is used for data generation. |

## <a id="frameworks-and-introductory-studies"></a>14.7 Frameworks and introductory studies

| Name, language and license | Description | Note |
| --- | --- | --- |
| [hmjeon/<br>FEM-ML](https://github.com/hmjeon/FEM-ML)<br><sub>Jupyter Notebook</sub><br><sub>GPL-3.0</sub> | Experiments in finite element analysis with machine learning. | Sparse documentation. |
| [mimesis-inria/<br>DeepPhysX](https://github.com/mimesis-inria/DeepPhysX)<br><sub>Python</sub><br><sub>AGPL-3.0</sub> | Interface between numerical simulations and learning algorithms for training and prediction. |  |
| [oleksiyskononenko/<br>mlfem](https://github.com/oleksiyskononenko/mlfem)<br><sub>Jupyter Notebook</sub><br><sub>none found</sub> | Notebook and report on deep learning with finite element models of physical systems. |  |

## <a id="benchmark-datasets"></a>14.8 Benchmark datasets

| Name, language and license | Description | Note |
| --- | --- | --- |
| [elejeune11/<br>Mechanical-MNIST](https://github.com/elejeune11/Mechanical-MNIST)<br><sub>Python</sub><br><sub>MIT code, CC-BY-SA-3.0 data</sub> | Benchmark of 70,000 large-deformation finite element simulations for surrogate models. |  |

[← Back to the main list](../README.md#contents)
