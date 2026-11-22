# 7. Soft-body, real-time and differentiable simulation

[← Back to the main list](../README.md#contents)

- [7.1 Real-time finite elements](#real-time-finite-elements) (7)
- [7.2 Soft robotics](#soft-robotics) (6)
- [7.3 Position-based and implicit dynamics](#position-based-and-implicit-dynamics) (4)
- [7.4 Differentiable simulation](#differentiable-simulation) (6)
- [7.5 Manipulation benchmarks](#manipulation-benchmarks) (3)

## <a id="real-time-finite-elements"></a>7.1 Real-time finite elements

| Name, language and license | Description | Note |
| --- | --- | --- |
| [Interactive<br>ComputerGraphics/<br>FastCorotatedFEM](https://github.com/InteractiveComputerGraphics/FastCorotatedFEM)<br><sub>C++</sub><br><sub>MIT</sub> | Minimal fast corotated finite element method using operator splitting. |  |
| [jinaojakezhang/<br>DJTLED](https://github.com/jinaojakezhang/DJTLED)<br><sub>C++</sub><br><sub>MIT</sub> | Direct-Jacobian explicit dynamics finite elements for real-time hyperelastic simulation. |  |
| [ltt1598/<br>Quasi-Newton-<br>Methods-for-Real-<br>time-Simulation-<br>of-Hyperelastic-<br>Materials](https://github.com/ltt1598/Quasi-Newton-Methods-for-Real-time-Simulation-of-Hyperelastic-Materials)<br><sub>C++</sub><br><sub>BSD-3-Clause (stated in source)</sub> | Quasi-Newton methods for real-time hyperelastic simulation. | Only a Visual Studio build is provided. |
| [sofa-framework/<br>sofa](https://github.com/sofa-framework/sofa)<br><sub>C++</sub><br><sub>LGPL-2.1</sub> | Interactive finite element physics framework for medical simulation and robotics. |  |
| [sofa-framework/<br>SofaPython3](https://github.com/sofa-framework/SofaPython3)<br><sub>C++ and Python</sub><br><sub>LGPL-2.1</sub> | Python interface to the SOFA simulation framework. | Requires SOFA; README describes it as work in progress. |
| [x9m/<br>DJTLED_fast](https://github.com/x9m/DJTLED_fast)<br><sub>C++</sub><br><sub>MIT</sub> | Speed-optimized DJ-TLED soft-tissue solver, with Jinao Zhang's original solver for comparison. | **By the list maintainer.** Derived from Jinao Zhang's DJTLED; developed and tested on macOS. |
| [x9m/<br>JANP-DJTLED-GPU](https://github.com/x9m/JANP-DJTLED-GPU)<br><sub>C++ and CUDA</sub><br><sub>MIT</sub> | DJTLED with average nodal pressure for nearly incompressible soft tissue, on CPU and GPU. | **By the list maintainer.** Builds on Jinao Zhang's DJTLED; the GPU solver needs an NVIDIA GPU. |

## <a id="soft-robotics"></a>7.2 Soft robotics

| Name, language and license | Description | Note |
| --- | --- | --- |
| [SofaDefrost/<br>CondensedFEMModel](https://github.com/SofaDefrost/CondensedFEMModel)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Learned condensed finite element models for soft robot control and design. | Requires SOFA. |
| [SofaDefrost/<br>SofaGym](https://github.com/SofaDefrost/SofaGym)<br><sub>Python</sub><br><sub>none found</sub> | Reinforcement learning environments built from SOFA scenes. | Requires SOFA; source files carry Inria and partner copyright notices. |
| [SofaDefrost/<br>SoftRobots](https://github.com/SofaDefrost/SoftRobots)<br><sub>C++</sub><br><sub>LGPL-3.0</sub> | SOFA components for modeling, actuating and controlling soft robots. | Requires SOFA. |
| [SofaDefrost/<br>SoftRobots.Design<br>Optimization](https://github.com/SofaDefrost/SoftRobots.DesignOptimization)<br><sub>Python</sub><br><sub>AGPL-3.0</sub> | Design optimization toolbox for soft robots. | Requires SOFA. |
| [SofaDefrost/<br>SoftRobots.Inverse](https://github.com/SofaDefrost/SoftRobots.Inverse)<br><sub>C++</sub><br><sub>AGPL-3.0 with a patent clause</sub> | Inverse methods for soft robot control. | Requires SOFA; implements a patented Inria method. |
| [StanfordASL/<br>soft-robot-control](https://github.com/StanfordASL/soft-robot-control)<br><sub>Python</sub><br><sub>MIT</sub> | Optimal control of soft robots with reduced-order finite element models. | Requires SOFA; setup uses a Gurobi license. |

## <a id="position-based-and-implicit-dynamics"></a>7.3 Position-based and implicit dynamics

| Name, language and license | Description | Note |
| --- | --- | --- |
| [Interactive<br>ComputerGraphics/<br>PositionBased<br>Dynamics](https://github.com/InteractiveComputerGraphics/PositionBasedDynamics)<br><sub>C++</sub><br><sub>MIT</sub> | Position-based simulation of rigid bodies, deformable solids and fluids. |  |
| [Interactive<br>ComputerGraphics/<br>stark](https://github.com/InteractiveComputerGraphics/stark)<br><sub>C++ and Python</sub><br><sub>Apache-2.0</sub> | Strongly coupled rigid and deformable bodies with shells, rods and frictional contact. |  |
| [mattoverby/<br>admm-elastic](https://github.com/mattoverby/admm-elastic)<br><sub>C++</sub><br><sub>MIT</sub> | ADMM generalization of projective dynamics to hyperelastic models. |  |
| [Q-Minh/<br>position-based-<br>dynamics](https://github.com/Q-Minh/position-based-dynamics)<br><sub>C++</sub><br><sub>BSL-1.0</sub> | Academic prototype of soft-body simulation with extended position-based dynamics. |  |

## <a id="differentiable-simulation"></a>7.4 Differentiable simulation

| Name, language and license | Description | Note |
| --- | --- | --- |
| [NVlabs/<br>DiffRL](https://github.com/NVlabs/DiffRL)<br><sub>Python</sub><br><sub>NVIDIA Source Code License (non-commercial)</sub> | Differentiable simulation and policy learning from the SHAC paper. | Restricted to non-commercial use. |
| [NVlabs/<br>DiSECt](https://github.com/NVlabs/DiSECt)<br><sub>Python</sub><br><sub>NVIDIA Source Code License (non-commercial)</sub> | Differentiable finite element simulator for robotic cutting of deformable materials. | Code and dataset are restricted to non-commercial use. |
| [rewarped/<br>rewarped](https://github.com/rewarped/rewarped)<br><sub>Python</sub><br><sub>Apache-2.0, with NVIDIA-restricted files</sub> | Reinforcement learning with parallel differentiable multiphysics simulation. | Some NVIDIA file headers forbid use without a license agreement. |
| [taichi-dev/<br>difftaichi](https://github.com/taichi-dev/difftaichi)<br><sub>Python</sub><br><sub>none found</sub> | Examples of differentiable physical simulators written in Taichi. |  |
| [taichi-dev/<br>taichi](https://github.com/taichi-dev/taichi)<br><sub>C++</sub><br><sub>Apache-2.0</sub> | Parallel programming language in Python for simulation on CPUs and GPUs. |  |
| [YilingQiao/<br>diff_fem](https://github.com/YilingQiao/diff_fem)<br><sub>C++</sub><br><sub>Apache-2.0</sub> | Differentiable simulation of soft multibody systems. | Paper code. |

## <a id="manipulation-benchmarks"></a>7.5 Manipulation benchmarks

| Name, language and license | Description | Note |
| --- | --- | --- |
| [hzaskywalker/<br>PlasticineLab](https://github.com/hzaskywalker/PlasticineLab)<br><sub>Python</sub><br><sub>none found</sub> | Differentiable physics benchmark for soft-body manipulation. | Only some bundled algorithm folders have license files. |
| [Xingyu-Lin/<br>softagent](https://github.com/Xingyu-Lin/softagent)<br><sub>Python</sub><br><sub>none found</sub> | Benchmarked learning algorithms for deformable object manipulation in SoftGym. | Some bundled folders have their own licenses. |
| [Xingyu-Lin/<br>softgym](https://github.com/Xingyu-Lin/softgym)<br><sub>C++</sub><br><sub>BSD-3-Clause, with separately licensed NVIDIA FleX</sub> | Deformable object manipulation benchmarks for cloth, rope and fluid. | Bundles NVIDIA FleX under the NVIDIA Source Code License (1-Way Commercial); some FleX headers also forbid use without an agreement with NVIDIA. |

[← Back to the main list](../README.md#contents)
