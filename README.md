This repository is a research artifact for 
"[Register Tiling for Unstructured Sparsity in Neural Network Inference](https://dl.acm.org/doi/pdf/10.1145/3591302), Lucas Wilkinson*, Kazem Cheshmi*, Maryam Mehri Dehnavi
, PLDI23". 

# Code overview

- `cpp_testbed/demo/SPMM_demo.cpp`: benchmarking code (best to use the `python3 artifact/run_matrix.py` wrapper)
- `spmm_nano_kernels/codegen/generate_ukernels.py`: entry point for generating scheduler/executor pairs
- `spmm_nano_kernels/codegen/base_ukernel_codegen.py`: code for generating mini-register tiles, this code in conjunction with `spmm_nano_kernels/include/Executor.h` forms the executor code
- `spmm_nano_kernels/include/MicroKernelPacker.h`: templated scheduler + data-compressor code
- `spmm_nano_kernels/include/MatMulSpecialized.h`: wrapper that contains a scheduler/executor pair
- `sbench/ilp_pad/nano_solver.py` contains the code for the mathematical model
