# The clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.
# Your task is to make the 'past' function return the time converted to milliseconds.
# More examples in the test cases below.

import pytest

from tasks.exercise002 import past


def test_exercise1_past():
    assert past(0, 1, 1) == 61000

def test_exercise2_past():   
    assert past(1,1,1) == 3661000
    
def test_exercise3_past():
    assert past(1,0,1) == 3601000

def test_exercise4_past():
    assert past(1,0,0) == 3600000

def test_exercise5_check_past_no_difference():
    assert past(0,0,0) == 0
