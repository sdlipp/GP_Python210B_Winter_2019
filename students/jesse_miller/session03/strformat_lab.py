#!/usr/local/bin/python3
#Task 1
#Defining the tuple, just in case
tuple = ( 2, 123.4567, 10000, 12345.67)

#Formatting needs to be this:  'file_002 :   123.46, 1.00e+04, 1.23e+04'
#Apparently, the old fashioned way:
print('File_00{0} :  {1:.2f}, {2:.2e}, {3:.2e}'.format(2, 123.4567, 10000, 12345.67))

#Task 2
#Using an f-string
print(f"File_00{2} :  {123.4567:.2f}, {10000:.2e}, {12345.67:.2e}")

#Task 3
#reference example
#print("the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3))
n = len(tuple)
def formatter(self):
    form_string = "{:d}" * n
    print(f"{}" * n)
formatter(tuple)
