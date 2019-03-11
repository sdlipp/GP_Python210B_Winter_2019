

#-----------------------------
#!/usr/bin/env python3

# Lesson 04 Exercise: Trigrams

# Shirin Akther
#----------------------------

 
import sys 

import random



def words_from_file(filename):
    
    """ This function takes  a filename, opens that file, read each line and returns it as 

        a list of words.

    """


    with open(filename, 'r') as textfile: 

        return [word.strip('\n') for l in textfile.readlines() 

                for word in l.split(' ')] 




 
def build_trigrams_dict(words):

    """ This function takes a list of strings and create a dictionary where 

        a key of two consecutive strings in the list and the value is a list of 

        all possible strings that come after the key in the original list."""

    trigrams = {}
    
    for i, w in enumerate(words): 

        if i + 2 < len(words): 

            one = w.strip() 

            two = words[i + 1].strip() 
            three = words[i + 2].strip() 
            onetwo = '{} {}'.format(one, two) 

            if onetwo not in trigrams.keys(): 

                trigrams[onetwo] = [] 

            trigrams[onetwo].append(three) 

    return trigrams 




 
def build_text(trigrams, num, new_words=[]):
    
    """This function creates a new text that randomly select a key from trigram_dictionary,
       that will be the beginning of next text."""
        

    if len(new_words) >= int(num) or int(num) < 3: 

        return ' '.join(new_words) 


    if not new_words: 

        starting_two = random.choice(list(trigrams.keys())) 

        new_words.extend(starting_two.split(' ')) 

    if len(new_words) > 1: 
        onetwo = '{} {}'.format(new_words[-2], new_words[-1])
        
        
#If the new key isn't in the trigram dict it will start again with a
# randomly chosen key.

        if onetwo not in trigrams.keys(): 
            onetwo = random.choice(list(trigrams.keys()))
            
        three = random.choice(trigrams[onetwo]) 
        new_words.append(three) 

        return build_text(trigrams, num, new_words)
    


  
if __name__ == '__main__':

    #get the file name
    
    filename = input('Please enter a filename:\n--->')
    
        
    new_story_length = 100
        
    words = words_from_file(filename)
      

    trigrams = build_trigrams_dict(words)
      

    new_text = build_text(trigrams, new_story_length)
    
    print (new_text) 


    


      
       
      
      



      

     
     
          
        
           
