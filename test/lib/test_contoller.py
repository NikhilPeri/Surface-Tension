import pytest
import serial

from lib.controller import Controller

@pytest.fixture
def controller():
    return Controller('loop://test', intervals_file='test/fixtures/intervals.yml')

@pytest.mark.freeze_time('2018-04-20 11:21:00.012')
def test_valid_run_interval_returns_true_when_current_time_is_valid_interval(controller):
    assert controller.valid_run_interval()

@pytest.mark.freeze_time('2018-04-20 16:20:00.012')
def test_valid_run_interval_returns_false_when_current_time_is_not_valid_interval(controller):
    assert not controller.valid_run_interval()
