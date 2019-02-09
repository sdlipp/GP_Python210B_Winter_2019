
# coding: utf-8

# In[5]:


#Task 1 
def task1():
    print('Task 1:')
    given = (2, 123.4567, 10000, 12345.67)
    string = 'file_{:03d} :\t{:.2f}, {:.2e}, {:.3g}'
    print(string.format(*given))
    print()
# task 2
def task2():
    print('Task 2:')
    tuple_to_format = (2, 123.4567, 10000, 12345.67)
    print(f'file_{tuple_to_format[0]:03d} :\t{tuple_to_format[1]:.2f}, '
          f'{tuple_to_format[2]:.2e}, {tuple_to_format[3]:.3g}')
    print()
# task 3
def task3():
    print('Task 3:')
    tuple_to_format = (1, 2, 3)
    print(formatter(tuple_to_format))
    tuple_to_format = (1, 2, 3, 4, 5)
    print(formatter(tuple_to_format))
    tuple_to_format = (1, 2, 3, 4, 5, 6, 7, 8)
    print(formatter(tuple_to_format))
    print()
def formatter(tuple_to_format):
    length = len(tuple_to_format)
    formatted_string = ('The {} numbers are: ' + ', '.join(['{}'] * length))        .format(length, *tuple_to_format)
    return formatted_string
#task 4
def task4():
    print('Task 4:')
    tuple_to_format = (4, 30, 2019, 2, 27)
    string_formatter = ' '.join(['{:02d}'] * len(tuple_to_format))
    print("'" + string_formatter.format(tuple_to_format[3], tuple_to_format[4],
          tuple_to_format[2], tuple_to_format[0], tuple_to_format[1]) + "'")
    print()
#task 5
def task5():
    print('Task 5:')
    list_to_format = ['oranges', 1.3, 'lemons', 1.1]
    print(f'The weight of an {list_to_format[0]:.6} '
          f'is {list_to_format[1]} '
          f'and the weight of a {list_to_format[2]:.5}'
          f'is {list_to_format[3]}')
    print(f'The weight of an {(list_to_format[0]).upper():.6} '
          f'is {(list_to_format[1]) * 1.2} '
          f'and the weight of a {(list_to_format[2]).upper():.5} '
          f'is {(list_to_format[3]) * 1.2}')
    print()
#task 6
def task6():
    print('Task 6:')
    tuple_to_format = (('Daniel', 21, 3200.00),('Sam', 22, 0.00),('Andrew', 20, 1200.00))
    for i in range(len(tuple_to_format)):
        print('%10s, %3d,  $%9.2f' % tuple_to_format[i])
def main():
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()


if __name__ == "__main__":
    main()

