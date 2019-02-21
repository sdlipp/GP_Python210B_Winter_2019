#/usr/bin/env python3

# Dictionaries 1

#create the dictionary
d = {}
d['name'] = "Chris"
d['city'] = "Seattle"
d['cake'] = "Chocolate"
print(d)

#remove the entry for cake
d.pop("cake")
print(d)

#add and entry for fruit
d['fruit'] = "Mango"
print(d)

#display the dictionary keys
print(d.keys())

#display the dictionary values
print(d.values())

#display whether or not "cake" is a key in the dictionary
'cake' in d

#display whether or not "Mango" is a value in the dictionary
'Mango' in d.values()


#Dictionaries 2

d2 = d.copy()
for k, v in d2.items():
    d2[k] = v.count('t')
print(d2)    


#Sets

#Set 1 - create sets s2, s3, s4 that contain numbers 0-20, divisible by 2, 3, and 4

s2 = set()
s3 = set()
s4 = set()

for x in range(21):
    if not x % 2:
        s2.add(x)
    if not x % 3:    
        s3.add(x)
    if not x % 4:   
        s4.add(x) 
print(s2)
print(s3)
print(s4)

#display if s3 is a subset of s2 (False)

print(s3.issubset(s2))

#display if s4 is a subset of s2 (True)

print(s4.issubset(s2))


#Set 2 - create a set with the letters in 'Python' and add 'i'

p_set = set()
for p in 'Python':
    p_set.add(p.lower())
p_set.add('i')    


#create a frozen set with the letters in 'marathon'
f_set = frozenset('marathon')

#display the union and intersection of the two sets

print("Union: ", p_set.union(f_set))
print("Intersection: ", p_set.intersection(f_set))
  

