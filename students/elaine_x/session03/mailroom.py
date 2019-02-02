'''
##########################
#Python 210
#Session 03 - Mailroom Part 1
#Elaine Xu
#Jan 29,2019
###########################
'''

def menu():
    '''print out the main menu of options'''
    print('''Menu
    Please choose from below options:
    1 - Send a Thank You
    2 - Create a Report
    3 - quit''')


def send_a_thankyou():
    '''send a thankyou note to donor'''
    # creating a list of donors
    donor_list = []
    for donor in donor_db:
        donor_list.append(donor[0].lower())
    #print(donor_list) #for testing
    #prompt for a full name
    while True:
        fullname = input("Enter full name of the donor (type 'list' to show all donor names): ")
        if fullname.lower() == 'list':
            for donor in donor_db:
                print(donor[0])
        elif fullname.lower() not in donor_list:
            print(f'{fullname} does not exist in current donor data, '
                  f'adding {fullname} to the donor data.')
            #prompt for a donation amount
            donation_amount = float(input("Enter the donation amount: "))
            donor_db.append((fullname, [donation_amount, 1]))
            print(f"{donation_amount} has been added to {fullname}'s donation history.")
            #print(donor_db) #for testing
            break
        elif fullname.lower() in donor_list:
            fullname_index = donor_list.index(fullname.lower())
            #prompt for a donation amount
            donation_amount = float(input("Enter the donation amount: "))
            donor_db[fullname_index][1][0] = donor_db[fullname_index][1][0] + donation_amount
            donor_db[fullname_index][1][1] = donor_db[fullname_index][1][1] + 1
            print(f"{donation_amount} has been added to {fullname}'s donation history.")
            #print(donor_db) #for testing
            break
    #send thankyou note
    print("Composing Thank You email:")
    print(f'Thank you {fullname} for your generous donation of {donation_amount:^10.2f}!')
    print()
    menu()


def create_a_report():
    '''create a report in tabular and return to original prompt'''
    donor_db.sort(key=sort_total_donation, reverse=True)
    print("Printing report:")
    title = ('Donor Name', 'Total Given', "Num Gifts", 'Average Gift')
    print("{:<24} | {:^13} | {:^11} | {:^11}".format(*title))
    print("-"*70)
    for i, row in enumerate(donor_db):
        print("{:<25} ${:>13.2f} {:>13}  ${:>12.2f}"
              .format(donor_db[i][0], donor_db[i][1][0], donor_db[i][1][1],
                      donor_db[i][1][0]/donor_db[i][1][1]))
    print()
    menu()


def sort_total_donation(number):
    '''sort donors by total historical donation amount'''
    return number[1][0]


def main():
    '''main operation of the program'''
    menu()
    choice = ''
    while True:
        choice = int(input("Enter your selection: "))
        if choice == 1:
            send_a_thankyou()
        elif choice == 2:
            create_a_report()
        elif choice == 3:
            print("Exiting the program")
            break
        else:
            print("Not a valid option, try again.")


#############################################################
if __name__ == "__main__":

    donor_db = [("William Gates, III", [653772.32, 2]),
                ("Jeff Bezos", [877.33, 1]),
                ("Paul Allen", [663.23, 3]),
                ("Mark Zuckerberg", [1663.23, 3]),
                ("Bob Smith", [500.00, 1]),
                ]

    main()
