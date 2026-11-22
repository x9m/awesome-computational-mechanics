# 2. Finite volume methods

[← Back to the main list](../README.md#contents)

- [2.1 Solid mechanics and fluid-solid interaction](#solid-mechanics-and-fluid-solid-interaction) (6)
- [2.2 Porous media and geomechanics](#porous-media-and-geomechanics) (3)

## <a id="solid-mechanics-and-fluid-solid-interaction"></a>2.1 Solid mechanics and fluid-solid interaction

| Name, language and license | Description | Note |
| --- | --- | --- |
| [foam-for-nuclear/<br>offbeat](https://gitlab.com/foam-for-nuclear/offbeat)<br><sub>C++</sub><br><sub>GPL-3.0, with MIT SCIANTIX</sub> | Finite volume nuclear fuel performance code with thermomechanics, creep and contact. | Requires OpenFOAM. |
| [jibranhaider/<br>explicitSolid<br>Dynamics](https://github.com/jibranhaider/explicitSolidDynamics)<br><sub>C++</sub><br><sub>GPL-3.0</sub> | Cell-centered finite volume explicit dynamics of large-deformation solids. | Requires OpenFOAM 7; last commit in 2021. |
| [jibranhaider/<br>explicitSolid<br>Dynamics_vc](https://github.com/jibranhaider/explicitSolidDynamics_vc)<br><sub>C++</sub><br><sub>GPL-3.0</sub> | Vertex-centered finite volume explicit dynamics of large-deformation solids. | Requires OpenFOAM 5, 6 or 7; last commit in 2021. |
| [solids4foam/<br>beamFoam](https://github.com/solids4foam/beamFoam)<br><sub>C++</sub><br><sub>GPL-3.0-or-later (stated in source)</sub> | Cell-centered finite volume solver for geometrically exact Simo-Reissner beams. | No license file; requires OpenFOAM. |
| [solids4foam/<br>cardiacFoam](https://github.com/solids4foam/cardiacFoam)<br><sub>C++</sub><br><sub>GPL-3.0</sub> | Finite volume toolbox for cardiac electrophysiology and electromechanics. | Requires OpenFOAM; electromechanics also needs solids4foam. |
| [solids4foam/<br>solids4foam](https://github.com/solids4foam/solids4foam)<br><sub>C++</sub><br><sub>GPL-3.0</sub> | Toolbox for solid mechanics and fluid-solid interaction in OpenFOAM. | Requires OpenFOAM. |

## <a id="porous-media-and-geomechanics"></a>2.2 Porous media and geomechanics

| Name, language and license | Description | Note |
| --- | --- | --- |
| [baw-de/<br>poroMechanicalFoam](https://github.com/baw-de/poroMechanicalFoam)<br><sub>C++</sub><br><sub>GPL-3.0, with an unlicensed UMAT</sub> | Finite volume flow and deformation in partially saturated porous media. | Requires OpenFOAM and solids4foam; the bundled Mohr-Coulomb UMAT by Johan Clausen and Lars Andersen states no license. |
| [keileg/<br>fvbiot](https://github.com/keileg/fvbiot)<br><sub>MATLAB</sub><br><sub>GPL-3.0</sub> | Multipoint stress finite volume discretizations of elasticity and Biot poromechanics. | Written for MATLAB, Octave support not documented; uses MRST; last commit in 2019. |
| [pmgbergen/<br>porepy](https://github.com/pmgbergen/porepy)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Thermo-poromechanics of fractured media, with multipoint stress approximation. |  |

[← Back to the main list](../README.md#contents)
