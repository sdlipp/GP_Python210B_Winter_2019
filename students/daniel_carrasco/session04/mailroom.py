#!/usr/bin/env python3
def main():
    print('\nChoose an action(1-4):\n\n\
1 - Send a Thank You to a single donor.\n\
2 - Create a Report.\n\
3 - Send letters to all donors.\n\
4 - Quit\n')
    VALID_RESPONSES = (1,2,3,4)

    choice = int(input(''))
    while choice not in VALID_RESPONSES:
        print('Not a valid response, please reselect\n')
        choice = int(input('Select 1 -4\n'))
    arg_dict = {1:thankyou(), 2:report(), 3: letter(),4:quit()}
    arg_dict.get(choice)
    return None

def thankyou():
    print('thank you')
def report():
    print('report')
def letter():
    print('letter')







donors = ['art bart', 'harry scary', 'hay boo']
cash = [1000,50,50000]
times = [1,5,3]
if __name__ == '__main__':
    main()
