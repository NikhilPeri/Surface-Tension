import serial
import time
from lib.wall import Wall

# Vertical wave run
def run(wall):
    for i in range(3):
    	wall.write_row('B', 0.8)
    	wall.write_row('D', -1)
    	time.sleep(3)

    	wall.write_row('C', 0.8)
    	wall.write_row('E', -1)
    	time.sleep(3)

    	wall.write_row('D', 0.8)
    	wall.write_row('B', -1)
    	time.sleep(3)

    	wall.write_row('E', 0.8)
    	wall.write_row('C', -1)
    	time.sleep(3)

    wall.write_row('D', -1)
    wall.write_row('E', -1)


if __name__ == '__main__':
    wall = Wall()
    run(wall)
