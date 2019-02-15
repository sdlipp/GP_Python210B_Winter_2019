#!/usr/bin/env python3

import random
import string

def clean_words(terms):
#remove all the punctuation to make it easier to create a list of words
#found this on stackoverflow, still trying to understand it
    table = {}
    if terms not in string.punctuation:
        table[terms]
    terms = terms.lower() 
    words = terms.split()   
    words2 = []    
    for word in words: #capitalize the word "I"
        if word == "i":
            words2.append("I")
        else:
            words2.append(word)
    return words2

def read_book(filename):
    start = "*** START OF THIS PROJECT GUTENBERG EBOOK"
    with open(filename, 'r') as f:
        for num, l in enumerate(f, 1):
            if start in l:
                f.readline()
        text = []
        #read the rest of the file line by line
        for row in f:   
            if row.startswith("End of the Project Gutenberg EBook"):
                break
            else:        
                text.append(line)
       


def build_trigrams(words):
    trigrams = {}
    for tri in range(len(words)-2):
        pair = tuple(words[tri:tri+2])
        follower = words[tri+2]
        if pair in trigrams:
            trigrams[pair].append(follower)
        else:
            trigrams[pair] = [follower]
    return trigrams

  
def write_book(trigrams):
    new_book = []
    for x in range(15): #testing with 15 sentences, add more if needed
        sentence = list(random.choice(list(trigrams.keys())))
    for y in range(random.randint(2,20)):
        last_two = tuple(sentence[-2:]) #last two words create next key
        sentence.append(random.choice(trigrams[last_two]))
    
    return " ".join(new_book) 


if __name__ == "__main__":
    
    filename = input("Please enter the name of the file: ")
    if filename[-4:] == ".txt":
        filename = filename
    else:
        filename = filename+".txt"    

    book = read_book(filename)
    words = clean_words(book)
    trigrams = build_trigrams(words)
    new_book = write_book(trigrams)
    print(new_book)

