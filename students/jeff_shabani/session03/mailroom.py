#!/usr/bin/env python3
import sys

from operator import itemgetter
from collections import OrderedDict

DONORS = {'William B': [120, 130, 50],
          'Sammy Maudlin': [500, 125, 670, 1000],
          'Bobby Bittman': [10],
          'Skip Bittman': {75, 125, 19},
          'Ashley Lashbrooke': [10000, 15000]}

prompt = "\n".join(("Welcome to my charity!",
          "Please select and option below:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Quit",
          ">>> "))

def view_donor_names():
    for k,v in DONORS.items():
        print(k)

def add_new_donor(name, donor_list):
    amount = int(input(f'How much would this donor like to donate?'))
    donor_list[name] = [amount]



def get_a_name():
    answer = input('Please enter a donor Full Name.')
    if answer.lower() == 'list':
        view_donor_names()
        answer = input('Please enter a donor Full Name.')
    amount = int(input('How much would this donor like to donate?'))
    if answer not in DONORS:
        DONORS[answer] = [amount]
    else:
        for k,v in DONORS.items():
            if k.lower() == answer.lower():
                v.append(amount)
    print(f'Thank you {answer.split()[0]} for you generous donation of ${amount:,.0f}')
    print()

def create_report():
    header=f'{"Name".ljust(20)}{"| Total Donations".rjust(20)}{"| # of Donations".rjust(20)}{"| Average Donation".rjust(20)}'
    print(header)
    print('-'*len(header))
    new_donors = {k: (sum(v), len(v), (sum(v) / len(v))) for k, v in DONORS.items()}
    new_donors = OrderedDict(sorted(new_donors.items(), key=itemgetter(1), reverse=True))
    for k,v in new_donors.items():
        print(f'{str(k).ljust(20)}{str(v[0]).rjust(20)}{str(v[1]).rjust(20)}{str(v[2]).rjust(20)}')

def quit_the_program():
    print('Tschüss')
    sys.exit()

def main():
    while True:
        response = input(prompt)
        if response == '1':
            get_a_name()
        elif response == '2':
            create_report()
        elif response == '3':
            quit_the_program()
        else:
            print('Please make a valid selection')

main()
