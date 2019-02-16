"""  Slicing Lab """


first_last_list = [0, 1, 2, 3, 4, 5, 6, 7]

def exchange_first_last(input_list):
    new_list = input_list[-1:8] + input_list[1:7] + input_list[:1]
    return new_list


print(exchange_first_last(first_last_list))



my_str = "a tuple is immutable"

def every_other(input_str):
    new_str = input_str[::2]
    return new_str


print(every_other(my_str))



my_str = "a tuple is immutable"

def first_four_last_four(input_str):
    new_str = input_str[4:-4:2]
    return new_str


print(first_four_last_four(my_str))



rev_list = [0, 1, 2, 3, 4, 5, 6, 7]

def elements_rev(input_list):
    new_list = input_list[::-1]
    return new_list


print(elements_rev(rev_list))


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def first_third_last_third(input_list):
    new_list = input_list[6:] + my_list[:3] + my_list[3:6]
    return new_list


print(first_third_last_third(my_list))


if __name__ == "__main__":
    # run some tests
    assert exchange_first_last(first_last_list) == [7, 1, 2, 3, 4, 5, 6, 0]
    assert every_other(my_str) == "atpei mual"
    assert first_four_last_four(my_str) == "pei mu"
    assert elements_rev(rev_list) == [7, 6, 5, 4, 3, 2, 1, 0]
    assert first_third_last_third(my_list) == [6, 7, 8, 0, 1, 2, 3, 4, 5]

    print("test passed")
