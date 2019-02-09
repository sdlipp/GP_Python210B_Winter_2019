for number in range(101):
    if number % 15 == 0:
        print("FizzBuzz")
        continue
    if number % 3 == 0:
        print("Fizz")
        continue
    if number % 5 == 0:
        print("Buzz")
        continue
    print(number)