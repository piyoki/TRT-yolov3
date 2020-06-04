#!/bin/bash

git clone https://github.com/AlexeyAB/darknet
cd ./darknet/
wget https://hidden-boat-623a.keviny-cloud.workers.dev/DeepLearning/yolov3-weights/darknet53.conv.74 -q --show-progress --no-clobber
sed -i 's|GPU=0|GPU=1|' Makefile
sed -i 's|CUDNN=0|CUDNN=1|' Makefile
sed -i 's|OPENCV=0|OPENCV=1|' Makefile
make
