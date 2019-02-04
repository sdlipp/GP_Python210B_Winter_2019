#!/usr/local/bin/python3
"""
Starting the file exercise
"""
import sys
import pathlib


def dir_list():
    """
    Lists a hard coded dir.
    """
    directory = ('/Users/junya/Python/GP_Python210B_Winter_2019/students/'
                 'jesse_miller/session04/')
    for filepath in pathlib.Path(directory).glob('**/*'):
        print(filepath.absolute())


def read_file():
    """
    Should read the file...
    """
    students = {}
    with open('students.txt') as f:
        students = dict(x.rstrip().split(None, 1) for x in f)
        print(students)


def goodbye():
    '''
    Gracefully exits
    '''
    print("Goodbye!")
    sys.exit()


def main():
    '''
    The man menu and the calls to other functions
    '''
    print("Section 1 of File Lab \n")
    print("Listing directory:")
    dir_list()
    print("\n")
    print("Reading the students file. \n \n")
    read_file()
    goodbye()


if __name__ == "__main__":
    main()
