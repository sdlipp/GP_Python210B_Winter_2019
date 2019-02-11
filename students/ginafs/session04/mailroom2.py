# Mailroom Part2

import datetime

edge_str = "| "
donations = {"William Gates" : [90000, 50000, 20000], "Mark Zuckerberg": [100000], "Jeff Bezos": [90000, 85000, 1000000], "Paul Allen": [11000, 9000000, 800, 5500], "Warren Buffet": [1000000, 40000]}
VALID_MENU_ITEMS = ('1', '2', '3', '4')

single_donation_letter = "Dear {:s},\n\n\tThank you for your donation of ${:,.2f}.\n\n\tIt will be put to good use.\n\n\t\tSincerely,\n\t\t-The Team"
multiple_donation_letter = "Dear {:s},\n\n\tThank you for your {:d} donations totalling ${:,.2f}.\n\n\tIt will be put to good use.\n\n\t\tSincerely,\n\t\t-The Team"

# prints list of donors from donations, or the keys from the dictionary

def print_donor_list():
    print()
    print("List of Donors")
    print("-" * 14)
    
    for key in donations:
        print (key)
    print()
    return

# Menu item 1 - Enter the name of a new or existing donor and add a donation
# this should add a new donor if needed and add the donation to the list of values for that donor
# and print a thank you letter to teh screen

def thank_donor():
    print("Here is the list of donors")
    print_donor_list()
    donor_name  = input("Enter a name from this list or the full name of the new donor : ")
    
    #check if the donor is in the database or is a new donor
    #if it is a new donor set the new_donor flag to true
    new_donor = False
    if donor_name not in donations:
        new_donor = True
    
    donation_amount = input(f"Enter donation amount > ")
    if new_donor:
        #add donor_name and donation_amount to donations
        donations[donor_name] = [int(donation_amount)]
    else:
        #add donation_amount to list of donations of the donor in donations
        donations[donor_name].append(int(donation_amount))
    print(f"\nThe donation of ${donation_amount} by {donor_name} was successfully added to the database\nThe letter follows\n\n")
    t = (donor_name, float(donation_amount))
    print(single_donation_letter.format(*t))
    return True

# Pretty much the same from Part 1
    
def create_report():
    print_donor_report()
    print()
    print()
    return True
    
#Uses the donations dictionary to create Thank you letter.txt files for each donor in donations dict
# Builds a file_name from the donor's name and timestamp. Creates modified letters for donors with a single donation
# and for donors with multiple donations    
    
def letters_to_donors():
    print("Printing letters to donors")
    for key in donations:
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
        num_donations = len(donations[key])
        total_amount = sum(donations[key])
        
        #Build the string to write into the file. Use tuples to send in values
        outstr = ""
        if num_donations > 1:
            out_str = multiple_donation_letter
            t = (key, int(num_donations), float(total_amount))
        else:
            #donor with single donation does not need number of donations
            out_str = single_donation_letter
            t = (key, float(total_amount))
        
        #create file and write into it
        outfile = open(file_name, 'w')
        outfile.write(out_str.format(*t))
        outfile.close()
    return True

# Quit with a message    
def quit():
    print("\nGoodbye! Thank you for using the Donor Management Program")
    return False


def print_border():
    print("-" * 74)
    return

def print_heading():
    # defing column names
    columns = ["{:25}".format("Donor Name"), "{:14}".format("Total Given"), "{:12}".format("Num Gifts"), "{:14}".format("Average Gift")]
    
    # build heading string
    heading_str = edge_str
    for i in range(len(columns)):
        heading_str += columns[i] + edge_str
    
    # remove trailing blank
    print(heading_str[:-1])
    return
    
def print_donor_report():
    print_border()
    print_heading()
    print_border()

  
    for key in donations:
        line_str = edge_str
        # Donor Name
        line_str += "{:25}".format(key) + edge_str
        # Total Given
        sum_gifts = sum(donations[key])
        line_str += "{: 14.2f}".format(sum_gifts) + edge_str
        # Num Gifts
        num_gifts = len(donations[key])
        line_str += "{: 12d}".format(num_gifts) + edge_str
        # Average
        avg = sum_gifts/num_gifts
        line_str += "{: 14.2f}".format(avg) + edge_str
        # remove trailing blank
        print(line_str[:-1])
    print_border()
    return
    
# displays the menu
def display_menu():
    print("Please make a choice from these menu items")
    print()
    print("1 - Thank a single donor")
    print("2 - Create a Report")
    print("3 - Send letters to all donors")
    print("4 - Quit")
    print()
    return
  
# adds a new donor to the end of the list
def add_donor(new_donor):
    donations.append(new_donor)
    return

# gets donation amount from user
def get_donation_amount():
    amount = input(f"Enter new donor donation amount > ")
    return amount

#process the donation. If it is a new donor, add donor and donation to donations dict.
# if it is an existing donor, add donation to the list of donations   
def process_donation(new_donor_flag, donor_index):
    amount = get_donation_amount()
    if new_donor_flag:
        donations.append(list(int(amount)))
    else:
        donations[donor_index + 1].append(int(amount))
    return

        
#*********************
#Main Program
#*********************

if __name__ == "__main__":
   
    menu_dict = {
        "1": thank_donor, 
        "2": create_report, 
        "3": letters_to_donors, 
        "4": quit
    }

    print("Welcome to the Donor Management Program")
    show_menu = True
    
    while show_menu:
        display_menu()
        menu_item = input("enter your menu choice : ")
        while menu_item not in VALID_MENU_ITEMS:
            print ("Invalid menu item - Please make a valid selection")
            menu_item = input("enter a menu choice :")
        show_menu = menu_dict.get(menu_item)()
        

