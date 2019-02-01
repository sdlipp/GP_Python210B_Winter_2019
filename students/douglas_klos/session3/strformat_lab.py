#!/usr/bin/env python3

# Douglas Klos
# Python 210, Exersice 3
# January 24rd, 2019
# strformat_lab.py


def task1():
    """
    Given an input tuple(2, 123.4567, 10000, 12345.67), display it back
    as "file_002 :	123.46, 1.00e+04, 1.23e+04" such that:
    The first value is padded with two 0's and the text 'file_',
    The second is a float shown with two deciaml places,
    The third is in scientific notation with two deicamls,
    The fourth is in scientific notation with three significant digis.
    """
    print('Task 1:')
    tuple_to_format = (2, 123.4567, 10000, 12345.67)

    # file_{:03d} indicates to display the first value as a deciaml
    # with length 3.  If there's not three digits, it's padded with 0s,
    # and the text 'file_' is added to the beginning.
    # \t is a tab.
    # {:.2f} displays the value as a float with two decimal places.
    # {:.2e} displays as scientific notation with two decimal places.
    # {:.3g} displays as 'general' notation with three significant
    #    digits.  Python determines if it should be displayed in
    #    scientific notattion.  In our case, it does.
    string_formatter = 'file_{:03d} :\t{:.2f}, {:.2e}, {:.3g}'
    print(string_formatter.format(*tuple_to_format))
    print()


def task2():
    """ Repeat of task1, except using an f-string """
    print('Task 2:')
    tuple_to_format = (2, 123.4567, 10000, 12345.67)

    # f-strings are new, but this is a bit ugly.
    # Is there a way to pass a *tuple to an f string?
    # Similar syntax to to task1(), however the name of the tuple and
    # the field to be displayed are added to each {}.
    print(f'file_{tuple_to_format[0]:03d} :\t{tuple_to_format[1]:.2f}, '
          f'{tuple_to_format[2]:.2e}, {tuple_to_format[3]:.3g}')
    print()


def task3():
    """
    The string 'The 3 numbers are: {:d}, {:d}, {:d}'.format(1, 2, 3)'
    rewritten to take an arbitrary number of values.  This function
    generates the tuples, passes them to formatter(), and displays
    the returned tuple.
    """
    print('Task 3:')
    tuple_to_format = (1, 2, 3)
    print(formatter(tuple_to_format))
    tuple_to_format = (1, 2, 3, 4, 5)
    print(formatter(tuple_to_format))
    tuple_to_format = (1, 2, 3, 4, 5, 6, 7, 8)
    print(formatter(tuple_to_format))
    print()


def formatter(tuple_to_format):
    """
    Formats the input tuple such that all fields in the tuple
    are displayed seperated by a comma.
    """
    length = len(tuple_to_format)

    # {} indicated where a value passed from str.format is displayed
    # ', '.join(['{}'] * length) dynamically adds a bracket for each
    # tuple in the list, determined by length.
    formatted_string = ('The {} numbers are: ' + ', '.join(['{}'] * length))\
        .format(length, *tuple_to_format)
    return formatted_string


def task4():
    """
    Given the string (4, 30, 2019, 2, 27), it is displayed as
    '02 27 2019 04 30' using a str.format.
    """
    print('Task 4:')
    tuple_to_format = (4, 30, 2019, 2, 27)

    # We join each number with a space.  {:02d} forces each number to
    # be at least two digits, and padds with 0's to meet this.
    # The string is dynamically formatted using len(tuple_to_format)
    # although we still are specifying indicies so doesn't matter
    string_formatter = ' '.join(['{:02d}'] * len(tuple_to_format))
    print("'" + string_formatter.format(tuple_to_format[3], tuple_to_format[4],
          tuple_to_format[2], tuple_to_format[0], tuple_to_format[1]) + "'")
    print()


def task5():
    """
    Using f-strings, the list ['oranges', 1.3, 'lemons', 1.1] is output
    as a string in the format 'The weight of an orange is 1.3 and the
    weight of a lemon is 1.1'.  For the second print, the fruit
    is displayed in uppercase and the weight increased by 20%.abs
    """
    print('Task 5:')

    # Worth noting, the list has plural oranges and lemons,
    # but the requested output is singular orange and lemon.
    list_to_format = ['oranges', 1.3, 'lemons', 1.1]

    # We use precision of 6 for oranges and 5 for lemons to drop
    # the plural 's'.  f-string usage here is more simple than task2().
    print(f'The weight of an {list_to_format[0]:.6} '
          f'is {list_to_format[1]} '
          f'and the weight of a {list_to_format[2]:.5}'
          f'is {list_to_format[3]}')
    print(f'The weight of an {(list_to_format[0]).upper():.6} '
          f'is {(list_to_format[1]) * 1.2} '
          f'and the weight of a {(list_to_format[2]).upper():.5} '
          f'is {(list_to_format[3]) * 1.2}')
    print()


def task6():
    """
    Displays a table of several rows, each with a name, an age, and a
    cost.  Tested with hundreds and thounds for alignment.
    Given a tuple with 10 consecutive numbers, the tuple is printed
    in columns that are five characters wide.
    """
    print('Task 6:')

    # Given a tuple of i rows, each containing a name, age, and value,
    # display the tuple in formatted columns.
    tuple_to_format = (('Doug', 38, 3000.00),
                       ('Maggie', 38, 25000.00),
                       ('Sam', 43, 400.00))

    # This will break alignment if strings are over 10 characters,
    # if ages are somehow four digits, or if currency is over
    # nine digits in length.  Acceptable for our values.
    # We could loop through the tuple to find the longest values for
    # each field, and then format the string to take these into account
    # but it seems unnecessary for this.
    for i in range(len(tuple_to_format)):
        print('%10s, %3d,  $%9.2f' % tuple_to_format[i])

    # Given a tuple with 10 consecutive numbers, the tuple is printed
    # in columns that are 5 characters wide.  Given these parameters,
    # if the number is over 5 characters, anything beyond 5 is dropped.
    # Wasn't specified how to handle this sceanario, this seemed
    # reasonable.  The %5s.5 means a column width of at least 5,
    # and to use string precision of 5.  This way all columns end
    # up being length 5 regardless of the input length.
    consecutive_num_tuple1 = (100001, 100002, 100003, 100004, 100005,
                              100006, 100007, 100008, 100009, 100010)
    consecutive_num_tuple2 = (101, 102, 103, 104, 105,
                              106, 107, 108, 109, 110)
    print()
    print('%5.5s ' * len(consecutive_num_tuple1) % consecutive_num_tuple1)
    print('%5.5s ' * len(consecutive_num_tuple2) % consecutive_num_tuple2)

    print()


def main():
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()


if __name__ == "__main__":
    main()
