#!/usr/bin/env python3

import random
import string

def read_book(filename):
    text = []
    #string.punctuation removes punctuation, found this on stackoverflow, still trying to understand it fully
    translator = str.maketrans('','', string.punctuation) 
    with open(filename) as book:
        for row in book:   
            row = row.strip() #removes carriage lines
            if row.startswith("End of the Project Gutenberg EBook"):
                break    
    #second part of removing punctuation, combine with extend
            text.extend(row.translate(translator).split(' ')) #use extend to add multiple words to list
    return text            
       
      
    for word in text: #capitalize the word "I"
        if word == "i":
            text.append("I")
        else:
            text.append(word)
    return text

def build_trigrams(text):
    trigrams = {}
    for tri in range(len(text)-2):
        pair = (text[tri],text[tri+1]) #create the key from two words
        follower = text[tri+2] #create the value, one word

        if pair in trigrams: #add the key, value to dictionary
            trigrams[pair].append(follower)
        else:
            trigrams[pair] = [follower]
    return trigrams

  
def write_book(trigrams, num):
    t_keys = list(trigrams.keys()) #turn the keys into a list
    start_two = random.choice(t_keys) #pick a random key to start 
    z = random.choice(trigrams[start_two]) #choose a random word
    story = ' '.join(start_two) + ' ' + z

    tri_words = 3
    while tri_words < num:
        start_two = (start_two[1], z) #new trigram - second word of key + value

        if start_two in trigrams:
            z = random.choice(trigrams[start_two])
            story += ' ' + z
            tri_words += 1
        else:
            break
    return story     




if __name__ == "__main__":
    
    filename = input("Please enter the name of the file: ")
    if filename[-4:] == ".txt":
        filename = filename
    else:
        filename = filename+".txt"    

    book = read_book(filename)
    trigrams = build_trigrams(book)
    story = write_book(trigrams,100)
    print(story)

