"""detector.py
This script demonstrates how to do real-time object detection with
TensorRT optimized Single-Shot Multibox Detector (SSD) engine.
"""

import sys
import argparse
import cv2
import pycuda.autoinit  # This is needed for initializing CUDA driver

from utils.yolo_classes import get_cls_dict
from utils.yolov3 import TrtYOLOv3
from utils.camera import add_camera_args, Camera
from utils.visualization import open_window, show_fps, record_time, show_runtime
from utils.engine import BBoxVisualization


WINDOW_NAME = 'TensorRT YOLOv3 Detector'
INPUT_HW = (300, 300)
SUPPORTED_MODELS = [
    'ssd_mobilenet_v2_coco'
]


def parse_args():
    """Parse input arguments."""
    desc = ('Capture and display live camera video, while doing '
            'real-time object detection with TensorRT optimized '
            'YOLOv3 model on Jetson Family')
    parser = argparse.ArgumentParser(description=desc)
    parser = add_camera_args(parser)
    parser.add_argument('--model', type=str, default='yolov3-416',
                        choices=['yolov3-288', 'yolov3-416', 'yolov3-608',
                                 'yolov3-tiny-288', 'yolov3-tiny-416'])
    parser.add_argument('--runtime', action='store_true',
                        help='display detailed runtime')
    args = parser.parse_args()
    return args


def loop_and_detect(cam, runtime, trt_yolov3, conf_th, vis):
    """Continuously capture images from camera and do object detection.
    # Arguments
      cam: the camera instance (video source).
      trt_ssd: the TRT SSD object detector instance.
      conf_th: confidence/score threshold for object detection.
      vis: for visualization.
    """

    while True:
        if cv2.getWindowProperty(WINDOW_NAME, 0) < 0:
            break
        timer = cv2.getTickCount()
        img = cam.read().copy()
        if img is not None:
            if runtime:
                boxes, confs, clss, _preprocess_time, _postprocess_time,_network_time = trt_yolov3.detect(img, conf_th)
                img, _visualize_time = vis.draw_bboxes(img, boxes, confs, clss)
                time_stamp = record_time(_preprocess_time, _postprocess_time, _network_time, _visualize_time)
                show_runtime(time_stamp)
            else:
                boxes, confs, clss, _, _, _ = trt_yolov3.detect(img, conf_th)
                img, _ = vis.draw_bboxes(img, boxes, confs, clss)
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
            img = show_fps(img, fps)
            cv2.imshow(WINDOW_NAME, img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def main():
    args = parse_args()
    cam = Camera(args)
    cam.open()
    if not cam.is_opened:
        sys.exit('[INFO]  Failed to open camera!')

    cls_dict = get_cls_dict('coco')
    yolo_dim = int(args.model.split('-')[-1])  # 416 or 608
    trt_yolov3 = TrtYOLOv3(args.model, (yolo_dim, yolo_dim))

    print('[INFO]  Camera: starting')
    cam.start()
    open_window(WINDOW_NAME, args.image_width, args.image_height,
                'TensorRT YOLOv3 Detector')
    vis = BBoxVisualization(cls_dict)
    loop_and_detect(cam, args.runtime, trt_yolov3, conf_th=0.3, vis=vis)

    print('[INFO]  Program: stopped')
    cam.stop()
    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
