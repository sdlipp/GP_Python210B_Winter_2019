#!/usr/local/bin/python3
"""This is a test to make sure I understand how the code works."""
import sys
"""import sys for .argv input"""
n = int(sys.argv[1])

def fibonacci(n):
   """This is a recusive loop to calc the sequence"""
   if n <= 1:
	   return n
   else:
	   return(fibonacci(n-1) + fibonacci(n-2))

if n <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(n):
	   print(fibonacci(i))
