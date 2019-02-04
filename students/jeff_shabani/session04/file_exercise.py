#!/usr/bin/env python3

import collections
import os
import glob
import shutil
import gc
import threading, time
from time import time
from functools import wraps

from pathlib import Path

#get current working directory
cd = Path.cwd()
src = Path(r'D:\JRS\Python\UW\Intro_Class\students\jeff_shabani\session04\files_to_copy')
destination = Path(r'D:\JRS\Python\UW\Intro_Class\students\jeff_shabani\session04\copied_files')

def return_full_path_of_all_source_files(source):
    for child in source.iterdir():
        print(child)

#return_full_path_of_all_source_files(src)

def copy_file_to_new_dir(starting, target):
    for i in os.walk(starting):
        for j in i[2]:
            f = open(j, 'w')
            f.write(f'{os.chdir(target)}+{f}')
            f.close()
    for child in target.iterdir():
        print(child)

copy_file_to_new_dir(src, destination)






