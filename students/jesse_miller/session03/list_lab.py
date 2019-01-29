#!/usr/local/bin/python3
#As stated in the instructions, below is a simple list and a prompt for a new
#entry.
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print("Here is the current list of fruits:")
print(fruits)
#Here, we ask for a new fruit input.  There's no error correction, so the user
#can input any string, but I suppose that'd be a possibliity unless we checked
#against a list of every possible fruit.
n = str(input("Please enter a new fruit: "))
#Here we're appending the user input to the list above.  If there's another way
#that y'all wanted us to do this I have no idea what it would be.
fruits.append(n)
print(fruits)
#Getting user input for the number in the list to display.
m = int(input("Please enter a number to show the fruit you want: "))
#The -1 is to compensate for the fact that arrays start with 0 and people don't
#think that way.
print(fruits[m-1])
