'''
##########################
#Python 210
#Session 04 - File Exercise
#Elaine Xu
#Feb 5, 2019
###########################
'''
import os

############## Paths and File Processing #####################
#Write a program which prints the full path for all files in the current directory, one per line
for root, dirs, files in os.walk('.'):
    for file in files:
        print(os.path.join(root, file))
    for directory in dirs:
        print(os.path.join(root, dir))

'''
Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy
command). Advanced: make it work for any size file: i.e. don't read the entire contents of the file into memory
at once. This should work for any kind of file, so you need to open the files in binary mode: open(filename, 'rb') 
(or 'wb' for writing). Note that for binary files, you can't use readline() - lines don't have any meaning for 
binary files. Test it with both text and binary files (maybe jpeg or something of your choosing).
'''
with open('students.txt', 'rb') as f1, open('students_copy.txt', 'wb') as f2:
    Text = f1.read()
    f2.write(Text)


############## File reading and parsing #####################
'''
Write a little script that reads that file, and generates a list of all the languages that have been used.
What might be the best data structure to use to keep track of bunch of values without duplication?
'''
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
    lang_list += clean_language_or_nickname

for lang in lang_list:
    if lang and (lang not in lang_dict) and (lang[0].islower()) and (lang != 'nothing'):
        lang_dict[lang] = 1
    elif lang in lang_dict:
        lang_dict[lang] += 1

for key, value in lang_dict.items():
    print(key, ":", value)
