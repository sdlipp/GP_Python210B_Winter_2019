#!/usr/bin/env python3

# Douglas Klos
# January 30th, 2019
# Python 210, Activity #4
# dict_lab.py

my_dict = {'name': 'Chris',
            'city': 'Seattle',
            'cake': 'chocolate', }


def dictionary1():
    """ Dictionary 1 activites """
    
    print(my_dict)

    # Delete the entry for cake
    del(my_dict['cake'])
    print(my_dict)
    
    # Add entry for fruit with mango for dictionary
    my_dict['fruit'] = 'mango'
    print(my_dict)

    # Display the dictionary keys
    print(my_dict.keys())

    # Display the dictionary values
    print(my_dict.values())

    # Display if 'cake' is a key in the dictionary
    print('cake' in my_dict)

    # Display if 'mango' is a vlue in the dictionary
    print('mango' in my_dict.values())

def dictionary2():
    """ Dictionary 2 activities """
    new_dict = {}

    # Create a new dictionary wit the same key, but for value
    # use the number of "t" in the original value
    for key in my_dict:
        new_dict[key] = my_dict[key].lower().count('t')

    print(new_dict)


def set1():
    # Create a list of number 0 - 20
    numbers = list(range(21))
    s2 = set(numbers[0:21:2])
    s3 = set(numbers[0:21:3])
    s4 = set(numbers[0:21:4])
    print(s2)
    print(s3)
    print(s4)
    print(s2.issubset(s3))
    print(s3.issubset(s2))
    print(s4.issubset(s2))


def set2():
    python_set = set('Python')
    print(python_set)
    python_set.add('i')
    print(python_set)
    python_set2 = frozenset('marathon')
    print(python_set2)
    print(python_set.union(python_set2))
    print(python_set.intersection(python_set2))

def main():
    dictionary1()
    dictionary2()
    set1()
    set2()

if __name__ == '__main__':
    main()
