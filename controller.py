from routines import list_routines
from lib.wall import Wall
import time
from datetime import datetime
import sys
import os
import serial
import logging

'''
DEFAULT_COM_PORT='/dev/ttyUSB0'

def connect_wall(comm, retry=5):
    for i in range(retry):
        try:
            wall = Wall
        except e:
'''
def configure_logging():
    formatter = logging.Formatter(
        fmt='[%(levelname)s] %(asctime)s.%(msecs)03d | %(message)s',
        datefmt='%Y-%m-%d %I:%M:%-S'
    )
    file_stream = logging.StreamHandler(
        stream=open(os.path.join('logs', "{}.log".format(datetime.now().strftime('%Y-%m-%d-%H%M'))), 'w+'))
    file_stream.setFormatter(formatter)
    file_stream.setLevel(20)
    console_stream = logging.StreamHandler(stream=sys.stdout)
    console_stream.setFormatter(formatter)
    console_stream.setLevel(30)

    logging.getLogger().setLevel(20)
    logging.getLogger().addHandler(file_stream)
    logging.getLogger().addHandler(console_stream)

if __name__ == '__main__':
    configure_logging()
    logging.warn('YOOO')
