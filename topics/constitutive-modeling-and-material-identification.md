# 9. Constitutive modeling and material identification

[← Back to the main list](../README.md#contents)

- [9.1 Neural network constitutive models](#neural-network-constitutive-models) (16)
- [9.2 Unsupervised model discovery](#unsupervised-model-discovery) (7)
- [9.3 Material subroutines and libraries](#material-subroutines-and-libraries) (10)
- [9.4 Experimental parameter identification](#experimental-parameter-identification) (6)

## <a id="neural-network-constitutive-models"></a>9.1 Neural network constitutive models

| Name, language and license | Description | Note |
| --- | --- | --- |
| [abuganza/<br>NN_aniso_UMAT](https://github.com/abuganza/NN_aniso_UMAT)<br><sub>Jupyter Notebook</sub><br><sub>GPL-3.0</sub> | Neural network models of anisotropic hyperelastic materials, with a UMAT. | Requires Abaqus for the UMAT. |
| [filippo-masi/<br>Thermodynamics-<br>Neural-Networks](https://github.com/filippo-masi/Thermodynamics-Neural-Networks)<br><sub>Jupyter Notebook and Python</sub><br><sub>MIT</sub> | Thermodynamics-based neural networks for inelastic constitutive modeling. |  |
| [FuhgJan/<br>Extreme<br>Sparsification<br>ConstitutiveLaws](https://github.com/FuhgJan/ExtremeSparsificationConstitutiveLaws)<br><sub>Python</sub><br><sub>GPL (stated in README)</sub> | Sparse physics-augmented neural networks for interpretable constitutive laws. |  |
| [FuhgJan/<br>invariant_DD_CM](https://github.com/FuhgJan/invariant_DD_CM)<br><sub>MATLAB</sub><br><sub>conflicting statements</sub> | Space-filling sampling of invariant space for data-driven constitutive models. | Requires MATLAB R2017a or later; README states both GPL-3.0 and a non-commercial Creative Commons license. |
| [FuhgJan/<br>modelDataDriven_<br>YieldFunction](https://github.com/FuhgJan/modelDataDriven_YieldFunction)<br><sub>Python</sub><br><sub>conflicting statements</sub> | Hybrid model-data-driven yield functions. | README states both GPL-3.0 and a non-commercial Creative Commons license. |
| [hyoungsuksuh/<br>ABAQUS_NN](https://github.com/hyoungsuksuh/ABAQUS_NN)<br><sub>Python</sub><br><sub>none found</sub> | PyTorch-to-UMAT framework for deep-learning level-set plasticity. | Requires Abaqus. |
| [LivingMatterLab/<br>CANN](https://github.com/LivingMatterLab/CANN)<br><sub>Jupyter Notebook</sub><br><sub>none found</sub> | Constitutive artificial neural networks for automated material model discovery. |  |
| [meghbali/<br>ANNElastoplasticity](https://github.com/meghbali/ANNElastoplasticity)<br><sub>Python</sub><br><sub>MIT</sub> | Neural network approach to elastoplastic constitutive modeling. |  |
| [nanogchen/<br>rnn-<br>viscoelasticity](https://github.com/nanogchen/rnn-viscoelasticity)<br><sub>Python</sub><br><sub>MIT</sub> | Recurrent neural networks that learn viscoelastic constitutive laws. | Paper code. |
| [pantale/<br>Algorithms-2023](https://github.com/pantale/Algorithms-2023)<br><sub>Fortran and Jupyter Notebook</sub><br><sub>GPL-3.0</sub> | Activation function comparison for neural flow laws in thermomechanical forming. | Requires Abaqus for the subroutines. |
| [pantale/<br>ANN-Constitutive<br>Law](https://github.com/pantale/ANN-ConstitutiveLaw)<br><sub>Jupyter Notebook</sub><br><sub>none found</sub> | Neural network flow laws for metals, implemented as VUHARD subroutines. | Requires Abaqus/Explicit for the subroutines. |
| [tajtac/<br>Anisotropic_NN_<br>UMAT](https://github.com/tajtac/Anisotropic_NN_UMAT)<br><sub>Jupyter Notebook and Fortran</sub><br><sub>none found</sub> | Neural network model of anisotropic soft tissue with a UMAT. | Requires Abaqus for the UMAT. |
| [tajtac/<br>hypermodelcomp](https://github.com/tajtac/hypermodelcomp)<br><sub>Jupyter Notebook</sub><br><sub>none found</sub> | Comparison of CANN, input-convex network and neural ODE models of hyperelasticity. |  |
| [tajtac/<br>node_diffusion](https://github.com/tajtac/node_diffusion)<br><sub>Jupyter Notebook</sub><br><sub>none found</sub> | Research notebooks combining neural ODE hyperelastic models with diffusion models. | No README. |
| [tajtac/<br>NODE_v2](https://github.com/tajtac/NODE_v2)<br><sub>Jupyter Notebook and Fortran</sub><br><sub>none found</sub> | Polyconvex strain energy functions from neural ODEs, with finite element examples. | LICENSE file is empty; finite element examples use Abaqus. |
| [tgulikers/<br>ABAQUS_ANN_<br>constitutive_model](https://github.com/tgulikers/ABAQUS_ANN_constitutive_model)<br><sub>Fortran</sub><br><sub>none found</sub> | Thesis code that trains neural network constitutive models and generates a UMAT. | Requires Abaqus for the UMAT. |

## <a id="unsupervised-model-discovery"></a>9.2 Unsupervised model discovery

| Name, language and license | Description | Note |
| --- | --- | --- |
| [EUCLID-code/<br>EUCLID-<br>hyperelasticity](https://github.com/EUCLID-code/EUCLID-hyperelasticity)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Unsupervised discovery of hyperelastic strain energy functions from full-field displacement data. |  |
| [EUCLID-code/<br>EUCLID-<br>hyperelasticity-<br>bayesian](https://github.com/EUCLID-code/EUCLID-hyperelasticity-bayesian)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Bayesian discovery of hyperelastic laws with uncertainty. |  |
| [EUCLID-code/<br>EUCLID-<br>hyperelasticity-NN](https://github.com/EUCLID-code/EUCLID-hyperelasticity-NN)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Neural network hyperelasticity learned without stress data. |  |
| [EUCLID-code/<br>EUCLID-<br>hyperelasticity-<br>PlaneStress-<br>ExperimentalData](https://github.com/EUCLID-code/EUCLID-hyperelasticity-PlaneStress-ExperimentalData)<br><sub>Python</sub><br><sub>none found</sub> | Discovery of plane-stress hyperelastic laws from experimental data. |  |
| [EUCLID-code/<br>EUCLID-plasticity](https://github.com/EUCLID-code/EUCLID-plasticity)<br><sub>MATLAB</sub><br><sub>GPL-3.0</sub> | Discovery of plasticity and generalized standard material models without stress data. | Written for MATLAB, Octave support not documented. |
| [EUCLID-code/<br>EUCLID-plasticity-<br>pressure-<br>sensitive-non-<br>associated](https://github.com/EUCLID-code/EUCLID-plasticity-pressure-sensitive-non-associated)<br><sub>MATLAB</sub><br><sub>none found</sub> | Discovery of non-associated pressure-sensitive plasticity models. | Written for MATLAB, Octave support not documented. |
| [EUCLID-code/<br>EUCLID-<br>viscoelasticity](https://github.com/EUCLID-code/EUCLID-viscoelasticity)<br><sub>MATLAB</sub><br><sub>GPL-3.0</sub> | Automated identification of linear viscoelastic laws. | Written for MATLAB, Octave support not documented. |

## <a id="material-subroutines-and-libraries"></a>9.3 Material subroutines and libraries

| Name, language and license | Description | Note |
| --- | --- | --- |
| [abuganza/<br>UMAT_anisotropic_<br>damage](https://github.com/abuganza/UMAT_anisotropic_damage)<br><sub>Fortran</sub><br><sub>GPL-3.0, with BSD-style file headers</sub> | Anisotropic damage subroutines for collagenous tissue fracture and needle insertion. | Requires Abaqus; no README. |
| [adtzlr/<br>hyperelastic](https://github.com/adtzlr/hyperelastic)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Building blocks for hyperelastic material formulations in FElupe. |  |
| [adtzlr/<br>matadi](https://github.com/adtzlr/matadi)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Hyperelastic material definitions with automatic differentiation. |  |
| [bleyerj/<br>dolfinx_materials](https://github.com/bleyerj/dolfinx_materials)<br><sub>Python</sub><br><sub>CC-BY-SA-4.0</sub> | Complex constitutive behaviors for FEniCSx. | MFront behaviors require TFEL. |
| [jgomezc1/<br>ABAQUS-US](https://github.com/jgomezc1/ABAQUS-US)<br><sub>Fortran</sub><br><sub>MIT</sub> | User element and user material subroutines, including classical and Cosserat elements. | Requires Abaqus. |
| [jpsferreira/<br>abaqus-material-<br>lab](https://github.com/jpsferreira/abaqus-material-lab)<br><sub>Fortran</sub><br><sub>GPL-3.0 (stated in README)</sub> | Composable UMAT and UEL framework for soft tissues and filament networks. | Requires Abaqus; no license file. |
| [jpsferreira/<br>UMAT-ABAQUS](https://github.com/jpsferreira/UMAT-ABAQUS)<br><sub>Fortran</sub><br><sub>GPL-3.0</sub> | Fortran framework for large-deformation material models, aimed at soft tissues and cells. | README invites non-commercial use, although the license is GPL-3.0. |
| [pantale/<br>abaqusVumat](https://github.com/pantale/abaqusVumat)<br><sub>Fortran</sub><br><sub>BSD-3-Clause</sub> | Johnson-Cook VUMAT subroutines. | Requires Abaqus/Explicit. |
| [SofaDefrost/<br>SofaViscoElastic](https://github.com/SofaDefrost/SofaViscoElastic)<br><sub>C++</sub><br><sub>LGPL-2.1</sub> | SOFA plugin for linear viscoelastic and visco-hyperelastic laws on tetrahedral meshes. | Requires SOFA. |
| [thelfer/<br>tfel](https://github.com/thelfer/tfel)<br><sub>C++</sub><br><sub>GPL with linking exception, or CeCILL-A</sub> | TFEL and MFront, a code generator for material knowledge and behavior laws. |  |

## <a id="experimental-parameter-identification"></a>9.4 Experimental parameter identification

| Name, language and license | Description | Note |
| --- | --- | --- |
| [BinChenOPEN/<br>FEMU-DIC](https://github.com/BinChenOPEN/FEMU-DIC)<br><sub>MATLAB</sub><br><sub>GPL-3.0</sub> | Digital image correlation and finite element model updating for strain measurement and parameter identification. | Requires MATLAB and COMSOL. |
| [dicengine/<br>dice](https://github.com/dicengine/dice)<br><sub>C++</sub><br><sub>BSD-3-Clause, with restricted Triangle code</sub> | Stereo digital image correlation engine for full-field displacements and strains. | Bundled Triangle restricts commercial distribution. |
| [lululxvi/<br>deep-learning-for-<br>indentation](https://github.com/lululxvi/deep-learning-for-indentation)<br><sub>Python</sub><br><sub>Apache-2.0</sub> | Extraction of material properties from instrumented indentation with deep learning. | Depends on DeepXDE. |
| [MultiDIC/<br>MultiDIC](https://github.com/MultiDIC/MultiDIC)<br><sub>MATLAB</sub><br><sub>Apache-2.0</sub> | Multi-view 3D digital image correlation toolbox. | Requires MATLAB with the Image Processing, Computer Vision and Statistics toolboxes. |
| [PolymerGuy/<br>muDIC](https://github.com/PolymerGuy/muDIC)<br><sub>Python</sub><br><sub>MIT</sub> | Python toolkit for digital image correlation and virtual experiments. |  |
| [vincentjzy/<br>OpenCorr](https://github.com/vincentjzy/OpenCorr)<br><sub>C++</sub><br><sub>MPL-2.0</sub> | Library for 2D, stereo and volumetric digital image correlation. |  |

[← Back to the main list](../README.md#contents)
