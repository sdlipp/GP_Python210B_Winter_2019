#!/usr/local/bin/python3

# Lesson 01 Activity: Python Pushups Part 1 of 2.
# Task:1 Explore Errors
# Written by Paul C.

# Function to demonstrate name errors. NameError: name 'name' is not defined
def name_error(error):
    print(error)

name_error(name)

# Function to demonstrate type errors. TypeError: type_error() Missing 1 required positional argument: 'name'
def type_error(error):
    print(error)

type_error()

# Function to demonstrate syntax errors. I used a semicolon instead of a colon.
def syntax_error(error);
    print(error)

syntax_error(error)

# Function to demonstrate attribute errors. AttributeError: type object 'range' has no attribute 'attributeerror'
def attribute_error():
    error = range.attributeerror()
    print(error)

attribute_error()