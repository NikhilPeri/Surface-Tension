import pyserial_motor as servo
import time
import queue

def main():
	global dis;
	dis = 0.8;
	#ts = 6;
	global queue;	
	queue = queue.Queue();
	
	servosDictionary = {}
	
	servosDictionary['B2'] = 0
	servosDictionary['B4'] = 1
	servosDictionary['B6'] = 2
	servosDictionary['B8'] = 3
	servosDictionary['B10'] = 4
	servosDictionary['C3'] = 5
	servosDictionary['C5'] = 6
	servosDictionary['C7'] = 7
	servosDictionary['C9'] = 8
	servosDictionary['D2'] = 9
	servosDictionary['D4'] = 10
	servosDictionary['D6'] = 11
	servosDictionary['D8'] = 12
	servosDictionary['D10'] = 13
	servosDictionary['E3'] = 14
	servosDictionary['E5'] = 15
	servosDictionary['E7'] = 16
	servosDictionary['E9'] = 17

	print('start');
	global com_port
	com_port = servo.servo_init('COM3')
	
	servo.servo_move_float(0, -1)
	servo.servo_move_float(1, -1)
	servo.servo_move_float(2, -1)
	time.sleep(0.05)
	servo.servo_move_float(3, -1)
	servo.servo_move_float(4, -1)
	servo.servo_move_float(5, -1)
	time.sleep(0.05)
	servo.servo_move_float(6, -1)
	servo.servo_move_float(7, -1)
	servo.servo_move_float(8, -1)
	time.sleep(0.05)
	servo.servo_move_float(9, -1)
	servo.servo_move_float(10, -1)
	servo.servo_move_float(11, -1)
	time.sleep(0.05)
	servo.servo_move_float(12, -1)
	servo.servo_move_float(13, -1)
	servo.servo_move_float(14, -1)
	time.sleep(0.05)
	servo.servo_move_float(15, -1)
	servo.servo_move_float(16, -1)
	servo.servo_move_float(17, -1)
	time.sleep(0.05)
	
	servo.servo_move_float(30, 0)
	servo.servo_move_float(31, 0)
	
	time.sleep(5)
	
	while True:
		# servo.servo_move_float_cmd_1(0, 1, 0)
		# servo.servo_move_float_cmd_1(1, 1, 0)
		# servo.servo_move_float_cmd_1(2, 1, 0)
		# servo.servo_move_float_cmd_1(3, 1, 0)
		# servo.servo_move_float_cmd_1(4, 1, 0)
		# servo.servo_move_float_cmd_1(5, 1, 0)
		# servo.servo_move_float_cmd_1(6, 1, 8)
		# servo.servo_move_float_cmd_1(7, 1, 0)
		# servo.servo_move_float_cmd_1(8, 1, 0)
		# servo.servo_move_float_cmd_1(9, 1, 0)
		# servo.servo_move_float_cmd_1(10, 1, 0)
		# servo.servo_move_float_cmd_1(11, 1, 0)
		# servo.servo_move_float_cmd_1(12, 1, 0)
		# servo.servo_move_float_cmd_1(13, 1, 0)
		# servo.servo_move_float_cmd_1(14, 1, 0)
		# servo.servo_move_float_cmd_1(15, 1, 0)
		# servo.servo_move_float_cmd_1(16, 1, 0)
		# servo.servo_move_float_cmd_1(17, 1, 8)
		# servo.servo_move_float_cmd_1(0, -1, 0)
		# servo.servo_move_float_cmd_1(1, -1, 0)
		# servo.servo_move_float_cmd_1(2, -1, 0)
		# servo.servo_move_float_cmd_1(3, -1, 0)
		# servo.servo_move_float_cmd_1(4, -1, 0)
		# servo.servo_move_float_cmd_1(5, -1, 0)
		# servo.servo_move_float_cmd_1(6, -1, 8)
		# servo.servo_move_float_cmd_1(7, -1, 0)
		# servo.servo_move_float_cmd_1(8, -1, 0)
		# servo.servo_move_float_cmd_1(9, -1, 0)
		# servo.servo_move_float_cmd_1(10, -1, 0)
		# servo.servo_move_float_cmd_1(11, -1, 0)
		# servo.servo_move_float_cmd_1(12, -1, 0)
		# servo.servo_move_float_cmd_1(13, -1, 0)
		# servo.servo_move_float_cmd_1(14, -1, 0)
		# servo.servo_move_float_cmd_1(15, -1, 0)
		# servo.servo_move_float_cmd_1(16, -1, 0)
		# servo.servo_move_float_cmd_1(17, -1, 8)
		
		vertical_wave_1()
	
	# while True:
		# servo.servo_move_float(7, 1)
		# time.sleep(val)
		# servo.servo_move_float(8, 1)
		# time.sleep(val)
		# servo.servo_move_float(7, -1)
		# time.sleep(val)
		# servo.servo_move_float(8, -1)
		# time.sleep(val)
	
	global counter
	counter = 0
	while True:
		
		vertical_wave(counter)
		
		#drop_wave(counter)
		#circle_wave(counter)
		
		#below are background tasks needed to run the machine
		counter = (counter+1) % 24000
		
		scheduler()
		time.sleep(0.05)
		
