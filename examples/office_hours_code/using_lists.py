'''
This file includes a few examples on using lists in Python
'''
from random import choice
from collections import Counter

def select_student(student_list):
    '''
    Randomly selects a student from a list
    '''
    return choice(student_list)

def validate_votes(voting_results, valid_values):
    '''
    Checks that all values in the list are valid
    '''
    for vote in voting_results:
        if vote not in valid_values:
            print('ERROR: Invalid vote value: {0}'.format(vote))
            voting_results.remove(vote)
    return voting_results

def count_votes(voting_results):
    '''
    Counts votes and returns the results
    '''
    results = Counter(voting_results)
    for value, total_votes in results.items():
        print('{0} obtained a total of {1} votes'.format(value, total_votes))


# Some variables to use in the examples
GP_STUDENT_LIST = ['Shirin', 'Begum', 'Anthony', 'Daniel', 'Marisa', 'Paul', 'Wooseok', 'Douglas',
                   'Scott', 'Brick', 'Jesse', 'Jeremy', 'Eric', 'Gina', 'Jeff', 'Marsha', 'Alex',
                   'Elaine', 'Xuan']

VALID_VOTE_VALUES = [1, 2, 4, 8]
STORY_POINT_VOTES = [2, 2, 4, 8, 2, 1, 4, 8, 2, 1, 1, 4, 6, 2, 3, 4, 4, 5]



def main():
    '''
    Our main execution function
    '''
    #print(select_student(GP_STUDENT_LIST))
    print(STORY_POINT_VOTES)
    validate_votes(STORY_POINT_VOTES, VALID_VOTE_VALUES)
    print(STORY_POINT_VOTES)
    count_votes(STORY_POINT_VOTES)

if __name__ == '__main__':
    main()
