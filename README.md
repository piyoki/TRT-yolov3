# TRT-yolov3

*** Copy Right 2020 Kevin Yu. All rights reserved.

*** Author: Kevin Yu

*** Update Time: 2020/06/02

Table of Contents
-----------------

* [Demo](#demo)
* [Dependencies](#dependencies)
* [Installation](#installation)
* [Usage](#usage)

Demo
----



Dependencies
------------

The following packages are required for this project. If you are using a **x86 PC**, you have to make sure you have CUDA, cuDNN, and TensorRT installed.

For **Jetson User**, CUDA, cuDNN, and TensorRT are pre-installed with JetPack. Assuming you are using JetPack >=4.2, you should be good to go.

- Python==3.6
- Onnx==1.4.1
- Protobuf==3.8.0
- Pycuda==2019.1.2
- OpenCV>=3.4
- CUDA>=10.0
- cuDNN>=7.5
- TensorRT>=6.0.1
- Numpy==1.16.0

**Notes:** You do not need to install the above dependencies separately, the installation script below will handle all the heavy-lifting installation work for you.

<a name="dependencies"></a>

Installation
------------

```bash
bash <(wget -qO- https://raw.githubusercontent.com/yqlbu/TRT-yolov3/master/setup.sh)
```

<a name="installation"></a>

Usage
-----

Command Chart

<a name="usage"></a>

Training
--------

Coming soon, please stay tuned.

Reference
---------

This project is built based on the source code provide by Mr. JkJung, you may find his wonderful TensorRT Tutorial [HERE](https://jkjung-avt.github.io/tensorrt-yolov3/). I also referenced source code of [NVIDIA/TensorRT](https://github.com/NVIDIA/TensorRT) samples to develop the ONNX >> TensorRT conversion.

Source: [jkjung-avt tensorrt_demos](https://github.com/jkjung-avt/tensorrt_demos#yolov3)

Lisense
-------

[MIT License](https://github.com/yqlbu/TRT-yolov3/blob/master/LICENSE)