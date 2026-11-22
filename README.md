# Awesome Computational Mechanics and AI

**549 entries for computational mechanics, from finite elements and soft tissue to AI-coupled CFD, LLM agents, solvers and validation**, with licenses, commercial-software requirements and known usage restrictions noted.

<p align="center">
<img src="assets/banner.png" width="420" alt="A soft cube with circular cuts at 0, 25 and 50 mm of stretch, colored by displacement">
<br>
<sub>Soft-tissue cube simulated with <a href="https://github.com/x9m/JANP-DJTLED-GPU">JANP-DJTLED</a> (<a href="assets/LICENSE">MIT</a>)</sub>
</p>

## Start here

| I want to | Start with | Then browse |
| --- | --- | --- |
| Learn finite elements | [Imperial College course](https://github.com/finite-element/finite-element-course) | [Teaching and compact codes](topics/finite-and-boundary-element-methods.md#teaching-and-compact-codes) |
| Write a solver in Python | [scikit-fem](https://github.com/kinnala/scikit-fem) | [General-purpose frameworks](topics/finite-and-boundary-element-methods.md#general-purpose-frameworks) |
| Simulate soft tissue | [FEBio](https://github.com/febiosoftware/FEBio) | [Real-time finite elements](topics/soft-body-real-time-and-differentiable-simulation.md#real-time-finite-elements) |
| Model contact | [IPC Toolkit](https://github.com/ipc-sim/ipc-toolkit) | [Contact mechanics](topics/contact-mechanics.md) |
| Learn material laws from data | [EUCLID](https://github.com/EUCLID-code/EUCLID-hyperelasticity) | [Unsupervised model discovery](topics/constitutive-modeling-and-material-identification.md#unsupervised-model-discovery) |
| Try virtual elements | [50 lines of VEM](https://github.com/oliversutton/50LinesOfVEM) | [Virtual element method](topics/virtual-element-method.md) |
| Solve large systems | [PETSc](https://gitlab.com/petsc/petsc) | [Linear, eigenvalue and nonlinear solvers](topics/linear-eigenvalue-and-nonlinear-solvers.md) |
| Combine AI with CFD | [TU Dresden course](https://github.com/AndreWeiner/ml-cfd-lecture) | [Hybrid AI and computational fluid dynamics](topics/hybrid-ai-and-computational-fluid-dynamics.md) |
| Verify and validate a model | [SimEval](https://github.com/OSEL-DAM/SimEval) | [Verification, validation and uncertainty](topics/verification-validation-and-uncertainty.md) |

## Contents

1. [Finite and boundary element methods](topics/finite-and-boundary-element-methods.md) (76)
2. [Finite volume methods](topics/finite-volume-methods.md) (9)
3. [Virtual element method](topics/virtual-element-method.md) (30)
4. [Contact mechanics](topics/contact-mechanics.md) (9)
5. [Third medium contact](topics/third-medium-contact.md) (12)
6. [Meshfree and particle methods](topics/meshfree-and-particle-methods.md) (28)
7. [Soft-body, real-time and differentiable simulation](topics/soft-body-real-time-and-differentiable-simulation.md) (26)
8. [Multibody dynamics and biomechanics](topics/multibody-dynamics-and-biomechanics.md) (10)
9. [Constitutive modeling and material identification](topics/constitutive-modeling-and-material-identification.md) (39)
10. [Multiscale and homogenization](topics/multiscale-and-homogenization.md) (15)
11. [Thermal, multiphysics and additive manufacturing](topics/thermal-multiphysics-and-additive-manufacturing.md) (11)
12. [Optimization and inverse problems](topics/optimization-and-inverse-problems.md) (18)
13. [Physics-informed learning and energy methods](topics/physics-informed-learning-and-energy-methods.md) (17)
14. [Surrogates and reduced-order models](topics/surrogates-and-reduced-order-models.md) (49)
15. [Hybrid AI and numerical solvers](topics/hybrid-ai-and-numerical-solvers.md) (30)
16. [Hybrid AI and computational fluid dynamics](topics/hybrid-ai-and-computational-fluid-dynamics.md) (31)
17. [LLMs and simulation agents](topics/llms-and-simulation-agents.md) (22)
18. [Meshing, pre- and post-processing](topics/meshing-pre--and-post-processing.md) (20)
19. [Linear, eigenvalue and nonlinear solvers](topics/linear-eigenvalue-and-nonlinear-solvers.md) (35)
20. [Verification, validation and uncertainty](topics/verification-validation-and-uncertainty.md) (33)
21. [Courses and references](topics/courses-references-and-agents-for-mechanics.md) (29)

<details>
<summary>All 99 sub-topics</summary>

1. <a id="finite-and-boundary-element-methods"></a><a id="open-finite-and-boundary-element-methods"></a>[Finite and boundary element methods](topics/finite-and-boundary-element-methods.md) (76)<br>
   1.1 <a id="general-purpose-frameworks"></a><a id="open-finite-and-boundary-element-methods--general-purpose-frameworks"></a>[General-purpose frameworks](topics/finite-and-boundary-element-methods.md#general-purpose-frameworks) (20)<br>
   1.2 <a id="structural-and-solid-mechanics-solvers"></a><a id="open-finite-and-boundary-element-methods--structural-and-solid-mechanics-solvers"></a>[Structural and solid mechanics solvers](topics/finite-and-boundary-element-methods.md#structural-and-solid-mechanics-solvers) (16)<br>
   1.3 <a id="differentiable-and-gpu-finite-elements"></a><a id="open-finite-and-boundary-element-methods--differentiable-and-gpu-finite-elements"></a>[Differentiable and GPU finite elements](topics/finite-and-boundary-element-methods.md#differentiable-and-gpu-finite-elements) (6)<br>
   1.4 <a id="phase-field-fracture"></a><a id="open-finite-and-boundary-element-methods--phase-field-fracture"></a>[Phase-field fracture](topics/finite-and-boundary-element-methods.md#phase-field-fracture) (6)<br>
   1.5 <a id="fracture-boundary-and-scaled-boundary-methods"></a><a id="open-finite-and-boundary-element-methods--fracture-boundary-and-scaled-boundary-methods"></a>[Fracture, boundary and scaled boundary methods](topics/finite-and-boundary-element-methods.md#fracture-boundary-and-scaled-boundary-methods) (5)<br>
   1.6 <a id="unfitted-and-embedded-methods"></a><a id="open-finite-and-boundary-element-methods--unfitted-and-embedded-methods"></a>[Unfitted and embedded methods](topics/finite-and-boundary-element-methods.md#unfitted-and-embedded-methods) (1)<br>
   1.7 <a id="smoothed-finite-elements"></a><a id="open-finite-and-boundary-element-methods--smoothed-finite-elements"></a>[Smoothed finite elements](topics/finite-and-boundary-element-methods.md#smoothed-finite-elements) (1)<br>
   1.8 <a id="beams-rods-and-shells"></a><a id="open-finite-and-boundary-element-methods--beams-rods-and-shells"></a>[Beams, rods and shells](topics/finite-and-boundary-element-methods.md#beams-rods-and-shells) (3)<br>
   1.9 <a id="solver-interfaces-and-utilities"></a><a id="open-finite-and-boundary-element-methods--solver-interfaces-and-utilities"></a>[Solver interfaces and utilities](topics/finite-and-boundary-element-methods.md#solver-interfaces-and-utilities) (5)<br>
   1.10 <a id="teaching-and-compact-codes"></a><a id="open-finite-and-boundary-element-methods--teaching-and-compact-codes"></a>[Teaching and compact codes](topics/finite-and-boundary-element-methods.md#teaching-and-compact-codes) (13)
2. <a id="finite-volume-methods"></a><a id="open-finite-volume-methods"></a>[Finite volume methods](topics/finite-volume-methods.md) (9)<br>
   2.1 <a id="solid-mechanics-and-fluid-solid-interaction"></a><a id="open-finite-volume-methods--solid-mechanics-and-fluid-solid-interaction"></a>[Solid mechanics and fluid-solid interaction](topics/finite-volume-methods.md#solid-mechanics-and-fluid-solid-interaction) (6)<br>
   2.2 [Porous media and geomechanics](topics/finite-volume-methods.md#porous-media-and-geomechanics) (3)
3. <a id="virtual-element-method"></a><a id="open-virtual-element-method"></a>[Virtual element method](topics/virtual-element-method.md) (30)<br>
   3.1 <a id="vem-libraries"></a><a id="open-virtual-element-method--vem-libraries"></a>[VEM libraries](topics/virtual-element-method.md#vem-libraries) (6)<br>
   3.2 <a id="elasticity"></a><a id="open-virtual-element-method--elasticity"></a>[Elasticity](topics/virtual-element-method.md#elasticity) (9)<br>
   3.3 <a id="dynamics-and-fracture"></a><a id="open-virtual-element-method--dynamics-and-fracture"></a>[Dynamics and fracture](topics/virtual-element-method.md#dynamics-and-fracture) (3)<br>
   3.4 <a id="coupled-fields-and-electronic-packaging"></a><a id="open-virtual-element-method--coupled-fields-and-electronic-packaging"></a>[Coupled fields and electronic packaging](topics/virtual-element-method.md#coupled-fields-and-electronic-packaging) (4)<br>
   3.5 <a id="topology-optimization-with-vem"></a><a id="open-virtual-element-method--topology-optimization-with-vem"></a>[Topology optimization with VEM](topics/virtual-element-method.md#topology-optimization-with-vem) (2)<br>
   3.6 <a id="introductory-vem-codes"></a><a id="open-virtual-element-method--introductory-vem-codes"></a>[Introductory VEM codes](topics/virtual-element-method.md#introductory-vem-codes) (6)
4. <a id="contact-mechanics"></a><a id="open-contact-mechanics"></a>[Contact mechanics](topics/contact-mechanics.md) (9)<br>
   4.1 <a id="contact-formulations"></a><a id="open-contact-mechanics--contact-formulations"></a>[Contact formulations](topics/contact-mechanics.md#contact-formulations) (4)<br>
   4.2 <a id="incremental-potential-contact"></a><a id="open-contact-mechanics--incremental-potential-contact"></a>[Incremental potential contact](topics/contact-mechanics.md#incremental-potential-contact) (5)
5. <a id="third-medium-contact"></a><a id="open-third-medium-contact"></a>[Third medium contact](topics/third-medium-contact.md) (12)<br>
   5.1 <a id="modules-and-examples-in-fem-libraries"></a><a id="open-third-medium-contact--modules-and-examples-in-fem-libraries"></a>[Modules and examples in FEM libraries](topics/third-medium-contact.md#modules-and-examples-in-fem-libraries) (7)<br>
   5.2 <a id="optimization-and-metamaterials"></a><a id="open-third-medium-contact--optimization-and-metamaterials"></a>[Optimization and metamaterials](topics/third-medium-contact.md#optimization-and-metamaterials) (4)<br>
   5.3 <a id="standalone-study-codes"></a><a id="open-third-medium-contact--standalone-study-codes"></a>[Standalone study codes](topics/third-medium-contact.md#standalone-study-codes) (1)
6. <a id="meshfree-and-particle-methods"></a><a id="open-meshfree-and-particle-methods"></a>[Meshfree and particle methods](topics/meshfree-and-particle-methods.md) (28)<br>
   6.1 <a id="material-point-method"></a><a id="open-meshfree-and-particle-methods--material-point-method"></a>[Material point method](topics/meshfree-and-particle-methods.md#material-point-method) (11)<br>
   6.2 <a id="smoothed-particle-hydrodynamics"></a><a id="open-meshfree-and-particle-methods--smoothed-particle-hydrodynamics"></a>[Smoothed particle hydrodynamics](topics/meshfree-and-particle-methods.md#smoothed-particle-hydrodynamics) (4)<br>
   6.3 <a id="meshless-methods"></a><a id="open-meshfree-and-particle-methods--meshless-methods"></a>[Meshless methods](topics/meshfree-and-particle-methods.md#meshless-methods) (5)<br>
   6.4 <a id="peridynamics"></a><a id="open-meshfree-and-particle-methods--peridynamics"></a>[Peridynamics](topics/meshfree-and-particle-methods.md#peridynamics) (3)<br>
   6.5 <a id="discrete-and-coarse-grained-particle-models"></a><a id="open-meshfree-and-particle-methods--discrete-and-coarse-grained-particle-models"></a>[Discrete and coarse-grained particle models](topics/meshfree-and-particle-methods.md#discrete-and-coarse-grained-particle-models) (5)
7. <a id="soft-body-real-time-and-differentiable-simulation"></a><a id="open-soft-body-real-time-and-differentiable-simulation"></a>[Soft-body, real-time and differentiable simulation](topics/soft-body-real-time-and-differentiable-simulation.md) (26)<br>
   7.1 <a id="real-time-finite-elements"></a><a id="open-soft-body-real-time-and-differentiable-simulation--real-time-finite-elements"></a>[Real-time finite elements](topics/soft-body-real-time-and-differentiable-simulation.md#real-time-finite-elements) (7)<br>
   7.2 <a id="soft-robotics"></a><a id="open-soft-body-real-time-and-differentiable-simulation--soft-robotics"></a>[Soft robotics](topics/soft-body-real-time-and-differentiable-simulation.md#soft-robotics) (6)<br>
   7.3 <a id="position-based-and-implicit-dynamics"></a><a id="open-soft-body-real-time-and-differentiable-simulation--position-based-and-implicit-dynamics"></a>[Position-based and implicit dynamics](topics/soft-body-real-time-and-differentiable-simulation.md#position-based-and-implicit-dynamics) (4)<br>
   7.4 <a id="differentiable-simulation"></a><a id="open-soft-body-real-time-and-differentiable-simulation--differentiable-simulation"></a>[Differentiable simulation](topics/soft-body-real-time-and-differentiable-simulation.md#differentiable-simulation) (6)<br>
   7.5 <a id="manipulation-benchmarks"></a><a id="open-soft-body-real-time-and-differentiable-simulation--manipulation-benchmarks"></a>[Manipulation benchmarks](topics/soft-body-real-time-and-differentiable-simulation.md#manipulation-benchmarks) (3)
8. <a id="multibody-dynamics-and-biomechanics"></a><a id="open-multibody-dynamics-and-biomechanics"></a>[Multibody dynamics and biomechanics](topics/multibody-dynamics-and-biomechanics.md) (10)<br>
   8.1 <a id="physics-engines-for-multibody-systems"></a><a id="open-multibody-dynamics-and-biomechanics--physics-engines-for-multibody-systems"></a>[Physics engines for multibody systems](topics/multibody-dynamics-and-biomechanics.md#physics-engines-for-multibody-systems) (6)<br>
   8.2 <a id="musculoskeletal-biomechanics"></a><a id="open-multibody-dynamics-and-biomechanics--musculoskeletal-biomechanics"></a>[Musculoskeletal biomechanics](topics/multibody-dynamics-and-biomechanics.md#musculoskeletal-biomechanics) (2)<br>
   8.3 <a id="cardiovascular-mechanics"></a><a id="open-multibody-dynamics-and-biomechanics--cardiovascular-mechanics"></a>[Cardiovascular mechanics](topics/multibody-dynamics-and-biomechanics.md#cardiovascular-mechanics) (2)
9. <a id="constitutive-modeling-and-material-identification"></a><a id="open-constitutive-modeling-and-material-identification"></a>[Constitutive modeling and material identification](topics/constitutive-modeling-and-material-identification.md) (39)<br>
   9.1 <a id="neural-network-constitutive-models"></a><a id="open-constitutive-modeling-and-material-identification--neural-network-constitutive-models"></a>[Neural network constitutive models](topics/constitutive-modeling-and-material-identification.md#neural-network-constitutive-models) (16)<br>
   9.2 <a id="unsupervised-model-discovery"></a><a id="open-constitutive-modeling-and-material-identification--unsupervised-model-discovery"></a>[Unsupervised model discovery](topics/constitutive-modeling-and-material-identification.md#unsupervised-model-discovery) (7)<br>
   9.3 <a id="material-subroutines-and-libraries"></a><a id="open-constitutive-modeling-and-material-identification--material-subroutines-and-libraries"></a>[Material subroutines and libraries](topics/constitutive-modeling-and-material-identification.md#material-subroutines-and-libraries) (10)<br>
   9.4 <a id="experimental-parameter-identification"></a><a id="open-constitutive-modeling-and-material-identification--experimental-parameter-identification"></a>[Experimental parameter identification](topics/constitutive-modeling-and-material-identification.md#experimental-parameter-identification) (6)
10. <a id="multiscale-and-homogenization"></a><a id="open-multiscale-and-homogenization"></a>[Multiscale and homogenization](topics/multiscale-and-homogenization.md) (15)<br>
    10.1 <a id="fft-based-homogenization"></a><a id="open-multiscale-and-homogenization--fft-based-homogenization"></a>[FFT-based homogenization](topics/multiscale-and-homogenization.md#fft-based-homogenization) (3)<br>
    10.2 <a id="fe-and-computational-homogenization"></a><a id="open-multiscale-and-homogenization--fe2-and-computational-homogenization"></a>[FE² and computational homogenization](topics/multiscale-and-homogenization.md#fe2-and-computational-homogenization) (3)<br>
    10.3 <a id="inverse-homogenization"></a><a id="open-multiscale-and-homogenization--inverse-homogenization"></a>[Inverse homogenization](topics/multiscale-and-homogenization.md#inverse-homogenization) (1)<br>
    10.4 [Machine learning for multiscale simulation](topics/multiscale-and-homogenization.md#machine-learning-for-multiscale-simulation) (3)<br>
    10.5 <a id="crystal-plasticity"></a><a id="open-multiscale-and-homogenization--crystal-plasticity"></a>[Crystal plasticity](topics/multiscale-and-homogenization.md#crystal-plasticity) (5)
11. <a id="thermal-multiphysics-and-additive-manufacturing"></a><a id="open-thermal-multiphysics-and-additive-manufacturing"></a>[Thermal, multiphysics and additive manufacturing](topics/thermal-multiphysics-and-additive-manufacturing.md) (11)<br>
    11.1 <a id="heat-transfer-and-bio-heat"></a><a id="open-thermal-multiphysics-and-additive-manufacturing--heat-transfer-and-bio-heat"></a>[Heat transfer and bio-heat](topics/thermal-multiphysics-and-additive-manufacturing.md#heat-transfer-and-bio-heat) (5)<br>
    11.2 <a id="thermoelasticity"></a><a id="open-thermal-multiphysics-and-additive-manufacturing--thermoelasticity"></a>[Thermoelasticity](topics/thermal-multiphysics-and-additive-manufacturing.md#thermoelasticity) (1)<br>
    11.3 <a id="additive-manufacturing"></a><a id="open-thermal-multiphysics-and-additive-manufacturing--additive-manufacturing"></a>[Additive manufacturing](topics/thermal-multiphysics-and-additive-manufacturing.md#additive-manufacturing) (3)<br>
    11.4 <a id="multiphysics-coupling"></a><a id="open-thermal-multiphysics-and-additive-manufacturing--multiphysics-coupling"></a>[Multiphysics coupling](topics/thermal-multiphysics-and-additive-manufacturing.md#multiphysics-coupling) (2)
12. <a id="optimization-and-inverse-problems"></a><a id="open-optimization-and-inverse-problems"></a>[Optimization and inverse problems](topics/optimization-and-inverse-problems.md) (18)<br>
    12.1 <a id="topology-optimization-solvers"></a><a id="open-optimization-and-inverse-problems--topology-optimization-solvers"></a>[Topology optimization solvers](topics/optimization-and-inverse-problems.md#topology-optimization-solvers) (9)<br>
    12.2 <a id="learning-based-topology-optimization"></a><a id="open-optimization-and-inverse-problems--learning-based-topology-optimization"></a>[Learning-based topology optimization](topics/optimization-and-inverse-problems.md#learning-based-topology-optimization) (5)<br>
    12.3 <a id="inverse-problems"></a><a id="open-optimization-and-inverse-problems--inverse-problems"></a>[Inverse problems](topics/optimization-and-inverse-problems.md#inverse-problems) (4)
13. <a id="physics-informed-learning-and-energy-methods"></a><a id="open-physics-informed-learning-and-energy-methods"></a>[Physics-informed learning and energy methods](topics/physics-informed-learning-and-energy-methods.md) (17)<br>
    13.1 <a id="deep-energy-methods"></a><a id="open-physics-informed-learning-and-energy-methods--deep-energy-methods"></a>[Deep energy methods](topics/physics-informed-learning-and-energy-methods.md#deep-energy-methods) (8)<br>
    13.2 <a id="residual-based-networks"></a><a id="open-physics-informed-learning-and-energy-methods--residual-based-networks"></a>[Residual-based networks](topics/physics-informed-learning-and-energy-methods.md#residual-based-networks) (6)<br>
    13.3 <a id="pinn-libraries-and-examples"></a><a id="open-physics-informed-learning-and-energy-methods--pinn-libraries-and-examples"></a>[PINN libraries and examples](topics/physics-informed-learning-and-energy-methods.md#pinn-libraries-and-examples) (3)
14. <a id="surrogates-and-reduced-order-models"></a><a id="open-surrogates-and-reduced-order-models"></a>[Surrogates and reduced-order models](topics/surrogates-and-reduced-order-models.md) (49)<br>
    14.1 <a id="stress-field-prediction"></a><a id="open-surrogates-and-reduced-order-models--stress-field-prediction"></a>[Stress-field prediction](topics/surrogates-and-reduced-order-models.md#stress-field-prediction) (7)<br>
    14.2 <a id="deformation-and-reduced-dynamics"></a><a id="open-surrogates-and-reduced-order-models--deformation-and-reduced-dynamics"></a>[Deformation and reduced dynamics](topics/surrogates-and-reduced-order-models.md#deformation-and-reduced-dynamics) (8)<br>
    14.3 [Classical machine learning and equation discovery](topics/surrogates-and-reduced-order-models.md#classical-machine-learning-and-equation-discovery) (8)<br>
    14.4 <a id="projection-based-model-reduction"></a><a id="open-surrogates-and-reduced-order-models--projection-based-model-reduction"></a>[Projection-based model reduction](topics/surrogates-and-reduced-order-models.md#projection-based-model-reduction) (4)<br>
    14.5 <a id="graph-neural-networks"></a><a id="open-surrogates-and-reduced-order-models--graph-neural-networks"></a>[Graph neural networks](topics/surrogates-and-reduced-order-models.md#graph-neural-networks) (3)<br>
    14.6 <a id="biomechanical-surrogates"></a><a id="open-surrogates-and-reduced-order-models--biomechanical-surrogates"></a>[Biomechanical surrogates](topics/surrogates-and-reduced-order-models.md#biomechanical-surrogates) (2)<br>
    14.7 <a id="response-histories-and-operator-learning"></a><a id="open-surrogates-and-reduced-order-models--response-histories-and-operator-learning"></a>[Response histories and operator learning](topics/surrogates-and-reduced-order-models.md#response-histories-and-operator-learning) (7)<br>
    14.8 <a id="frameworks-and-introductory-studies"></a><a id="open-surrogates-and-reduced-order-models--frameworks-and-introductory-studies"></a>[Frameworks and introductory studies](topics/surrogates-and-reduced-order-models.md#frameworks-and-introductory-studies) (4)<br>
    14.9 <a id="benchmark-datasets"></a><a id="open-surrogates-and-reduced-order-models--benchmark-datasets"></a>[Benchmark datasets](topics/surrogates-and-reduced-order-models.md#benchmark-datasets) (6)
15. [Hybrid AI and numerical solvers](topics/hybrid-ai-and-numerical-solvers.md) (30)<br>
    15.1 [Learned preconditioners and iterative solvers](topics/hybrid-ai-and-numerical-solvers.md#learned-preconditioners-and-iterative-solvers) (5)<br>
    15.2 [Finite element and neural network hybrids](topics/hybrid-ai-and-numerical-solvers.md#finite-element-and-neural-network-hybrids) (7)<br>
    15.3 [Connecting machine learning to solvers](topics/hybrid-ai-and-numerical-solvers.md#connecting-machine-learning-to-solvers) (8)<br>
    15.4 [Neural subspaces inside simulators](topics/hybrid-ai-and-numerical-solvers.md#neural-subspaces-inside-simulators) (4)<br>
    15.5 [Learned physics inside simulators](topics/hybrid-ai-and-numerical-solvers.md#learned-physics-inside-simulators) (4)<br>
    15.6 [Learned meshing and coarsening](topics/hybrid-ai-and-numerical-solvers.md#learned-meshing-and-coarsening) (2)
16. [Hybrid AI and computational fluid dynamics](topics/hybrid-ai-and-computational-fluid-dynamics.md) (31)<br>
    16.1 [Differentiable CFD for machine learning](topics/hybrid-ai-and-computational-fluid-dynamics.md#differentiable-cfd-for-machine-learning) (8)<br>
    16.2 [Learned turbulence closures](topics/hybrid-ai-and-computational-fluid-dynamics.md#learned-turbulence-closures) (8)<br>
    16.3 [Learned correction and acceleration](topics/hybrid-ai-and-computational-fluid-dynamics.md#learned-correction-and-acceleration) (6)<br>
    16.4 [Connecting machine learning to CFD codes](topics/hybrid-ai-and-computational-fluid-dynamics.md#connecting-machine-learning-to-cfd-codes) (5)<br>
    16.5 [Reinforcement learning with flow solvers](topics/hybrid-ai-and-computational-fluid-dynamics.md#reinforcement-learning-with-flow-solvers) (4)
17. [LLMs and simulation agents](topics/llms-and-simulation-agents.md) (22)<br>
    17.1 <a id="agents-for-mechanics"></a><a id="open-courses-references-and-agents-for-mechanics--agents-for-mechanics"></a>[Agents for mechanics](topics/llms-and-simulation-agents.md#agents-for-mechanics) (8)<br>
    17.2 [Agents for fluid dynamics](topics/llms-and-simulation-agents.md#agents-for-fluid-dynamics) (3)<br>
    17.3 [Tool servers for simulation software](topics/llms-and-simulation-agents.md#tool-servers-for-simulation-software) (3)<br>
    17.4 [Language models for material and solver code](topics/llms-and-simulation-agents.md#language-models-for-material-and-solver-code) (4)<br>
    17.5 [Language model benchmarks and datasets](topics/llms-and-simulation-agents.md#language-model-benchmarks-and-datasets) (4)
18. <a id="meshing-pre--and-post-processing"></a><a id="open-meshing-pre--and-post-processing"></a>[Meshing, pre- and post-processing](topics/meshing-pre--and-post-processing.md) (20)<br>
    18.1 <a id="mesh-generation"></a><a id="open-meshing-pre--and-post-processing--mesh-generation"></a>[Mesh generation](topics/meshing-pre--and-post-processing.md#mesh-generation) (11)<br>
    18.2 <a id="mesh-processing-and-formats"></a><a id="open-meshing-pre--and-post-processing--mesh-processing-and-formats"></a>[Mesh processing and formats](topics/meshing-pre--and-post-processing.md#mesh-processing-and-formats) (4)<br>
    18.3 <a id="visualization-and-export"></a><a id="open-meshing-pre--and-post-processing--visualization-and-export"></a>[Visualization and export](topics/meshing-pre--and-post-processing.md#visualization-and-export) (5)
19. <a id="linear-eigenvalue-and-nonlinear-solvers"></a><a id="open-linear-eigenvalue-and-nonlinear-solvers"></a>[Linear, eigenvalue and nonlinear solvers](topics/linear-eigenvalue-and-nonlinear-solvers.md) (35)<br>
    19.1 <a id="solver-toolkits"></a><a id="open-linear-eigenvalue-and-nonlinear-solvers--solver-toolkits"></a>[Solver toolkits](topics/linear-eigenvalue-and-nonlinear-solvers.md#solver-toolkits) (4)<br>
    19.2 <a id="dense-linear-algebra"></a><a id="open-linear-eigenvalue-and-nonlinear-solvers--dense-linear-algebra"></a>[Dense linear algebra](topics/linear-eigenvalue-and-nonlinear-solvers.md#dense-linear-algebra) (4)<br>
    19.3 <a id="sparse-direct-solvers"></a><a id="open-linear-eigenvalue-and-nonlinear-solvers--sparse-direct-solvers"></a>[Sparse direct solvers](topics/linear-eigenvalue-and-nonlinear-solvers.md#sparse-direct-solvers) (6)<br>
    19.4 <a id="iterative-solvers-and-preconditioners"></a><a id="open-linear-eigenvalue-and-nonlinear-solvers--iterative-solvers-and-preconditioners"></a>[Iterative solvers and preconditioners](topics/linear-eigenvalue-and-nonlinear-solvers.md#iterative-solvers-and-preconditioners) (8)<br>
    19.5 <a id="nonlinear-solvers-time-integration-and-continuation"></a><a id="open-linear-eigenvalue-and-nonlinear-solvers--nonlinear-solvers-time-integration-and-continuation"></a>[Nonlinear solvers, time integration and continuation](topics/linear-eigenvalue-and-nonlinear-solvers.md#nonlinear-solvers-time-integration-and-continuation) (5)<br>
    19.6 <a id="eigenvalue-solvers"></a><a id="open-linear-eigenvalue-and-nonlinear-solvers--eigenvalue-solvers"></a>[Eigenvalue solvers](topics/linear-eigenvalue-and-nonlinear-solvers.md#eigenvalue-solvers) (4)<br>
    19.7 <a id="matrix-free-operators-and-partitioning"></a><a id="open-linear-eigenvalue-and-nonlinear-solvers--matrix-free-operators-and-partitioning"></a>[Matrix-free operators and partitioning](topics/linear-eigenvalue-and-nonlinear-solvers.md#matrix-free-operators-and-partitioning) (4)
20. <a id="verification-validation-and-uncertainty"></a><a id="open-verification-validation-and-uncertainty"></a>[Verification, validation and uncertainty](topics/verification-validation-and-uncertainty.md) (33)<br>
    20.1 <a id="code-and-solution-verification"></a><a id="open-verification-validation-and-uncertainty--code-and-solution-verification"></a>[Code and solution verification](topics/verification-validation-and-uncertainty.md#code-and-solution-verification) (4)<br>
    20.2 <a id="benchmarks-and-reference-solutions"></a><a id="open-verification-validation-and-uncertainty--benchmarks-and-reference-solutions"></a>[Benchmarks and reference solutions](topics/verification-validation-and-uncertainty.md#benchmarks-and-reference-solutions) (8)<br>
    20.3 <a id="experimental-data-for-validation"></a><a id="open-verification-validation-and-uncertainty--experimental-data-for-validation"></a>[Experimental data for validation](topics/verification-validation-and-uncertainty.md#experimental-data-for-validation) (4)<br>
    20.4 <a id="calibration-and-bayesian-inference"></a><a id="open-verification-validation-and-uncertainty--calibration-and-bayesian-inference"></a>[Calibration and Bayesian inference](topics/verification-validation-and-uncertainty.md#calibration-and-bayesian-inference) (4)<br>
    20.5 <a id="uncertainty-and-sensitivity-analysis"></a><a id="open-verification-validation-and-uncertainty--uncertainty-and-sensitivity-analysis"></a>[Uncertainty and sensitivity analysis](topics/verification-validation-and-uncertainty.md#uncertainty-and-sensitivity-analysis) (13)
21. <a id="courses-references-and-agents-for-mechanics"></a><a id="open-courses-references-and-agents-for-mechanics"></a>[Courses and references](topics/courses-references-and-agents-for-mechanics.md) (29)<br>
    21.1 <a id="courses-and-tutorials"></a><a id="open-courses-references-and-agents-for-mechanics--courses-and-tutorials"></a><a id="textbooks-and-numerical-tutorials"></a><a id="open-courses-references-and-agents-for-mechanics--textbooks-and-numerical-tutorials"></a>[Courses and tutorials](topics/courses-references-and-agents-for-mechanics.md#courses-and-tutorials) (17)<br>
    21.2 <a id="element-definitions-and-form-languages"></a><a id="open-courses-references-and-agents-for-mechanics--element-definitions-and-form-languages"></a>[Element definitions and form languages](topics/courses-references-and-agents-for-mechanics.md#element-definitions-and-form-languages) (5)<br>
    21.3 <a id="reproducible-research-software"></a><a id="open-courses-references-and-agents-for-mechanics--reproducible-research-software"></a>[Reproducible research software](topics/courses-references-and-agents-for-mechanics.md#reproducible-research-software) (2)<br>
    21.4 <a id="curated-lists"></a><a id="open-courses-references-and-agents-for-mechanics--curated-lists"></a>[Curated lists](topics/courses-references-and-agents-for-mechanics.md#curated-lists) (5)

</details>

[Archived and unmaintained projects](archive.md) (6)

## Contributing

Corrections and additions are welcome. See [contributing.md](contributing.md).

## Acknowledgements

Thanks to the authors and maintainers of the listed projects, and to those of the [curated lists](topics/courses-references-and-agents-for-mechanics.md#curated-lists) that helped shape this collection. Descriptions and guides were drafted with the help of Claude Opus 5.5, an AI model by Anthropic.
