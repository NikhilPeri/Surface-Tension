import pytest
import serial
import numpy as np
from mock import patch

from datetime import datetime
from routines import list_routines

from lib.wall import Wall

class FakeWall(Wall):
    def __init__(self):
        pass

    def write_servo(*args):
        pass

    def write_row(*args):
        pass

    def write_column(*args):
        pass

@pytest.fixture
def wall():
    return FakeWall()

def test_all_routines_are_valid_imports():
    for routine in list_routines().values():
        assert routine.run

@patch('time.sleep', return_value=None)
def test_routines_run_in_under_two_minutes(time_sleep, wall):
    for name, routine in list_routines().items():
        routine.run(wall)
        total_time = np.sum(map(lambda call: call[0][0], time_sleep.call_args_list))
        assert total_time < 120, 'Routine "{}" exceeds 120 second limit'.format(name)
        time_sleep.reset_mock()
