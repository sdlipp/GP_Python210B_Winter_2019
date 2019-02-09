#!/usr/local/bin/python3

#NameError
a=str(input("Enter a number"))
if(a == '1'):
   one()
    print(one)
#This results in a nameerror as one is not defined
#minerva:session01 junya$ python break_me.py
#Enter a number1
#Traceback (most recent call last):
#  File "break_me.py", line 5, in <module>
#    one()
#NameError: name 'one' is not defined

#TypeError
len(13)
#This causes a TypeError due to the fact that a number
#is the wrong type for this function.  (It's expecting
#a string, not an integer)

#SyntaxError
print "Done and done"
#This errors because there are no parentesis surrounding
#the string value to be printed

#AttributeError
import math
test = len.math("ernie.ball")
#This causes an AttributeError because math isn't an
#attribute
