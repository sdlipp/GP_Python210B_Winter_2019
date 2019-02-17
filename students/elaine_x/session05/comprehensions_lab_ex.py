'''
##########################
#Python 210
#Session 05 - Comprehensions Lab
#Elaine Xu
#Feb 12,2019
###########################
'''
############## Unpacking tuples in list comprehensions #############
list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]

comprehension = [ skit * number for number, skit in list_of_tuples ]

print(comprehension[0])

print(len(comprehension[2]))


############### Double list comprehensions #########################
eggs = ['poached egg', 'fried egg']

meats = ['lite spam', 'ham spam', 'fried spam']

comprehension = [ '{0} and {1}'.format(egg, meat) for egg in eggs for meat in meats]

print(len(comprehension))

print(comprehension[0])


############### Set comprehensions ##################################
comprehension = { c for c in 'aabbbcccc'}

print(comprehension)


################ Dictionary comprehensions ##########################
dict_of_weapons = {'first': 'fear',
                   'second': 'surprise',
                   'third':'ruthless efficiency',
                   'forth':'fanatical devotion',
                   'fifth': None}
dict_comprehension = { k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}

print('first' in dict_comprehension)

print('FIRST' in dict_comprehension)

print(len(dict_of_weapons))

print(len(dict_comprehension))


################## Count Even Numbers ################################
#Can you do this with a single line comprehension?
def count_evens(nums):
    new_list = [num for num in nums if not num%2]
    return len(new_list)

print(count_evens([2, 1, 2, 3, 4]) == 3)

print(count_evens([2, 2, 0]) == 3)

print(count_evens([1, 3, 5]) == 0)


################## dict and set comprehensions #######################
food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}
#Print the dict by passing it to a string format method, so that you get something like:
#“Chris is from Seattle, and he likes chocolate cake, mango fruit, greek salad, and lasagna pasta”
print(f'{food_prefs["name"]} is from {food_prefs["city"]}, and he likes {food_prefs["cake"]} cake, '
      f'{food_prefs["fruit"]} fruit, {food_prefs["salad"]} salad, and {food_prefs["pasta"]} pasta')

#Using a list comprehension, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent
#(string is fine). (the hex() function gives you the hexidecimal representation of a number as a string)
numbers = [i for i in range(16)]
values = [hex(i) for i in range(16)]
d = {number: value for number, value in zip(numbers, values)}
print(d)

#Do the previous entirely with a dict comprehension – should be a one-liner
d = {number: value for number, value in zip([i for i in range(16)], [hex(i) for i in range(16)])}
print(d)

#Using the dictionary from item (1): Make a dictionary using the same keys but with the number of ‘a’s in
# each value. You can do this either by editing the dict in place, or making a new one. If you edit in place
# make a copy first!
new_dict = food_prefs.copy()
new_dict = {key: new_dict[key].count('a') for key in food_prefs}
print(new_dict)

#make new dict
new_dict2 = {key: food_prefs[key].count('a') for key in food_prefs}
print(new_dict2)

#Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
#1. Do this with one set comprehension for each set.
#2. What if you had a lot more than 3? – Don’t Repeat Yourself (DRY).
#    a. create a sequence that holds all the divisors you might want – could be 2,3,4, or could be any other
# arbitrary divisors.
#    b. loop through that sequence to build the sets up – so no repeated code. you will end up with a list of
# sets – one set for each divisor in your sequence.
#    c. The idea here is that when you see three (Or more!) lines of code that are almost identical, then you
# you want to find a way to generalize that code and have it act on a set of inputs, so the actual code is only
# written once.
#3. Extra credit: do it all as a one-liner by nesting a set comprehension inside a list comprehension. (OK,
# that may be getting carried away!)

#1.
s2 = {i for i in range(21) if not i%2}
s3 = {i for i in range(21) if not i%3}
s4 = {i for i in range(21) if not i%4}
print(s2,s3,s4)

#2.
divisor = [2, 3, 4]
s5 = [{i for i in range(21) if not i%num} for num in divisor]
print(s5)

#3. see #2.