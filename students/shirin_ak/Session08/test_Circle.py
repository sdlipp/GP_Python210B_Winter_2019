import pytest

from Circle import Circle


def test_radius():
    c = Circle(4)
    assert c.radius == 4
    
def test_diameter(): 
    c = Circle(4) 
    assert c.diameter == 8


def test_set_diameter():
    c = Circle(4)
    c.diameter = 10
    assert c.diameter == 10
    assert c.radius == 5

def test_area():
    c = Circle(1)
  
    assert c.area == 3.141592653589793
    
def test_constructor():
    c = Circle.from_diameter(4)
    assert c.diameter == 4
    assert c.radius == 2
