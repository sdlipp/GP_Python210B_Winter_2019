import io
import pytest

from circle import *

def test_init():
    """
    This only tests that it can be initialized with and without
    some content -- but it's a start
    """
    c = Circle(4)


def test_radius():

    "check to see if it outputs correct radius"
    c = Circle(5)
    # making sure radius outputs correctly.
    assert c.radius == 5

def test_diameter():

    "check to see if it outputs correct diameter"
    c = Circle(5)
    # making sure radius outputs correctly.
    assert c.diameter == 10
    assert c.diameter == c.radius*2
    c.diameter = 6
    assert c.radius == 3
    assert c.diameter == 6
