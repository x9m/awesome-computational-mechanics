# 18. Meshing, pre- and post-processing

[← Back to the main list](../README.md#contents)

- [18.1 Mesh generation](#mesh-generation) (11)
- [18.2 Mesh processing and formats](#mesh-processing-and-formats) (4)
- [18.3 Visualization and export](#visualization-and-export) (5)

## <a id="mesh-generation"></a>18.1 Mesh generation

| Name, language and license | Description | Note |
| --- | --- | --- |
| [fangq/<br>iso2mesh](https://github.com/fangq/iso2mesh)<br><sub>MATLAB</sub><br><sub>GPL-2.0-or-later, excluding bundled binaries</sub> | Surface and volumetric mesh generation from 3D images. | Runs in MATLAB or Octave; bundled binaries have their own licenses. |
| [gmsh/<br>gmsh](https://gitlab.onelab.info/gmsh/gmsh)<br><sub>C++</sub><br><sub>GPL-2.0-or-later with linking exception</sub> | 3D finite element mesh generator with pre- and post-processing. |  |
| [inducer/<br>meshpy](https://github.com/inducer/meshpy)<br><sub>C++</sub><br><sub>MIT wrapper, with Triangle and AGPL-3.0 components</sub> | Python interfaces to the Triangle and TetGen mesh generators. | Triangle restricts commercial distribution. |
| [meshpro/<br>pygalmesh](https://github.com/meshpro/pygalmesh)<br><sub>C++</sub><br><sub>GPL-3.0</sub> | Python front end to CGAL's 2D and 3D mesh generators. | Commercial license offered separately. |
| [NGSolve/<br>netgen](https://github.com/NGSolve/netgen)<br><sub>C++</sub><br><sub>LGPL-2.1</sub> | Automatic 3D tetrahedral mesh generator. |  |
| [nschloe/<br>pygmsh](https://github.com/nschloe/pygmsh)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Python abstractions for building geometries and meshes with Gmsh. |  |
| [pyvista/<br>scikit-gmsh](https://github.com/pyvista/scikit-gmsh)<br><sub>Python</sub><br><sub>GPL-3.0</sub> | Python interface to Gmsh for finite element meshes. |  |
| [pyvista/<br>tetgen](https://github.com/pyvista/tetgen)<br><sub>C++ and Python</sub><br><sub>MIT wrapper, with AGPL-3.0 TetGen</sub> | Python interface to the TetGen tetrahedral mesh generator. |  |
| [sandialabs/<br>vorocrust-meshing](https://github.com/sandialabs/vorocrust-meshing)<br><sub>C++</sub><br><sub>BSD-3-Clause</sub> | Conforming Voronoi meshing of non-convex and non-manifold domains. |  |
| [wildmeshing/<br>fTetWild](https://github.com/wildmeshing/fTetWild)<br><sub>C++</sub><br><sub>MPL-2.0</sub> | Fast and robust tetrahedral meshing of imperfect input geometry. |  |
| [wildmeshing/<br>TriWild](https://github.com/wildmeshing/TriWild)<br><sub>C++</sub><br><sub>MPL-2.0</sub> | Robust triangulation with curve constraints. | README requires citation. |

## <a id="mesh-processing-and-formats"></a>18.2 Mesh processing and formats

| Name, language and license | Description | Note |
| --- | --- | --- |
| [mikedh/<br>trimesh](https://github.com/mikedh/trimesh)<br><sub>Python</sub><br><sub>MIT</sub> | Python library for loading, editing and analyzing triangular meshes. |  |
| [nschloe/<br>meshio](https://github.com/nschloe/meshio)<br><sub>Python</sub><br><sub>MIT</sub> | Reader, writer and converter for many mesh file formats. |  |
| [sandialabs/<br>seacas](https://github.com/sandialabs/seacas)<br><sub>C, Fortran and C++</sub><br><sub>BSD-3-Clause</sub> | Suite for finite element pre-processing, post-processing and translation. |  |
| [wildmeshing/<br>wildmeshing-<br>toolkit](https://github.com/wildmeshing/wildmeshing-toolkit)<br><sub>C++</sub><br><sub>MIT</sub> | Parallel triangle and tetrahedral mesh generation and editing. |  |

## <a id="visualization-and-export"></a>18.3 Visualization and export

| Name, language and license | Description | Note |
| --- | --- | --- |
| [GLVis/<br>glvis](https://github.com/GLVis/glvis)<br><sub>C++</sub><br><sub>BSD-3-Clause</sub> | OpenGL visualization of finite element meshes and functions. |  |
| [Kitware/<br>ParaView](https://github.com/Kitware/ParaView)<br><sub>C++</sub><br><sub>BSD-3-Clause</sub> | Parallel data analysis and visualization application built on VTK. |  |
| [Liujie-SYSU/<br>odb2vtk](https://github.com/Liujie-SYSU/odb2vtk)<br><sub>Python</sub><br><sub>none found</sub> | Converter from Abaqus ODB results to VTK for ParaView. | Requires Abaqus Python to read ODB files. |
| [paulo-herrera/<br>PyEVTK](https://github.com/paulo-herrera/PyEVTK)<br><sub>Python</sub><br><sub>MIT (stated in source)</sub> | Pure-Python export of data to binary VTK files. |  |
| [pyvista/<br>pyvista](https://github.com/pyvista/pyvista)<br><sub>Python</sub><br><sub>MIT</sub> | 3D visualization and mesh analysis with a NumPy-based interface. |  |

[← Back to the main list](../README.md#contents)
