#!/usr/bin/env python3

donor_db = [("Eliza Sommers",[4000, 250, 70]),
("Tao Chien",[350, 1000, 225]), 
("Joaquin Andieta",[100, 25]), 
("Paulina Rodriguez",[50000]), 
("Jacob Todd",[75, 80])]

def home():
    print("""
    Please enter a number from the following options:
        1 - Send a Thank You
        2 - Create a Report
        3 - Quit
    """)       

def thank_you(): # adding a new vendor
    d_list = []
    for donor in donor_db:
        d_list.append(donor[0].lower())

    while True:
        name = input("Please enter a full name (or 'list' for a list of current donors): ")
        name = name.title() #keeps capitalization format the same
        if name.lower() == "list":
            for donor in donor_db: # print list of donor names
                print(donor[0]) 
        elif name.lower() not in d_list: #adding new donor
            print("Adding {} to the donor list".format(name))
            donation = input("Enter the donation amount from {}: ".format(name)) #adding donation from new donor
            donation = float(donation) #converting to a float
            donor_db.append((name, [donation]))
            # print(donor_db) # use this for testing only
            break
        elif name.lower() in d_list:

            donation = input("Enter the new donation amount: ") 
            donation = float(donation) #convert to a float
            # donor_db[] = donor_db + donation


# send the thank you letter
    print("\n \n Generating the letter for {}\n \n".format(name))
    print("Dear {}, \n On behalf of all of us, we thank your for your generous donation of ${:10.2f}. \n You have helped make a big impact on the community!".format(name, donation))


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
    home()



def quit_program():
    SystemExit


def main():    
    while True:
        response = ''
        response = input("""
    Please enter a number from the following options:
        1 - Send a Thank You
        2 - Create a Report
        3 - Quit
    """)
        if response == "1":
            thank_you()
        elif response == "2":
            donor_report()
        elif response == "3":
            quit_program()
            break
        else:
            print("Please select from the available options")   

if __name__ == "__main__": 

    donor_db = [("Eliza Sommers",[4000, 250, 70]),
                ("Tao Chien",[350, 1000, 225]), 
                ("Joaquin Andieta",[100, 25]), 
                ("Paulina Rodriguez",[50000]), 
                ("Jacob Todd",[75, 80])]   
    main()             