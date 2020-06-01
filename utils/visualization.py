"""visualization.py
draw widgets on main frame
"""

import cv2


def open_window(window_name, width, height, title):
    """Open the display window."""
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, width, height)
    cv2.setWindowTitle(window_name, title)

def show_fps(img, fps):
    """Draw fps number at top-left corner of the image."""
    font = cv2.FONT_HERSHEY_SIMPLEX
    line = cv2.LINE_AA
    cv2.putText(img, "FPS: {:.1f}".format(fps), (11, 25), font, 0.5, (32, 32, 32), 4, line)
    cv2.putText(img, "FPS: {:.1f}".format(fps), (10, 25), font, 0.5, (240, 240, 240), 1, line)
    return img


def record_time(a, b, c, d):
    time_stamp = {
        '_preprocess': a,
        '_postprocess': b,
        '_network': c,
        '_visualize': d,
        '_total': round((a + b + c + d), 4)
    }
    return time_stamp


def show_runtime(time_stamp):
    print('[TRT]  ', 'Timing Report')
    print('[TRT]  ', '-' * 30)
    print('[TRT]  ', 'Pre-Process  ', 'CUDA ', str(round(time_stamp['_preprocess'], 5)) + 'ms')
    print('[TRT]  ', 'Post-Process ', 'CUDA ', str(round(time_stamp['_postprocess'], 5)) + 'ms')
    print('[TRT]  ', 'Network ', ' ' * 4, 'CUDA ', str(round(time_stamp['_network'], 5)) + 'ms')
    print('[TRT]  ', 'Visualize', ' ' * 3, 'CUDA ', str(round(time_stamp['_visualize'], 5)) + 'ms')
    print('[TRT]  ', 'Total', ' ' * 7, 'CUDA ', str(round(time_stamp['_total'], 5)) + 'ms')
    print('[TRT]  ', '-' * 30, '\n')
