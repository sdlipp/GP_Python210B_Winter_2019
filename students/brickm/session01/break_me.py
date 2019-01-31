# Lesson 01 Activity: Python Pushups Part 1 of 2.
# Lesson:1 Break Me
# Written by Brick


#Function to demonstrate syntax errors.  AttributeError: 'builtin_function_or_method' object has no attribute 'shiftvar'

def attribute_error():
    format_error = format.shiftvar()
    print(format_error)

attribute_error()


# Function to demonstrate name errors. NameError: name 'wrong_arg' is not defined
def name_error(error):
    print(error)

name_error(wrong_arg)


#Function to demonstrate syntax errors.  SyntaxError: 'addthistothat' invalid syntax
def error_syntax(q):
    run addthistothat(q)
    
error_syntax()

#Function to demonstrate syntax errors.  TypeError: unsupported operand type(s) for /: 'str' and 'int'
def error_type(num):
    x = str(num)
    return x/2

error_type(2)

