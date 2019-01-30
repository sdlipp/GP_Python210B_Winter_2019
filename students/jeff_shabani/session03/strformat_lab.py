#!/usr/bin/env python3

ELEMENTS_TO_FORMAT = ( 2, 123.4567, 10000, 12345.67)

def task_one(item):
    result = f'file_00{item[0]}: {item[1]:.2f}, {item[2]:.2e}, {item[3]:.2e}'
    print(result)


def task_two(item):
    binary = 'b'
    precision = 7
    print(f'First item as binary: {item[0]:{binary}}.\nSecond item as character:'
          f' {item[1]:.{precision}f}.\nThird item as hex: {hex(item[2])}.\nLast item as int: {int(item[3])}')


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



task_one(ELEMENTS_TO_FORMAT)
#task_two(ELEMENTS_TO_FORMAT)
task_three((1.2, 3.0, 4.56, 9.12, 78.8923421))