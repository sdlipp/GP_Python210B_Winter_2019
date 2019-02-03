# Lesson: 02 Excercises 
# Title: Fizzbuzz
# Author: Brick

def fizzbuzz(start, end): 
    def int_to_fizzbuzz(i): 
        entry = '' 
        if i%3 == 0: 
            entry += "fizz" 
        if i%5 == 0: 
            entry += "buzz" 
        if i%3 != 0 and i%5 != 0: 
            entry = i 
        return entry 
 
    return [int_to_fizzbuzz(i) for i in range(start, end+1)] 
 
if __name__ == "__main__": 
    start = 1 
    end = 100 
    for i in fizzbuzz(start, end): 
        print(i)