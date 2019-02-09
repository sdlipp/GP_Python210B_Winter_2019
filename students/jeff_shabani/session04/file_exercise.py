#!/usr/bin/env python3

import os

from collections import Counter


def main():
    root = os.getcwd()
    src = f'{root}/files_to_copy'
    destination = f"{root}/copied_files"

    def return_full_path_of_all_source_files(source: str):
        for name in os.listdir(src):
            path = os.path.join(src, name)
            if os.path.isfile(path):
                print(path)

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

    def read_students_return_languages(text_file):
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

        with open(text_file, 'rt') as f:
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
