"""
Completes the file exercise from lesson 4
"""
import string
from collections import Counter

def parse_file(filename):
    """
    Parses the file and returns a single list of words
    """
    word_list = []
    translator = str.maketrans('', '', string.punctuation)
    with open(filename) as input_file:
        for line in input_file:
            # Remove carriage return
            line = line.rstrip()
            # Remove punctuation and add to full list
            word_list.extend(line.translate(translator).split(' '))
    return word_list

def remove_name_and_nickname(word_list):
    """
    Removes names and nicknames
    """
    new_list = []
    for word in word_list:
        try:
            if not word[0].isupper():
                new_list.append(word)
        except:
            continue
    return new_list

def main():
    """
    Main program flow
    """
    word_list = parse_file('students.txt')
    word_list = remove_name_and_nickname(word_list)
    unique_list = set(word_list)
    for language in unique_list:
        print(language)
    language_users = Counter(word_list)
    for language, users in language_users.items():
        print(f"{language} has {users} users")

if __name__ == "__main__":
    main()
