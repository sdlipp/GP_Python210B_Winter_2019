#!/usr/bin/env python3

mydict = {'Name': 'Chris', 'City': 'Seattle', 'Cake': 'Chocolate', 'Status': 'Single', 'Vegetable': 'Turnip'}
        
        
if __name__ == "__main__":
    
    #print dictionary
    print("Display Dictionary")
    print(mydict)
    print()
    
    #delete entry for cake
    print("Deleting entry for cake")
    try:
        #del mydict['Cake']
        mydict.pop('Cake')
    except KeyError:
        pass
    print("Display Dictionary after Deleting Cake")
    print(mydict)
    print()
    
    #add new key to dictionary
    print("Adding key Fruit with value Mango to Dictionary")
    mydict['Fruit'] = 'Mango'
    print("Display Dictionary after Adding Fruit")
    print(mydict)
    print()
    
    #display dictionary keys
    print(mydict.keys())
    print()
    
    # display dictionary values
    print(mydict.values())
    print()
      
    #display if cake is a key
    print("Is 'Cake' a key in the dictionary?" ,'Cake' in mydict)
    print()
    
    #display if cake is a key
    print("Is 'Mango' a value in the dictionary?" ,'Mango' in mydict.values())
    
    #Creating dictionary with t count
    tcountDict = {}
    for key in mydict:
        tcountDict[key] = mydict[key].lower().count('t')
    print("original dictionary")
    print(mydict)
    print()
    
    print("New dictionary with case insensitive t count")
    print(tcountDict)
    print()
    
    #Create sets s2, s3, s4
    s2_list = []
    s3_list = []
    s4_list = []
    
    for i in range(20):
        if i % 2 == False:
            s2_list.append(i)
        if i % 3 == False:
            s3_list.append(i)
        if i % 4 == False:
            s4_list.append(i)
    
    #Create and display sets
    s2_set  = set(s2_list)
    print(f"printing s2 {s2_set}")
    print()
    
    s3_set  = set(s3_list)
    print(f"printing s2 {s3_set}")
    print()
    
    s4_set  = set(s4_list)
    print(f"printing s4 {s4_set}")
    print()
    
    #Is s3_set a subset of s2_set
    print(f"Is s3 a subset of s2 --", (s3_set.issubset(s2_set)))
    
    #Is s4_set a subset of s2_set
    print(f"Is s4 a subset of s2 --", (s4_set.issubset(s2_set)))
    
    #create a set of letters in Python
    myset = set(list('Python'))
    print(f"Printing set with letters in 'Python' ", myset)
    
    myset.add('i')
    print(f"Printing set with letters in 'Python' and adding 'i' ", myset)
    print()
    
    #create a frozen set with letters in 'marathon'
    fs = frozenset(list('marathon'))
    print(f"Printing frozen set with letters in 'marathon' ", fs)
    print()
    
    #displaying union of myset and fs
    print(f"Union of the sets are ", myset.union(fs))
    print()
    
    #displaying intersection of myset and fs
    print(f"Intersection of the sets are ", myset.intersection(fs))
    print()