# Awesome Mechanical Simulation

A collection of public repositories for mechanical simulation: solid and structural mechanics, soft bodies, biomechanics, particle methods, and machine learning applied to them.

It lists 112 repositories, plus 4 archived or unmaintained ones in [archive.md](archive.md).

> **Before you rely on this list:** it started from one person's GitHub stars, so it is not complete. Descriptions were drafted with AI from README excerpts, file listings and repository metadata. The code was not run or validated, and a listing is not an endorsement. License labels are a convenience, not legal advice. "None found" means no license was found in the places checked, so do not assume you may reuse that code. Public does not always mean open source.

## Contents

- [Finite and boundary element methods](#finite-and-boundary-element-methods) (23)
- [Meshfree and particle methods](#meshfree-and-particle-methods) (9)
- [Soft-body, real-time and differentiable simulation](#soft-body-real-time-and-differentiable-simulation) (9)
- [Constitutive modeling and material identification](#constitutive-modeling-and-material-identification) (14)
- [Multiscale and homogenization](#multiscale-and-homogenization) (2)
- [Thermal, multiphysics and additive manufacturing](#thermal-multiphysics-and-additive-manufacturing) (6)
- [Optimization and inverse problems](#optimization-and-inverse-problems) (4)
- [Physics-informed learning and energy methods](#physics-informed-learning-and-energy-methods) (12)
- [Surrogates and reduced-order models](#surrogates-and-reduced-order-models) (18)
- [Meshing, pre- and post-processing](#meshing-pre--and-post-processing) (10)
- [Courses, references and agents for mechanics](#courses-references-and-agents-for-mechanics) (5)
- [Contributing](#contributing)

## Finite and boundary element methods

- [ansys/pymapdl](https://github.com/ansys/pymapdl) - Python interface to the Ansys MAPDL solver. _(Python; license: MIT)_ **Note:** Requires a licensed copy of Ansys.
- [AppliedMechanics-EAFIT/SolidsPy](https://github.com/AppliedMechanics-EAFIT/SolidsPy) - Simple finite element code for 2D elasticity. _(Python; license: MIT)_
- [dilevin/CSC417-a3-finite-elements-3d](https://github.com/dilevin/CSC417-a3-finite-elements-3d) - Course assignment on 3D finite element simulation of elastic objects. _(C++; license: none found)_ **Note:** Starter code for an assignment.
- [dmitryikh/nla3d](https://github.com/dmitryikh/nla3d) - C++ framework for writing nonlinear finite element codes in solid mechanics. _(C++; license: MIT)_
- [hplgit/fenics-tutorial](https://github.com/hplgit/fenics-tutorial) - Sources and example programs for the FEniCS Tutorial book. _(TeX; license: none found)_
- [isaar/MSolve](https://github.com/isaar/MSolve) - C# solver for computational mechanics problems. _(C#; license: Apache-2.0)_
- [jjcremmers/PyFEM](https://github.com/jjcremmers/PyFEM) - Educational and research finite element code for nonlinear solid mechanics. _(Python; license: MIT)_
- [JWock82/Pynite](https://github.com/JWock82/Pynite) - 3D structural analysis library with static, P-Delta, modal and pushover analysis. _(Python; license: MIT)_
- [largurajr/FEA-Protus](https://github.com/largurajr/FEA-Protus) - Teaching code for 2D plane stress and plane strain finite element analysis. _(Python; license: none found)_ **Note:** Python 2.7.
- [lcharleux/abapy](https://github.com/lcharleux/abapy) - Finite element pre- and post-processing in Python. _(Python; license: GPL-2.0)_ **Note:** No README.
- [liangbright/pytorch_fea_paper](https://github.com/liangbright/pytorch_fea_paper) - Differentiable finite element analysis applied to human aorta biomechanics. _(Python; license: none found)_ **Note:** Paper code.
- [lyc102/ifem](https://github.com/lyc102/ifem) - Adaptive finite element package for 2D and 3D simplicial grids. _(MATLAB; license: GPL-3.0)_ **Note:** Requires MATLAB.
- [mo-hanxuan/FEMcy](https://github.com/mo-hanxuan/FEMcy) - Taichi-based parallel structural finite element solver with small and large deformation. _(Python; license: MIT)_
- [nasa/NASTRAN-95](https://github.com/nasa/NASTRAN-95) - NASA's historical structural analysis system for static, dynamic and stability problems. _(Fortran; license: NASA Open Source Agreement 1.3)_ **Note:** No technical support.
- [Qinxiaoye/FEM3D-C3D8-](https://github.com/Qinxiaoye/FEM3D-C3D8-) - MATLAB finite element code with 3D hexahedral element routines. _(MATLAB; license: none found)_ **Note:** README calls it 2D; input scripts use Ansys or Abaqus.
- [Qinxiaoye/xpfem](https://github.com/Qinxiaoye/xpfem) - Linear elastic finite element package with quadrilateral, hexahedral and B-bar elements. _(Python; license: none found)_
- [sandialabs/optimism](https://github.com/sandialabs/optimism) - JAX finite element library that poses nonlinear solid mechanics as optimization. _(Python; license: MIT)_
- [sfepy/sfepy](https://github.com/sfepy/sfepy) - Finite element solver and library for coupled PDEs in 1D, 2D and 3D. _(Python; license: BSD-3-Clause)_
- [ShelvanLee/XFEM](https://github.com/ShelvanLee/XFEM) - Extended finite element program for multiple crack propagation in 2D linear elastic solids. _(MATLAB; license: MIT)_ **Note:** Requires MATLAB.
- [Terenceyuyue/varFEM](https://github.com/Terenceyuyue/varFEM) - Finite element programming in a variational-form style. _(MATLAB; license: GPL-3.0)_ **Note:** Requires MATLAB.
- [Timmmdavis/CutAndDisplace](https://github.com/Timmmdavis/CutAndDisplace) - Boundary element code for faults and deformation. _(MATLAB; license: GPL-3.0)_ **Note:** Requires MATLAB; README restricts use to academia, although the license is GPL-3.0.
- [tjfulle/fem-with-python](https://github.com/tjfulle/fem-with-python) - Course notes, assignments and code for an introductory finite element course. _(Python; license: MIT (stated in README))_
- [weihuayi/fealpy](https://github.com/weihuayi/fealpy) - Python finite element library for algorithm research and computer-aided engineering. _(Python; license: GPL-3.0-or-later with added notice)_ **Note:** License notice also restricts commercial use.

## Meshfree and particle methods

- [adevaucorbeil/karamelo](https://github.com/adevaucorbeil/karamelo) - Parallel material point method simulator with CPU and GPU support. _(C++; license: GPL-2.0)_ **Note:** GPU support is on a separate branch.
- [bcolloran/tlmpm](https://github.com/bcolloran/tlmpm) - Teaching implementation of the total Lagrangian material point method in Taichi. _(Python; license: none found)_
- [cb-geo/mpm](https://github.com/cb-geo/mpm) - High-performance material point method code for computational geomechanics. _(C++; license: MIT)_
- [iwf-inspire/mfree_iwf](https://github.com/iwf-inspire/mfree_iwf) - Comparison of meshless methods for large-deformation elastodynamics. _(C++; license: GPL-3.0)_ **Note:** Paper code.
- [pypr/pysph](https://github.com/pypr/pysph) - Smoothed particle hydrodynamics framework with OpenMP, OpenCL and MPI support. _(Python; license: BSD-3-Clause)_ **Note:** Some directories may carry other licenses.
- [saullocastro/meshless](https://github.com/saullocastro/meshless) - Meshless methods for computational mechanics, including ES-PIM. _(Python; license: BSD-2-Clause)_
- [Xiangyu-Hu/SPHinXsys](https://github.com/Xiangyu-Hu/SPHinXsys) - SPH-based multiphysics library for coupled simulation and optimization. _(C++; license: Apache-2.0)_
- [yuanming-hu/GPUMPM](https://github.com/yuanming-hu/GPUMPM) - GPU-optimized material point method from a SIGGRAPH Asia 2018 paper. _(license: GPL-3.0)_ **Note:** README asks commercial users to contact the authors.
- [yuanming-hu/taichi_mpm](https://github.com/yuanming-hu/taichi_mpm) - MLS-MPM solver with cutting and two-way rigid body coupling. _(C++; license: MIT)_

## Soft-body, real-time and differentiable simulation

- [hzaskywalker/PlasticineLab](https://github.com/hzaskywalker/PlasticineLab) - Differentiable physics benchmark for soft-body manipulation. _(Python; license: none found)_ **Note:** Only some bundled algorithm folders have license files.
- [jinaojakezhang/DJTLED](https://github.com/jinaojakezhang/DJTLED) - Direct-Jacobian explicit dynamics finite elements for real-time hyperelastic simulation. _(C++; license: MIT)_
- [NVlabs/DiSECt](https://github.com/NVlabs/DiSECt) - Differentiable finite element simulator for robotic cutting of deformable materials. _(Python; license: NVIDIA Source Code License (non-commercial))_ **Note:** Code and dataset are restricted to non-commercial use.
- [Q-Minh/position-based-dynamics](https://github.com/Q-Minh/position-based-dynamics) - Academic prototype of soft-body simulation with extended position-based dynamics. _(C++; license: BSL-1.0)_
- [SofaDefrost/CondensedFEMModel](https://github.com/SofaDefrost/CondensedFEMModel) - Learned condensed finite element models for soft robot control and design. _(Python; license: GPL-3.0)_ **Note:** Requires SOFA.
- [SofaDefrost/SoftRobots](https://github.com/SofaDefrost/SoftRobots) - SOFA components for modeling, actuating and controlling soft robots. _(C++; license: LGPL-3.0)_ **Note:** Requires SOFA.
- [taichi-dev/difftaichi](https://github.com/taichi-dev/difftaichi) - Examples of differentiable physical simulators written in Taichi. _(license: none found)_
- [taichi-dev/taichi](https://github.com/taichi-dev/taichi) - Parallel programming language in Python for simulation on CPUs and GPUs. _(C++; license: Apache-2.0)_
- [Xingyu-Lin/softgym](https://github.com/Xingyu-Lin/softgym) - Deformable object manipulation benchmarks for cloth, rope and fluid. _(C++; license: BSD-3-Clause)_ **Note:** Depends on NVIDIA FleX.

## Constitutive modeling and material identification

- [abuganza/NN_aniso_UMAT](https://github.com/abuganza/NN_aniso_UMAT) - Neural network models of anisotropic hyperelastic materials, with a UMAT. _(Jupyter Notebook; license: GPL-3.0)_ **Note:** Abaqus for the UMAT.
- [BinChenOPEN/FEMU-DIC](https://github.com/BinChenOPEN/FEMU-DIC) - Digital image correlation and finite element model updating for strain measurement and parameter identification. _(MATLAB; license: GPL-3.0)_ **Note:** Requires MATLAB and COMSOL.
- [EUCLID-code/EUCLID-hyperelasticity](https://github.com/EUCLID-code/EUCLID-hyperelasticity) - Unsupervised discovery of hyperelastic strain energy functions from full-field displacement data. _(HTML; license: GPL-3.0)_
- [hyoungsuksuh/ABAQUS_NN](https://github.com/hyoungsuksuh/ABAQUS_NN) - PyTorch-to-UMAT framework for deep-learning level-set plasticity. _(Python; license: none found)_ **Note:** Requires Abaqus.
- [jgomezc1/ABAQUS-US](https://github.com/jgomezc1/ABAQUS-US) - User element and user material subroutines, including classical and Cosserat elements. _(Fortran; license: MIT)_ **Note:** Requires Abaqus.
- [jpsferreira/UMAT-ABAQUS](https://github.com/jpsferreira/UMAT-ABAQUS) - Fortran framework for large-deformation material models, aimed at soft tissues and cells. _(Fortran; license: GPL-3.0)_ **Note:** README invites non-commercial use, although the license is GPL-3.0.
- [LivingMatterLab/CANN](https://github.com/LivingMatterLab/CANN) - Constitutive artificial neural networks for automated material model discovery. _(Jupyter Notebook; license: none found)_
- [lululxvi/deep-learning-for-indentation](https://github.com/lululxvi/deep-learning-for-indentation) - Extraction of material properties from instrumented indentation with deep learning. _(Python; license: Apache-2.0)_ **Note:** Depends on DeepXDE.
- [meghbali/ANNElastoplasticity](https://github.com/meghbali/ANNElastoplasticity) - Neural network approach to elastoplastic constitutive modeling. _(Python; license: MIT)_
- [pantale/ANN-ConstitutiveLaw](https://github.com/pantale/ANN-ConstitutiveLaw) - Neural network flow laws for metals, implemented as VUHARD subroutines. _(Jupyter Notebook; license: none found)_ **Note:** Abaqus/Explicit for the subroutines.
- [SofaDefrost/SofaViscoElastic](https://github.com/SofaDefrost/SofaViscoElastic) - SOFA plugin for linear viscoelastic and visco-hyperelastic laws on tetrahedral meshes. _(C++; license: LGPL-2.1)_ **Note:** Requires SOFA.
- [tajtac/hypermodelcomp](https://github.com/tajtac/hypermodelcomp) - Comparison of CANN, input-convex network and neural ODE models of hyperelasticity. _(Jupyter Notebook; license: none found)_
- [tajtac/node_diffusion](https://github.com/tajtac/node_diffusion) - Research notebooks combining neural ODE hyperelastic models with diffusion models. _(Jupyter Notebook; license: none found)_ **Note:** No README.
- [tgulikers/ABAQUS_ANN_constitutive_model](https://github.com/tgulikers/ABAQUS_ANN_constitutive_model) - Thesis code that trains neural network constitutive models and generates a UMAT. _(Fortran; license: none found)_ **Note:** Abaqus for the UMAT.

## Multiscale and homogenization

- [tdegeus/GooseFFT](https://github.com/tdegeus/GooseFFT) - Small teaching scripts for FFT-based micromechanical solvers. _(Python; license: MIT)_
- [vondrejc/FFTHomPy](https://github.com/vondrejc/FFTHomPy) - FFT-based homogenization with guaranteed bounds on effective properties. _(Python; license: MIT)_

## Thermal, multiphysics and additive manufacturing

- [CMSL-HKUST/jax-am](https://github.com/CMSL-HKUST/jax-am) - Differentiable GPU toolbox for additive manufacturing process, structure and property simulation. _(Jupyter Notebook; license: GPL-3.0)_
- [jinaojakezhang/FEDFEM](https://github.com/jinaojakezhang/FEDFEM) - Fast explicit dynamics finite elements for transient heat transfer. _(C++; license: MIT)_
- [jinaojakezhang/FEDFEMBioheat](https://github.com/jinaojakezhang/FEDFEMBioheat) - Real-time bio-heat transfer with fast explicit dynamics finite elements. _(C++; license: MIT)_
- [jinaojakezhang/FEDFEMBioheatDamage](https://github.com/jinaojakezhang/FEDFEMBioheatDamage) - CEM43 thermal damage added to real-time bio-heat simulation. _(C++; license: MIT)_
- [jinaojakezhang/FEDFEMBioheatDeform](https://github.com/jinaojakezhang/FEDFEMBioheatDeform) - Soft tissue thermal response under deformation for surgical simulation. _(C++; license: MIT)_
- [jinaojakezhang/FEDFEMBioheatExpan](https://github.com/jinaojakezhang/FEDFEMBioheatExpan) - Anisotropic thermo-visco-elastodynamics of soft tissue for ablation therapy. _(C++; license: MIT)_

## Optimization and inverse problems

- [deng-cy/deep_learning_topology_opt](https://github.com/deng-cy/deep_learning_topology_opt) - Self-directed online learning for topology optimization. _(MATLAB; license: MIT)_ **Note:** Most examples need MATLAB and COMSOL.
- [gigatskhondia/gigala](https://github.com/gigatskhondia/gigala) - Structural topology optimization with reinforcement learning, genetic algorithms and finite elements. _(Jupyter Notebook; license: MIT)_
- [kailaix/PhysGNN](https://github.com/kailaix/PhysGNN) - Physics-constrained generative networks, including a stochastic elasticity example. _(Julia; license: none found)_
- [nandakishorebm1995/FOR3022_Code](https://github.com/nandakishorebm1995/FOR3022_Code) - Bayesian damage identification in fiber metal laminates with model order reduction. _(MATLAB; license: none found)_ **Note:** Requires MATLAB and COMSOL.

## Physics-informed learning and energy methods

- [ehsanhaghighat/sciann-applications](https://github.com/ehsanhaghighat/sciann-applications) - SciANN examples, including elasticity, elastoplasticity, vibration and poroelasticity. _(Jupyter Notebook; license: MIT)_ **Note:** SciANN itself is unmaintained.
- [FuhgJan/mixedDEM](https://github.com/FuhgJan/mixedDEM) - Mixed deep energy method for stress concentrations in finite-strain hyperelasticity. _(Python; license: conflicting statements)_ **Note:** README states both GPL-3.0 and a non-commercial Creative Commons license.
- [ISM-Weimar/DeepEnergyMethods](https://github.com/ISM-Weimar/DeepEnergyMethods) - Companion code for energy-based deep learning solutions of PDEs in mechanics. _(Python; license: MIT)_
- [Jasiuk-Research-Group/DEM_for_J2_plasticity](https://github.com/Jasiuk-Research-Group/DEM_for_J2_plasticity) - Deep energy method for 3D J2 elastoplasticity. _(Python; license: MIT)_
- [Jasiuk-Research-Group/Graph_DEM](https://github.com/Jasiuk-Research-Group/Graph_DEM) - Comparison of graph convolution and MLP deep energy methods for elastic solids. _(Python; license: none found)_
- [JinshuaiBai/LSWR_loss_function_PINN](https://github.com/JinshuaiBai/LSWR_loss_function_PINN) - Least squares weighted residual loss for PINN solid mechanics. _(Python; license: none found)_
- [JinshuaiBai/PINN_Comp_Mech](https://github.com/JinshuaiBai/PINN_Comp_Mech) - Introductory PINN examples in solid mechanics with collocation and energy losses. _(Python; license: none found)_
- [JinshuaiBai/PIRBN](https://github.com/JinshuaiBai/PIRBN) - Physics-informed radial basis networks with spring, wave and viscoelastic flow examples. _(Python; license: none found)_
- [lululxvi/deepxde](https://github.com/lululxvi/deepxde) - Library for physics-informed learning of forward and inverse differential equation problems. _(Python; license: LGPL-2.1)_
- [MinhNguyenIKM/dem_hyperelasticity](https://github.com/MinhNguyenIKM/dem_hyperelasticity) - Deep energy method for finite-deformation hyperelasticity. _(Python; license: none found)_
- [Raocp/PINN-elastodynamics](https://github.com/Raocp/PINN-elastodynamics) - Physics-informed networks for elastodynamics without labeled data. _(Python; license: none found)_
- [yizheng-wang/Research-on-Solving-Partial-Differential-Equations-of-Solid-Mechanics-Based-on-PINN](https://github.com/yizheng-wang/Research-on-Solving-Partial-Differential-Equations-of-Solid-Mechanics-Based-on-PINN) - Thesis code for solid mechanics with deep energy, CENN, DCEM and KINN methods. _(Python; license: none found)_

## Surrogates and reduced-order models

- [AlbanOdot/DeepPhysics-article](https://github.com/AlbanOdot/DeepPhysics-article) - Paper code for physics-aware deep learning in real-time simulation. _(Python; license: CC0-1.0)_
- [dabiriyaghoub/Ventricular_ML_DecisionTrees](https://github.com/dabiriyaghoub/Ventricular_ML_DecisionTrees) - Machine learning prediction of left ventricular mechanics. _(Python; license: all rights reserved)_
- [farazarbabi/CNN_FEM](https://github.com/farazarbabi/CNN_FEM) - Convolutional network prediction of stress fields in solids from simulation data. _(Python; license: none found)_
- [federicosanna/UNet-for-FEM-and-Stress-Distribution-Inference](https://github.com/federicosanna/UNet-for-FEM-and-Stress-Distribution-Inference) - U-Net inference of stress distributions from finite element data. _(Python; license: none found)_ **Note:** Some trained models are not included.
- [hmjeon/FEM-ML](https://github.com/hmjeon/FEM-ML) - Experiments in finite element analysis with machine learning. _(Jupyter Notebook; license: GPL-3.0)_ **Note:** Sparse documentation.
- [Jianxun-Wang/graphGalerkin](https://github.com/Jianxun-Wang/graphGalerkin) - Physics-informed graph neural Galerkin networks for forward and inverse PDE problems. _(Python; license: GPL-3.0)_ **Note:** Requires pyCaMOtk.
- [lawsonfulton/AutoDef](https://github.com/lawsonfulton/AutoDef) - Latent-space dynamics for reduced deformable simulation. _(C++; license: MIT)_ **Note:** Install script can overwrite your Keras configuration.
- [lrquad/NNWarp](https://github.com/lrquad/NNWarp) - Neural network-based nonlinear deformable simulator. _(C++; license: MIT)_
- [m-ulmestrand/gcn-collisions](https://github.com/m-ulmestrand/gcn-collisions) - Graph convolutional network that learns particle collision responses. _(Python; license: Apache-2.0)_
- [michetonu/MALTIDEM--Machine-Learning-for-Tissue-Deformation-Modelling](https://github.com/michetonu/MALTIDEM--Machine-Learning-for-Tissue-Deformation-Modelling) - Data-driven real-time model of brain tumor deformation for neurosurgery. _(MATLAB; license: none found)_ **Note:** Workflow uses MATLAB and FEBio.
- [mimesis-inria/DeepPhysX](https://github.com/mimesis-inria/DeepPhysX) - Interface between numerical simulations and learning algorithms for training and prediction. _(Python; license: AGPL-3.0)_
- [oleksiyskononenko/mlfem](https://github.com/oleksiyskononenko/mlfem) - Notebook and report on deep learning with finite element models of physical systems. _(Jupyter Notebook; license: none found)_
- [saurabhdeshpande93/convolution-aggregation-attention](https://github.com/saurabhdeshpande93/convolution-aggregation-attention) - CNN, graph and attention surrogates for nonlinear finite element simulations. _(Mathematica; license: MIT)_ **Note:** Data generation uses AceFEM.
- [TML-Gatech/DL_Stress_TAA](https://github.com/TML-Gatech/DL_Stress_TAA) - Deep learning surrogate of finite element stress analysis. _(license: all rights reserved)_ **Note:** Source files are supplied as PDFs.
- [vividda/3D-PhysNet](https://github.com/vividda/3D-PhysNet) - Learned prediction of non-rigid 3D object deformation. _(Python; license: none found)_ **Note:** Python 2.7.
- [wwMark/meshgraphnets](https://github.com/wwMark/meshgraphnets) - PyTorch port of MeshGraphNets with cloth simulation. _(Python; license: none found)_ **Note:** Author says results do not fully match the original.
- [YasminSalehi/PhysGNN](https://github.com/YasminSalehi/PhysGNN) - Graph neural network prediction of soft tissue deformation in neurosurgery. _(Python; license: BSD-4-Clause)_
- [zhenguonie/stress_net](https://github.com/zhenguonie/stress_net) - Convolutional prediction of stress fields in cantilevered structures. _(Python; license: none found)_

## Meshing, pre- and post-processing

- [inducer/meshpy](https://github.com/inducer/meshpy) - Python interfaces to the Triangle and TetGen mesh generators. _(C++; license: mixed, including Triangle and AGPL-3.0)_ **Note:** Triangle restricts commercial distribution.
- [Liujie-SYSU/odb2vtk](https://github.com/Liujie-SYSU/odb2vtk) - Converter from Abaqus ODB results to VTK for ParaView. _(Python; license: none found)_ **Note:** Input is Abaqus output.
- [meshpro/meshplex](https://github.com/meshpro/meshplex) - Geometric quantities such as areas and volumes for simplex meshes. _(license: proprietary)_ **Note:** No source in the repository; full use requires a paid license.
- [meshpro/meshzoo](https://github.com/meshpro/meshzoo) - Generators of meshes for simple canonical domains. _(license: none found)_ **Note:** No source in the repository.
- [meshpro/pygalmesh](https://github.com/meshpro/pygalmesh) - Python front end to CGAL's 2D and 3D mesh generators. _(C++; license: GPL-3.0)_ **Note:** Commercial license offered separately.
- [mikedh/trimesh](https://github.com/mikedh/trimesh) - Python library for loading, editing and analyzing triangular meshes. _(Python; license: MIT)_
- [nschloe/meshio](https://github.com/nschloe/meshio) - Reader, writer and converter for many mesh file formats. _(Python; license: MIT)_
- [nschloe/pygmsh](https://github.com/nschloe/pygmsh) - Python abstractions for building geometries and meshes with Gmsh. _(Python; license: GPL-3.0)_
- [paulo-herrera/PyEVTK](https://github.com/paulo-herrera/PyEVTK) - Pure-Python export of data to binary VTK files. _(Python; license: MIT (stated in source))_
- [pyvista/pyvista](https://github.com/pyvista/pyvista) - 3D visualization and mesh analysis with a NumPy-based interface. _(Python; license: MIT)_

## Courses, references and agents for mechanics

- [Ceyron/machine-learning-and-simulation](https://github.com/Ceyron/machine-learning-and-simulation) - Notes and code for a video course on simulation and machine learning, including continuum mechanics and FEniCS. _(Jupyter Notebook; license: MIT)_
- [lamm-mit/MechAgents](https://github.com/lamm-mit/MechAgents) - Multi-agent language model workflows for solving mechanics problems numerically. _(Jupyter Notebook; license: Apache-2.0)_
- [ltt1598/GAMES_Xi-an_forward_physics](https://github.com/ltt1598/GAMES_Xi-an_forward_physics) - Notes and Taichi sample code from a physically based simulation course. _(license: none found)_
- [nschloe/awesome-scientific-computing](https://github.com/nschloe/awesome-scientific-computing) - Curated list of scientific computing tools, including finite element and meshing software. _(Python; license: CC0-1.0)_
- [thunil/Physics-Based-Deep-Learning](https://github.com/thunil/Physics-Based-Deep-Learning) - Curated list of research on physics-based deep learning. _(license: none found)_

## Contributing

Corrections and additions are welcome. See [contributing.md](contributing.md).
