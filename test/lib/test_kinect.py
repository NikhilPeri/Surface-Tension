import pytest
from mock import patch
import numpy as np

from lib.kinect import Kinect

@pytest.fixture
def mock_frame():
    with open('test/fixtures/kinect.frame', 'r') as kinect_frame:
        return np.load(kinect_frame)

@pytest.fixture
def kinect():
    return Kinect()

def test_kinect_is_valid_import():
    kinect = Kinect()

@patch('lib.kinect.Kinect.get_frame', return_value=mock_frame())
def test_get_reduced_frame_returns_correct_value(get_frame_mock, kinect):
    assert (kinect.get_reduced_frame() == np.array([
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
    ])).all()
