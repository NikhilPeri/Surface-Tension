import sys
import time
import serial
import signal
import yaml
import logging
from numpy import random
from threading import Thread
from datetime import datetime

from routines import list_routines
from lib.logger import configure_logger
from lib.wall import Wall

DEFAULT_COM_PORT='/dev/ttyUSB0'
ROUTINE_BUTTON_PIN=23
ROUTINE_LED_PIN=24
DEFAULT_TIMEOUT=15

# Controller for the wall
class Controller(Thread):
    def __init__(self, com_port):
        self.active = False
        configure_logger()
        self.connect_comm(com_port)

        try:
            from gpiozero import Button, LED
            self.routine_indicator = LED(ROUTINE_LED_PIN)
            self.routine_indicator.on()
            time.sleep(3)
            self.routine_indicator.off()
            self.routine_button = Button(ROUTINE_BUTTON_PIN)
        except Exception as e:
            logging.error('Could not connect to GPIO')
            raise(e)

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
            self.routine_button.wait_for_press(timeout=None)
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


if __name__ == '__main__':
    com_port = DEFAULT_COM_PORT
    if len(sys.argv) == 2:
        com_port = sys.argv[1]

    controller = Controller(com_port)
    signal.signal(signal.SIGINT, controller.deactivate)
    signal.signal(signal.SIGTERM, controller.deactivate)
    controller.activate()
