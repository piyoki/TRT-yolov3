export DARKNET=/home/kev/TRT-yolov3/train/darknet
export PRJ_PATH=/home/kev/TRT-yolov3/train

cd $DARKNET
./darknet detector test \
$PRJ_PATH/model.data \
$PRJ_PATH/model-yolov3-tiny.cfg \
$PRJ_PATH/backup/model-yolov3-tiny_final.weights \
-ext_output $PRJ_PATH/img/test.jpg \
-dont_show