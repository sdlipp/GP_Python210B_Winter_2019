"""Testing out common exception types"""

"""Name Error"""
def simpleMult(a, b):

    try:
        y = 2 * x

        return y

    except NameError:
        print("A 'NameError' occurred because one of the variables was not defined")

A1 = simpleMult(2,3)

def simpleDiv(a, b):

    try:
        y = a
        z = b

        m = y/z

        return m

    except TypeError:
        print("A 'TypeError' occurred because a mathematical operation was applied to an incorrect object type")

A2 = simpleDiv("2", "3")

def simpleAdd(a, b):

    try:
        y = a
        z = b

        m = y//z
        return m

    except SyntaxError:
        print("A 'SyntaxError' occurred because the computer did not recognize the requested function")

"A3 = simpleAdd(2, 3)"

def simpleSubtract(a, b):

    try:
        y = a
        z = b

        m = a - b
        return m.lower()
    except AttributeError:
        print("An attribute error occurred an attribute was requested of an object that doesn't exist")

A4 = simpleSubtract(3, 2)