def scheduler():
	if(not(queue.empty())):
		command = queue.get()
		com_port.write(command.encode('utf-8'))
		
		
def vertical_wave_1():
		servo.servo_move_float_cmd_1(0, dis, 0)
		servo.servo_move_float_cmd_1(1, dis, 0)
		servo.servo_move_float_cmd_1(2, dis, 0)
		servo.servo_move_float_cmd_1(3, dis, 0)
		servo.servo_move_float_cmd_1(4, dis, 3)
		servo.servo_move_float_cmd_1(9, -1, 0)
		servo.servo_move_float_cmd_1(10, -1, 0)
		servo.servo_move_float_cmd_1(11, -1, 0)
		servo.servo_move_float_cmd_1(12, -1, 0)
		servo.servo_move_float_cmd_1(13, -1, 3)
		
		servo.servo_move_float_cmd_1(5, dis, 0)
		servo.servo_move_float_cmd_1(6, dis, 0)
		servo.servo_move_float_cmd_1(7, dis, 0)
		servo.servo_move_float_cmd_1(8, dis, 3)
		servo.servo_move_float_cmd_1(14, -1, 0)
		servo.servo_move_float_cmd_1(15, -1, 0)
		servo.servo_move_float_cmd_1(16, -1, 0)
		servo.servo_move_float_cmd_1(17, -1, 3)
		
		
		servo.servo_move_float_cmd_1(9, dis, 0)
		servo.servo_move_float_cmd_1(10, dis, 0)
		servo.servo_move_float_cmd_1(11, dis, 0)
		servo.servo_move_float_cmd_1(12, dis, 0)
		servo.servo_move_float_cmd_1(13, dis, 3)
		servo.servo_move_float_cmd_1(0, -1, 0)
		servo.servo_move_float_cmd_1(1, -1, 0)
		servo.servo_move_float_cmd_1(2, -1, 0)
		servo.servo_move_float_cmd_1(3, -1, 0)
		servo.servo_move_float_cmd_1(4, -1, 3)
		
		
		servo.servo_move_float_cmd_1(14, dis, 0)
		servo.servo_move_float_cmd_1(15, dis, 0)
		servo.servo_move_float_cmd_1(16, dis, 0)
		servo.servo_move_float_cmd_1(17, dis, 3)
		servo.servo_move_float_cmd_1(5, -1, 0)
		servo.servo_move_float_cmd_1(6, -1, 0)
		servo.servo_move_float_cmd_1(7, -1, 0)
		servo.servo_move_float_cmd_1(8, -1, 3)
				
	 
	
	
