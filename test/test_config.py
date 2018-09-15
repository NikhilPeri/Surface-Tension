import pytest
import yaml
import numpy as np
import datetime

def test_calibration_file_contains_valid_numpy_array():
    with open('config/calibration.frame', 'r') as calibration_file:
        calibration_array = np.load(calibration_file)
        assert type(calibration_array) == np.ndarray

def test_intervals_yaml_contains_no_conflicts():
    with open('config/intervals.yml', 'r') as intervals_file:
        interval_config = yaml.load(intervals_file)
        assert sorted(interval_config.keys()) == sorted(['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])
        for intervals in interval_config.values():
            for period in intervals:
                assert type(datetime.datetime.strptime(period['start'], '%H:%M').time()) == datetime.time
                assert type(datetime.datetime.strptime(period['stop'], '%H:%M').time()) == datetime.time
