import sys
import time
import serial
import logging
import threading
from datetime import datetime

from routines import list_routines
from lib.logger import configure_logger
from lib.wall import Wall

INTERVALS_FILE_PATH='config/intervals.yml'
DEFAULT_COM_PORT='/dev/ttyUSB0'

# Controller for the wall
class Controller(threading.Thread):
    def __init__(self, com_port='/dev/ttyUSB0', ):
        configure_logger()
        self.connect_comm(com_port)
        self.routines = list_routines()
        self.wall = Wall(self.comm)
        self.active = False

    # Run specific wall routine (pattern)
    def run_routine(self, routine_name):
        try:
            self.routines[routine_name].run(self.wall)
        except Exception as e:
            logging.error('Routine "{}" failed'.format(routine_name))
            logging.error(e)

    # Activate the wall
    def activate(self):
        if not self.active:
            Thread.__init__(self)
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
            pass

    # Run a random routine from the list of routines
    def random_routine(self):
        return self.routines.values()[0]

    # Connect to COM port in order to run
    def connect_comm(self, com_port, retry=5, timeout=15):
        for i in range(retry):
            try:
                self.comm = serial.Serial(com_port, 115200)
                return comm
            except Exception as e:
                logging.error(e)
                logging.warn('Retry count {}'.format(i))
                time.sleep(timeout)

        raise IOError('Failed to connect to wall on comm: {}'.format(comm))

if __name__ == '__main__':
    configure_logger()
    logging.warn('BITCHHH')
