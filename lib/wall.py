from time import sleep
from lib.constants import DEFAULT_CHANNEL_MAPPINGS
from lib.servo import Servo

# Wall object takes in it's own instance, set the servo to comm
class Wall(object):
    def __init__(self, comm, channel_mappings=DEFAULT_CHANNEL_MAPPINGS):
        self.comm = comm
        self.servos = DEFAULT_CHANNEL_MAPPINGS
        for row, columns in self.servos.items():
            for column, channel in columns.items():
                self.servos[row][column] = Servo(channel, comm)

    # Write to the wall
    def write(self, array):
        pass
    
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
