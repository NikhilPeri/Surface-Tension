import os
import importlib

BLACKLIST = [
    '__init__.py'
]

def list_routines():
    routines = {}

    for routine in os.listdir('routines'):
        if routine in BLACKLIST or not routine.endswith('.py'):
            continue
        name = routine.replace('.py', '')
        module = importlib.import_module("routines.{}".format(name))
        routines[name] = module

    return routines
