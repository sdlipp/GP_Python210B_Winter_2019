#!/usr/bin/env python3
#task1
list1 = ['Apples','Pears','Oranges','Peaches']
print(list1)
response = input(" name another fruit ")
list1.append(response)
print(list1)
response2 = input(" name a number ")
print(f'the {response2}rd item in the list is {list1[int(response2)-1]}')
list1 = ['Cherry']+list1
print(list1)
list1.insert(0,'Kiwi')

for value in list1:
    if 'P' in value[0]:
        print(value)
#task 2
print(list1)
list1.pop()
print(list1)
response3 = input(" name a fruit to delete ")
for num,value in enumerate(list1):
    if response3 in value:
        list1.pop(num)
print(list1)
#task 3
for num,value in enumerate(list1):
    response4 = ''
    while response4 != 'yes' and response4 != 'no':
        response4 = input(f'Do you like {value.lower()}?')
    print(response4)
    if response4 =='no':
        list1.pop(num)
    print(list1)
#task 4
list2 = [value[::-1] for value in list1]
print(list2)
list1.pop()
print(list1,list2)

