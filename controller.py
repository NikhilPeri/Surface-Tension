import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

from skimage.measure import block_reduce
from skimage.transform import rescale

import freenect as kinect
import numpy as np
import logging
import sys

FRAME_SHAPE=(480, 640)
WALL_SHAPE=(6, 8)
BLOCK_SIZE=(
    int(FRAME_SHAPE[0]/WALL_SHAPE[0]),
    int(FRAME_SHAPE[1]/WALL_SHAPE[1])
)

CALIBRATION_PATH='responsive_wall/tmp/calibration.frame'

global debug_plot

def get_frame():
    try:
        frame, _ = kinect.sync_get_depth()
        return frame.astype(np.uint16)
    except:
        logging.error('Failed to read frame')
        return np.full(FRAME_SHAPE, 255)

def transform_frame(frame):
    frame = block_reduce(frame, BLOCK_SIZE, np.mean)
    frame = frame[1:4, 1:6]
    return frame

def display_frame(frame):
    print frame

def debug_frame(frame):
    debug_plot.set_array(frame)
    debug_plot.figure.canvas.draw()

if __name__ == '__main__':
    calibration_frame = None
    with open(CALIBRATION_PATH) as calibration_file:
        calibration_frame = np.load(calibration_file)

    if calibration_frame is None:
        raise ValueError('Could not load calibration file: {}'.format(CALIBRATION_PATH))

    debug_mode = '--debug' in sys.argv
    if debug_mode:
        debug_plot = (
            plt.figure()
            .add_subplot(111)
            .imshow(np.random.rand(4,6), cmap='hot')
        )
        plt.legend()
        plt.show(block=False)

    while True:
        frame = get_frame()
        print 'read frame'
        frame = calibration_frame - frame
        frame = (frame < 100).astype(np.uint8)
        debug_frame(frame)
        frame = 6000*transform_frame(frame)
        if debug_mode:
            debug_frame(frame)
