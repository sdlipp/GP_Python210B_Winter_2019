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
               ('Youjo Senki', [13498.00, 9876, 1234]),
               ('Motoko Kusanagi', [57892, 239857, 87265]),
               ('Jo', [8814, 2320])
               ]

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
                  '\tThank you for your very kind donation of ${:.2f}.\n'
                  '\tIt will be put to very good use.\n'
                  '\t\tSincerely\n'
                  '\t\t\tThe Team')


def get_new_donations():
    """ Queries user for donations """

    donations = []

    # Gets an input from the user.  If the input is an integer, it is
    # added to the donation list as an integer.  If it's a float, it
    # is added as a float.  I didn't want tailing 0's on integer input
    # values showing up in the database, hene the 'if' inside the try.
    # If it is anything expect an int or a float, the error is caught
    # and the while loop is exited.  I had an alternative of
    # if not donation_input.isdigit() that worked, but it didn't
    # support floats, so all I could find was to use a
    # try / except statement.  There's probably a more graceful way
    # but this seems to work.
    while True:
        donation_input = str(input('Please enter donations, blank to quit: '))
        try:
            if donation_input.isdigit():
                donations.append(int(donation_input))
            else:
                donations.append(float(donation_input))
        except ValueError:
            break

        # if not donation_input.isdigit():
        #     break
        # donations.append(float(donation_input))

    return donations


def add_donation():
    """ Add new donations to a current donor """

    display_database()
    while True:
        name = input('\nPlease select a donor to add a donation to: ')
        if name.lower() in ('q', 'quit', ''):
            return
        elif not any(name in sub_list for sub_list in mailroom_db):
            print('Donor not found, please select from list')
        else:
            break

    donations = get_new_donations()

    # Find the name in the database and add new donations
    for donor, donation in mailroom_db:
        if donor == name:
            donation.extend(donations)


def add_donor(name_input):
    """ Adds name_input to the database """

    # Check to see if a name was passed in, if not, read user input
    if name_input is '':
        name_input = input("Please enter new donor's name: ")

    donations = get_new_donations()

    mailroom_db.extend([(name_input, donations)])


def display_database():
    """ Displays all donors and their donations """

    print()
    for donor, donations in mailroom_db:
        print(f'{donor:>24} : {donations:}')


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
                    donation = float(input('Please enter a donation amount: '))
                    print(donations)
                    if donation in donations:
                        print(THANK_YOU_NOTE.format(donor, float(donation)))
                    else:
                        print(f'Donation from {donor} '
                              f'in the amount of {donation} not found')


def create_report():
    """ Prints a report of donors and their donations """

    print()
    print("Donor Name\t\t| Total Given\t\t| Num Gifts | Average Gift")
    print("-" * 79)
    for donor in mailroom_db:
        if donor[1] == []:
            print(f'{donor[0]:24s}\t\t       {len(donor[1]):10}')
        else:
            print(f'{donor[0]:24s} '
                  f'$ {sum(donor[1]):16,.2f}    '
                  f'{len(donor[1]):10}    '
                  f'$ {sum(donor[1])/len(donor[1]):16,.2f}')


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
        elif selection == 'p':
            display_database()
        elif selection.lower() in ('q', 'quit'):
            break
        else:
            print("Not a valid entry")


if __name__ == '__main__':
    main()
