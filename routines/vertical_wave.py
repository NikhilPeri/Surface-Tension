from lib.wall import Wall

def run(wall):
    #
    pass

if __name__ == '__main__':
    serial.Serial('com3', 115200)
    wall = Wall(serial.Serial('com3', 115200))
    run(wall)
