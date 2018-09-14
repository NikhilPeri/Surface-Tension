from lib.wall import Wall

def run(wall):

	for i in range(3):
		wall.write_column('2', 0.8)
		wall.write_column('13', -1)
		sleep(3)
		wall.write_column('3', 0.8)
		wall.write_column('14', -1)
		sleep(3)
		wall.write_column('4', 0.8)
		wall.write_column('2', -1)
		sleep(3)
		wall.write_column('5', 0.8)
		wall.write_column('3', -1)
		sleep(3)
		wall.write_column('6', 0.8)
		wall.write_column('4', -1)
		sleep(3)
		wall.write_column('7', 0.8)
		wall.write_column('5', -1)
		sleep(3)
		wall.write_column('8', 0.8)
		wall.write_column('6', -1)
		sleep(3)
		wall.write_column('9', 0.8)
		wall.write_column('7', -1)
		sleep(3)
		wall.write_column('10', 0.8)
		wall.write_column('8', -1)
		sleep(3)
		wall.write_column('11', 0.8)
		wall.write_column('9', -1)
		sleep(3)
		wall.write_column('12', 0.8)
		wall.write_column('10', -1)
		sleep(3)
		wall.write_column('13', 0.8)
		wall.write_column('11', -1)
		sleep(3)
		wall.write_column('14', 0.8)
		wall.write_column('12', -1)
		sleep(3)

	wall.write_column('13', -1)
	wall.write_column('14', -1)



if __name__ == '__main__':
    serial.Serial('com3', 115200)
    wall = Wall(serial.Serial('com3', 115200))
    run(wall)
