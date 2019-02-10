

import os
import pathlib


#Paths and File Processing

#Write a program which prints the full path for all files in the current directory, one per line


print(" Print all files in the current directory : ")
"""for dirname, dirs, files in os.walk('.'):

    for file in files:

        print(os.path.join(dirname, file))

#    for directory in dirs:

#        print(os.path.join(dirname, dir))
"""

directory = ('./')


for filepath in pathlib.Path(directory).glob('**/*'):
    

    print(filepath.absolute())





#Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command).

print ("\nCopies a file from a source, to a destination\n ")

with open('students.txt', 'rb') as f1, open('students_copy.txt', 'wb') as f2:

    Text = f1.read()

    f2.write(Text)


# File reading and parsing 

#Write a little script that reads that file, and generates a list of all the languages that have been used.

#What might be the best data structure to use to keep track of bunch of values without duplication?


print("Display list of all language:")

with open('students.txt', 'r') as f:

    Text2 = f.readlines()[1:]
    
    lang_dict = {}

    lang_list = []

for line in Text2:

    #split name and content

    name, content = line.strip().split(':')
    
  #split content into list

    languages_or_nickname = content.strip().split(',')



    #make a clean copy of langurage or nickname

    clean_language_or_nickname = []

    for item in languages_or_nickname:

        clean_language_or_nickname.append(item.strip())

    #print(clean_language_or_nickname) #for testing



    #combine into one list
        

    lang_list = lang_list + clean_language_or_nickname



for lang in lang_list:

    if lang and (lang not in lang_dict) and (lang[0].islower()) and (lang != 'nothing'):

        lang_dict[lang] = 1

    elif lang in lang_dict:

        lang_dict[lang] += 1



for key, value in lang_dict.items():

    print(key, ":", value)




    
