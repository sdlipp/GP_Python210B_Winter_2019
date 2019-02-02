'''
##########################
#Python 210
#Session 03 - Slicing Lab
#Elaine Xu
#Jan 28,2019
###########################
'''

#Write some functions that take a sequence as an argument, and return a copy of that sequence:

#with the first and last items exchanged.
def exchange_first_last(seq):
    '''exchange the first and last items'''
    first = seq[len(seq)-1:len(seq)]
    mid = seq[1:len(seq)-1]
    last = seq[0:1]
    return first+mid+last

#with every other item removed.
def remove_every_other(seq):
    '''remove every other item'''
    return seq[::2]

#with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
def remove_4_every_other(seq):
    '''remove the first 4 and last 4, the nevery other item'''
    seq1 = seq[4:-4]
    seq2 = seq1[::2]
    return seq2

#with the elements reversed (just with slicing).
def reverse_element(seq):
    '''reverse the elements'''
    return seq[::-1]

#with the last third, then first third, then the middle third in the new order.
def last_first_mid(seq):
    '''with the last third, then first third, then the middle third in the new order'''
    mid_seq = len(seq)//2
    return seq[-3:]+seq[:3]+seq[mid_seq-1:mid_seq+2]

#tests
A_STRING = "this is a string"
A_TUPLE = (2, 54, 13, 12, 5, 32)
B_TUPLE = (2, 54, 13, 12, 5, 32, 2, 5, 17, 37, 23, 14)
assert exchange_first_last(A_STRING) == "ghis is a strint"
assert exchange_first_last(A_TUPLE) == (32, 54, 13, 12, 5, 2)

assert remove_every_other(A_STRING) == "ti sasrn"
assert remove_every_other(A_TUPLE) == (2, 13, 5)

assert remove_4_every_other(A_STRING) == " sas"
assert remove_4_every_other(B_TUPLE) == (5, 2)

assert reverse_element(A_STRING) == "gnirts a si siht"
assert reverse_element(A_TUPLE) == (32, 5, 12, 13, 54, 2)

assert last_first_mid(A_STRING) == "ingthi a "
assert last_first_mid(A_TUPLE) == (12, 5, 32, 2, 54, 13, 13, 12, 5)

print("test completed")
