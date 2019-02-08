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


