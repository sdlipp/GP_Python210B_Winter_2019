'''
Tests for Circle program
You'll note that this is chock full of pylint disables.  This is because I use
Atom's pylinter plugin, and while it's fantastic at helping me with problems
while I'm going, unit testing is going to have linting problems, so I disable
them as they come up, that way I know when I'm doing something bad.
'''
from math import pi
import pytest
from circle import Circle


def test_empty_circle():
    '''
    Test 1:  No values insertered.
    '''
    #pylint: disable=E1120
    with pytest.raises(TypeError):
        Circle()


def test_new_circle():
    '''
    Test 2:  Testing a value for the circle.
    '''
    Circle(1)


def test_radius():
    '''
    Test 3:  Testing inserting a radius.
    '''
    #pylint: disable=C0103
    c = Circle(2)

    assert c.radius == 2


def test_diameter():
    '''
    Test 4:  Testing diameter calculation.
    '''
    #pylint: disable=C0103
    c = Circle(3)

    assert c.diameter == 6


def test_set_diameter():
    '''
    Test 5: Testing manually setting a diameter.
    '''
    #pylint: disable=C0103
    c = Circle(4)
    c.diameter = 5

    assert c.diameter == 5
    assert c.radius == 2.5


def test_area():
    '''
    Test 6:  Testing area calculation.
    '''
    #pylint: disable=C0103
    c = Circle(6)

    assert c.area == pi * 36


def test_set_area():
    '''
    Test 7:  Testing AttributeError
    '''
    #pylint: disable=C0103
    c = Circle(7)

    with pytest.raises(AttributeError):
        c.area = 10


def test_from_diameter():
    '''
    Test 8:  Testing calculating circle from diameter insertion
    '''
    #pylint: disable=C0103
    c = Circle.from_diameter(8)

    assert c.diameter == 8
    assert c.radius == 4


def test_string():
    '''
    Test 9:  String insertion and formatted print
    '''
    #pylint: disable=C0103
    c = Circle(9)
    assert str(c) == "Circle with radius: 9"

def test_string_representation():
    '''
    Test 10:  Testing string representation, turns out it's a lot like string
    '''
    #pylint: disable=C0103
    c = Circle(12)
    assert repr(c) == "Circle(12)"

def test_add_circles():
    '''
    Test 11:  Testing adding circles
    '''
    #pylint: disable=C0103
    c1 = Circle(4)
    c2 = Circle(6)

    assert c1 + c2 == Circle(10)
