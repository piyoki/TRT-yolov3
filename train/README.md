# Yolov3 Dataloader (Local Machine)

![](https://img.shields.io/static/v1?label=Python&message=3.6&color=green)
![](https://img.shields.io/static/v1?label=ONNX&message=1.4.1&color=yellow)
![](https://img.shields.io/static/v1?label=TRT&message=6.0.1&color=orange)
![](https://img.shields.io/static/v1?label=License&message=MIT&color=red)

*** Author: Kevin Yu (www.github.com/yqlbu)

*** Email: kevinyu211@yahoo.com

- This tool is tailored for those who want to train their custom dataset on a Yolov3 Model. 

- Make sure you read the instructions in the **training.ipynb** for each step carefully !!!

- If you following the instructions below step by step, it will generate a new trained-weight in the end, and you are able to re-build the model with TensorRT Engine.

- Make sure you open Jupyter Notebook or JupyterLab at **/TRT-yolov3** directory.

Table of Contents
-----------------

* [Demo](#demo)
* [Train Model](#train-model)
* [Export Model](#export-model)
* [Build Engine](#build-engine)

Demo
----

Hardware specs and training params: 

- Device Name: NVIDIA Jetson AGX Xavier DevKit
- Memory: 32G
- Model: YOLOv3-tiny (Mask dataset)
- Batch: 32 (recommended)
- Subdivisions: 4 (recommended)
- Maxbatches: 5000 epoches
- Number of classes: 2
- Total training time: 1.5 hrs

![](../demo_screenshots/training.png)

<a name="demo"></a>

Train Model
-----------

The detailed steps are all demonstrated in the **[TRT-yolov3/train/training.ipynb](https://github.com/yqlbu/TRT-yolov3/blob/master/train/training.ipynb)**, if you carefully read and properly follow the steps, you should be able to train a YOLOv3 with your custom dataset.

<a name="train-model"></a>

Export Model
------------

<a name="export-model"></a>

Build Engine
----------------

<a name="build-engine"></a>


Lisense
-------

[MIT License](https://github.com/yqlbu/TRT-yolov3/blob/master/LICENSE)