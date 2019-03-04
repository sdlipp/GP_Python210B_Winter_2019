#!/usr/bin/env python3

import math
import pytest
from circle import *


def test_set_radius_init():
    """ Tests that you can set the radius of a circle during init """
    circle1 = Circle()
    circle2 = Circle(5)

    assert circle1.radius == 0
    assert circle1.diameter == 0
    assert circle2.radius == 5
    assert circle2.diameter == 10


def test_set_diameter():
    """ Tests that you can set the diameter of circle and that radius updates """
    circle1 = Circle()
    circle1.diameter = 10

    assert circle1.radius == 5
    assert circle1.diameter == 10


def test_area():
    """ Tests that the area of a circle is computed properly """
    circle1 = Circle(10)

    assert circle1.radius == 10
    assert circle1.diameter == 20
    assert circle1.area == 2 * math.pi * circle1.radius ** 2


def test_set_area():
    """ Tests that setting the area fails and returns an AttributeError """
    circle1 = Circle(10)
    
    with pytest.raises(AttributeError):
        circle1.area = 100


def test_from_diameter():
    """ Tests that a circle can be created from a diameter """
    circle1 = Circle.from_diameter(10)

    assert circle1.radius == 5 
    assert circle1.diameter == 10
    assert circle1.area == 2 * math.pi * circle1.radius ** 2


def test_str():
    """ Tests that __str__ is working """
    circle1 = Circle(10)
    
    assert 'Circle with radius: 10' == str(circle1)

    
def test_repr():
    """ Tests that __repr__ is working """
    circle1 = Circle(10)

    assert 'Circle(10)' == repr(circle1)
    

def test_addition():
    """ Tests that __add___ is working """
    circle1 = Circle(10)
    circle2 = Circle(20)
    circle3 = circle1 + circle2
    
    assert circle3.radius == 30
    assert circle1 + 5 == Circle(15)


def test_radd():
    """ Tests that reflected addition works """
    circle1 = Circle(2)
    circle2 = Circle(4)

    assert circle1 + 2 == 2 + circle1
    assert 2 + circle1 == circle2
    assert 5 + circle1 == Circle(7)


def test_subtraction():
    """ Tests that __sub___ is working """
    circle1 = Circle(10)
    circle2 = Circle(6)
    circle3 = circle1 - circle2
    
    assert circle3.radius == 4
    assert circle1 - 5 == Circle(5)
    assert circle2 - 2 == Circle(4)


def test_rsub():
    circle1 = Circle(10)
    circle2 = Circle(6)

    assert 10 - circle1 == circle1 - 10
    assert 10 - circle2 == Circle(4)
    assert 10.0 - circle2 == Circle(4)
    

def test_multiplication():
    """ Tests that __mul__ is working """
    circle1 = Circle(2)
    circle2 = Circle(4)
    circle3 = circle1 * circle2

    assert circle3.radius == 8
    assert circle1 * 2 == Circle(4)
    assert circle2 * 2 == Circle(8)


def test_rmul():
    circle1 = Circle(2)
    circle2 = Circle(4)

    assert 2 * circle1 == circle1 * 2
    assert 2 * circle1 == Circle(4)
    assert 2 * circle2 == Circle(8)


def test_comparisons1():
    """ Tests comparison operations when circle1 is less than circle 2 """
    circle1 = Circle(2)
    circle2 = Circle(4)

    assert not circle1 > circle2
    assert not circle1 >= circle2
    assert circle1 < circle2
    assert circle1 <= circle2
    assert not circle1 == circle2
    assert circle1 != circle2


def test_comparisons2():
    """ Tests comparison operations when circle1 is greater than circle 2 """
    circle1 = Circle(4)
    circle2 = Circle(2)

    assert circle1 > circle2
    assert circle1 >= circle2
    assert not circle1 < circle2
    assert not circle1 <= circle2
    assert not circle1 == circle2
    assert circle1 != circle2


def test_comparisons3():
    """ Tests comparison operations when circle1 is equal to circle 2 """
    circle1 = Circle(2)
    circle2 = Circle(2)

    assert not circle1 > circle2
    assert circle1 >= circle2
    assert not circle1 < circle2
    assert circle1 <= circle2
    assert circle1 == circle2
    assert not circle1 != circle2


def test_sort():
    """ Tests that .sort() functions properly """
    circle1 = Circle(10)
    circle2 = Circle(5)
    circle3 = Circle(2)
    circle_list = [circle1, circle2, circle3]
    circle_list.sort()

    assert circle_list == [circle3, circle2, circle1]
