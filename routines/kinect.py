import serial
from lib.wall import Wall
from lib.kinect import Kinect
from datetime import timedelta, datetime

def run(wall):
    kinect = Kinect()
    stop_time = datetime.now() + timedelta(seconds=180)
    while datetime.now() < stop_time:
        frame = kinect.get_reduced_frame()
        frame = -1 + 1.8*frame
        wall.write(frame)

if __name__ == '__main__':
    wall = Wall()
    run(wall)
