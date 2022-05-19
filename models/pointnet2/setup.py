from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
import torch

TORCH_MAJOR_VERSION = torch.__version__.split(".")[0]
TORCH_MINOR_VERSION = torch.__version__.split(".")[1]
setup(
    name='pointnet2',
    ext_modules=[
        CUDAExtension('pointnet2_cuda', [
            'src/pointnet2_api.cpp',

            'src/ball_query.cpp',
            'src/ball_query_gpu.cu',
            'src/group_points.cpp',
            'src/group_points_gpu.cu',
            'src/interpolate.cpp',
            'src/interpolate_gpu.cu',
            'src/sampling.cpp',
            'src/sampling_gpu.cu',
        ],
                      extra_compile_args={'cxx': ['-g', '-DTORCH_MAJOR_VERSION={}'.format(TORCH_MAJOR_VERSION),
                                                  '-DTORCH_MINOR_VERSION={}'.format(TORCH_MINOR_VERSION)],
                                          'nvcc': ['-O2']})
    ],
    cmdclass={'build_ext': BuildExtension}
)

