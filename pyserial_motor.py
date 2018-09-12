#To do: add a scheduler so that all the servos dont move at once

import serial
import time


def servo_init(port_name):
	global com_port
	com_port = serial.Serial(port_name, 115200)
	return com_port

def servo_move_us(channel, value_us):
	if value_us < 1000 or value_us > 2000:
		return

	string_temp = '#' + str(channel) + 'P' + str(value_us) + '\r'
	
	com_port.write(string_temp.encode('utf-8'))
	
def servo_move_float(channel, value_float):
	if value_float < -1.0 or value_float > 1.0:
		return
		
	#map the float to servo's pulse width
	value_us = (value_float+1)*500 + 1000

	string_temp = '#' + str(channel) + 'P' + str(int(value_us)) + '\r'
	
	com_port.write(string_temp.encode('utf-8'))
	
#only returns the generated command to be sent through Serial
def servo_move_float_cmd(channel, value_float):
	if value_float < -1.0 or value_float > 1.0:
		return
		
	#map the float to servo's pulse width
	value_us = (value_float+1)*500 + 1000

	string_temp = '#' + str(channel) + 'P' + str(int(value_us)) + '\r'
	return string_temp
	
def servo_move_float_cmd_1(channel, value_float, sleep):
	if value_float < -1.0 or value_float > 1.0:
		return
		
	#map the float to servo's pulse width
	value_us = (value_float+1)*500 + 1000

	string_temp = '#' + str(channel) + 'P' + str(int(value_us)) + '\r'
	com_port.write(string_temp.encode('utf-8'))
	time.sleep(sleep);

	
def servo_move_mm(channel, value_mm):
	return