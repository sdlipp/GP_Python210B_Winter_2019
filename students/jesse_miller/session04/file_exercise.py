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
#    for k,v in open('students.txt'):
#        students[k].append(v)
    with open('students.txt', 'r') as f:
        for line in f:
            if ":" in line:
                splitLine = line.split(":")
                students[str(splitLine[0])]= " ".join(splitLine[1:])
            else:
                students[k].append(line.rstrip())


#    del students["Name:"]
    print_file(students)


def print_file(students):
    """
    This will print the file in a formatted manner
    """
    summary = []
    not_nickname = ('c', 'perl', 'java', 'erlang', 'python', 'c#', 'c++', \
    'ansible', 'powershell', 'fortran', 'shell', 'matlab', 'bash', 'r', 'php', \
    'mysql', 'db', 'rex', 'Gene')
    for k, v in students.items():
        name = k, v[0].split()
        languages = v
        summary.append([name, languages])
        print("-"*80)
        print("{:18} | {}".format(k, v))

    print("-"*80)


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
