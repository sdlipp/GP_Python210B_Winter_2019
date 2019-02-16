
# Task 1
t = (2, 123.4567, 10000, 12345.67)

new_string = 'This is the new string file_{:0>3d}:  {:.2f}, {:.2e}, {:.2e}'.format(*t)
print(new_string)

# Task 2
print('{:.2e}'.format(10000))
print('{:.2e}'.format(12345.67))

s1 = 'This is the new file format {}.'.format('"file_002"')
print(s1)

s2 = 'The location is {0} N, {1} W.'.format(47.6062, 123.3321)
print(s2)

new_nums = 'These are the new numbers {}'.format(new_string)
print(f"{new_nums}")


# Task 3
t1 = (1, 2, 3)

my_string = 'the 3 numbers are: {:d}, {:d}, {:d}'.format(*t1)
print(my_string)


form_string = "{:d}, {:d}, {:d}, {:d}, {:d}, {:d}, {:d}"
nums = (12, 22, 30, 34, 42, 49, 56)
print(form_string.format(*nums))


def formatter(nums):
    form_string = '{:d}, {:d}, {:d}, {:d}, {:d}, {:d}, {:d}'
    return form_string.format(*nums)


print(formatter(nums))

# Task 4
t2 = (4, 30, 2017, 2, 27)
t_string = 'This is the new string {0:0>2d}, {1}, {2}, {3:0>2d}, {4}'.format(2, 27, 2017, 4, 30)

print(t_string)


# Task 5
my_list = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {my_list[0].upper()} is {my_list[1]*1.2} and the weight of a {my_list[2].upper()} is {my_list[3]*1.2}")

# Task 6
s6 = '{:20}{:10}{:20}{:8}'.format('First', '$99.01', 'Second', '$88.09')
print(s6)

s7 = '{:20}{:10}{:^35}'.format('Name', 'Age', 'Cost')
c1 = '{:20}{:10}{:>20}'.format('Alexander Whitty', '35', '$100.56')
c2 = '{:20}{:10}{:>20}'.format('Alexander Whitty', '21', '$10,000.56')
c3 = '{:20}{:10}{:>20}'.format('Alexander Whitty', '49', '$100.56')
c4 = '{:20}{:10}{:>20}'.format('Alexander Whitty', '62', '$1000.56')
c5 = '{:20}{:10}{:>20}'.format('Alexander Whitty', '18', '$1000.56')
c6 = '{:20}{:10}{:>20}'.format('Alexander Whitty', '55', '$100,000.56')
c7 = '{:20}{:10}{:>20}'.format('Alexander Whitty', '77', '$100.56')

print(s7)
print(c1)
print(c2)
print(c3)
print(c4)
print(c5)
print(c6)
print(c7)

t9 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
width = 5
for i in t9:
    for base in 'dXob':
        print('{0:{width}{base}}'.format(i, base=base, width=width), end=' ')
        print()
