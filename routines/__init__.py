import os
import importlib
import numpy as np

from lib.constants import DEFAULT_CHANNEL_MAPPINGS
from lib.servo import Servo
from lib.wall import Wall

BLACKLIST = [
    '__init__.py',
    'sample_routine.py',
]

# List all the routines available for the wall
def list_routines():
    routines = {}

    for routine in os.listdir('routines'):
        if routine in BLACKLIST or routine.startswith('test') or not routine.endswith('.py'):
            continue
        name = routine.replace('.py', '')
        module = importlib.import_module("routines.{}".format(name))
        routines[name] = module

    return routines
