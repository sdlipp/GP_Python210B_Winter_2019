#!/usr/bin/env python3

#NameError Exception
def test_fun(var):
    return x * 3
#NameError: name x is not defined

#TypeError Exception
def test_funA(var):
    var = chr(var)
    return var / 3
#TypeError: unsupported operand type(s) for /: 'str' and 'int'

#SyntaxError Exception
def test_funB(var):
    var = (var + 2
    return var * 3
#Syntax Error: invalid syntax - missing closing parenthesis on line 16

#AttributeError Exception
def test_funC(var):
    var = int(var)
    var.append(4)
    return var * 3
#AttributeError: 'int' object has no attribute 'append'
