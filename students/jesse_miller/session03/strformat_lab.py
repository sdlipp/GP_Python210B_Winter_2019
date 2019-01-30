#!/usr/local/bin/python3
#Task 1

#Formatting needs to be this:  'file_002 :   123.46, 1.00e+04, 1.23e+04'
#Apparently, the old fashioned way:
print('File_00{0} :  {1:.2f}, {2:.2e}, {3:.2e}'.format(2, 123.4567, 10000, 12345.67))

#Task 2
#Using an f-string
print(f"File_00{2} :  {123.4567:.2f}, {10000:.2e}, {12345.67:.2e}")

#Task 3
#reference example
#Defining tuple
nums = (1, 2, 3, 4, 5, 6)
#Defining the function.  This takes the len of the nums variable, and uses that
#to iterate the print process. I have a nasty suspicion this took me too long
#because I was overthinking again.
def formatter(nums):
    print(f'%2d '*len(nums) % tuple(nums))
formatter(nums)

#Task 4
nums = ( '4', '30', '2017', '2', '27' )
fstring = "{:d} {:d} {:d} {:d} {:d}"
fnums = nums[3], nums[4], nums[2], nums[0], nums[1]

#iterating to get the proper output.
output = ''
for number in fnums:
    output += number.zfill(2) + " "
print(output)
#Task 5
fruits = ['oranges', 1.3, 'lemons', 1.1]
fstring = "{:d} {:d} {:d} {:d}"
def display(s):
    print(f"The weight of an {fruits[0][:-1]} is {fruits[1]} and the weight of a {fruits[2][:-1]} is {fruits[3]}".format(fstring))
display(fruits)

#Task 6
