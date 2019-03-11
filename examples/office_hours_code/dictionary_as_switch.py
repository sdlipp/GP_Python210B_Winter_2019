'''
Demonstrate the use of a Python dictionary as a switch statement
'''
VALID_OPERATIONS = ('+', '-', '*', '/')

def add(first_number, second_number):
    '''
    Adds two numbers
    '''
    return first_number + second_number

def subtract(first_number, second_number):
    '''
    Subtracts two numbers
    '''
    return first_number - second_number

def multiply(first_number, second_number):
    '''
    Multiplies two numbers
    '''
    return first_number * second_number

def divide(first_number, second_number):
    '''
    Divides two numbers
    '''
    return first_number / second_number

def calculator_switch(operation, first_number, second_number):
    '''
    Implements math operations as dictionary switch
    '''
    # This is a dictionary where operation symbols are the keys and the functions
    # calling those operations are the values.
    math_operations = {
        '+' : add,
        '-' : subtract,
        '*' : multiply,
        '/' : divide
    }
    # Note the function call below. The name of the function called is not fixed
    # but instead pulled from the math operations dictionary
    return math_operations[operation](first_number, second_number)


def main():
    '''
    Main flow execution
    '''
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    operation = input(("Choose an operation (+, -, *, /): "))

    while operation not in VALID_OPERATIONS:
        operation = input("Invalid operation. Try again, choose an operation (+, -, *, /): ")

    print(f'The result from {first_number} {operation} {second_number} is {calculator_switch(operation, first_number, second_number)}')

if __name__ == '__main__':
    main()
    