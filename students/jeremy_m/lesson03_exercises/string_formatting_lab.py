#!/usr/bin/env python3

# lesson 03 Exercise - String Formatting Lab
# Jeremy Monroe


# TASK 1
first_tup = (2, 123.4567, 10000, 12345.67)
print('Task one:')
print('file_{:03d} : {:06.2f}, {:.2E}, {:.2E}'.format(*first_tup))


# TASK 2
print('\nTask Two:')
print(f'file_{first_tup[0]:03d} : {first_tup[1]:06.2f}, {first_tup[2]:.2E}, {first_tup[3]:.2E}')



# TASK 3
print("\nTask Three:")
def formatter(seq):
    l = len(seq)
    return ("the {} numbers are: " + ", ".join(['{}'] * l)).format(l, *seq)

print(formatter(first_tup))
print(formatter((1, 4, 5, 6, 7, 3, 2, 1)))



# TASK 4
print("\nTask Four:")
task_four_tup = (4, 30, 2017, 2, 27)
print(sorted(task_four_tup))



# TASK 5
print("\nTask Five:")
task_five_list = ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an {task_five_list[0][:-1]} is {task_five_list[1]} and the weight of a {task_five_list[2][:-1]} is {task_five_list[3]}')
print(f'The weight of an {task_five_list[0][:-1].upper()} is {task_five_list[1] * 1.2} and the weight of a {task_five_list[2][:-1].upper()} is {task_five_list[3] * 1.2}')



# TASK 6
print("\nTask Six:")
task_six_tup = (['Pretzel', '12', '$5.75'],
                ['Tuna Fish', '62', '$62.99'],
                ['PB&J', '4', '$126.33'],
                ['Freeze Dried Tomato', '664', '$1242.96']
                )

days_old = 'Days Old'
for task in task_six_tup:
    print(f'{task[0]:25}{task[1]:5}{days_old:15}{task[2]}')

print('\nSecond part of task six')
task_six_tup_two = (123, 223, 32, 3, 53, 623, 7124, 842, 9, 10)
print(("".join(['{:5}'] * 10).format(*task_six_tup_two)))