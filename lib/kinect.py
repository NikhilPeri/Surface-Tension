import matplotlib.pyplot as plt
from skimage.measure import block_reduce

import freenect as kinect
import numpy as np
import logging

FRAME_SHAPE=(480, 640)
WALL_SHAPE=(6, 8)
BLOCK_SIZE=(
    int(FRAME_SHAPE[0]/WALL_SHAPE[0]),
    int(FRAME_SHAPE[1]/WALL_SHAPE[1])
)
class Kinect(object):
    def __init__(self, calibration_file='config/calibration.frame', debug=False):
        try:
            self.device = kinect.open_device(kinect.init(), 0)
            kinect.set_tilt_degs(self.device, -90)
            kinect.close_device(self.device)
        except Exception as e:
            logging.error('No Kinect detected')
            self.device = None

        with open(calibration_file) as calibration_file:
            self.calibration_frame = np.load(calibration_file)
        if debug:
            self.debug_plot = (
                plt.figure()
                .add_subplot(111)
                .imshow(np.ones(WALL_SHAPE), cmap='hot')
            )
            plt.show(block=False)
        else:
            self.debug_plot = None

    def get_frame(self):
        try:
            frame, _ = kinect.sync_get_depth()
            return frame.astype(np.int16)
        except:
            return np.full(FRAME_SHAPE, 255)

    def get_reduced_frame(self):
        frame = self.calibration_frame - self.get_frame()
        frame = (frame > 0).astype(np.uint8)
        frame = block_reduce(frame, BLOCK_SIZE, np.mean)[1:5, 1:7]
        frame = (frame > 0).astype(np.uint8)
        frame = np.flip(frame, axis=1)

        return frame

    def debug_frame(self):
        if not self.debug_plot:
            return

        self.debug_plot.set_array(
            6000*self.get_reduced_frame()
        )
        self.debug_plot.figure.canvas.draw()
