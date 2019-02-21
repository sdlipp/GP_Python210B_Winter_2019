''' Mailroom Part2 '''

import datetime

EDGE_STR = "| "
DONATIONS = {
    "William Gates" : [90000, 50000, 20000],
    "Mark Zuckerberg": [100000],
    "Jeff Bezos": [90000, 85000, 1000000],
    "Paul Allen": [11000, 9000000, 800, 5500],
    "Warren Buffet": [1000000, 40000]
    }

VALID_MENU_ITEMS = ('1', '2', '3', '4')

SINGLE_DONATION_LETTER = "Dear {:s},\n\n\tThank you for your donation of ${:,.2f}.\n\n"
SINGLE_DONATION_LETTER += "\tIt will be put to good use.\n\n\t\tSincerely,\n\t\t-The Team"

MULTIPLE_DONATION_LETTER = "Dear {:s},\n\n"
MULTIPLE_DONATION_LETTER += "\tThank you for your {:d} donations totalling ${:,.2f}.\n\n"
MULTIPLE_DONATION_LETTER += "\tIt will be put to good use.\n\n\t\tSincerely,\n\t\t-The Team"


def print_donor_list():
    '''prints list of donors from donations, or the keys from the dictionary'''
    print()
    print("List of Donors")
    print("-" * 14)

    [print(key) for key in DONATIONS]
    print()


def print_goodbye():
    ''' print goodbye message'''
    print("Looks like you want to leave. Goodbye!")


def thank_donor():
    ''' Menu item 1 - Enter the name of a new or existing donor and add a donation
    this should add a new donor if needed and add the donation to the list of values for that donor
    and print a thank you letter to the screen '''
    print("Here is the list of donors")
    print_donor_list()
    try:
        donor_name = input("Enter a name from this list or the full name of the new donor : ")
    except KeyboardInterrupt:
        print_goodbye()
        return False

    #check if the donor is in the database or is a new donor
    #if it is a new donor set the new_donor flag to true
    new_donor = False
    if donor_name not in DONATIONS:
        new_donor = True

    ''' exit the program with a message if user enters ^C, or
    keep prompting the user for a valid input until user enters a
    valid input. Break out of the loop if user enters valid number'''
    while True:
        try:
            donation_amount = float(input(f"Enter donation amount > "))
        except KeyboardInterrupt:
            print_goodbye()
            return False
        except ValueError:
            print("Please enter a valid number for the donation amount")
            continue
        else:
            break

    if new_donor:
        #add donor_name and donation_amount to donations
        DONATIONS[donor_name] = [donation_amount]
    else:
        #add donation_amount to list of donations of the donor in donations
        DONATIONS[donor_name].append(donation_amount)
    print(f"\nThe donation of ${donation_amount} by {donor_name} was successfully added to the database\nThe letter follows\n\n")
    out_tuple = (donor_name, float(donation_amount))
    print(SINGLE_DONATION_LETTER.format(*out_tuple))
    return True


def create_report():
    '''Pretty much the same from Part 1'''
    print_donor_report()
    print()
    print()
    return True


def letters_to_donors():
    '''Uses the donations dictionary to create Thank you letter.txt files for each
    donor in donations dict. Builds a file_name from the donor's name and timestamp.
    Creates modified letters for donors with a single donation and for donors
    with multiple donations '''

    print("Printing letters to donors")
    print()
    for key in DONATIONS:
        #form file name from key
        file_name = str(key).replace(' ', '_')

        #get time stamp
        timestamp = str(datetime.datetime.now()).split('.')[0]

        #format the timestamp into an valid and readable string
        timestamp = str(timestamp).replace(' ', '_')
        timestamp = str(timestamp).replace(':', '.')
        timestamp = str(timestamp).replace('-', '.')
        file_name += '.' + timestamp

        #get the number of donations for the donor and the total donation amount
        num_donations = len(DONATIONS[key])
        total_amount = sum(DONATIONS[key])

        #Build the string to write into the file. Use tuples to send in values
        out_str = ""
        if num_donations > 1:
            out_str = MULTIPLE_DONATION_LETTER
            out_tuple = (key, int(num_donations), float(total_amount))
        else:
            #donor with single donation does not need number of donations
            out_str = SINGLE_DONATION_LETTER
            out_tuple = (key, float(total_amount))

        #create file and write into it
        with open(file_name, 'w') as outfile:
            outfile.write(out_str.format(*out_tuple))
            outfile.close()
    return True


def exit_program():
    '''Exit the program with a message'''
    print("\nGoodbye! Thank you for using the Donor Management Program")
    return False


def print_border():
    ''' prints border '''
    print("-" * 74)

def print_heading():
    '''prints headings
    defining column names'''
    columns = [
        "{:25}".format("Donor Name"),
        "{:14}".format("Total Given"),
        "{:12}".format("Num Gifts"),
        "{:14}".format("Average Gift")
    ]
    # build heading string
    heading_str = EDGE_STR
    for i, heading in enumerate(columns, 1):
        heading_str += heading + EDGE_STR
    # remove trailing blank
    print(heading_str[:-1])

def print_donor_report():
    '''prints donor report'''
    print_border()
    print_heading()
    print_border()

    for key in DONATIONS:
        line_str = EDGE_STR
        # Donor Name
        line_str += "{:25}".format(key) + EDGE_STR
        # Total Given
        sum_gifts = sum(DONATIONS[key])
        line_str += "{: 14.2f}".format(sum_gifts) + EDGE_STR
        # Num Gifts
        num_gifts = len(DONATIONS[key])
        line_str += "{: 12d}".format(num_gifts) + EDGE_STR
        # Average
        avg = sum_gifts/num_gifts
        line_str += "{: 14.2f}".format(avg) + EDGE_STR
        # remove trailing blank
        print(line_str[:-1])
    print_border()


def display_menu():
    '''displays the menu'''
    print("Please make a choice from these menu items")
    print()
    print("1 - Thank a single donor")
    print("2 - Create a Report")
    print("3 - Send letters to all donors")
    print("4 - Quit")
    print()


#*********************
#Main Program
#*********************

if __name__ == "__main__":

    MENU_DICT = {
        "1": thank_donor,
        "2": create_report,
        "3": letters_to_donors,
        "4": exit_program
    }

    print("Welcome to the Donor Management Program")
    SHOW_MENU = True

    while SHOW_MENU:
        display_menu()
        try:
            MENU_ITEM = input("enter your menu choice : ")
        except KeyboardInterrupt:
            print_goodbye()
            SHOW_MENU = False
        else:    
            if MENU_ITEM not in VALID_MENU_ITEMS:
                print("Invalid menu item - Please make a valid selection")
                continue
            SHOW_MENU = MENU_DICT.get(MENU_ITEM)()        