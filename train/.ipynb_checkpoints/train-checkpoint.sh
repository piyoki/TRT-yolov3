export DARKNET=/home/nvidia/yolov3-dataloader/darknet
export PRJ_PATH=/home/nvidia/yolov3-dataloader

cd $DARKNET
time ./darknet detector train \
$PRJ_PATH/pastry.data \
$PRJ_PATH/pastry-yolov3-tiny.cfg \
$DARKNET/cfg/darknet53.conv.74 \
-dont_show