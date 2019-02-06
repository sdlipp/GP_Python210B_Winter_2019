#!/usr/bin/env python3

import os

from collections import Counter
from pathlib import Path



def main():
    if os.name == 'nt':
        root = Path(r'D:/JRS/Python/UW/Intro_Class/students/jeff_shabani/session04')
        src = Path(r'D:/JRS/Python/UW/Intro_Class/students/jeff_shabani/session04/files_to_copy')
        destination = Path(r'D:/JRS/Python/UW/Intro_Class/students/jeff_shabani/session04/copied_files')
    else:
        root = Path('/Volumes/GASecure/JRS/Python/UW/Intro_Class/students/jeff_shabani/session04')
        src = Path('/Volumes/GASecure/JRS/Python/UW/Intro_Class/students/jeff_shabani/session04/files_to_copy')
        destination = ('/Volumes/GASecure/JRS/Python/UW/Intro_Class/students/jeff_shabani/session04/copied_files')

    def return_full_path_of_all_source_files(source: str):
        for child in source.iterdir():
            print(child)

    return_full_path_of_all_source_files(src)



    def copy_file_to_new_dir(starting: str, target: str):
        cd = os.chdir(starting)
        cd = os.getcwd()

        for item in os.walk(cd):
            for filename in item[2]:
                with open(filename, 'r') as infile, open(f'{target}//{filename}', 'w') as outfile:
                    outfile.write(infile.read())
                    infile.close()
                    outfile.close()

    copy_file_to_new_dir(src, destination)



    def read_students_return_languages(file):
        os.chdir(root)
        acceptable_languages = {'ansible',
                                'bash',
                                'c',
                                'c#',
                                'c++',
                                'db',
                                'erlang',
                                'fortran',
                                'java',
                                'javascript',
                                'lisp',
                                'matlab',
                                'mysql',
                                'perl',
                                'php',
                                'powershell',
                                'python',
                                'r',
                                'ruby',
                                'shell',
                                'sql',
                                'typescript',
                                'vb',
                                'visualbasic',
                                }
        # 1st list containing text to right of ":" and stripped of white space
        languages = []
        # final list of acceptable languages cleaned of extra characters and white space
        cleaned_languages = []

        with open(file, 'rt') as f:
            lines = f.readlines()
            for line in lines:
                # strip leading & trailing spaces
                clean_line = line.strip()
                if clean_line:
                    # split line at ":" and return chars to the right
                    languages.append(clean_line.split(':', 1)[1])

        # list comprehension of languages text split by ','
        split_languages = [i.split(',') for i in languages]

        # strip whitespace from split_language items and append to
        # final list of in acceptable_languages set
        for i in split_languages:
            for k in i:
                if k.strip() in acceptable_languages:
                    cleaned_languages.append(k.strip())

        counts = Counter(cleaned_languages)

        for language, count in sorted(counts.items()):
            print(f'{count} - {language}')

    read_students_return_languages('students.txt')


if __name__ == '__main__':
    main()
