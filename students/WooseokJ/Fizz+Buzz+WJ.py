
# coding: utf-8

# In[54]:


#Test1 (failed)
#the first is failed because i didn't use the elif command
for number in range(1,101):
        x = ""
        if number % 3 == 0:
            x += "Fizz"
        if number % 5 == 0:
            x += "Buzz"
            print (x)


# In[3]:


#Test 2
#the parameter fizzy first it has to be the higest number you want plus one
#creates one parameter for when the number is devisable by both 3 and 5
#then for when divisable for 3 print buzz
#then for when divisable for 5 print fizz
Fizzy=100
for number in range(1,Fizzy+1):
    if number % 3 ==0 and number % 5 ==0:
        print ("FizzBuzz")
    elif number % 3 == 0:
        print ("Fizz")
    elif number % 5 == 0:
        print ("Buzz")
    else:
        print(number)

