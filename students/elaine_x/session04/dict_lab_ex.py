#!/usr/bin/env python3
'''
##########################
#Python 210
#Session 04 - Dictionary and Set Lab
#Elaine Xu
#Feb 5,2019
###########################
'''
############# Dictionaries 1 ##############
print("Display the dictionary:")
d = {'name':'Chris', 'city':'Seattle', 'cake':'Chocolate'}
print(d)

#Delete the entry for 'cake'
print("\nDelete the entry for cake:")
d.pop('cake')
print(d)

#Add an entry for 'fruit' with 'Mango' and display the dictionary
print("\nAdd an entry for 'fruit' with 'Mango':")
d['fruit'] = 'Mango'
print(d)

#Display the dictionary keys
print()
print(d.keys())

#Display the dictionary values
print()
print(d.values())

#Display whether or not 'cake' is a key in the dictionary (i.e. False) (now)
print()
print("Whether or not 'cake' is a key in the dictionary:")
print('cake' in d)

#Display whether or not 'Mango' is a value in the dictionary (i.e. True)
print()
print("Whether or not 'Mango' is a value in the dictionary:")
print('Mango' in d.values())


############# Dictionaries 2 ##############
#Using the dictionary from item 1: Make a dictionary using the same keys but
#with the number of 't's in each value as the value (consider upper and lower case)
print("Dictionaries 2:")
d2 = {}
for key in d:
    d2[key] = d[key].lower().count('t')
print(d2)


############# Sets ##############
#Create sets s2, s3 and s4 that contain numbers from zero through twenty,
#divisible by 2, 3 and 4.
print("\nSets:")
def create_set(number):
    '''create sets that contains number n'''
    set1 = set()
    for i in range(0, 21):
        if i%number == 0:
            set1.add(i)
    return set1
s2 = create_set(2)
print("s2:", s2)
s3 = create_set(3)
print("s3:", s3)
s4 = create_set(4)
print("s4:", s4)

#Display if s3 is a subset of s2 (False)
print()
print("If s3 is a subset of s2:", s3.issubset(s2))

#Display if s4 is a subset of s2 (True)
print()
print("If s4 is a subset of s2:", s4.issubset(s2))


############# Sets 2 ##############
#Create a set with the letters in 'Python' and add 'i' to the set
set_2 = set()
for letter in 'Python':
    set_2.add(letter)
set_2.add('i')
print("\nSet with the letters in 'Python':")
print(set_2)

#Create a frozenset with the letters in 'marathon'
fs = frozenset(['m', 'a', 'r', 'a', 't', 'h', 'o', 'n'])
print("\nFrozenset with the letters in 'marathon':", fs)

#Display the union and intersection of the two sets
print("\nThe union of the two sets:", set_2.union(fs))

print("\nThe intersection of the two sets:", set_2.intersection(fs))
