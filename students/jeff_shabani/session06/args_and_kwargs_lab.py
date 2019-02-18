#!/usr/bin/env python3

"""
this is the 1st function for the first part
of the args & kwargs lab
"""


def colors(fore_color='white', back_color='black', link_color='green', visited_color='blue'):
    return fore_color, back_color, link_color, visited_color


"""
this is the 2nd function for the first part 
of the args & kwargs lab
"""


def colors_two(*args, **kwargs):
    if args:
        if not kwargs:
            return (args)
        else:
            return (args, kwargs)
    else:
        return (kwargs)


if __name__ == '__main__':
    colors()
    colors_two()
