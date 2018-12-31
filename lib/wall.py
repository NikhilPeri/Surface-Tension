import serial
from time import sleep
from lib.constants import DEFAULT_CHANNEL_MAPPINGS, DEFAULT_COM_PORT, DEFAULT_COM_BAUD
from lib.servo import Servo
import numpy as np

ROWS=['E', 'D', 'C', 'B']
# Wall object takes in it's own instance, set the servo to comm
class Wall(object):
    def __init__(self, comm=None):
        if comm is None or not comm.is_open:
            self.comm = serial.Serial(DEFAULT_COM_PORT, DEFAULT_COM_BAUD)
        else:
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
        for row_index, row in enumerate(array):
            for col_index, position in enumerate(row):
                if row_index % 2 == 0:
                    self.write_servo(ROWS[row_index], 2*col_index + 3, position)
                else:
                    self.write_servo(ROWS[row_index], 2*col_index + 2, position)

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
