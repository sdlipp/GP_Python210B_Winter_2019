
'''
##########################
#Python 210
#Session 04 - Trigrams
#Elaine Xu
#Feb 9,2019
###########################
'''
import random
import string

def read_in_data(filename):
    '''read the input text'''
    with open(filename, 'r') as f_input:
        #Look for start and stop point - row numbers of "*** '
        row_index = []
        for j, line in enumerate(f_input):
            if line[0:4] == '*** ':
                row_index.append(j)
        #Read data
        f_input.seek(0)
        data_list = f_input.readlines()[row_index[0]+1:row_index[1]]
        in_data = " ".join(data_list)
    return in_data


def make_words(in_data):
    '''breaking text into a list of words, remove capitalization and punctuation'''
    words = in_data.split()
    #remove capitalization
    proper_nouns_list = create_proper_nouns(words)
    words_no_cap = []
    for word in words:
        if word.islower():
            words_no_cap.append(word)
        elif word[0] + word[1:].lower() in proper_nouns_list:
            words_no_cap.append(word[0]+word[1:].lower())
        else:
            words_no_cap.append(word.lower())
    #strips punctuation
    words_no_punct = []
    for word in words_no_cap:
        words_no_punct.append(strip_punctuation(word))
    return words_no_punct


def create_proper_nouns(words):
    '''create a list of proper nouns that keep capitalization'''
    proper_nouns = ['I']
    for i, word in enumerate(words):
        if word[0].isupper() and word[1:].islower():
            # if word is not the first word of a sentence
            if i > 1 and words[i - 1][-1] not in string.punctuation:
                proper_nouns.append(word)
    return proper_nouns


def strip_punctuation(word):
    '''check every word for punctuation and strip them out'''
    word_no_punct = ''
    for i, letter in enumerate(word):
        # if letter -> keep, if punct is sandwiched between letters -> keep
        if letter not in string.punctuation or \
                (i in range(1, len(word)-1) and word[i-1] not in string.punctuation
                 and word[i+1] not in string.punctuation):
            word_no_punct += letter
    return word_no_punct


def build_trigrams(words):
    """
    build up the trigrams dict from the list of words
    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}
    for i in range(len(words)-2):
        key_pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        if key_pair not in trigrams:
            trigrams[key_pair] = [follower]
        else:
            trigrams[key_pair] += [follower]
    #print(trigrams)
    return trigrams


def build_text(word_pairs, words):
    '''adding words to new text'''
    key_text = (words[0], words[1])
    new_text = list(key_text)
    word_count = 0
    while True:
        key_text = tuple(new_text[-2:])
        if word_count > 1000:
            #terminates when total word count exceeds 1000
            break
        elif key_text in word_pairs:
            new_text += [random.choice(word_pairs[key_text])]
            word_count += 1
        else:
            #terminates when key_text is not a part of trigrams key
            break
    #print(new_text)
    return new_text


def post_process(new_text):
    '''write trigrams into a text file'''
    with open('trigrams_output.txt', 'w') as f_output:
        line = new_text[0]
        #write to a txt that has 65 characters in one line
        for word in new_text[1:]:
            if len(word)+len(line)+1 <= 65:
                line = line + ' ' + word
            else:
                line += '\n'
                f_output.write(line)
                line = word
        f_output.write(line)


##########################################################################
if __name__ == "__main__":
    #text_file = 'sherlock_small.txt'
    text_file = 'sherlock.txt'
    data_str = read_in_data(text_file)
    words_lst = make_words(data_str)
    word_pairs_dict = build_trigrams(words_lst)
    new_text_lst = build_text(word_pairs_dict, words_lst)
    post_process(new_text_lst)
