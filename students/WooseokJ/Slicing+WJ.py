
# coding: utf-8

# In[2]:


# slicing with the first and last items exchanged of the list
#first isolate the first and last and add them the a list where both of them are removed
#in reverse order
def exchange_first_last(sequence):

    first = sequence[:1]
    last = sequence[-1:]
    middle = sequence[1:-1]
    newsequence1 = last + middle + first
    return newsequence1

#this just simply removes everyother element in the sequence
def remove_every_other(sequence):

    newsequence2 = sequence[::2]
    return newsequence2

#This removes the first 4 and the last 4  and every other element in the squence
def first_last_four(sequence):

    return sequence[4:-4:2]
#this is sequence just reversed
def elements_reversed(sequence):

    newsequence3 = sequence[::-1]
    return newsequence3

#more the to the first sequence removes last third, then first third, then the middle third
def in_thirds(sequence):

    midsequence = len(sequence)//2
    return sequence[-3:]+sequence[:3]+sequence[midsequence-1:midsequence+2]


##Performes a test that tests each of the slicings 
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert remove_every_other(a_string) == "ti sasrn"
assert first_last_four(a_string) == " sas"
assert elements_reversed(a_string) == "gnirts a si siht"
assert in_thirds(a_string) == "ingthi a "
print("test complete")

