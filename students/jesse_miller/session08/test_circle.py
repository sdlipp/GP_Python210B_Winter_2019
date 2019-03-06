# Tests for Circle Class

import pytest
from math import pi
from circle import Circle


# Step 1
def test_empty():
    with pytest.raises(TypeError):
        Circle()


def test_new():
    Circle(1)


def test_radius():
    c = Circle(2)

    assert c.radius == 2


# Step 2
def test_diameter():
    c = Circle(3)

    assert c.diameter == 6


# Step 3
def test_diameter_set():
    c = Circle(4)
    c.diameter = 5

    assert c.diameter == 5
    assert c.radius == 2.5


# Step 4
def test_area():
    c = Circle(6)

    assert c.area == pi * 36


def test_area_set():
    c = Circle(7)

    with pytest.raises(AttributeError):
        c.area = 10
