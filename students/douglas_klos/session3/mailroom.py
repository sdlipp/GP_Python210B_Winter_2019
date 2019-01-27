#!/usr/bin/env python3

# Douglas Klos
# January 26th, 2019
# Python 210
# mailroom.py


mailroom_db = [('Douglas', [5000, 2000]),
               ('Maggie', [2222, 3333, 4444]),
               ('Light Yagami', [124, 8975]),
               ('Makise Kurisu', [235987]),
               ('Youjo Senki', [13498, 9876, 1234]),
               ('Jo', [1488, 420]),
               ]

prompt = '\n'.join(('Welcome to the Mail Room!',
                    'Please choose from the following options: ',
                    '1: Send a Thank You',
                    '2: Create a report',
                    'q: Quit',
                    '>>> '))


def send_thank_you():
    pass


def create_report():
    print()
    print("Donor Name\t\t| Total Given | Num Gifts | Average Gift")
    print("-" * 64)
    for donor in mailroom_db:
        print(f'{donor[0]:24s} $ {sum(donor[1]):10,}'
              f'{len(donor[1]):12d}  $ {sum(donor[1])/len(donor[1]):11,.2f}')
    print()


def main():
    while True:
        selection = input(prompt)
        if selection == '1':
            send_thank_you()
        elif selection == '2':
            create_report()
        elif selection in ('q', 'Q'):
            break
        else:
            print("Not a valid entry")


if __name__ == '__main__':
    main()
