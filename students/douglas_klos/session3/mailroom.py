#!/usr/bin/env python3

# Douglas Klos
# January 27th, 2019
# Python 210
# mailroom.py


mailroom_db = [('Douglas', [5000, 2000]),
               ('Maggie', [2222, 3333, 4444]),
               ('Light Yagami', [124, 8975]),
               ('Makise Kurisu', [235987]),
               ('Youjo Senki', [13498, 9876, 1234]),
               ('Jo', [1488, 420])
               ]

main_prompt = '\n'.join(('\nWelcome to the Mail Room!',
                         'Please choose from the following options: ',
                         '1: Send a Thank You',
                         '2: Create a report',
                         'q: Quit',
                         '>>> '))

thank_you_prompt = '\n'.join(('\nPlease enter one of the following:',
                              '<Name> to select person to send a '
                              'thank you note to,',
                              '"list" to display names in the database,',
                              'q to return to main menu ',
                              '>>> '))

thank_you_note = 'Thank you {} for your donation of {}'


def send_thank_you():
    """ Sends a thank you note to selected donor """

    name_input = input(thank_you_prompt)
    if name_input in ('Q', 'q'):
        return
    
    elif name_input.lower() == 'list':
        print("\nDonors in database:")
        for donor in mailroom_db:
            print(donor[0])
    
    elif not any(name_input in sub_list for sub_list in mailroom_db):
        print('Donor not found, adding')
        donation_amounts = [int(x) for x in 
                input('Enter donations seperated by a space').split()]
        mailroom_db.extend([(name_input, donation_amounts)])

        for donor,donations in mailroom_db:
            print(f'donor = {donor}, donations = {donations}')


    else:
        for donor, donations in mailroom_db:
            if name_input == donor:
                print(f'Donation amounts for {donor}: {donations}')
                donation = input('Please enter a donation amount: ')
                if donation in str(donations):
                    print(thank_you_note.format(donor, donation))
                else:
                    print(f'Donation from {donor} '
                          f'in the amount of {donation} not found')


def create_report():
    """ Prints a report of donors and their donations """

    print()
    print("Donor Name\t\t| Total Given | Num Gifts | Average Gift")
    print("-" * 64)
    for donor in mailroom_db:
        print(f'{donor[0]:24s} $ {sum(donor[1]):10,}'
              f'{len(donor[1]):12d}  $ {sum(donor[1])/len(donor[1]):11,.2f}')


def main():
    while True:
        selection = input(main_prompt)
        if selection == '1':
            send_thank_you()
        elif selection == '2':
            create_report()
        elif selection in ('Q', 'q'):
            break
        else:
            print("Not a valid entry")


if __name__ == '__main__':
    main()
