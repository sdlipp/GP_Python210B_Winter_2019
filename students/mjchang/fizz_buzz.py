for num in range(0,101):
    """specifies the numbers from 1 to 100 inclusive, which will be evaluated based on the parameters below"""

# specify output if both parameters are met     
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
# specify output if one parameter is met        
    elif num % 3 == 0:
        print("Fizz")
# specify output if other parameter is met        
    elif num % 5 == 0:
        print("Buzz")
# output if neither parameter is met        
    else:
        print(num)            