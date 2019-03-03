#!/usr/bin/env python3

import math
import pytest
from circle import *


def test_set_radius_init():
    """ Tests that you can set the radius of a circle during init """

    circle1 = Circle()
    assert circle1.radius == 0
    assert circle1.diameter == 0

    circle2 = Circle(5)
    assert circle2.radius == 5
    assert circle2.diameter == 10


def test_set_diameter():
    """ Tests that you can set the diameter of circle and that radius updates """

    circle1 = Circle()
    circle1.diameter = 10

    assert circle1.radius == 5
    assert circle1.diameter == 10


def test_area():

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
