'''
##########################
#Python 210
#Session 03 - String Formatting
#Elaine Xu
#Jan 28,2019
###########################
'''

############ Task 1 #################
print("Task 1")
SEQ = (2, 123.4567, 10000, 12345.67)
print("file_{:0>3d} : {:8.2f}, {:.2e}, {:.3}".format(*SEQ))


############ Task 2 #################
print("\nTask 2")
print(f"file_{SEQ[0]:0>3d} : {SEQ[1]:8.2f}, {SEQ[2]:.2e}, {SEQ[3]:.3}")


############ Task 3 #################
print("\nTask 3")
def formatter(in_tuple):
    '''format a tuple into a string'''
    length = len(in_tuple)
    form_string = "the {} numbers are: ".format(length)+",".join(["{:d}"]*length).format(*in_tuple)
    return form_string

TUPLE = (2, 3, 5, 6)
print(formatter(TUPLE))


############ Task 4 #################
print("\nTask 4")
SEQ1 = (4, 30, 2017, 2, 27)
print("{:0>2d} {:d} {:d} {:0>2d} {:d}".format(SEQ1[3], SEQ1[4], SEQ1[2], SEQ1[0], SEQ1[1]))


############ Task 5 #################
print("\nTask 5")
SEQ2 = ['orange', 1.3, 'lemons', 1.1]
FRUIT1 = SEQ2[0]
WEIGHT1 = SEQ2[1]
FRUIT2 = SEQ2[2]
WEIGHT2 = SEQ2[3]
print(f"The weight of an {FRUIT1} is {WEIGHT1} and the weight of a {FRUIT2} is {WEIGHT2}")


############ Task 6 #################
print("\nTask 6")
TITLE = ('Name', 'Age', 'Cost')
CUST1 = ('Bob', 30, 1000)
CUST2 = ('Susan', 45, 100)
print("{:>8} {:>8} {:>8}".format(*TITLE))
print("{:>8} {:>8} {:>8.2f}".format(*CUST1))
print("{:>8} {:>8} {:>8.2f}".format(*CUST2))

# Extra Task
print("\nExtra Task")
print("".join(["{:^5}"] * 10).format(*range(1, 11)))
