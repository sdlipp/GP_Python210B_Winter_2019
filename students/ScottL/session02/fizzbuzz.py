def FizzBuzz():
    """Return a list of integers from 1 - 100 (inclusive) where numbers divisible by 3 return 'Fizz',
    integers divisible by 5 return 'Buzz' and integers divisible by both 3 & 5 return 'FizzBuzz'
    """

    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

FizzBuzz()