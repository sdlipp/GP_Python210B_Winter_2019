#!/usr/bin/env python3

#series 1

FRUIT_LIST = ['Apples', 'Pears', 'Oranges', 'Peaches']

#print(FRUIT_LIST)

def series_one(flist):
    answer = input('What fruit to you want to add?')
    flist.append(answer)
    print(flist)
    ind_answer = int(input(f'Please enter a number between 1 and {len(flist)}'))
    print(flist[ind_answer-1])
    #add new fruit begging of list
    flist=['Pineapple']+flist
    print(flist)
    flist.insert(0, 'Tomato')
    print(flist)
    for i in flist:
        if i[0] == 'P':
            print(i)

def series_two(flist):
    #includes bonus
    print(flist)
    flist.pop()
    print(flist)
    delete_answer = input('Select a fruit to delete')
    flist = flist *2
    while delete_answer not in flist:
        delete_answer = input('Please select another fruit')
    else:
        for i in flist:
            if i == delete_answer:
                flist.remove(i)
    print(flist)


def series_three(flist):
    acceptable_answers = {'yes', 'no'}
    result = []
    for i in flist:
        answer = input(f'Do you like {i}?')
        while answer.lower() not in acceptable_answers:
            answer = input(f'Please answer yes or no: Do you like {i}?')
        if answer.lower() != 'no':
            result.append(i)
    print(result)

if __name__ == '__main__':
    #series_one(FRUIT_LIST)
    #series_two(FRUIT_LIST)
    series_three(FRUIT_LIST)




