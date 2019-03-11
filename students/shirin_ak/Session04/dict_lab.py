#-------------------
#!/usr/bin/env python3
#Session 04 Exercise:dict_lab.py
#Shirin Akther
#-------------------------



#Create a dictionary containing “name”, “city”, and “cake” for “Chris”
#from “Seattle” who likes “Chocolate”


print("\n............ Dictionaries-1 ........... ")
 
 
Dict={"name": "Chris",
      "City":"Seattle",
      "cake":"Chocolate"}

print(" {name} from {City} who likes {cake}".format(**Dict))

# Delete the entry for cake
del Dict["cake"]
print("\n Display the dict after deletion:\n", Dict)


#Add an entry for “fruit” with “Mango” and display the dictionary.

Dict["fruit"]= "Mango"
print("\n Display the dict after adding:\n", Dict)

#Display dictionary keys
print( Dict.keys())


print("\nDictionary keys :")  
for key, value in Dict.items():
    print( key)


#Display dictionary values
#print( Dict.values())

print("\nDictionary values :")  
for key, value in Dict.items():
    print( value)



#Display whether or not “cake” is a key in the dictionary
print("\nIs cake is a key in Dictionary? ")   
key = Dict.keys()

print("cake" in key)




# Display whether or not "Mango" is a value in the dictionary.

print("\nIs mango is a value in Dictionary? ")  
print ("Mango" in Dict.values())



print("\n............... Dictionaries-2 ................. \n")

Dict={"name": "Chris",
      "City":"Seattle",
      "cake":"Chocolate"}


# Using the dictionary from item 1: Make a dictionary using the same keys

# but with the number of 't's in each value.

new_lab = {}

Dict = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}

print("Display the dictionary with a number of 't' in each value")

for a, number in Dict.items():
    new_lab[a] = number.lower().count("t")

    print(new_lab)


#Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.
#Display the sets.

    
print('\n\nSets 1-----\n')
print("Print set s2,s3 and s4:")

s2 = {i for i in range(0,21) if i % 2 == 0}

s3 = {i for i in range(0,21) if i % 3 == 0}

s4 = {i for i in range(0,21) if i % 4 == 0}

print('s2: {}\ns3: {}\ns4: {}'.format(s2, s3, s4))

print('\nIs s3 subset of s2? : {}'.format(s3.issubset(s2)))

print('Is s4 subset of s2? : {}'.format(s4.issubset(s2)))


#Display if s3 is a subset of s2 (False)
#and if s4 is a subset of s2 (True).

print('\n\nSets 2--------')

set_python = {'P', 'y', 't', 'h', 'o', 'n'}

set_python.add('i')

marathon = {'m', 'a', 'r', 'a', 't', 'h', 'o', 'n'}

mara_frozenset = frozenset(marathon)

print('Intersection of sets: {}'.format(set_python.intersection(mara_frozenset)))
print('Union of sets: {}'.format(set_python.union(mara_frozenset)))

print("\n")








 

    



 
