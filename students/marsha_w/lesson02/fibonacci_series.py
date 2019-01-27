'''
Title:Fibonacci and Lucas
Dev:Marsha Wheeler
Date:01-23-18
'''

'''Create a new module series.py in the session02 folder in your student folder.
In it, add a function called fibonacci.
The function should have one parameter n.
The function should return the nth value in the fibonacci series (starting with zero index).
Ensure that your function has a well-formed docstring'''
# fibonacci series function
def fib(n):
   n1 = 0
   n2 = 1
   count = 0
   nterms = n
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

#lucas series function
def lucas(n):
   n1 = 2
   n2 = 1
   count = 0
   nterms = n
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
#sum series

def sumSeries():
