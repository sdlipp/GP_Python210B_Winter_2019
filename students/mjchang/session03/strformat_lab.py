# #!/usr/bin/env python3

# # Task 1: goal is to get 'file_002 : 123.46, 1.00e+04, 1.23e+04'
list_data = ( 2, 123.4567, 10000, 12345.67)
first = "{:0>3d}".format(list_data[0])
second = "{:.2f}".format(list_data[1])
third = "{:.2e}".format(list_data[2])
fourth = "{:.2e}".format(list_data[3])

mod_data = "file_{} :   {}, {}, {}".format(first, second, third, fourth)


# # Task 2: repeat Task 1 using an alternate type of format string

mod_data2 = f"file_{first} : {second}, {third}, {fourth}"
print(mod_data2)


# Task 3: Dynamically building up format strings
def formatter(in_tuple):
    count = len(in_tuple)
    return ("There are {} items and they are: " + ", ".join(["{}"] * count)).format(count,*in_tuple)


# Task 4: given a 5 element tuple, reformat it to print in a different order

def date_formatter(time):
    month = "{:0>2d}".format(time[3])
    day = "{:0>2d}".format(time[4])
    year = "{:0>4d}".format(time[2])
    hour = "{:0>2d}".format(time[0])
    minute = "{:0>2d}".format(time[1])
    return "{} {} {} {} {}".format(month, day, year, hour, minute)


# Task 5: display the weight of and orange and lemon
elements = ['orange', 1.3, 'lemon', 1.1]
f"The weight of an {elements[0]} is {elements[1]} and the weight of a {elements[2]} is {elements[3]}"
f"The weight of an {elements[0]} is {elements[1]*1.2} and the weight of a {elements[2]} is {elements[3]*1.2}"