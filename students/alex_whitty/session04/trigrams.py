import random
import string
#!/usr/bin/env python3
def parse_file():
    '''
    Takes a hardcoded file name and returns a list of words
    '''
    # Setup a translator to remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    # Setup an empty list to contain the full list of words in the text
    full_list = []
    with open('double_take.txt', 'r') as f:
        for line in f:
            line = line.rstrip('\r\n')
            # This will take each line, remove punctuation and then split it
            # into a list of words and attach this list to the full_list
            # note the use of "extend()" instead of "append()"
            # TODO: Figure out how to remove carriage returns - TASK COMPLETED!
            full_list.extend(line.translate(translator).split(' '))
        return full_list

print(parse_file())

def build_trigrams(words):

    trigrams = {}

    for i in range(len(words) - 2):


        pair = tuple(words[i:i + 2])
        follower = words[i + 2]

        if pair not in trigrams:

            trigrams[pair] = [follower]
        else:
            trigrams[pair].append(follower)


    return trigrams

# build up the dict here!


new_words = {("from", "Outer"): ["space"],
            ("Outer", "Space"): ["dug"],
            ("Space", "dug"): ["into"],
            ("dug", "into"): ["the"],
            ("into", "the"): ["pile"],
            ("When", "the"): ['Travelers'],
            ("the", "Travelers"): ["from"],
            ("Travelers", "from"): ["Outer"],
            }


def build_dict(words):
    while True:
        starter = random.choice(list(words.keys()))
        print(starter)
        # Start the text with the random key
        # now turned into a string
        new_text = ' '.join(starter)

        # Now, pick a random word from the list
        # associated to the key
        key_value = words["from"]
        next_word = random.choice(key_value)

        # Add next_word to new_text
        for item in new_words.keys():
            new_text += 'outer' + next_word
            return item

        print(new_text)



if __name__ == "__main__":
    try:
        filename = [1]
    except NameError:
        print("You must pass in a filename")
        sys.exit(1)


    words = "When the Travelers from outer Space dug into the pile".split()
    parse_file()
    print(words)
    trigrams = build_trigrams(words)
    print(trigrams)