def horz_wave(counter):
	print(counter)
	
	if(counter == 0.0):
		queue.put(servo.servo_move_float_cmd(7, 1))
	elif(counter == 10):
		queue.put(servo.servo_move_float_cmd(8, 1))
	elif(counter == 20):
		queue.put(servo.servo_move_float_cmd(7, 0))
		queue.put(servo.servo_move_float_cmd(9, 1))
	elif(counter == 30):
		queue.put(servo.servo_move_float_cmd(8, 0))
	elif(counter == 40):
		queue.put(servo.servo_move_float_cmd(9, 0))

		
def vertical_wave(counter):
	print(counter)
	
	temp_counter = counter % 80
	
	if(temp_counter == 0):
		queue.put(servo.servo_move_float_cmd(0, 1))
		queue.put(servo.servo_move_float_cmd(1, 1))
	elif(temp_counter == 10):
		queue.put(servo.servo_move_float_cmd(2, 1))
		queue.put(servo.servo_move_float_cmd(3, 1))
		queue.put(servo.servo_move_float_cmd(4, 1))
	elif(temp_counter == 20):
		queue.put(servo.servo_move_float_cmd(5, 1))
		queue.put(servo.servo_move_float_cmd(6, 1))
	elif(temp_counter == 30):
		queue.put(servo.servo_move_float_cmd(7, 1))
		queue.put(servo.servo_move_float_cmd(8, 1))
		queue.put(servo.servo_move_float_cmd(9, 1))
	elif(temp_counter == 40):
		queue.put(servo.servo_move_float_cmd(0, -1))
		queue.put(servo.servo_move_float_cmd(1, -1))
	elif(temp_counter == 50):
		queue.put(servo.servo_move_float_cmd(2, -1))
		queue.put(servo.servo_move_float_cmd(3, -1))
		queue.put(servo.servo_move_float_cmd(4, -1))
	elif(temp_counter == 60):
		queue.put(servo.servo_move_float_cmd(5, -1))
		queue.put(servo.servo_move_float_cmd(6, -1))
	elif(temp_counter == 70):
		queue.put(servo.servo_move_float_cmd(7, -1))
		queue.put(servo.servo_move_float_cmd(8, -1))
		queue.put(servo.servo_move_float_cmd(9, -1))

def circle_wave(counter):
	temp_counter = counter % 120
	
	queue.put(servo.servo_move_float_cmd(3, 0))
	
	if(temp_counter == 0):
		queue.put(servo.servo_move_float_cmd(0, 1))
		queue.put(servo.servo_move_float_cmd(6, -1))
	elif(temp_counter == 20):
		queue.put(servo.servo_move_float_cmd(1, 1))
		queue.put(servo.servo_move_float_cmd(5, -1))
	elif(temp_counter == 40):
		queue.put(servo.servo_move_float_cmd(4, 1))
		queue.put(servo.servo_move_float_cmd(2, -1))
	elif(temp_counter == 60):
		queue.put(servo.servo_move_float_cmd(6, 1))
		queue.put(servo.servo_move_float_cmd(0, -1))
	elif(temp_counter == 80):
		queue.put(servo.servo_move_float_cmd(5, 1))
		queue.put(servo.servo_move_float_cmd(1, -1))
	elif(temp_counter == 100):
		queue.put(servo.servo_move_float_cmd(2, 1))
		queue.put(servo.servo_move_float_cmd(4, -1))
		
def circle_wave2(counter):
	temp_counter = counter % 120
	
	if(temp_counter == 0):
		queue.put(servo.servo_move_float_cmd(0, 0))
	elif(temp_counter == 10):
		queue.put(servo.servo_move_float_cmd(1, 0))
	elif(temp_counter == 20):
		queue.put(servo.servo_move_float_cmd(4, 0))
	elif(temp_counter == 30):
		queue.put(servo.servo_move_float_cmd(6, 0))
	elif(temp_counter == 40):
		queue.put(servo.servo_move_float_cmd(5, 0))
	elif(temp_counter == 50):
		queue.put(servo.servo_move_float_cmd(2, 0))
		
	elif(temp_counter == 60):
		queue.put(servo.servo_move_float_cmd(0, -1))
	elif(temp_counter == 70):
		queue.put(servo.servo_move_float_cmd(1, -1))
	elif(temp_counter == 80):
		queue.put(servo.servo_move_float_cmd(4, -1))
	elif(temp_counter == 90):
		queue.put(servo.servo_move_float_cmd(6, -1))
	elif(temp_counter == 100):
		queue.put(servo.servo_move_float_cmd(5, -1))
	elif(temp_counter == 110):
		queue.put(servo.servo_move_float_cmd(2, -1))	
		
