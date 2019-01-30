#!/usr/bin/env python3

ELEMENTS_TO_FORMAT = ( 2, 123.4567, 10000, 12345.67)

def task_one(item):
    print(f'file_00{item[0]}: {item[1]:.2f}, {item[2]:.2e}, {item[3]:.2e}')


def task_two(item):
    binary = 'b'
    precision = 7
    print(f'First item as binary: {item[0]:{binary}}.\nSecond item as character:'
          f' {item[1]:.{precision}f}.\nThird item as hex: {hex(item[2])}.\nLast item as int: {int(item[3])}')


#task_one(ELEMENTS_TO_FORMAT)
task_two(ELEMENTS_TO_FORMAT)