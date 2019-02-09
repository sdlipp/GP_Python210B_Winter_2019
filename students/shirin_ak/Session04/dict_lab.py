#Create a dictionary containing “name”, “city”, and “cake” for “Chris”
#from “Seattle” who likes “Chocolate”


print("............ Dictionaries-1 ........... ")
 
 
Dict={"name": "Chris",
      "City":"Seattle",
      "cake":"Chocolate"}

print("{name} from {City} who likes {cake}".format(**Dict))

# Delete the entry for cake
del Dict["cake"]
print("\n Display the dict after deletion\n", Dict)

#Add an entry for “fruit” with “Mango” and display the dictionary.

Dict["fruit"]= "Mango"
print("\n Display the dict after add\n", Dict)

#Display dictionary keys
print( Dict.keys())


print("Dictionary keys :")  
for key, value in Dict.items():
    print( key)

#Display dictionary values
print( Dict.values())

print("Dictionary values :")  
for key, value in Dict.items():
    print( value)

key = Dict.keys()

print("cake" in key)
print("\n")


# Display whether or not "Mango" is a value in the dictionary.

print ("Mango" in Dict.values())

print("............ Dictionaries-2 ........... ")

Dict={"name": "Chris",
      "City":"Seattle",
      "cake":"Chocolate"}


# Using the dictionary from item 1: Make a dictionary using the same keys

# but with the number of 't's in each value.

new_lab = {}

Dict = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}

for a, number in Dict.items():
    new_lab[a] = number.count("t")

    print(new_lab)


#Problem-4
"""Create sets s2, s3 and s4 that contain numbers from zero through twenty,

    divisible 2, 3 and 4.

    Display the sets.

    Display if s3 is a subset of s2 (False)

    and if s4 is a subset of s2 (True)."""

    
print("\nDisplay the set s2,s3 and s4\n")

s2 = set(range(0, 21)[::2])

s3 = set(range(0, 21)[::3])
s4 = set(range(0, 21)[::4])

print(s2)
print(s3)

print(s4)


 

    



 
