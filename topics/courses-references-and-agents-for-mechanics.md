# 20. Courses, references and agents for mechanics

[← Back to the main list](../README.md#contents)

Besides learning material, this topic covers large language models (LLMs) that set up, run or write simulations, and benchmarks that test them.

A simulation that runs can still solve the wrong physics ([Song et al., 2026](https://arxiv.org/abs/2605.09360), preprint), so check equations, units, boundary conditions and convergence yourself. Agents and tool servers can also execute arbitrary code ([MCP specification](https://modelcontextprotocol.io/specification/2025-06-18)), so isolate them from files, credentials and license servers they don't need, and don't send confidential models to a hosted LLM without permission.

- [20.1 Courses and tutorials](#courses-and-tutorials) (17)
- [20.2 Element definitions and form languages](#element-definitions-and-form-languages) (5)
- [20.3 Reproducible research software](#reproducible-research-software) (2)
- [20.4 Curated lists](#curated-lists) (5)
- [20.5 Agents for mechanics](#agents-for-mechanics) (8)
- [20.6 Agents for fluid dynamics](#agents-for-fluid-dynamics) (3)
- [20.7 Tool servers for simulation software](#tool-servers-for-simulation-software) (3)
- [20.8 Language models for material and solver code](#language-models-for-material-and-solver-code) (4)
- [20.9 Language model benchmarks and datasets](#language-model-benchmarks-and-datasets) (4)

## <a id="courses-and-tutorials"></a><a id="textbooks-and-numerical-tutorials"></a>20.1 Courses and tutorials

| Name, language and license | Description | Note |
| --- | --- | --- |
| [albower/<br>Applied_Mechanics_<br>of_Solids](https://github.com/albower/Applied_Mechanics_of_Solids)<br><sub>MATLAB</sub><br><sub>none found</sub> | Problem sets and finite element codes for Bower's Applied Mechanics of Solids. | Requires MATLAB. |
| [AndreWeiner/<br>ml-cfd-lecture](https://github.com/AndreWeiner/ml-cfd-lecture)<br><sub>Python</sub><br><sub>GPL-3.0, with CC-BY-4.0 content</sub> | Course on machine learning in fluid mechanics, with notes and exercises. |  |
| [bleyerj/<br>comet-fenicsx](https://github.com/bleyerj/comet-fenicsx)<br><sub>Python</sub><br><sub>CC-BY-SA-4.0</sub> | Numerical tours of computational mechanics with FEniCSx. |  |
| [bueler/<br>p4pdes](https://github.com/bueler/p4pdes)<br><sub>C</sub><br><sub>MIT</sub> | Example programs from a book on solving PDEs with PETSc and Firedrake. |  |
| [Ceyron/<br>machine-learning-<br>and-simulation](https://github.com/Ceyron/machine-learning-and-simulation)<br><sub>Jupyter Notebook</sub><br><sub>MIT</sub> | Notes and code for a video course on simulation and machine learning, including continuum mechanics and FEniCS. |  |
| [cooperrc/<br>computational-<br>mechanics](https://github.com/cooperrc/computational-mechanics)<br><sub>MATLAB</sub><br><sub>CC-BY-4.0 content, BSD-3-Clause code (stated in README)</sub> | Open course materials on computational mechanics. | Includes code written for MATLAB, Octave support not documented. |
| [dilevin/<br>CSC417-a4-cloth-<br>simulation](https://github.com/dilevin/CSC417-a4-cloth-simulation)<br><sub>C++</sub><br><sub>none found</sub> | Course assignment on finite element cloth simulation with contact. | Starter code for an assignment. |
| [finite-element/<br>finite-element-<br>course](https://github.com/finite-element/finite-element-course)<br><sub>Python</sub><br><sub>MIT (stated in pyproject.toml)</sub> | Imperial College course on finite element analysis and implementation. | No README. |
| [gridap/<br>Tutorials](https://github.com/gridap/Tutorials)<br><sub>Julia</sub><br><sub>MIT</sub> | Worked tutorials on solving PDEs with Gridap. |  |
| [Interactive<br>ComputerGraphics/<br>physics-simulation](https://github.com/InteractiveComputerGraphics/physics-simulation)<br><sub>MIT</sub> | Introduction to simulation of rigid bodies, deformable solids and fluids. | Documents only, no code. |
| [jomorlier/<br>feacourse](https://github.com/jomorlier/feacourse)<br><sub>MATLAB</sub><br><sub>none found</sub> | Materials for a computational solid mechanics course. | Tutorials are written for MATLAB; assignments also use commercial solvers. |
| [jorgensd/<br>dolfinx-tutorial](https://github.com/jorgensd/dolfinx-tutorial)<br><sub>Jupyter Notebook</sub><br><sub>CC-BY-4.0 content, MIT in some files</sub> | Tutorial book on solving PDEs with FEniCSx, including elasticity and hyperelasticity. |  |
| [Kevin-Mattheus-<br>Moerman/<br>NonlinearContinuum<br>Mechanics](https://github.com/Kevin-Mattheus-Moerman/NonlinearContinuumMechanics)<br><sub>Jupyter Notebook</sub><br><sub>MIT</sub> | Notebooks deriving stresses in Ogden hyperelasticity. |  |
| [ltt1598/<br>GAMES_Xi-an_<br>forward_physics](https://github.com/ltt1598/GAMES_Xi-an_forward_physics)<br><sub>Python</sub><br><sub>none found</sub> | Notes and Taichi sample code from a physically based simulation course. |  |
| [matthias-research/<br>pages](https://github.com/matthias-research/pages/tree/master/tenMinutePhysics)<br><sub>JavaScript</sub><br><sub>MIT (stated in source)</sub> | Ten Minute Physics tutorials on soft bodies, cloth, collisions and other simulation methods. |  |
| [mitmath/<br>18335](https://github.com/mitmath/18335)<br><sub>Jupyter Notebook</sub><br><sub>none found</sub> | MIT course notes on numerical linear algebra, stability and iterative methods. |  |
| [phys-sim-book/<br>solid-sim-tutorial](https://github.com/phys-sim-book/solid-sim-tutorial)<br><sub>Python</sub><br><sub>Apache-2.0</sub> | Readable examples of optimization-based solid simulation. |  |

## <a id="element-definitions-and-form-languages"></a>20.2 Element definitions and form languages

| Name, language and license | Description | Note |
| --- | --- | --- |
| [DefElement/<br>DefElement](https://github.com/DefElement/DefElement)<br><sub>Python</sub><br><sub>MIT code, CC-BY-4.0 content</sub> | Source of DefElement, an encyclopedia of finite element definitions. |  |
| [FEniCS/<br>basix](https://github.com/FEniCS/basix)<br><sub>C++</sub><br><sub>MIT</sub> | Runtime tabulation of finite element basis functions, quadrature and mappings. |  |
| [FEniCS/<br>ufl](https://github.com/FEniCS/ufl)<br><sub>Python</sub><br><sub>LGPL-3.0-or-later</sub> | Language for writing variational forms in notation close to the mathematics. |  |
| [firedrakeproject/<br>fiat](https://github.com/firedrakeproject/fiat)<br><sub>Python</sub><br><sub>LGPL-3.0-or-later</sub> | Tabulation of arbitrary-order finite elements and quadrature rules. |  |
| [mscroggs/<br>symfem](https://github.com/mscroggs/symfem)<br><sub>Python</sub><br><sub>MIT</sub> | Symbolic definitions of finite elements and their basis functions. |  |

## <a id="reproducible-research-software"></a>20.3 Reproducible research software

| Name, language and license | Description | Note |
| --- | --- | --- |
| [betterscientificsoftware/<br>bssw.io](https://github.com/betterscientificsoftware/bssw.io)<br><sub>MIT</sub> | Articles on testing, sustaining and improving scientific software. |  |
| [the-turing-way/<br>the-turing-way](https://github.com/the-turing-way/the-turing-way)<br><sub>MIT code, CC-BY-4.0 content</sub> | Handbook on reproducible, ethical and collaborative research. |  |

## <a id="curated-lists"></a>20.4 Curated lists

| Name, language and license | Description | Note |
| --- | --- | --- |
| [kimimgo/<br>awesome-ai-cae](https://github.com/kimimgo/awesome-ai-cae)<br><sub>CC0-1.0</sub> | Curated list of engineering simulation tools that software agents can drive. |  |
| [modenaxe/<br>awesome-<br>biomechanics](https://github.com/modenaxe/awesome-biomechanics)<br><sub>CC0-1.0 (stated in README)</sub> | Curated resources for biomechanics and human motion analysis. |  |
| [nschloe/<br>awesome-<br>scientific-<br>computing](https://github.com/nschloe/awesome-scientific-computing)<br><sub>CC0-1.0</sub> | Curated list of scientific computing tools, including finite element and meshing software. |  |
| [thunil/<br>Physics-Based-<br>Deep-Learning](https://github.com/thunil/Physics-Based-Deep-Learning)<br><sub>none found</sub> | Curated list of research on physics-based deep learning. |  |
| [tkoyama010/<br>awesome-finite-<br>elements](https://github.com/tkoyama010/awesome-finite-elements)<br><sub>CC0-1.0</sub> | Curated list of finite element software. |  |

## <a id="agents-for-mechanics"></a>20.5 Agents for mechanics

| Name, language and license | Description | Note |
| --- | --- | --- |
| [Farhad-Davaripour/<br>FEA_Assisted_Agent](https://github.com/Farhad-Davaripour/FEA_Assisted_Agent)<br><sub>Python</sub><br><sub>MIT</sub> | Language model agent that automates Abaqus simulations. | Requires Abaqus and OpenAI models. |
| [lamm-mit/<br>MechAgents](https://github.com/lamm-mit/MechAgents)<br><sub>Jupyter Notebook</sub><br><sub>Apache-2.0</sub> | Multi-agent language model workflows for solving mechanics problems numerically. |  |
| [LIRAM-LIN/<br>AbaqusAgent](https://github.com/LIRAM-LIN/AbaqusAgent)<br><sub>Python</sub><br><sub>MIT</sub> | Language model agents for finite element analysis of solids in Abaqus. | Requires Abaqus and language model API keys. |
| [LuoXueling/<br>MechFoundry](https://github.com/LuoXueling/MechFoundry)<br><sub>Python</sub><br><sub>Apache-2.0, with non-commercial dependencies</sub> | Agent-driven shape generation, meshing and finite element analysis. | README says some dependencies are restricted to non-commercial use. |
| [MatPro-IFE/<br>pde-agents](https://github.com/MatPro-IFE/pde-agents)<br><sub>Python</sub><br><sub>MIT</sub> | Agents on local language models that run FEniCSx finite element simulations. | Documented setup uses two high-memory GPUs. |
| [shaokun-chen/<br>Agent4Abaqus](https://github.com/shaokun-chen/Agent4Abaqus)<br><sub>Python</sub><br><sub>MIT</sub> | Language model agent that writes, runs and repairs Abaqus scripts. | Requires Abaqus and a language model API key. |
| [taozhan18/<br>MooseAgent](https://github.com/taozhan18/MooseAgent)<br><sub>Python</sub><br><sub>MIT</sub> | Language model agents that write, run and repair MOOSE input files. | Requires MOOSE and a language model backend. |
| [viktor-platform/<br>opensees-ai-agent](https://github.com/viktor-platform/opensees-ai-agent)<br><sub>Python</sub><br><sub>none found</sub> | Agent that builds and analyzes steel platform models with OpenSees. | Requires VIKTOR and OpenAI models; OpenSeesPy restricts commercial redistribution. |

## <a id="agents-for-fluid-dynamics"></a>20.6 Agents for fluid dynamics

| Name, language and license | Description | Note |
| --- | --- | --- |
| [AGN000/<br>AutoFOAM](https://github.com/AGN000/AutoFOAM)<br><sub>Python</sub><br><sub>PolyForm-Noncommercial-1.0.0 (stated in README)</sub> | Language model agent that writes and refines OpenFOAM cases and meshes. | Restricted to non-commercial use; requires OpenFOAM. |
| [csml-rpi/<br>Foam-Agent](https://github.com/csml-rpi/Foam-Agent)<br><sub>Python</sub><br><sub>MIT</sub> | Language model agents that automate OpenFOAM simulations. | Requires OpenFOAM and a language model backend. |
| [tianhanz/<br>ChatCFD](https://github.com/tianhanz/ChatCFD)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Language model agent that sets up and runs OpenFOAM cases from text or papers. | Requires OpenFOAM and language model API keys. |

## <a id="tool-servers-for-simulation-software"></a>20.7 Tool servers for simulation software

| Name, language and license | Description | Note |
| --- | --- | --- |
| [Cai-aa/<br>abaqus-mcp](https://github.com/Cai-aa/abaqus-mcp)<br><sub>Python</sub><br><sub>MIT</sub> | Tool server that lets language models run scripts and inspect results in Abaqus/CAE. | Requires Abaqus; runs model-written Python. |
| [open-PASO/<br>openPASO](https://github.com/open-PASO/openPASO)<br><sub>Python</sub><br><sub>MIT</sub> | Tool server that lets language models run open finite element and multiphysics solvers. | Under active development; solvers are installed separately. |
| [Whfkl/<br>Abaqus-Control-MCP](https://github.com/Whfkl/Abaqus-Control-MCP)<br><sub>Python</sub><br><sub>MIT</sub> | Local bridge that lets coding agents control an open Abaqus/CAE session. | Requires Abaqus; runs model-written Python. |

## <a id="language-models-for-material-and-solver-code"></a>20.8 Language models for material and solver code

| Name, language and license | Description | Note |
| --- | --- | --- |
| [AgenticModeling/<br>MultiAgent<br>Constitutive<br>Modeling26](https://github.com/AgenticModeling/MultiAgentConstitutiveModeling26)<br><sub>Python</sub><br><sub>MIT</sub> | Two agents that propose constitutive models and audit their physical constraints. | Paper code. |
| [gencann26/<br>GenCANN](https://github.com/gencann26/GenCANN)<br><sub>Python</sub><br><sub>MIT</sub> | Language models that write constitutive artificial neural networks. | Paper code; uses OpenAI models. |
| [LithiumDA/<br>CodePDE](https://github.com/LithiumDA/CodePDE)<br><sub>Python</sub><br><sub>none found, with Apache-2.0 files</sub> | Language models that write, debug and refine numerical PDE solvers. | Paper code. |
| [MariusTacke/<br>CSGA](https://github.com/MariusTacke/CSGA)<br><sub>Python</sub><br><sub>MIT</sub> | Scientific generative agents that propose constitutive models. | Paper code. |

## <a id="language-model-benchmarks-and-datasets"></a>20.9 Language model benchmarks and datasets

| Name, language and license | Description | Note |
| --- | --- | --- |
| [elejeune11/<br>FEM-bench](https://github.com/elejeune11/FEM-bench)<br><sub>Python</sub><br><sub>MIT</sub> | Benchmark of language models writing finite element code and tests. | Work in progress. |
| [fenics-llm/<br>FEM_Dataset](https://github.com/fenics-llm/FEM_Dataset)<br><sub>Python</sub><br><sub>none found, with CC-BY-SA-4.0 files</sub> | Finite element problem statements paired with FEniCS code and solutions. | Solutions are simulated, not measured. |
| [NLR-Theseus/<br>cfdllmbench](https://github.com/NLR-Theseus/cfdllmbench)<br><sub>Python</sub><br><sub>BSD-3-Clause</sub> | Benchmarks of language models on CFD knowledge, code and OpenFOAM workflows. |  |
| [YusanX/<br>pde-agent-bench](https://github.com/YusanX/pde-agent-bench)<br><sub>Python</sub><br><sub>CC-BY-4.0 (stated in README)</sub> | Benchmark of agents writing DOLFINx, Firedrake and deal.II solvers. | References are numerical or manufactured solutions, not measurements. |

[← Back to the main list](../README.md#contents)
