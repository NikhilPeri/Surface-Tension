import sys
import time
import serial
import signal
import yaml
import logging
from numpy import random
from threading import Thread
from datetime import datetime

import routines.kinect as kinect_routine
from routines import list_routines
from lib.logger import configure_logger
from lib.constants import DAYS_OF_WEEK
from lib.wall import Wall
from lib.kinect import Kinect
from gpiozero import Button, LED

DEFAULT_COM_PORT='/dev/ttyUSB0'
ROUTINE_BUTTON_PIN=23
ROUTINE_LED_PIN=24
DEFAULT_TIMEOUT=15

# Controller for the wall
class Controller(Thread):
    def __init__(self, com_port, intervals_file='config/intervals.yml'):
        self.active = False
        configure_logger()
        self.load_intervals(intervals_file)
        self.connect_comm(com_port)

        self.routine_interrupt = False
        time.sleep(10)
        try:
            self.routine_indicator = LED(ROUTINE_LED_PIN)
            self.routine_indicator.on()
            time.sleep(5)
            self.routine_indicator.off()
            self.routine_button = Button(ROUTINE_BUTTON_PIN)

            def _set_interrupt():
                self.routine_interrupt = True
                self.routine_indicator.on()

            self.routine_button.when_pressed = _set_interrupt
        except Exception as e:
            logging.error('Could not connect to GPIO')

        self.routines = list_routines()
        self.wall = Wall(self.comm)
        super(Controller, self).__init__()

    # Run specific wall routine (pattern)
    def run_routine(self, routine_name):
        try:
            self.routine_indicator.on()
            self.routines[routine_name].run(self.wall)
            self.wall.reset()
            time.sleep(5)
            self.routine_indicator.off()
        except (WallInterrupt, Exception) as e:
            logging.error('Routine "{}" failed'.format(routine_name))
            logging.error(e)


    # Activate the wall
    def activate(self):
        if not self.active:
            super(Controller, self).__init__()
            self.active = True
            self.start()
            if not self.is_alive():
                logging.error('Failed to activate controller')

    # Deactivate the wall
    def deactivate(self):
        if self.active:
            self.active = False
            self.join()
            if self.is_alive():
                raise Exception('Failed to deactivate controller')

    def run(self):
        while self.active:
            if self.routine_interrupt:
                self.routine_interrupt = False
                self.run_routine(random.choice(self.routines.keys()))

    # Connect to COM port in order to run
    def connect_comm(self, com_port, retry=5, timeout=DEFAULT_TIMEOUT):
        for i in range(retry):
            try:
                self.comm = serial.serial_for_url(com_port, baudrate=115200)
                return self.comm
            except Exception as e:
                logging.error(e)
                logging.warn('Retry count {}'.format(i))
                time.sleep(timeout)

        raise IOError('Failed to connect to wall on comm: {}'.format(com_port))

    def load_intervals(self, intervals_file):
        self.intervals = {}
        with open(intervals_file, 'r') as file:
            interval_config = yaml.load(file)
            for date, intervals in interval_config.items():
                self.intervals[date] = [ {'start': datetime.strptime(i['start'], '%H:%M').time(), 'stop': datetime.strptime(i['stop'], '%H:%M').time()} for i in intervals ]

if __name__ == '__main__':
    com_port = DEFAULT_COM_PORT
    if len(sys.argv) == 2:
        com_port = sys.argv[1]

    controller = Controller(com_port)
    signal.signal(signal.SIGINT, controller.deactivate)
    signal.signal(signal.SIGTERM, controller.deactivate)
    controller.activate()
