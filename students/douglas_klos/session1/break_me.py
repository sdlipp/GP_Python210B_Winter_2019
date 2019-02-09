#!/usr/bin/python3

# Lesson 1, break_me.py
# By Douglas Klos

# print(message) results in a NameError 
# as 'message' is not defined.
def name_error():
    print(message)

name_error()

# print('string' + 5) results in a TypeError
# as you cannot concatenate an int to a string.
def type_error():
    print('string' + 5)

type_error()

# The brackets in the following function generate a SyntaxError
# Brackets are not used for code blocks in python, thus violating syntax.
def syntax_error() {
    pass
}

syntax_error()

# num.toFail() generates an AttributeError
# int objects have no attribute 'toFail'
def attribute_error():
    num = 5
    num.toFail()

attribute_error()
