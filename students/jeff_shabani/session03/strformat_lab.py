#!/usr/bin/env python3

ELEMENTS_TO_FORMAT = (2, 123.4567, 10000, 12345.67)


def task_one(item):
    result = f'file_00{item[0]}: {item[1]:.2f}, {item[2]:.2e}, {item[3]:.2e}'
    print(result)


task_one(ELEMENTS_TO_FORMAT)


def task_two(item):
    binary = 'b'
    precision = 7
    print(f'First item as binary: {item[0]:{binary}}.\nSecond item as character:'
          f' {item[1]:.{precision}f}.\nThird item as hex: {hex(item[2])}.\nLast item as int: {int(item[3])}')


task_two(ELEMENTS_TO_FORMAT)


def task_three(variable_len_tuple):
    """Dynamically builds a string with tuple items. Tuple length is unknown.
    Begins with indicating length of tuple. Last tuple item is formatted as an
    integer and preceded with 'and' and ended with a period. Non-last items are
    formatted as a float with precion equal to index position in tuple.
    """
    result = f'The {len(variable_len_tuple)} numbers are:'
    for i in variable_len_tuple:
        if variable_len_tuple.index(i) == len(variable_len_tuple) - 1:
            result += f' and {int(i)}.'
        else:
            result += f' {i:.{variable_len_tuple.index(i)}f},'
    return result


print(task_three((1.2, 3.0, 4.56, 9.12, 78.8923421)))


def task_four(five_element_tuple):
    print(f'0{five_element_tuple[3]} {five_element_tuple[4]} {five_element_tuple[2]} 0{five_element_tuple[0]} '
          f'{five_element_tuple[1]}')


task_four((4, 30, 2017, 2, 27))


def task_five(four_element_list):
    print(
        f'The weight of an {four_element_list[0][:-1]} is {four_element_list[1]} and the weight of a'
        f' {four_element_list[2][:-1]} is {four_element_list[3]}')
    print(
        f'The weight of an {four_element_list[0][:-1].upper()} is {four_element_list[1] * 1.2} and the weight of a'
        f' {four_element_list[2][:-1].upper()} is {four_element_list[3] * 1.2}')


task_five(['oranges', 1.3, 'lemons', 1.1])

NAMES = ['Sammy', 'William', 'Bobby', 'Skip', 'Harry', 'Lesley', 'Ashley']
AGES = [29, 45, 3, 5, 90, 21, 51]
COSTS = [2900, 100, 15, 5, 100000, 23000, 81]


def task_six(iter1, iter2, iter3):
    print(f'{"Name".rjust(10)}{"Age".rjust(10)}{"Cost".rjust(10)}')
    for i in range(len(NAMES)):
        print(f'{str(NAMES[i]).rjust(10)}{str(AGES[i]).rjust(10)}{str(COSTS[i]).rjust(10)}')


task_six(NAMES, AGES, COSTS)


#task 6 extra
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for i in numbers:
    print(str(i).rjust(5))
