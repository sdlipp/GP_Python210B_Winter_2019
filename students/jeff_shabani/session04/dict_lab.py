#!/usr/bin/env python3

first = {'name': 'Chris',
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


dictionaries_one(first)
