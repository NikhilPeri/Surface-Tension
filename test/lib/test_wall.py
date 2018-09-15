import pytest
import serial

from lib.wall import Wall

@pytest.fixture
def mock_comm():
     return serial.serial_for_url(url='loop://test',
                                  timeout=0,
                                  baudrate=115200
    )

def test_init_wall_sets_list_servos_to_starting_position(mock_comm):
    wall = Wall(mock_comm)
    for servo in wall.list_servos():
        assert servo.position == -1.0

def test_init_wall_creates_correct_number_of_servos(mock_comm):
    wall = Wall(mock_comm)
    assert len(wall.list_servos()) == 26

def test_write_wall_writes_all_servos_on_wall(mock_comm):
    wall = Wall(mock_comm)
    wall.write([
        [0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
        [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
        [0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
        [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
    ])

    for servo in wall.list_servos():
        assert servo.position == 0.5

def test_write_servo_sets_servo_to_desired_position(mock_comm):
    wall = Wall(mock_comm)
    wall.write_servo('C', '7', 0.314)
    assert wall.servos['C']['7'].position == 0.314

def test_write_servo_raises_if_servo_location_invalid(mock_comm):
    wall = Wall(mock_comm)
    with pytest.raises(KeyError):
        wall.write_servo('C', '99', 0.69)

def test_write_row_sets_all_servos_in_desired_row_to_position(mock_comm):
    wall = Wall(mock_comm)
    wall.write_row('C', 0.314)
    for servo in wall.servos['C'].values():
        assert servo.position == 0.314

def test_write_row_raises_if_servo_location_invalid(mock_comm):
    wall = Wall(mock_comm)
    with pytest.raises(KeyError):
        wall.write_row('FF', 0.69)

def test_write_column_sets_all_servos_in_desired_columns_to_position(mock_comm):
    wall = Wall(mock_comm)
    wall.write_column('3', 0.314)

    assert wall.servos['E']['3'].position == 0.314
    assert wall.servos['C']['3'].position == 0.314

def test_write_column_raises_if_servo_location_invalid(mock_comm):
    wall = Wall(mock_comm)
    with pytest.raises(KeyError):
        wall.write_row('99', 0.69)
