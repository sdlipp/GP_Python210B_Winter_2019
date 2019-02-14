#!/usr/bin/env python3

import random

def build_trigrams(words):
    trigrams = {}
    for tri in range(len(words)-2):
        pair = tuple(words[tri:tri+2])
        next = words[tri+2]
        if pair in trigrams:
            trigrams[pair].append(next)
        else:
            trigrams[pair] = [next]
    return trigrams



def clean_words(term):
#remove all the punctuation to make it easier to create a list of words
    remove_punc = [('"', ''),
                    ('.', ''),
                    (',', ''),
                    ('-',''),
                    ('?',''),
                    ('!', '')]  
    replace_word = {}                
    for mark, blank in remove_punc: #removes punctuation
        replace_word[mark] = blank
    term = term.lower() #lowercase for uniformity
    words = term.split() #split string into list
    words2 = []    
    for word in words: #capitalize the word "I"
        if word == "i":
            words2.append("I")
        else:
            words2.append(word)
    return words2    










    return trigrams

if __name__ == "__main__":
    trigrams = build_trigrams(words)
    print(trigrams)

