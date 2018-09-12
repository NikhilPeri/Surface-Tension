from lib.servo import Servo

import serial
import pytest

@pytest.fixture
def mock_com():
     return serial.serial_for_url(url='loop://test',
                                  timeout=0,
                                  baudrate=115200
    )

def test_servo_init_sets_position_to_start(mock_com):
    servo = Servo('TEST', mock_com)
    assert mock_com.readline() == '#TESTP1000\r'
    assert servo.position == -1.0

def test_servo_write_sets_desired_position(mock_com):
    servo = Servo('TEST', mock_com)
    mock_com.reset_output_buffer()
    servo.write(0.4)
    assert mock_com.readline() == '#TESTP1700\r'
    assert servo.position == 0.4

def test_servo_write_raises_if_position_out_of_bounds(mock_com):
    servo = Servo('TEST', mock_com)
    with pytest.raises(ValueError):
        servo.write(-1.1)
