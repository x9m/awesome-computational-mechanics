# 17. LLMs and simulation agents

[← Back to the main list](../README.md#contents)

This topic covers large language models (LLMs) that set up, run or write simulations, the tool servers that connect them to simulation software, and benchmarks that test them.

A simulation that runs can still solve the wrong physics ([Song et al., 2026](https://arxiv.org/abs/2605.09360), preprint), so check equations, units, boundary conditions and convergence yourself.

Agents and tool servers can also execute arbitrary code ([MCP specification](https://modelcontextprotocol.io/specification/2026-07-28)), and papers, input files, logs and web pages they read can contain [hidden instructions](https://genai.owasp.org/llmrisk/llm01-prompt-injection/). Run them in a sandbox, restrict network access, keep them away from files, credentials and license servers they don't need, and approve consequential actions yourself. Don't send confidential geometry, input files, material data or results to a hosted LLM without permission.

- [17.1 Agents for mechanics](#agents-for-mechanics) (8)
- [17.2 Agents for fluid dynamics](#agents-for-fluid-dynamics) (3)
- [17.3 Tool servers for simulation software](#tool-servers-for-simulation-software) (3)
- [17.4 Language models for material and solver code](#language-models-for-material-and-solver-code) (4)
- [17.5 Language model benchmarks and datasets](#language-model-benchmarks-and-datasets) (4)

## <a id="agents-for-mechanics"></a>17.1 Agents for mechanics

| Name, language and license | Description | Note |
| --- | --- | --- |
| [Farhad-Davaripour/<br>FEA_Assisted_Agent](https://github.com/Farhad-Davaripour/FEA_Assisted_Agent)<br><sub>Python</sub><br><sub>MIT</sub> | Language model agent that automates Abaqus simulations. | Requires Abaqus and OpenAI models. |
| [lamm-mit/<br>MechAgents](https://github.com/lamm-mit/MechAgents)<br><sub>Jupyter Notebook</sub><br><sub>Apache-2.0</sub> | Multi-agent language model workflows for solving mechanics problems numerically. | Requires an OpenAI API key. |
| [LIRAM-LIN/<br>AbaqusAgent](https://github.com/LIRAM-LIN/AbaqusAgent)<br><sub>Python</sub><br><sub>MIT</sub> | Language model agents for finite element analysis of solids in Abaqus. | Requires Abaqus and language model API keys. |
| [LuoXueling/<br>MechFoundry](https://github.com/LuoXueling/MechFoundry)<br><sub>Python</sub><br><sub>Apache-2.0, with non-commercial dependencies</sub> | Agent-driven shape generation, meshing and finite element analysis. | README says some dependencies are restricted to non-commercial use. |
| [MatPro-IFE/<br>pde-agents](https://github.com/MatPro-IFE/pde-agents)<br><sub>Python</sub><br><sub>MIT</sub> | Agents on local language models that run FEniCSx finite element simulations. | Documented setup uses two high-memory GPUs. |
| [shaokun-chen/<br>Agent4Abaqus](https://github.com/shaokun-chen/Agent4Abaqus)<br><sub>Python</sub><br><sub>MIT</sub> | Language model agent that writes, runs and repairs Abaqus scripts. | Requires Abaqus and a language model API key. |
| [taozhan18/<br>MooseAgent](https://github.com/taozhan18/MooseAgent)<br><sub>Python</sub><br><sub>MIT</sub> | Language model agents that write, run and repair MOOSE input files. | Requires MOOSE and a language model backend. |
| [viktor-platform/<br>opensees-ai-agent](https://github.com/viktor-platform/opensees-ai-agent)<br><sub>Python</sub><br><sub>none found</sub> | Agent that builds and analyzes steel platform models with OpenSees. | Requires VIKTOR and OpenAI models; OpenSeesPy restricts commercial redistribution. |

## <a id="agents-for-fluid-dynamics"></a>17.2 Agents for fluid dynamics

| Name, language and license | Description | Note |
| --- | --- | --- |
| [AGN000/<br>AutoFOAM](https://github.com/AGN000/AutoFOAM)<br><sub>Python</sub><br><sub>PolyForm-Noncommercial-1.0.0 (stated in README)</sub> | Language model agent that writes and refines OpenFOAM cases and meshes. | Restricted to non-commercial use; requires OpenFOAM. |
| [csml-rpi/<br>Foam-Agent](https://github.com/csml-rpi/Foam-Agent)<br><sub>Python</sub><br><sub>MIT</sub> | Language model agents that automate OpenFOAM simulations. | Requires OpenFOAM and a language model backend. |
| [tianhanz/<br>ChatCFD](https://github.com/tianhanz/ChatCFD)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Language model agent that sets up and runs OpenFOAM cases from text or papers. | Requires OpenFOAM and language model API keys. |

## <a id="tool-servers-for-simulation-software"></a>17.3 Tool servers for simulation software

| Name, language and license | Description | Note |
| --- | --- | --- |
| [Cai-aa/<br>abaqus-mcp](https://github.com/Cai-aa/abaqus-mcp)<br><sub>Python</sub><br><sub>MIT</sub> | Tool server that lets language models run scripts and inspect results in Abaqus/CAE. | Requires Abaqus; runs model-written Python. |
| [open-PASO/<br>openPASO](https://github.com/open-PASO/openPASO)<br><sub>Python</sub><br><sub>MIT</sub> | Tool server that lets language models run open finite element and multiphysics solvers. | Under active development; solvers are installed separately. |
| [Whfkl/<br>Abaqus-Control-MCP](https://github.com/Whfkl/Abaqus-Control-MCP)<br><sub>Python</sub><br><sub>MIT</sub> | Local bridge that lets coding agents control an open Abaqus/CAE session. | Requires Abaqus; runs model-written Python. |

## <a id="language-models-for-material-and-solver-code"></a>17.4 Language models for material and solver code

| Name, language and license | Description | Note |
| --- | --- | --- |
| [AgenticModeling/<br>MultiAgent<br>Constitutive<br>Modeling26](https://github.com/AgenticModeling/MultiAgentConstitutiveModeling26)<br><sub>Python</sub><br><sub>MIT</sub> | Two agents that propose constitutive models and audit their physical constraints. | Paper code; requires an OpenRouter API key. |
| [gencann26/<br>GenCANN](https://github.com/gencann26/GenCANN)<br><sub>Python</sub><br><sub>MIT</sub> | Language models that write constitutive artificial neural networks. | Paper code; uses OpenAI models. |
| [LithiumDA/<br>CodePDE](https://github.com/LithiumDA/CodePDE)<br><sub>Python</sub><br><sub>none found, with Apache-2.0 files</sub> | Language models that write, debug and refine numerical PDE solvers. | Paper code; requires language model API keys. |
| [MariusTacke/<br>CSGA](https://github.com/MariusTacke/CSGA)<br><sub>Python</sub><br><sub>MIT</sub> | Scientific generative agents that propose constitutive models. | Paper code; requires a language model backend. |

## <a id="language-model-benchmarks-and-datasets"></a>17.5 Language model benchmarks and datasets

| Name, language and license | Description | Note |
| --- | --- | --- |
| [elejeune11/<br>FEM-bench](https://github.com/elejeune11/FEM-bench)<br><sub>Python</sub><br><sub>MIT</sub> | Benchmark of language models writing finite element code and tests. | Work in progress. |
| [fenics-llm/<br>FEM_Dataset](https://github.com/fenics-llm/FEM_Dataset)<br><sub>Python</sub><br><sub>none found, with CC-BY-SA-4.0 files</sub> | Finite element problem statements paired with FEniCS code and solutions. | Solutions are simulated, not measured. |
| [NLR-Theseus/<br>cfdllmbench](https://github.com/NLR-Theseus/cfdllmbench)<br><sub>Python</sub><br><sub>BSD-3-Clause</sub> | Benchmarks of language models on CFD knowledge, code and OpenFOAM workflows. | FoamBench requires OpenFOAM. |
| [YusanX/<br>pde-agent-bench](https://github.com/YusanX/pde-agent-bench)<br><sub>Python</sub><br><sub>CC-BY-4.0 (stated in README)</sub> | Benchmark of agents writing DOLFINx, Firedrake and deal.II solvers. | References are numerical or manufactured solutions, not measurements. |

[← Back to the main list](../README.md#contents)
