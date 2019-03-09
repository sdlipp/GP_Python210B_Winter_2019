import pytest

from Circle import Circle


def test_radius():
    """Test that the radius is the radius"""
    c = Circle(4)
    assert c.radius == 4
    
def test_diameter():
    """ test that diameter is calculated correctly"""
    c = Circle(4) 
    assert c.diameter == 8


def test_set_diameter():
    c = Circle(4)
    c.diameter = 10
    assert c.diameter == 10
    assert c.radius == 5

def test_area():
    """test that area gets calculated properly"""
    c = Circle(1)
  
    assert c.area == 3.141592653589793
    
def test_constructor():
    """Test that the alternate constructor of from_diameter() works"""
    
    c = Circle.from_diameter(4)
    assert c.diameter == 4
    assert c.radius == 2

def test_str():
    """Test that a Circle class object prints the string"""
    c = Circle(4)
    s = str(c)
    assert s == "Circle with radius: 4.0000"

def test_repr():
    c = Circle(4)
    d = repr(c)
    assert d == 'Circle(4)'

def test_add():
    """
    Testing that adding two Circle classes together yields a
    Circle class with sums of their radius
    """
    c1 = Circle(2)
    c2 = Circle(4)
    print(c1 + c2)
    assert(c1+c2) == Circle(6)
    
def test_mul():
    c1 = Circle(4)
    assert (c1 * 3) == Circle(12)

def test_less():
    """ Test that the Circles can be compared with less than statement"""
    c1 = Circle(3)
    c2 = Circle(5)
    assert c1.radius < c2.radius
    
       
def test_greater():
    """ Test that the Circles can be compared with greater than statement"""
    c1 = Circle(5)
    c2 = Circle(3)
    assert c1.radius > c2.radius

def test_equal():
    """Test that the Circles  can be compared with equal statement"""
    c1 = Circle(6)
    c2 = Circle(6)
    assert c1.radius == c2.radius
    

def test_sort_key():
    circles = [Circle(6), Circle(8), Circle(7), Circle(4), Circle(0), Circle(2)]
    circles.sort()
    assert circles == [Circle(0), Circle(2), Circle(4), Circle(6), Circle(7), Circle(8)]                    
    
