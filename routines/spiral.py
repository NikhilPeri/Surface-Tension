import serial
import time
from lib.wall import Wall

# Spiral wave run
def run(wall):
    for i in range(1):
        wall.write_servo('E', 3, 0.8)
        time.sleep(2)

        wall.write_servo('E', 5, 0.8)
        time.sleep(2)

        wall.write_servo('E', 3, -1)
        wall.write_servo('E', 7, 0.8)
        time.sleep(2)

        wall.write_servo('E', 5, -1)
        wall.write_servo('E', 9, 0.8)
        time.sleep(2)

        wall.write_servo('E', 7, -1)
        wall.write_servo('E', 11, 0.8)
        time.sleep(2)

        wall.write_servo('E', 9, -1)
        wall.write_servo('E', 13, 0.8)
        time.sleep(2)

        wall.write_servo('E', 11, -1)
        wall.write_servo('D', 14, 0.8)
        time.sleep(2)

        wall.write_servo('E', 13, -1)
        wall.write_servo('C', 13, 0.8)
        time.sleep(2)

        wall.write_servo('D', 14, -1)
        wall.write_servo('B', 14, 0.8)
        time.sleep(2)

        wall.write_servo('C', 13, -1)
        wall.write_servo('B', 12, 0.8)
        time.sleep(2)

        wall.write_servo('B', 14, -1)
        wall.write_servo('B', 10, 0.8)
        time.sleep(2)

        wall.write_servo('B', 12, -1)
        wall.write_servo('B', 8, 0.8)
        time.sleep(2)

        wall.write_servo('B', 10, -1)
        wall.write_servo('B', 6, 0.8)
        time.sleep(2)

        wall.write_servo('B', 8, -1)
        wall.write_servo('B', 4, 0.8)
        time.sleep(2)

        wall.write_servo('B', 6, -1)
        wall.write_servo('B', 2, 0.8)
        time.sleep(2)

        wall.write_servo('B', 4, -1)
        wall.write_servo('C', 3, 0.8)
        time.sleep(2)

        wall.write_servo('B', 2, -1)
        wall.write_servo('D', 2, 0.8)
        time.sleep(2)

        wall.write_servo('C', 3, -1)
        wall.write_servo('D', 4, 0.8)
        time.sleep(2)

        wall.write_servo('D', 2, -1)
        wall.write_servo('D', 6, 0.8)
        time.sleep(2)

        wall.write_servo('D', 4, -1)
        wall.write_servo('D', 8, 0.8)
        time.sleep(2)

        wall.write_servo('D', 6, -1)
        wall.write_servo('D', 10, 0.8)
        time.sleep(2)

        wall.write_servo('D', 8, -1)
        wall.write_servo('D', 12, 0.8)
        time.sleep(2)

        wall.write_servo('D', 10, -1)
        wall.write_servo('C', 11, 0.8)
        time.sleep(2)

        wall.write_servo('D', 12, -1)
        wall.write_servo('C', 9, 0.8)
        time.sleep(2)

        wall.write_servo('C', 11, -1)
        wall.write_servo('C', 7, 0.8)
        time.sleep(2)

        wall.write_servo('C', 9, -1)
        wall.write_servo('C', 5, 0.8)
        time.sleep(2)

        wall.write_servo('C', 7, -1)
        time.sleep(2)
        wall.write_servo('C', 5, -1)

if __name__ == '__main__':
    wall = Wall(serial.Serial('/dev/ttyUSB0', 115200))
    run(wall)
