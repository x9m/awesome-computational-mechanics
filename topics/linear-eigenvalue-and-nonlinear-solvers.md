# 16. Linear, eigenvalue and nonlinear solvers

[← Back to the main list](../README.md#contents)

The right solver depends on the structure of the discrete problem.

- **Symmetric positive definite**, as in many compressible elasticity problems: use Cholesky, or conjugate gradients with a preconditioner. For smoothed-aggregation multigrid, supply the rigid body modes.
- **Symmetric indefinite**, as in mixed formulations and frictionless Lagrange multiplier contact: use an LDLᵀ factorization, MINRES with a positive definite preconditioner, or GMRES with a block preconditioner.
- **Nonsymmetric**, as with friction or non-associated plasticity: use LU, or GMRES or BiCGSTAB with a preconditioner.
- **Snap-through and buckling**: the tangent becomes singular. Arc-length continuation can pass a limit point, where load-controlled Newton fails. Following a buckled branch from a bifurcation also needs an imperfection or branch switching.
- **Any system**: a small residual does not guarantee a small error when the matrix is ill-conditioned.

Further reading: [Davis et al. (2016)](https://doi.org/10.1017/S0962492916000076) on direct methods, [Saad (2003)](https://doi.org/10.1137/1.9780898718003) on iterative methods, [Benzi et al. (2005)](https://doi.org/10.1017/S0962492904000212) on saddle point problems and [Higham (2002)](https://doi.org/10.1137/1.9780898718027) on accuracy and stability.

- [16.1 Solver toolkits](#solver-toolkits) (4)
- [16.2 Dense linear algebra](#dense-linear-algebra) (4)
- [16.3 Sparse direct solvers](#sparse-direct-solvers) (6)
- [16.4 Iterative solvers and preconditioners](#iterative-solvers-and-preconditioners) (8)
- [16.5 Nonlinear solvers, time integration and continuation](#nonlinear-solvers-time-integration-and-continuation) (5)
- [16.6 Eigenvalue solvers](#eigenvalue-solvers) (4)
- [16.7 Matrix-free operators and partitioning](#matrix-free-operators-and-partitioning) (4)

## <a id="solver-toolkits"></a>16.1 Solver toolkits

| Name, language and license | Description | Note |
| --- | --- | --- |
| [ginkgo-project/<br>ginkgo](https://github.com/ginkgo-project/ginkgo)<br><sub>C++</sub><br><sub>BSD-3-Clause</sub> | Sparse linear algebra library for multicore processors and GPUs. |  |
| [petsc/<br>petsc](https://gitlab.com/petsc/petsc)<br><sub>C</sub><br><sub>BSD-2-Clause</sub> | Parallel toolkit of linear, nonlinear and time-stepping solvers for PDE-based models. |  |
| [polyfem/<br>polysolve](https://github.com/polyfem/polysolve)<br><sub>C++</sub><br><sub>MIT</sub> | Common interface to external linear solvers, with its own nonlinear solvers. |  |
| [trilinos/<br>Trilinos](https://github.com/trilinos/Trilinos)<br><sub>C++</sub><br><sub>BSD and (L)GPL, by package</sub> | Collection of packages for large-scale solvers, discretization and optimization. |  |

## <a id="dense-linear-algebra"></a>16.2 Dense linear algebra

| Name, language and license | Description | Note |
| --- | --- | --- |
| [flame/<br>blis](https://github.com/flame/blis)<br><sub>C</sub><br><sub>BSD-3-Clause</sub> | Framework for building BLAS-like dense linear algebra libraries. |  |
| [libeigen/<br>eigen](https://gitlab.com/libeigen/eigen)<br><sub>C++</sub><br><sub>MPL-2.0, with permissive third-party files</sub> | C++ template library for dense and sparse linear algebra. |  |
| [OpenMathLib/<br>OpenBLAS](https://github.com/OpenMathLib/OpenBLAS)<br><sub>C</sub><br><sub>BSD-3-Clause</sub> | Optimized implementation of the BLAS kernels used by many solvers. |  |
| [Reference-LAPACK/<br>lapack](https://github.com/Reference-LAPACK/lapack)<br><sub>Fortran</sub><br><sub>BSD-3-Clause</sub> | Reference routines for linear systems, least squares and eigenvalue problems. |  |

## <a id="sparse-direct-solvers"></a>16.3 Sparse direct solvers

| Name, language and license | Description | Note |
| --- | --- | --- |
| [DrTimothyAlden<br>Davis/<br>SuiteSparse](https://github.com/DrTimothyAldenDavis/SuiteSparse)<br><sub>C</sub><br><sub>BSD, Apache-2.0, LGPL and GPL, by package</sub> | Sparse matrix packages, including the CHOLMOD, UMFPACK and KLU factorizations. | Some packages, including UMFPACK, are GPL. |
| [pghysels/<br>STRUMPACK](https://github.com/pghysels/STRUMPACK)<br><sub>C++</sub><br><sub>BSD-3-Clause, with restricted MC64 code</sub> | Sparse direct solvers and preconditioners that use rank-structured compression. | Bundled MC64 may not be passed to third parties without its authors' consent. |
| [ralna/<br>spral](https://github.com/ralna/spral)<br><sub>Fortran</sub><br><sub>BSD-3-Clause</sub> | Sparse algorithms, including factorizations for symmetric systems. |  |
| [scivision/<br>mumps-superbuild](https://github.com/scivision/mumps-superbuild)<br><sub>CMake</sub><br><sub>MIT build scripts, CeCILL-C MUMPS</sub> | CMake build of the MUMPS parallel multifrontal solver and its dependencies. | Build scripts, not the official MUMPS repository. |
| [xiaoyeli/<br>superlu](https://github.com/xiaoyeli/superlu)<br><sub>C</sub><br><sub>BSD-3-Clause, with restricted MC64 code</sub> | Sequential supernodal LU factorization for sparse nonsymmetric systems. | Bundled MC64 may not be passed to third parties without its authors' consent. |
| [xiaoyeli/<br>superlu_dist](https://github.com/xiaoyeli/superlu_dist)<br><sub>C</sub><br><sub>BSD-3-Clause, with restricted MC64 code</sub> | Distributed-memory sparse LU factorization with static pivoting. | Bundled MC64 may not be passed to third parties without its authors' consent. |

## <a id="iterative-solvers-and-preconditioners"></a>16.4 Iterative solvers and preconditioners

| Name, language and license | Description | Note |
| --- | --- | --- |
| [anishida/<br>lis](https://github.com/anishida/lis)<br><sub>C</sub><br><sub>BSD-3-Clause</sub> | Parallel iterative solvers for linear systems and eigenvalue problems. |  |
| [ddemidov/<br>amgcl](https://github.com/ddemidov/amgcl)<br><sub>C++</sub><br><sub>MIT</sub> | Header-only algebraic multigrid for large sparse linear systems. |  |
| [gridap/<br>GridapSolvers.jl](https://github.com/gridap/GridapSolvers.jl)<br><sub>Julia</sub><br><sub>MIT</sub> | Block, multigrid and other physics-tailored solvers for Gridap. |  |
| [hpddm/<br>hpddm](https://github.com/hpddm/hpddm)<br><sub>C++</sub><br><sub>LGPL-3.0</sub> | Domain decomposition methods, including overlapping Schwarz, FETI and BDD. |  |
| [hypre-space/<br>hypre](https://github.com/hypre-space/hypre)<br><sub>C</sub><br><sub>MIT or Apache-2.0</sub> | Parallel preconditioners and solvers with algebraic and structured multigrid. |  |
| [JuliaSmooth<br>Optimizers/<br>Krylov.jl](https://github.com/JuliaSmoothOptimizers/Krylov.jl)<br><sub>Julia</sub><br><sub>MPL-2.0</sub> | Collection of Krylov methods for linear and least-squares problems. |  |
| [NVIDIA/<br>AMGX](https://github.com/NVIDIA/AMGX)<br><sub>C++ and CUDA</sub><br><sub>BSD-3-Clause, with Apache-2.0 CUSP</sub> | Distributed algebraic multigrid and Krylov solvers for GPUs. | Requires CUDA. |
| [pyamg/<br>pyamg](https://github.com/pyamg/pyamg)<br><sub>Python</sub><br><sub>MIT</sub> | Algebraic multigrid solvers in Python. |  |

## <a id="nonlinear-solvers-time-integration-and-continuation"></a>16.5 Nonlinear solvers, time integration and continuation

| Name, language and license | Description | Note |
| --- | --- | --- |
| [bifurcationkit/<br>BifurcationKit.jl](https://github.com/bifurcationkit/BifurcationKit.jl)<br><sub>Julia</sub><br><sub>MIT</sub> | Continuation and bifurcation analysis, for tracing instabilities and solution branches. |  |
| [coin-or/<br>Ipopt](https://github.com/coin-or/Ipopt)<br><sub>C++</sub><br><sub>EPL-2.0</sub> | Interior point solver for large constrained nonlinear optimization. | Optional HSL and Pardiso solvers have separate licenses. |
| [llnl/<br>sundials](https://github.com/llnl/sundials)<br><sub>C</sub><br><sub>BSD-3-Clause</sub> | Time integrators and nonlinear solvers for ODE and differential-algebraic systems. |  |
| [pprachas/<br>fenics_arclength](https://github.com/pprachas/fenics_arclength)<br><sub>Python</sub><br><sub>MIT</sub> | Riks arc-length solver for tracing unstable equilibrium paths in FEniCS. | Requires legacy FEniCS 2019.1, not FEniCSx. |
| [SciML/<br>NonlinearSolve.jl](https://github.com/SciML/NonlinearSolve.jl)<br><sub>Julia</sub><br><sub>MIT</sub> | Newton-type and other root-finding methods for nonlinear systems. |  |

## <a id="eigenvalue-solvers"></a>16.6 Eigenvalue solvers

| Name, language and license | Description | Note |
| --- | --- | --- |
| [opencollab/<br>arpack-ng](https://github.com/opencollab/arpack-ng)<br><sub>Fortran</sub><br><sub>BSD-3-Clause</sub> | Community-maintained ARPACK routines for large eigenvalue problems. |  |
| [primme/<br>primme](https://github.com/primme/primme)<br><sub>C</sub><br><sub>BSD-3-Clause, with LGPL test files</sub> | Preconditioned eigenvalue and singular value solvers for large problems. |  |
| [slepc/<br>slepc](https://gitlab.com/slepc/slepc)<br><sub>C</sub><br><sub>BSD-2-Clause</sub> | Parallel solvers for large sparse eigenvalue problems, built on PETSc. |  |
| [yixuan/<br>spectra](https://github.com/yixuan/spectra)<br><sub>C++</sub><br><sub>MPL-2.0</sub> | Header-only C++ library for computing a few eigenvalues of large matrices. |  |

## <a id="matrix-free-operators-and-partitioning"></a>16.7 Matrix-free operators and partitioning

| Name, language and license | Description | Note |
| --- | --- | --- |
| [CEED/<br>libCEED](https://github.com/CEED/libCEED)<br><sub>C</sub><br><sub>BSD-2-Clause, with LGPL deal.II examples</sub> | Matrix-free evaluation of finite element operators on CPUs and GPUs. |  |
| [KaHIP/<br>KaHIP](https://github.com/KaHIP/KaHIP)<br><sub>C++</sub><br><sub>MIT</sub> | Multilevel graph partitioning and node ordering. |  |
| [KarypisLab/<br>METIS](https://github.com/KarypisLab/METIS)<br><sub>C</sub><br><sub>Apache-2.0</sub> | Graph and mesh partitioning, and fill-reducing orderings for sparse matrices. |  |
| [KarypisLab/<br>ParMETIS](https://github.com/KarypisLab/ParMETIS)<br><sub>C</sub><br><sub>custom, with non-commercial restrictions</sub> | MPI library for parallel partitioning and fill-reducing ordering. | Free only for non-profit and US government education and research; others need approval for anything beyond evaluation; redistribution also needs approval. |

[← Back to the main list](../README.md#contents)
