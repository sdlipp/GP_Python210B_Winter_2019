#!/usr/bin/env python3


FRUIT_LIST = ['Apples', 'Pears', 'Oranges', 'Peaches']


def series_one(iterable):
    print(iterable)
    answer = str(input('What fruit to you want to add?'))
    iterable.append(answer)
    print(iterable)
    index_answer = int(input(f'Please enter a number between 1 and {len(iterable)}'))
    print(iterable[index_answer - 1])
    # add new fruit begging of list
    iterable = ['Pineapple'] + iterable
    print(iterable)
    iterable.insert(0, 'Tomato')
    print(iterable)
    for i in iterable:
        if i[0] == 'P':
            print(i)


def series_two(iterable):
    # includes bonus
    print(iterable)
    iterable.pop()
    print(iterable)
    delete_answer = input('Select a fruit to delete')
    iterable = iterable * 2
    while delete_answer not in iterable:
        delete_answer = input('Please select another fruit')
    else:
        for i in iterable:
            if i == delete_answer:
                iterable.remove(i)
    print(iterable)


def series_three(iterable):
    acceptable_answers = {'yes', 'no'}
    result = []
    for i in iterable:
        answer = input(f'Do you like {i}?')
        while answer.lower() not in acceptable_answers:
            answer = input(f'Please answer yes or no: Do you like {i}?')
        if answer.lower() != 'no':
            result.append(i)
    print(result)


def series_four(iterable):
    result = []
    for i in iterable:
        result.append(i[::-1])
    iterable.pop()
    print(f'Copy of original with letters of each item reversed: {result}')
    print(f'Original with last item removed: {iterable}')


if __name__ == '__main__':
    series_one(FRUIT_LIST)
    # series_two(FRUIT_LIST)
    # series_three(FRUIT_LIST)
    # series_four(FRUIT_LIST)
