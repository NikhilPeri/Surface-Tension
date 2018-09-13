import pytest

from routines import list_routines

def test_all_routines_are_valid_imports():
    for routine in list_routines().values():
        assert routine.run
