
def formatter (tuple):
    length = len(tuple)
    format = length*'{:d},'
    string = format[:-1]
    intro = 'the {} numbers are: '.format(length)

    form_string = intro + string.format(*tuple)
    return print(form_string)

print('\n')
#task 1
tuple = ( 2, 123.4567, 10000, 12345.67)
print('file_{:03d},{:.2f},{:.2e},{:.2e}'.format(*tuple))
print('\n')
#task 2
print('\n')
t2_tuple = ( 2, 123.4567, 10000, 12345.67)
print("file_%03d,%.2f,%.2e,%.2e" % t2_tuple)
print('\n')
#task 3
formatter((2,3,5))
formatter((2,3,5,7,9))
print('\n')
#task 4
t4_tuple = ( 4, 30, 2017, 2, 27)
print('{3:02d},{4},{2},{0:02d},{1}'.format(*t4_tuple))
print('\n')
#task 5
t5_list = ['oranges', 1.3, 'lemons', 1.1]
print(f'the weight of {t5_list[0].upper()} is {1.2*t5_list[1]} and the weight of {t5_list[2].upper()} is {1.2*t5_list[3]}')
print('\n')
#task 6
name = ['adfkjdsfd','aadkkdfkadjsf','asdoiwejf']
age = [32,6,101]
cost = ['$1000.45','$5.45','145.34']
row_format ="{:>15}" * (len(cost))
print(row_format.format('Name','Age','Cost'))
for name,age,cost in zip(name,age,cost):
    print(row_format.format(name,age,cost))
