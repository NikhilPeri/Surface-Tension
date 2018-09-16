import serial
from lib.wall import Wall
import time

def run(wall):
    for i in range(3):
        wall.write([
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
        ])
        time.sleep(6)
        wall.write([
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1],
        ])
        time.sleep(6)

if __name__ == '__main__':
    wall = Wall(serial.Serial('/dev/ttyUSB0', 115200))
    run(wall)
