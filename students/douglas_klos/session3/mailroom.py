#!/usr/bin/env python3

# Douglas Klos
# January 28th, 2019
# Python 210
# mailroom.py

# There are more functions than requested in the assignment.
# I felt it needed a better way to add new donors than just through
# send_thank_you function, and a way to add new donations to current
# donors.  Note that you can add new donors through send_thank_you
# as requested in the assignment.


mailroom_db = [('Douglas', [5000, 2000]),
               ('Maggie', [2222, 3333, 4444]),
               ('Light Yagami', [124, 8975]),
               ('Makise Kurisu', [235987]),
               ('Youjo Senki', [13498, 9876, 1234]),
               ('Motoko Kusanagi', [57892, 239857, 87265]),
               ('Jo', [8814, 2320])
               ]

MAIN_PROMPT = '\n'.join((
              '\nWelcome to the Mail Room!',
              'Please choose from the following options: ',
              '1: Send a Thank You',
              '2: Create a report',
              '3: Add a new donor',
              '4: Add a new donation',
              'q: Quit',
              '>>> '))

THANK_YOU_PROMPT = '\n'.join((
                   '\nPlease enter one of the following:',
                   '<Name>: Name of person to send a thank you note to',
                   'list: Display donors in the database',
                   'q: Return to main menu ',
                   '>>> '))

THANK_YOU_NOTE = '\n'.join((
                 '\nDear {}:',
                 '\tThank you for your very kind donation of ${:.2f}.',
                 '\tIt will be put to very good use.',
                 '\t\tSincerely',
                 '\t\t\tThe Team'))


def add_donation():
    """ Add new donations to a current donor """

    display_database()
    while True:
        name = input('\nPlease select a donor to add a donation to: ')
        if name.lower() in ('q', 'quit'):
            return
        elif not any(name in sub_list for sub_list in mailroom_db):
            print('Donor not found, please select from list')
        else:
            break

    donations = [int(x) for x in
                 input('Enter donations seperated by a space: ').split()]

    # Find the name in the database and add new donations
    for donor, donation in mailroom_db:
        if donor == name:
            donation.extend(donations)


def add_donor(name_input):
    """ Adds name_input to the database """

    if name_input is '':
        name_input = input("Please enter new donor's name: ")

    donations = [int(x) for x in
                 input('Enter donations seperated by a space: ').split()]

    # We don't want a donor without an entry for donations.
    # Set it to 0 to avoid erros in other functions.
    if donations == []:
        donations = [0]

    mailroom_db.extend([(name_input, donations)])


def display_database():
    """ Displays all donors and their donations """

    print()
    for donor, donations in mailroom_db:
        print(f'{donor:24s} donations = {donations}')


def send_thank_you():
    """ Sends a thank you note to selected donor """

    while True:
        name_input = input(THANK_YOU_PROMPT)
        if name_input.lower() in ('q', 'quit'):
            return
        elif name_input.lower() in('l', 'list'):
            display_database()

        # Check to see if the name entered exists in the database
        # If name not found, verify you want to add it.
        elif not any(name_input in sub_list for sub_list in mailroom_db):
            add_check = input('Donor not found, would you like to add?: ')
            if add_check.lower() in ('y', 'yes'):
                add_donor(name_input)

        # The name was found in the database, select a donation amount
        else:
            for donor, donations in mailroom_db:
                if name_input == donor:
                    print(f'Donation amounts for {donor}: {donations}')
                    donation = int(input('Please enter a donation amount: '))
                    print(donations)
                    if donation in donations:
                        print(THANK_YOU_NOTE.format(donor, float(donation)))
                    else:
                        print(f'Donation from {donor} '
                              f'in the amount of {donation} not found')


def create_report():
    """ Prints a report of donors and their donations """

    print()
    print("Donor Name\t\t| Total Given\t| Num Gifts | Average Gift")
    print("-" * 67)
    for donor in mailroom_db:
        print(f'{donor[0]:24s} $ {sum(donor[1]):12,.2f}'
              f'{len(donor[1]):12}  $ {sum(donor[1])/len(donor[1]):12,.2f}')


def main():
    """ Mailroom main function """

    while True:
        selection = input(MAIN_PROMPT)
        if selection == '1':
            send_thank_you()
        elif selection == '2':
            create_report()
        elif selection == '3':
            add_donor('')
        elif selection == '4':
            add_donation()
        elif selection.lower() in ('q', 'quit'):
            break
        else:
            print("Not a valid entry")


if __name__ == '__main__':
    main()
