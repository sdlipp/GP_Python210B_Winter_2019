#!/usr/bin/env python3


def word_list_generator(file_location):
    """
    Return a sequence of words, stripped of punctuation & capitalization, taken from a source file.
    :param file_location: a relative or absolute address to use as source of plain text
    :return: a sequence of individual or compound words
    """
    with open(file_location) as file:
        original_words = file.read().split()
    edited_words = []
    replaced_chars = ""
    replacement_chars = ""
    deleted_chars = ".,[]();'!?:<>*^"
    for word in original_words:
        table = word.maketrans(replaced_chars, replacement_chars, deleted_chars)
        edited_words.append(word.translate(table).lower())
    return edited_words


def trigram_dict_generator(word_list):
    """
    Return a dictionary containing 2-word keys and single word corresponding values.
    :param word_list: a sequence of individual words
    :return: a dictionary containing 2-element tuples and single string values
    """
    trigram_dict = {}
    for word in enumerate(word_list):
        if word[0] < len(word_list) - 3:
            new_key = (word[1], word_list[word[0] + 1])
            if new_key in trigram_dict:
                trigram_dict[new_key].append(word_list[word[0] + 2])
            else:
                trigram_dict[new_key] = [word_list[word[0] + 2]]
    return trigram_dict


def dict_key_pair(word_dict):
    """
    Generate an index-able dictionary to aid with random key generation in another function.
    :param word_dict: a dictionary containing 2-word keys and single word corresponding values
    :return: a dictionary containing an integer key and 2-element tuple
    """
    number_dict = {}
    intCounter = 0
    for item in word_dict:
        number_dict[intCounter] = item
        intCounter += 1
    return number_dict


def first_key_generator(number_dict):
    """
    Generate the first, random 2-word tuple that will be the starting key in the Trigrams sequence.
    :param number_dict: a dictionary with integer keys and 2-element tuple
    :return: a 2-element tuple which is the key for another dictionary
    """
    import random
    return number_dict[random.randint(0, (len(number_dict) - 1))]


def next_word_generator(word_dict, key, length_limit=10, list_words=None):
    """
    A recursive function that propagates a sequence of words until a length condition is met.
    :param word_dict: dictionary containing 2-element tuple as key and single string as value
    :param key: the specific 2-element tuple that will be used to search the dictionary
    :param length_limit: the word limit that will terminate the function
    :param list_words: the growing sequence of words that results from the Trigrams algorithm
    :return: ultimate solution: the full length of words that will comprise the Trigrams output
    """
    import random
    if list_words is None:
        list_words = []
        for word in key:
            list_words.append(word)
    if len(list_words) > length_limit:
        return list_words
    elif key not in word_dict:
        return list_words
    else:
        list_words.append(word_dict[key][random.randint(0, len(word_dict[key]) - 1)])
        new_key = (list_words[-2], list_words[-1])
        return next_word_generator(word_dict, new_key, length_limit, list_words)


def punctuation_editor(word_list):
    """
    Insert random punctuation and associated capitalization to enhance readability.
    :param word_list: a list of individual, lower-case words produced by the Trigrams algorithm
    :return: a modified version of the word list with punctuation and capitalization
    """
    import random
    edited_list = []
    for word in enumerate(word_list):
        punct_generator = random.randint(1, 1000)
        if word[0] == 0:
            edited_list.append(str(word[1]).capitalize())
        elif word[1] == "i":
            edited_list.append((word[1]).capitalize())
        elif edited_list[word[0] - 1][-1] in (".", "!", "?"):
            edited_list.append(str(word[1]).capitalize())
        elif punct_generator % 495 == 0:
            edited_list.append(word[1] + "?")
        elif punct_generator % 195 == 0:
            edited_list.append(word[1] + "!")
        elif punct_generator % 25 == 0:
            edited_list.append(word[1] + ".")
        elif punct_generator % 9 == 0:
            edited_list.append(word[1] + ",")
        else:
            edited_list.append(word[1])
    return edited_list


def main_program():
    """
    Get user input on file location to use as source text and catch any errors.
    Organize sequence of function calls to execute Trigrams algorithm and print output.
    """
    user_input = input("\nEnter the file name/location of the desired source text: \n\t")
    try:
        words_from_file = word_list_generator(user_input)
        trigram_dict = trigram_dict_generator(words_from_file)
        numerical_dict = dict_key_pair(trigram_dict)
        first_key = first_key_generator(numerical_dict)
        list_words = next_word_generator(trigram_dict, first_key, 200)
        modified_words = punctuation_editor(list_words)
        print("")
        for word in modified_words:
            print(word, end=" ")
    except FileNotFoundError:
        print("File name/location was not found. Please try again.")
    except Exception as e:
        print("The following error was encountered: ", e)


if __name__ == '__main__':
    main_program()

