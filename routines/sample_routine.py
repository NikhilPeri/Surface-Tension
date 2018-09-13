import serial
from lib.wall import Wall

def run(wall):
	return

if __name__ == '__main__':
    wall = Wall(serial.Serial('com3', 115200))
    run(wall)
