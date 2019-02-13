#!/usr/local/bin/python3

# Task One
print("\n*** Task One ***\n")
print("file_00{:d} :  {:.2f}, {:.2e}, {:.2e}".format(2, 123.4567, 10000, 12345.67))

# Task Two
print("\n*** Task Two ***\n")


def task_two(string):
    file_number = 2
    first_float = 123.4567
    first_int = 10000
    second_float = 12345.67
    print(string.format(file_number, first_float, first_int, second_float))


string = "file_00{:d} :  {:.2f}, {:.2e}, {:.2e}"
task_two(string)

# Task Three
print("\n*** Task Three ***\n")


def task_three(sequence):
    length = len(sequence)
    brackets = length * ['{}']
    commas = ", ".join(brackets)
    print(("the {} numbers are: " + commas).format(length, *sequence))


sequence = (2, 3, 5)
task_three(sequence)

# Task Four
print("\n*** Task Four ***\n")
a_tuple = (4, 30, 2017, 2, 27)
formatter = "{}, {}, {}, {}, {}"
formatted = formatter.format(a_tuple[3], a_tuple[4], a_tuple[2], a_tuple[0], a_tuple[1])
print(formatted)

# Task Five
print("\n*** Task Five ***\n")
four_list = ['oranges', 1.3, 'lemons', 1.1]
oranges = four_list[0]
orange = oranges[:-1]
lemons = four_list[2]
lemon = lemons[:-1]
first_string = f"The weight of an {orange} is {four_list[1]} and the weight of a {lemon} is {four_list[3]}"
print(first_string)
second_string = f"The weight of an {orange.upper()} is {four_list[1] * 1.2} and the weight of a {lemon.upper()} is {four_list[3] * 1.2}"
print(second_string)

# Task Six
print("\n*** Task Six ***\n")
list_of_lists = ['Anne', '30', '$199.95'], ['Bonnie', '35', '$15,000.01'], ['Chuck', '33', '$2.00']
for list in list_of_lists:
    string = '{:20}{:10}{:20}'.format(list[0], list[1], list[2])
    print(string)




