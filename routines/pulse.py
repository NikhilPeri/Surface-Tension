import serial
from lib.wall import Wall
import time

def run(wall):
    for i in range(2):
        wall.write([
            [0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
            [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
            [0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
            [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
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
    wall = Wall()
    run(wall)
