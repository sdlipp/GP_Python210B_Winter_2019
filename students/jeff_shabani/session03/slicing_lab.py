def switch_first_last(x):
    result = [x[-1]]
    for k in x[1:-2]:
        result.append(k)
    result.append(x[0])
    return result


def remove_every_other(x):
    return x[::2]


def get_middle(x):
    return x[5:-5:2]


def rev_it(x):
    return x[::-1]


def thirds(x):
    result = []
    for i in x[::-1][-5:]:
        result.append(i)
    for i in x[::-1][:5]:
        result.append(i)
    for i in x[::-1][5:-5]:
        result.append(i)

    return result


if __name__ == '__main__':
    test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert switch_first_last(test) == [15, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]
    assert remove_every_other(test) == [1, 3, 5, 7, 9, 11, 13, 15]
    assert get_middle(test) == [6, 8, 10]
    assert rev_it(test) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert thirds(test) == [5, 4, 3, 2, 1, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]

    print('Passed!')