def drop_wave(counter):
	temp_counter = counter % 160
	
	if(temp_counter == 0):
		queue.put(servo.servo_move_float_cmd(3, 1))
		
		queue.put(servo.servo_move_float_cmd(7, 0))
		queue.put(servo.servo_move_float_cmd(8, 0))
		queue.put(servo.servo_move_float_cmd(9, 0))
	elif(temp_counter == 40):
		queue.put(servo.servo_move_float_cmd(0, 1))
		queue.put(servo.servo_move_float_cmd(1, 1))
		queue.put(servo.servo_move_float_cmd(2, 1))
		queue.put(servo.servo_move_float_cmd(4, 1))
		queue.put(servo.servo_move_float_cmd(5, 1))
		queue.put(servo.servo_move_float_cmd(6, 1))
	elif(temp_counter == 80):
		queue.put(servo.servo_move_float_cmd(3, -1))
		
		queue.put(servo.servo_move_float_cmd(7, -1))
		queue.put(servo.servo_move_float_cmd(8, -1))
		queue.put(servo.servo_move_float_cmd(9, -1))
	elif(temp_counter == 120):
		queue.put(servo.servo_move_float_cmd(0, -1))
		queue.put(servo.servo_move_float_cmd(1, -1))
		queue.put(servo.servo_move_float_cmd(2, -1))
		queue.put(servo.servo_move_float_cmd(4, -1))
		queue.put(servo.servo_move_float_cmd(5, -1))
		queue.put(servo.servo_move_float_cmd(6, -1))

def lay_flat(value):
	queue.put(servo.servo_move_float_cmd(0, value))
	queue.put(servo.servo_move_float_cmd(1, value))
	queue.put(servo.servo_move_float_cmd(2, value))
	queue.put(servo.servo_move_float_cmd(3, value))
	queue.put(servo.servo_move_float_cmd(4, value))
	queue.put(servo.servo_move_float_cmd(5, value))
	queue.put(servo.servo_move_float_cmd(6, value))
	queue.put(servo.servo_move_float_cmd(7, value))
	queue.put(servo.servo_move_float_cmd(8, value))
	queue.put(servo.servo_move_float_cmd(9, value))
	
def test_func():
	while True:
		servo.servo_move_float(0, 1)
		time.sleep(9)
		servo.servo_move_float(0, -1)
		time.sleep(9)
		
		servo.servo_move_float(1, 1)
		time.sleep(9)
		servo.servo_move_float(1, -1)
		time.sleep(9)
		
		servo.servo_move_float(2, 1)
		time.sleep(9)
		servo.servo_move_float(2, -1)
		time.sleep(9)
		
		servo.servo_move_float(3, 1)
		time.sleep(9)
		servo.servo_move_float(3, -1)
		time.sleep(9)
		
		servo.servo_move_float(4, 1)
		time.sleep(9)
		servo.servo_move_float(4, -1)
		time.sleep(9)
		
		servo.servo_move_float(5, 1)
		time.sleep(9)
		servo.servo_move_float(5, -1)
		time.sleep(9)
		
		servo.servo_move_float(6, 1)
		time.sleep(9)
		servo.servo_move_float(6, -1)
		time.sleep(9)
		
		servo.servo_move_float(7, 1)
		time.sleep(9)
		servo.servo_move_float(7, -1)
		time.sleep(9)
		
		servo.servo_move_float(8, 1)
		time.sleep(9)
		servo.servo_move_float(8, -1)
		time.sleep(9)
		
		servo.servo_move_float(9, 1)
		time.sleep(9)
		servo.servo_move_float(9, -1)
		time.sleep(9)
		
		
if __name__ == '__main__':
	main()