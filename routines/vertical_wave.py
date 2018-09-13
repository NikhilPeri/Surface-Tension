import serial
from time import sleep
from lib.wall import Wall

def run(wall):
    for i in range(3):
    	wall.write_row('B', 0.8)
    	wall.write_row('D', -1)
    	sleep(3)
    	wall.write_row('C', 0.8)
    	wall.write_row('E', -1)
    	sleep(3)
    	wall.write_row('D', 0.8)
    	wall.write_row('B', -1)
    	sleep(3)
    	wall.write_row('E', 0.8)
    	wall.write_row('C', -1)
    	sleep(3)



if __name__ == '__main__':
    wall = Wall(serial.Serial('/dev/ttyUSB0', 115200))
    run(wall)
