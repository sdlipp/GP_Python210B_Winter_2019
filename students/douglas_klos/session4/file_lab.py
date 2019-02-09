#!/usr/bin/env python3

# Douglas Klos
# January 29th, 2019
# Python 210, Activity 4
# file_lab.py

import io
import os


def psuedo_file():
    """ Opens a string as a file for testing """

    file1 = io.StringIO()
    file1.write('test string')
    file1.seek(0)
    print(file1.read())
    print(file1.getvalue())
    file1.close()

    print(os.listdir('.'))


def students_file():
    """ Parse students.txt file """

    d1 = {} 

    with open('students.txt', 'r') as file2:
        next(file2)
        for line in file2.readlines():
            for word in line.replace(',', '').strip('\n').split(' '):
                if not (word == '' or word[0] == word[0].upper() or word == ' '):
                    if word in d1:
                        d1[word] += 1
                    else:
                        d1[word] = 1    

    for key in d1:
        print(f'{key} = {d1[key]}')
    

def main():
    #psuedo_file()
    students_file()


if __name__ == '__main__':
    main()
