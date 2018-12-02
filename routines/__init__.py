import os
import importlib
import numpy as np

from lib.constants import DEFAULT_CHANNEL_MAPPINGS
from lib.servo import Servo
from lib.wall import Wall

BLACKLIST = [
    '__init__.py',
    'sample_routine.py',
]

# List all the routines available for the wall
def list_routines():
    routines = {}

    for routine in os.listdir('routines'):
        if routine in BLACKLIST or routine.startswith('test') or not routine.endswith('.py'):
            continue
        name = routine.replace('.py', '')
        module = importlib.import_module("routines.{}".format(name))
        routines[name] = module

    return routines
'''
class FakeServo(Servo):
    def __init__(self, row, column, plot):
        self.row = row
        self.column = column
        self.plot = plot

    def write(self, position):
        import pdb; pdb.set_trace()
        new_plot = self.plot.get_array()
        new_plot[self.row][self.column] = 255*(1 + position)
        self.plot.set_array(new_plot)
        self.plot.figure.canvas.draw()

class FakeWall(Wall):
    def __init__(self):
        self.plot = (
            plt.figure()
            .add_subplot(111)
            .imshow(np.zeros((4, 14)))
        )
        plt.legend()
        plt.show(block=False)

        ROW_MAPPTINGS = {'E': 0, 'D': 1, 'C': 2, 'B': 3}
        self.servos = DEFAULT_CHANNEL_MAPPINGS
        for row, columns in self.servos.items():
            for column, channel in columns.items():
                self.servos[row][column] = FakeServo(ROW_MAPPTINGS[row], int(column), self.plot)
'''
