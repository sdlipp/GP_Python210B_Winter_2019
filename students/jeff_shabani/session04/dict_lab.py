#!/usr/bin/env python3

from copy import deepcopy

'''
This is the foundation dictionary.
It's name is all caps because it is never changed.
We only work with copies of this dictionary. 
'''
FIRST = {'name': 'Chris',
         'city': 'Seattle',
         'cake': 'Chocolate'}


def show_dict_items(any_dictionary):
    for k, v in any_dictionary.items():
        print(k, v)
    print()


def show_dict_keys(any_dictionary):
    for k in any_dictionary.keys():
        print(k)
    print()


def show_dict_values(any_dictionary):
    for v in any_dictionary.values():
        print(v)
    print()


def dictionaries_one(first_dict):

    #make a copy of the origingal dictionary
    first_dict = deepcopy(first_dict)

    show_dict_items(first_dict)
    first_dict.pop('cake')
    print('After popping "cake":')

    show_dict_items(first_dict)
    first_dict['fruit'] = 'Mango'
    print('Dict keys with fruit added:')

    show_dict_keys(first_dict)
    print('Dict values with fruit added:')

    show_dict_values(first_dict)
    print(f'Cake is a key in the dictionary: {"cake" in first_dict}')
    print(f'Cake is a value in the dictionary: {"Mango" in first_dict.values()}')


def dictionaries_two(a_dictionary):

    #make a copy of the original dictionary
    a_dictionary = deepcopy(a_dictionary)

    new_dictionary = dict()

    for key, value in a_dictionary.items():
        new_dictionary[key] = value.lower().count('t')
    show_dict_items(new_dictionary)

def sets():
    #set comprehension for each set
    s2 = {num for num in range(21) if num %2 == 0}
    s3 = {num for num in range(21) if num %3 == 0}
    s4 = {num for num in range(21) if num %4 == 0}
    sets = (s2, s3, s4)

    for index in range(len(sets)):
        print(f's{index+2}: {sets[index]}')

    print(f's3 is a subset of s2: {s3.issubset(s2)}')
    print(f's4 is a subset of s2: {s4.issubset(s2)}')

def sets_two():
    py_set = {letter for letter in 'Python'}
    marathon_set = frozenset({letter for letter in 'marathon'})

    print(f'Orginal Python set: {py_set}')
    py_set.update('i')
    print(f'Modified Python set: {py_set}')

    print(f'Marathon frozen set: {marathon_set} is a {type(marathon_set)}.')
    print(f'Union of the two sets: {py_set.union(marathon_set)}')
    print(f'Intersection of the two sets: {py_set.intersection(marathon_set)}')




if __name__ == '__main__':

    dictionaries_one(FIRST)
    dictionaries_two(FIRST)
    sets()
    sets_two()
    print('Alles gute!')
