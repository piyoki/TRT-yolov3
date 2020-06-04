export DARKNET=/home/kev/TRT-yolov3/train/darknet
export PRJ_PATH=/home/kev/TRT-yolov3/train

cd $DARKNET
mv darknet53.conv.74 cfg/
start=`date +%s`
./darknet detector train \
$PRJ_PATH/mask.data \
$PRJ_PATH/mask-yolov3-tiny.cfg \
$DARKNET/cfg/darknet53.conv.74 \
-dont_show
end=`date +%s`
echo "[BASH]  Total training time was `expr $end - $start` seconds"