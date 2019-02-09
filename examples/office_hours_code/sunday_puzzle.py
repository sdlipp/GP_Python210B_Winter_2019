'''
From: https://www.npr.org/2019/01/20/686968039/sunday-puzzle-youre-halfway-there
This week's challenge: This challenge comes from listener Steve Baggish of Arlington, Mass.
Take the name of a classic song that became the signature song of the artist who performed it.
It has two words; five letters in the first, three letters in the second. The letters can be
rearranged to spell two new words. One is a feeling. The other is an expression of that feeling.
What song is it?
'''

def open_song_list(song_list_file):
    '''
    Opens a file containing song names and returns a list
    '''
    with open(song_list_file) as text_file:
        song_list = text_file.read().splitlines()
    return song_list

def find_candidates(song_list):
    '''
    Splits each song in the list into a list of words.
    Checks if the song has two words and if they
    are the right size.
    Returns a list of candidate songs
    '''
    candidate_list = []
    for song in song_list:
        song_words = song.split(' ')
        if (len(song_words) == 2)and(len(song_words[0]) == 5)and(len(song_words[1]) == 3):
            candidate_list.append(song)
    return candidate_list

def main():
    '''
    Our main execution function
    '''
    song_file = 'signature_song.txt'
    top_song_list = open_song_list(song_file)
    candidate_songs = find_candidates(top_song_list)
    print(candidate_songs)

if __name__ == '__main__':
    main()
