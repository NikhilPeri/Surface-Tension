import serial
from lib.wall import Wall
from lib.kinect import Kinect
from datetime import timedelta, datetime

def run(wall):
    kinect = Kinect()
    stop_time = datetime.now() + timedelta(seconds=60)
    while datetime.now() < stop_time:
        frame = kinect.get_reduced_frame()
        frame = -1 + 2*frame
        wall.write(frame)

if __name__ == '__main__':
    wall = Wall(serial.Serial('/dev/ttyUSB0', 115200))
    run(wall)
