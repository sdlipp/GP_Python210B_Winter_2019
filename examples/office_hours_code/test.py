import string
import random

def parse_file(filename):
    full_list = []
    translator = str.maketrans('', '', string.punctuation)
    with open(filename) as input_file:
        for line in input_file:
            line = line.rstrip()
            full_list.extend(line.translate(translator).split(' '))
    return full_list

def build_trigram(full_list):
    trigams = {}
    for i in range(0, len(full_list) - 2):
        trigram_key = (full_list[i], full_list[i+1])
        trigram_value = full_list[i+2]
        if trigram_key in trigams:
            trigams[trigram_key].append(trigram_value)
        else:
            trigams[trigram_key] = [trigram_value]
    return trigams

def build_text(trigrams, word_target):
    next_key = random.choice(list(trigrams.keys()))
    word_list = trigrams[next_key]
    word = random.choice(word_list)
    output_text = ' '.join(next_key) + ' ' + word

    word_count = 3

    while word_count < word_target:
        next_key = (next_key[1], word)

        if next_key in trigrams:
            word_list = trigrams[next_key]
            word = random.choice(word_list)
            output_text += ' ' + word
            word_count += 1
        else:
            break

    return output_text

def main():
    words = parse_file("sherlock.txt")
    trigrams = build_trigram(words)
    #for key, value in trigrams.items():
    #    if len(value) > 1:
    #        print(f"Key:{key}, value:{value}")
    output_text = build_text(trigrams, 300)
    print(output_text)


if __name__ == "__main__":
    main()