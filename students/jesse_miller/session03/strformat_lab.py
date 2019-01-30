#!/usr/local/bin/python3
#Task 1
print("")
#Formatting needs to be this:  'file_002 :   123.46, 1.00e+04, 1.23e+04'
#Apparently, the old fashioned way:
print('File_00{0} :  {1:.2f}, {2:.2e}, {3:.2e}'.format(2, 123.4567, 10000, 12345.67))

#Task 2
print("")
#Using an f-string
print(f"File_00{2} :  {123.4567:.2f}, {10000:.2e}, {12345.67:.2e}")

#Task 3
print("")
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
print("")
nums = ( '4', '30', '2017', '2', '27' )
fstring = "{:d} {:d} {:d} {:d} {:d}"
fnums = nums[3], nums[4], nums[2], nums[0], nums[1]
#iterating to get the proper output.
output = ''
for number in fnums:
    output += number.zfill(2) + " "
print(output)

#Task 5
print("")
#Defining the list we're working with.
fruits = ['oranges', 1.3, 'lemons', 1.1]
#This function is just a collection of print statements.
def display(s):
    print(f"The weight of an {fruits[0][:-1]} is {fruits[1]} and the weight of a {fruits[2][:-1]} is {fruits[3]}")
    print(f"The weight of an {fruits[0].upper()[:-1]} is {fruits[1] * 1.20} and the weight of a {fruits[2].upper()[:-1]} is {fruits[3] * 1.20}")
    print(f"The weight of an {fruits[0].capitalize()[:-1]} is {fruits[1] * 1.20} and the weight of a {fruits[2].capitalize()[:-1]} is {fruits[3] * 1.20}")
display(fruits)
#Went ahead and did both upper and capitalize just in case I misunderstood.


#Task 6
print("")
names = [["Name", "Age", "Amount"],
         ["Robert", 61, 125.23],
         ["JD", 39, 25411.02],
         ["Chris", 41, 1243.87],
         ]
for name,age,amount in names:
    print("{:<15}{:^5}{:^2}".format(name,age,amount))
