import serial
import time
import numpy as np

from lib.wall import Wall

# Run a random routine on the wall
def run(wall):
	for i in range(15):
		rand = np.random.rand(4)
		odd = 3 + 2*np.random.randint(0, 6, size=2)
		even = 2 + 2*np.random.randint(0, 7, size=2)
		wall.write_servo('B', str(even[0]), -1.0 + rand[0]*1.8)
		wall.write_servo('C', str(odd[0]), -1.0 + rand[1]*1.8)
		time.sleep(3*rand[0])

		wall.write_servo('D', str(even[1]), -1.0 + rand[2]*1.8)
		wall.write_servo('E', str(odd[1]), -1.0 + rand[3]*1.8)
		time.sleep(3*rand[1])


if __name__ == '__main__':
    wall = Wall(serial.Serial('/dev/ttyUSB0', 115200))
    run(wall)
