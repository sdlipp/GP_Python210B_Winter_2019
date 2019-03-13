"""
test code for circle.py
"""
from circle import *
import pytest

#### Step 1 ####

def test_radius():
    c = Circle(4)
    assert c.radius == 4

#### Step 2 ####

def test_diameter():
    c = Circle(4)
    assert c.diameter == 8

#### Step 3 ####

def test_set_diameter():
    c = Circle(4)
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1

#### Step 4 ####

def test_area():
    c = Circle(2)
    assert round(c.area, 5) == 12.56637

    with pytest.raises(AttributeError):
        c.area = 12.56637


#### Step 5 ####
def test_alt_construct():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4


#### Step 6 ####
def test_print():
    c = Circle(4)
    assert c.__str__() == "Circle with radius: 4"
    assert c. __repr__() == "Circle(4)"


#### Step 7 ####
def test_protocol():
    c1 = Circle(2)
    c2 = Circle(4)
    assert c1 + c2 == 6
    assert c2 * 3 == 12


