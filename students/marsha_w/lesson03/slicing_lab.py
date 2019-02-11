#!/usr/bin/env python3

'''Title: Slicing lab
Dev: Marsha Wheeler
Date: 01/29/2019
'''

'''Write some functions that take a sequence as an argument, and return a copy of that sequence:
1. with the first and last items exchanged.
2. with every other item removed.
3. with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
4. with the elements reversed (just with slicing).
5. with the last third, then first third, then the middle third in the new order.
'''

def exchangeFirstLastItem(sequence):
    if type(sequence) == str:
        print("Your sequence is a string")
        s2 = sequence[-1] + sequence[1:-1] + sequence[0]
        print(s2)
    elif type(sequence) == list:
        print("Your sequence is a list")
        s2 = sequence[1:-1]
        firstItem = sequence[0]
        lastItem = sequence[-1]
        s2.insert(0,lastItem)
        s2.append(firstItem)
        print(s2)
    elif type(sequence) == tuple:
        print("Your sequence is a tuple and tuples are immutable")


def everyOtherItemRemoved(sequence):
    print(sequence[0::2])

def fourItemsRemoved(sequence):
    print(sequence[4:-4:2])


def reverseItems(sequence):
    print(sequence[::-1])

def orderThirds(sequence):
    oneThird = int(len(sequence)/3)
    print(oneThird)
    firstThird = (sequence[0:oneThird])
    lastThird = (sequence[-oneThird:])
    middleThird = (sequence[oneThird:-oneThird])
    s2 = lastThird + firstThird + middleThird
    print(s2)



#testing functions
s = "a bunch of words"
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)


exchangeFirstLastItem(s)
exchangeFirstLastItem(l)
exchangeFirstLastItem(t)

everyOtherItemRemoved(s)
everyOtherItemRemoved(l)
everyOtherItemRemoved(t)

fourItemsRemoved(s)
fourItemsRemoved(l)
fourItemsRemoved(t)

reverseItems(s)
reverseItems(l)
reverseItems(t)

orderThirds(s)
orderThirds(l)
orderThirds(t)




