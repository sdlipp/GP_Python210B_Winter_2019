#!/usr/bin/env python3
#part 1
dict1={'name':'Daniel','city':'Seattle','cake':'Chocolate'}
print(dict1)
dict1.pop('cake')
print(dict1)
dict1['fruit']='Mango'
print(dict1.keys())
print(dict1.values())
if 'cake' in dict1.keys():
    print(True)
else:
    print(False)
if 'Mango' in dict1.values():
    print(True)
else:
    print(False)
#part2
for key,value in dict1.items():
    value=value.upper()
    times = value.count('T')
    dict1[key]=times
#sets
counter = 0
s2list = [];s3list = [];s4list = []
while counter <=20:
    if counter%2==0:
        s2list.append(counter)
    if counter%3==0:
        s3list.append(counter)
    if counter%4==0:
        s4list.append(counter)
    counter+=1
s2 = set(s2list);s3 = set(s3list);s4 = set(s4list)
print(s2);print(s3);print(s4)
print(s3.issubset(s2))
print(s4.issubset(s2))
#sets2
word = list("Python")
s5 = set(word)
print(s5)
s5.add('i')
print(s5)
word2 = 'marathon'
s6 = frozenset(word2)
print(s6)
print(s5.union(s6))
print(s5.intersection(s6))