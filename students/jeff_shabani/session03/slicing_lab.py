"""
All the functions below return a new iterable from the iterable
entered as the argument
"""


def switch_first_last(x):
    """Moves 1st item to end and last item to beginning
    of the iterable
    """
    result = [x[-1]]
    for k in x[1:-2]:
        result.append(k)
    result.append(x[0])
    return result


def remove_every_other(x):
    """Returns every other item from x"""
    return x[::2]


def get_middle(x):
    """Removes 1st and last 4 items from x and
    return every other item of remaining sequence
    """
    return x[5:-5:2]


def rev_it(x):
    """returns x reversed"""
    return x[::-1]


def thirds(x):
    """returns last 3rd, then 1st 3rd, then middle third of reversed x"""
    result = []
    for i in x[::-1][-5:]:
        result.append(i)
    for i in x[::-1][:5]:
        result.append(i)
    for i in x[::-1][5:-5]:
        result.append(i)

    return result


if __name__ == '__main__':
    TEST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert switch_first_last(TEST) == [15, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]
    assert remove_every_other(TEST) == [1, 3, 5, 7, 9, 11, 13, 15]
    assert get_middle(TEST) == [6, 8, 10]
    assert rev_it(TEST) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert thirds(TEST) == [5, 4, 3, 2, 1, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]

    print('Passed!')
