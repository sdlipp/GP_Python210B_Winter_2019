#!/usr/bin/env python3

# Lesson 04 Exercise: Dictionary and Set Lab
# Jeremy Monroe

dict_one = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}

print("Dictionaries 1")
print(dict_one)

del dict_one['cake']

print(dict_one)


dict_one['fruit'] = 'Mango'
print('\n\nDict Keys:')
for key in dict_one:
    print(key + ', ', end='')
print()


print('\nDict Values:')
for value in dict_one.values():
    print(value + ', ', end='')
print()

print('\nIs cake a key in dict_one?')
print('cake' in dict_one)


print('\nIs Mango a value in dict_one?')
print('Mango' in dict_one.values())


print('\n\nDictionaries 2')
temp_dict = {}
t_count = 0
for key, value in dict_one.items():
    for letter in value:
        if letter.lower() == 't':
            t_count += 1
    
    temp_dict[key] = t_count
    t_count = 0

print(dict_one)
print(temp_dict)


print('\n\nSets 1')
s2 = {i for i in range(21) if i % 2 == 0}
s3 = {i for i in range(21) if i % 3 == 0}
s4 = {i for i in range(21) if i % 4 == 0}

print('s2: {}\ns3: {}\ns4: {}'.format(s2, s3, s4))

print('\nIs s3 subset of s2? : {}'.format(s3.issubset(s2)))
print('Is s4 subset of s2? : {}'.format(s4.issubset(s2)))



print('\n\nSets 2')
set_python = {'P', 'y', 't', 'h', 'o', 'n'}
set_python.add('i')

mara_set = {'m', 'a', 'r', 'a', 't', 'h', 'o', 'n'}
mara_frozen_set = frozenset(mara_set)

print('Union of sets: {}'.format(set_python.union(mara_frozen_set)))
print('Intersection of sets: {}'.format(set_python.intersection(mara_frozen_set)))