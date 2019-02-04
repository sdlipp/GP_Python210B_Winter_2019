#!/usr/bin/env python3

# Douglas Klos
# February 3st, 2019
# Python 210
# mailroom.py, Mailroom v2.0


mailroom_db = {'Douglas': [5000, 2000],
               'Maggie': [2222, 3333, 4444],
               'Light Yagami': [124, 8975],
               'Makise Kurisu': [235987],
               'Youjo Senki': [13498.00, 9876, 1234],
               'Motoko Kusanagi': [57892, 239857, 87265],
               'Jo': [8814, 2320]}

MAIN_PROMPT = ('\nWelcome to the Mail Room\n'
               'Please choose from the following options:\n'
               '1: Send a Thank You\n'
               '2: Create a report\n'
               '3: Add a new donor\n'
               '4: Add a new donation\n'
               '5: Print database\n'
               'q: Quit\n'
               '>>> ')

THANK_YOU_PROMPT = ('\nPlease enter one of the following:\n'
                    '<Name>: Name of person to send a thank you note to\n'
                    'list: Display donors in the database\n'
                    'q: Return to main menu\n'
                    '>>> ')

THANK_YOU_NOTE = ('\nDear {}:\n'
                  '\tThank you for your very kind donation of ${:,.2f}.\n'
                  '\tIt will be put to very good use.\n'
                  '\t\tSincerely\n'
                  '\t\t\tThe Team')


def display_database():
    """ Displays all donors and their donations """

    print()

    for key in mailroom_db:
        print(f'{key:>24} : {mailroom_db[key]:}')


def create_report():
    """ Prints a report of donors and their donations """

    print()
    print("Donor Name\t\t| Total Given\t\t| Num Gifts | Average Gift")
    print("-" * 79)
    for key in mailroom_db:
        if mailroom_db[key] == []:
            print(f'{key:24s}\t\t       {len(mailroom_db[key]):10}')
        else:
            print(f'{key:24s} '
                  f'$ {sum(mailroom_db[key]):16,.2f}    '
                  f'{len(mailroom_db[key]):10}    '
                  f'$ {sum(mailroom_db[key])/len(mailroom_db[key]):16,.2f}')


def add_donor(name_input):
    """ Adds name_input to the database """

    # Check to see if a name was passed in, if not, read user input
    while name_input in '':
        name_input = input("Please enter new donor's name: ")
        if name_input in mailroom_db.keys():
            print('Already exists')
            name_input = ''
        if name_input in ('q', 'Q'):
            return

    mailroom_db[name_input] = []


def add_donation():
    """ Add new donations to a current donor """

    display_database()
    while True:
        name = input('\nPlease select a donor to add a donation to: ')
        if name.lower() in ('q', 'quit'):
            return
        if name not in mailroom_db.keys():
            print('Donor not found, please select from list')
        else:
            break

    while True:
        try:
            donation_input = input('Please enter a donation: ')
            if float(donation_input) < 0:
                print('Donation must be a positive number')
            else:
                mailroom_db[name].append(float(donation_input))
                break
        except ValueError:
            print(f'{donation_input} is not a valid entry')


def thank_you_menu():
    """ Menu for Thank You options """

    while True:
        name_input = input(THANK_YOU_PROMPT)
        if name_input.lower() in ('q', 'quit'):
            return
        elif name_input.lower() in('l', 'list'):
            display_database()
            continue
        elif name_input in '':
            pass
        if name_input not in mailroom_db.keys():
            add_donor(name_input)
            print(f'\nAdding {name_input} to the database')
        else:
            send_thank_you(name_input)


def send_thank_you(name_input):
    """ Send thank you to donor for selected donation """

    if mailroom_db[name_input] == []:
        print(f'No donation from {name_input}')
        return

    print(f'Donation amounts for {name_input}: {mailroom_db[name_input]}')

    # All this try if else except is for error checking input
    while True:
        try:
            donation_input = float(input('Enter donation: '))
            if donation_input in mailroom_db[name_input]:
                print(THANK_YOU_NOTE.format(name_input, donation_input))
                return
            else:
                print(f'Donation from {name_input} '
                      f'in the amount of {donation_input} '
                      f'not found')
        except ValueError:
            print(f'Donation amountisfor {name_input}:'
                  f'{mailroom_db[name_input]}')


def main():
    """ Mailroom main function """

    selection = input(MAIN_PROMPT)

    while selection.lower() not in ('q', 'quit'):

        if selection == '1':
            thank_you_menu()
        elif selection == '2':
            create_report()
        elif selection == '3':
            add_donor('')
        elif selection == '4':
            add_donation()
        elif selection.lower() in ('5', 'p', 'print'):
            display_database()
        else:
            print("Not a valid entry")

        selection = input(MAIN_PROMPT)


if __name__ == '__main__':
    main()
