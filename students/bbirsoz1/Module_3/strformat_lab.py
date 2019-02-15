#!/usr/bin/env python3

#STRING LAB

#Task One
print("Task 1")
tuple = (2, 123.4567, 10000, 12345.67)
print("file_{:03d} : {:8.2f}, {:.2e}, {:.3}".format(*tuple))
print()
#Second way:
#print("file_00{} : {:.2f}, {:.2e}. {:.3e}".format(2, 123.4567, 10000, 12345.67))


#Task Two
print("Task 2")
print(f"file_{tuple[0]:03d} : {tuple[1]:8.2f}, {tuple[2]:.2e}, {tuple[3]:.3}")
print()

#Task Three
print("Task 3")
#Dynamically build up a format string from a tuple. Accommodate the length of the tuple.
def formatter(in_tuple):
    length = len(in_tuple)
    form_string = "The {} numbers are: ".format(length)+",".join(["{:d}"]*length)
    return form_string.format(*in_tuple)
tuple_b = (2, 3, 5, 7, 9, 11)
print(formatter(tuple_b))
print()

#Task Four
print("Task 4")
tuple_c = ( 4, 30, 2017, 2, 27)
print("{:02d} {:d} {:d} {:02d} {:d}".format(tuple_c[3], tuple_c[4], tuple_c[2], tuple_c[0], tuple_c[1]))
print()

#Task Five
print("Task 5")
# Display: The weight of an orange is 1.3 and the weight of a lemon is 1.1
elements = ['orange', 1.3, 'lemon', 1.1]
fruit = elements[0]
weight = elements[1]
fruit_b = elements[2]
weight_b = elements[3]
print(f"The weight of an {fruit} is {weight} and the weight of a {fruit_b} is {weight_b}")
print("Fruits in upper case and weights 20% higher:")
print(f"The weight of an {fruit.upper()} is {weight*1.2} and the weight of a {fruit_b.upper()} is {weight_b*1.2}")
print()
#Second way:
#print(f"The weight of an {elements[0]} is {elements[1]} and the weight of a {elements[2]} is {elements[3]}")

#Task Six
print("Task 6")
#print('{:20}{:10}{:20}{:8}'.format('First', '$99.01', 'Second', '$88.09'))
display = ('Name', 'Age', 'Cost')
input1 = ('Luis', 5, 1111)
input2 = ('Mike', 3, 111)
print("{:>7} {:>7} {:>9}".format(*display))
print("{:>7} {:>7} {:>9.2f}".format(*input1))
print("{:>7} {:>7} {:>9.2f}".format(*input2))
print()

