from time import sleep
from lib.constants import DEFAULT_CHANNEL_MAPPINGS
from lib.servo import Servo
import numpy as np

# Wall object takes in it's own instance, set the servo to comm
class Wall(object):
    def __init__(self, comm, channel_mappings=DEFAULT_CHANNEL_MAPPINGS):
        self.comm = comm
        self.servos = DEFAULT_CHANNEL_MAPPINGS
        for row, columns in self.servos.items():
            for column, channel in columns.items():
                self.servos[row][column] = Servo(channel, comm)

    def reset(self):
        for servo in self.list_servos():
            servo.write(-1)
    
    # Write to the wall
    def write(self, array):
        rowE, rowD, rowC, rowB = []
        rowE = array[0]
        rowD = array[1]
        rowC = array[2]
        rowB = array[3]

        for i in range(len(rowE))
            self.servos['E'][str((i*2)+3)].write(rowE[i])
        for i in range(len(rowD))
            self.servos['D'][str(i*2)+2].write(rowD[i])
        for i in range(len(rowC))
            self.servos['C'][str((i*2)+3)].write(rowC[i])
        for i in range(len(rowB))
            self.servos['B'][str(i*2)+2].write(rowB[i])
    
    # Write to servo
    def write_servo(self, row, col, position):
        self.servos[str(row)][str(col)].write(position)

    # Write to row
    def write_row(self, row, position):
        row = str(row)
        for servo in self.servos[row].values():
            servo.write(position)

    # Write to col
    def write_column(self, col, position):
        col = str(col)
        for columns in self.servos.values():
            if columns.has_key(col):
                columns[col].write(position)

    # List the servos of the wall
    def list_servos(self):
        servos = []
        for column in self.servos.values():
            for servo in column.values():
                servos.append(servo)
        return servos
