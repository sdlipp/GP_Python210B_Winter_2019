#!/usr/bin/env python3

import os
import datetime   

def thank_you_one(): # adding a new vendor
    while True:
        name = input("Please enter a full name (or 'list' for a list of current donors): ")
        name = name.title() #keeps capitalization format the same
        if name.lower() == "list":
            print('\n'.join(donor_db.keys())) #displays list of donors
        elif name not in donor_db.keys(): #adding new donor
            print("Adding {} to the donor list".format(name))
            donation = input("Enter the donation amount from {}: ".format(name)) #adding donation from new donor
            donation = float(donation) #converting to a float
            donor_db.setdefault(name, []).append(donation)
            break
        elif name in donor_db.keys(): #adding donation for existing donor
            name = name.title() #keep capitalization same as keys
            # name_index = d_list.index(name.lower())
            donation = input("Enter the new donation amount: ")
            donation = float(donation)
            donor_db[name].append(donation)
            print("\n \n The ${:.2f} donation from {} was added".format(donation, name))
            break
       

# send the thank you letter to one donor
    print("\n \n Generating the letter for {}\n \n".format(name))
    print("Dear {}, \n\n On behalf of all of us, we thank your for your generous donation of ${:10.2f}. \n You have helped make a big impact on the community!".format(name, donation))


# send the thank you letter to all donors
def thank_you_all():
    path = os.getcwd()
    folder = path + '/donor_letters/'
    os.mkdir(folder)
    os.chdir(folder)
    for key in donor_db:
        timestamp = str(datetime.date.today())
        with open(key + '_' + timestamp + ".txt", "w+") as f:
            f.write("Dear {}, \n\n On behalf of all of us, we thank your for your generous donation. \n You have helped make a big impact on the community!".format(key))
            f.close()

    print("Letters to all donors were generated.")


# set up for donor report
def sort_key(data):
    return data[1]

# create a report of donors and amounts
def donor_report():
    spreadsheet = []
    for name, gifts in donor_db.items():
        total_given = sum(gifts)
        num_gifts = len(gifts)
        avg_gift = total_given / num_gifts
        spreadsheet.append((name, total_given, num_gifts, avg_gift))

    #sort the report by total donation
    spreadsheet.sort(key = sort_key)

    print("{:<30} | {:<12} | {:>15} | {:12}".format("Donor Name", "Total Given", "Number of Gifts", "Average Gift")) #print the header
    print("-"*79) #print the dashed line
    for data in spreadsheet:    
        print("{:<30}  ${:12.2f}   {:>15}  ${:12.2f}".format(data[0], data[1], data[2], data[3]))



def quit_program():
    sys.exit()



def main():
    while True:
        response = ''
        response = input("""
        Please enter a number from the following options:
            1 - Send a Thank You to One Donor
            2 - Send a Thank You to All Donors
            3 - Create a Report
            4 - Quit
        """)
        response = int(response)
        selection = {1: thank_you_one, 
                    2: thank_you_all, 
                    3: donor_report,
                    4: quit_program
                    }
        if response in selection.keys():
            selection.get(response)()
        else:
            print("Please select from the available options")


if __name__ == "__main__": 

    donor_db = {"Eliza Sommers": [4000, 250, 70],
                "Tao Chien": [350, 1000, 225], 
                "Joaquin Andieta": [100, 25], 
                "Paulina Rodriguez": [50000], 
                "Jacob Todd": [75, 80]}   
    main()             