
"""engine.py

The BBoxVisualization class implements drawing of nice looking
bounding boxes based on object detection results.

This file was modified from:
https://github.com/jkjung-avt/tensorrt_demos/blob/master/utils/visualization.py
"""

import numpy as np
import cv2
import time

# Constants
ALPHA = 0.3
FONT = cv2.FONT_HERSHEY_COMPLEX
TEXT_SCALE = 0.5
TEXT_THICKNESS = 1
BLACK = (0, 0, 0)
GREY = (45, 45, 45)
WHITE = (255, 255, 255)

def gen_colors(num_colors):
    """Generate different colors.
    # Arguments
      num_colors: total number of colors/classes.
    # Output
      bgrs: a list of (B, G, R) tuples which correspond to each of
            the colors/classes.
    """
    import random
    import colorsys

    hsvs = [[float(x) / num_colors, 1., 0.9] for x in range(num_colors)]
    random.seed(2333)
    random.shuffle(hsvs)
    rgbs = list(map(lambda x: list(colorsys.hsv_to_rgb(*x)), hsvs))
    bgrs = [(int(rgb[2] * 255), int(rgb[1] * 255),  int(rgb[0] * 255))
            for rgb in rgbs]
    return bgrs

def draw_text(img,cls_name,x_min,y_min):
    if len(cls_name) > 6 and len(cls_name) <= 8:
        width = len(cls_name) * 10 + 10
    elif len(cls_name) > 8 and len(cls_name) <= 10:
        width = len(cls_name) * 10 + 5
    elif len(cls_name) > 10:
        width = len(cls_name) * 10 - 25
    else:
        width = len(cls_name) * 10 + 7
    cv2.rectangle(img, (x_min, y_min), (x_min+width, y_min-20), GREY, cv2.FILLED)
    cv2.putText(img,cls_name,(x_min+2, y_min-8),FONT,TEXT_SCALE,WHITE,TEXT_THICKNESS,cv2.LINE_8)
    return img

class Detect_Object(object):
    def __init__(self,classID,label,conf,x_min,y_min,x_max, y_max):
        self.classID = classID
        self.label = label
        self.conf = round(conf,2)
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
        self.area = (y_max-y_min) * (x_max-x_min)
        self.center = ((y_max+y_min)/2, (x_max+x_min)/2)
    def print_info(self):
        print(' ', '-' * 2, 'ClassID:  ', ' '*2, self.classID)
        print(' ', '-' * 2, 'Confidence:  ',     self.conf)
        print(' ', '-' * 2, 'X_min:  ', ' '*4,   self.x_min)
        print(' ', '-' * 2, 'Y_min:  ', ' '*4,   self.y_min)
        print(' ', '-' * 2, 'X_max:  ', ' '*4,   self.x_max)
        print(' ', '-' * 2, 'Y_max:  ', ' '*4,   self.y_max)
        print(' ', '-' * 2, 'Area:  ', ' '*5,    self.area)
        print(' ', '-' * 2, 'Center:  ', ' '*3,  self.center, '\n')

class BBoxVisualization():
    """BBoxVisualization class implements nice drawing of boudning boxes.
    # Arguments
      cls_dict: a dictionary used to translate class id to its name.
    """

    def __init__(self, cls_dict):
        self.cls_dict = cls_dict
        self.colors = gen_colors(len(cls_dict))

    def print_stats(self, obj_dict):
        print('\n')
        print('[INFO] ', 'Detection Stats')
        print('[INFO] ', '-' * 30)
        print('[INFO]  Detector: {} objects detected!'.format(obj_dict.get('objects')))
        for cls in obj_dict['counter']:
            print('[INFO] ', cls, ': {}'.format(obj_dict['counter'][cls]))
        print('[INFO] ', '-' * 30)

    def draw_bboxes(self, img, boxes, confs, clss):
        """Draw detected bounding boxes on the original image."""
        start_time = time.time()
        blk = np.zeros(img.shape, np.uint8)
        obj_dict = {
            'objects': 0,
            'counter': dict()
        }
        for bb, cf, cl in zip(boxes, confs, clss):
            cl = int(cl)
            x_min, y_min, x_max, y_max = bb[0], bb[1], bb[2], bb[3]
            color = self.colors[cl]
            cv2.rectangle(img, (x_min, y_min), (x_max, y_max), color, 2)
            cv2.rectangle(blk, (x_min, y_min), (x_max, y_max), color, cv2.FILLED)
            cls_name = self.cls_dict.get(cl, 'CLS{}'.format(cl))
            img = draw_text(img,cls_name,x_min,y_min)  # draw cls_label
            obj = Detect_Object(cl,cls_name,cf,x_min,y_min,x_max, y_max)  # create detection object
            obj.print_info()  # print object info
            print(obj)

            if cls_name in obj_dict['counter']:
                obj_dict['counter'][cls_name] += 1
            else:
                obj_dict['counter'][cls_name] = 1
            obj_dict['objects'] += 1

        img = cv2.addWeighted(img, 1, blk, ALPHA, 1)

        visualize_time = (time.time() - start_time)*1000
        self.print_stats(obj_dict)

        return img, visualize_time
