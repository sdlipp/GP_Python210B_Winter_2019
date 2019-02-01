#!/usr/bin/env python3

# Task 1: goal is to get 'file_002 : 123.46, 1.00e+04, 1.23e+04'
list_data = ( 2, 123.4567, 10000, 12345.67)
first = "{:0>3d}".format(list_data[0])
second = "{:.2f}".format(list_data[1])
third = "{:.2e}".format(list_data[2])
fourth = "{:.2e}".format(list_data[3])
print(list_data)

mod_data = "file_{} :   {}, {}, {}".format(first, second, third, fourth)
print(mod_data)