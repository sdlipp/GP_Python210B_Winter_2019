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
    
    print(s2_list)
    print()
    print(s3_list)
    print()
    print(s4_list)
    print()
    
    