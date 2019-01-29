#!/usr/bin/env python3

#series 1

FRUIT_LIST = ['Apples', 'Pears', 'Oranges', 'Peaches']

print(FRUIT_LIST)

def series_one(x):
    answer = input('What fruit to you want to add?')
    x.append(answer)
    print(x)
    ind_answer = int(input('Please enter a number'))
    print(x[ind_answer-1])
    #add new fruit begging of list
    x=['Pineapple']+x
    print(x)
    x.insert(0, 'Tomato')
    print(x)
    for i in x:
        if i[0] == 'P':
            print(i)




series_one(FRUIT_LIST)




