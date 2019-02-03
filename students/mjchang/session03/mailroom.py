#!/usr/bin/env python3

donor_db = [("Eliza Sommers",[4000, 250, 70]),
("Tao Chien",[350, 1000, 225]), 
("Joaquin Andieta",[100, 25]), 
("Paulina Rodriguez",[50000]), 
("Jacob Todd",[75, 80])]

user_selection = input("""
Please enter a number from the following options:
    1 - Send a Thank You
    2 - Create a Report
    3 - Quit
""")

# def donor_search(name):
#     for donor in donor_db:
#         if name.lower() == donor[0].lower():
#             return donor
#     return None        

def thank_you(): # adding a new vendor
    d_list = []
    for donor in donor_db:
        d_list.append(donor[0].lower())

    while True:
        donor_name = input("Please enter a full name (or 'list' for a list of current donors): ")
        donor_name = donor_name.title() #keeps capitalization format the same
        if donor_name.lower() == "list":
            for donor in donor_db: # print list of donor names
                print(donor[0]) 
        elif donor_name.lower() not in d_list: #adding new donor
            print("Adding {} to the donor list".format(donor_name))
            donation = input("Enter the donation amount from {}: ".format(donor_name)) #adding donation from new donor
            donation = float(donation) #converting to a float
            donor_db.append((donor_name, [donation]))
            print(donor_db) # use this for testing only
            break
        elif donor_name.lower() in d_list:

            




def ty_letter()





# set up for donor report
def sort_key(data):
    return data[1]

# create a report of donors and amounts
def donor_report():
    spreadsheet = []
    for (name, gifts) in donor_db:
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


if __name__ == "__main__":
    while True:
        response = input(user_selection)
        if response == "1":
            thank_you()
        elif response == "2":
            donor_report()
        elif response == "3":
            quit_program()
        else:
            print("Please select from the available options")                    