# [Wall]('lib/wall.py')
This is the primary interaction layer with the wall. The wall is composed of 26 linear actuators (servos) arranged in a
lattice structure shown below.
- Each actuator can be identified by its letter row and numeric column.
- Each actuator can be moved to an absolute position in the range of -1 (retracted) to +1 (extended)

![Wall Layout](./wall_layout.png)

## Methods
 **__init__(self, comm=None)**
  constructor
  *comm* is a comm port on which the wall is connected if no value is specified the [DEFAULT_COM_BAUD](../lib/constants.py) will be used

**reset(self)**
  moves all the servo to the fully retracted position

**write_servo(self, row, col, position)**
  writes an individual servo to a position
  *row* a single letter specifying the target row ('B', 'C', 'D', 'E')
  *col* a integer corresponding to a valid column for the desired row
  *position* a float between -1 and +1 representing the desired position

**write_row(self, row, position)**
  writes a complete row of servos to a position
  *row* a single letter specifying the target row ('B', 'C', 'D', 'E')
  *position* a float between -1 and +1 representing the desired position

**write_column(self, col, position)**
  writes a complete column of servos to a position
  *col* a integer corresponding to a valid column for the desired row
  *position* a float between -1 and +1 representing the desired position

**write(self, array)**
  writes each servo to a position
  *array* a 2D array where index 0 contains 6 values corresponsing to row E, index 1 contains 7 values corresponding to row D
  index 2 contains 6 values corresponding to row C, and index 3 contains 7 values corresponding to row B
