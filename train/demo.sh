export DARKNET=/home/kev/TRT-yolov3/train/darknet
export PRJ_PATH=/home/kev/TRT-yolov3/train

cd $DARKNET
./darknet detector test \
$PRJ_PATH/mask.data \
$PRJ_PATH/mask-yolov3-tiny.cfg \
$PRJ_PATH/backup/mask-yolov3-tiny_final.weights \
-ext_output $PRJ_PATH/img/test_2.jpg \
-dont_show