# install CUDA
- install CUDA tookit 11.8 from NVIDIA site

# install cupy
```shell
$ conda install -c conda-forge cupy cudatoolkit=11.8
```

# install opencl
```shell
$ conda install -c conda-forge pyopencl
```

# setup:
```shell
$ python setup.py install
```

# remove:
```shell
$ pip remove learn_python
```

# clean:
```shell
$ python setup.py clean -a
```