#!/usr/bin/env python3

import os
import shelve

from pathlib import Path

#get current working directory
cd = Path.cwd()

if os.name == 'nt':
    src = Path(r'D:/JRS/Python/UW/Intro_Class/students/jeff_shabani/session04/files_to_copy')
    destination = Path(r'D:/JRS/Python/UW/Intro_Class/students/jeff_shabani/session04/copied_files')
else:
    src = Path('/Volumes/GASecure/JRS/Python/UW/Intro_Class/students/jeff_shabani/session04/files_to_copy')
    destination = ('/Volumes/GASecure/JRS/Python/UW/Intro_Class/students/jeff_shabani/session04/copied_files')

def return_full_path_of_all_source_files(source):
    for child in source.iterdir():
        print(child)

#return_full_path_of_all_source_files(src)

def copy_file_to_new_dir(starting, target):
    cd = os.chdir(starting)
    cd = os.getcwd()
    for item in os.walk(cd):
        for filename in item[2]:
            with open(filename, 'r') as infile, open (f'{target}//{filename}', 'w') as outfile:
                outfile.write(infile.read())
                infile.close()
                outfile.close()

copy_file_to_new_dir(src, destination)






