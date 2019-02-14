import sys
import re
import random

def read_in_data(filename):
    f = open(filename)
    lines=[]
    while True:
        line = f.readline()
        if not line:
            break
        lines.append(line.strip('\n'))
    return lines

def make_words(in_data):
    new_data=[]
    for line in in_data:
        line = re.sub(r'[^\w\s]',',',line)
        line = re.sub(r',,',' ',line)
        line = re.sub(r',',' ',line)
        line = re.sub(r'  ',' ',line)
        if line == '':
            pass
        else:
            newline =line.split(' ')
            if newline[-1]=='':
                newline.pop()
                new_data.extend(newline)
            else:
                new_data.extend(newline)


    return new_data


def build_trigram(words):
    dict = {}
    for i in range(len(words)-2):
        trikey = (words[i],words[i+1])
        trivalue = words[i+2]
        group = dict.setdefault(trikey,[])
        group.append(trivalue)
    return dict

def build_text(word_pairs):
    new_text =[]
    randword = random.choice(list(word_pairs.keys()))
    new_text.extend(list(randword))
    while len(new_text) <250:
        randstart = randword
        randend = word_pairs[randstart]=random.choice(list(word_pairs.values()))
        full = (list(randstart)+randend)
        print(full)
        new_text.extend(randend)
        randword = (full[-2],full[-1])
    print(new_text)


if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigram(words)
    new_text = build_text(word_pairs)

    #print(new_text)