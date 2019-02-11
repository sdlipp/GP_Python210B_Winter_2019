#!/usr/bin/env python3

donor_db = {
'eliza_sommers': ("Eliza Sommers", [4000, 250, 70]),
'tao_chien': ("Tao Chien", [350, 1000, 225]), 
'joaquin_andieta': ("Joaquin Andieta", [100, 25]), 
'paulina_rodriguez': ("Paulina Rodriguez", [50000]), 
'jacob_todd': ("Jacob Todd", [75, 80])}

def home():
    print("""
    Please enter a number from the following options:
        1 - Send a Thank You to One Donor
        2 - Send a Thank You to ALL Donors
        3 - Create a Report
        4 - Quit
    """)       


def show_donors(): #creating a list of donors to be displayed if "list" option selected
    d_list = []
    for donor in donor_db.values():
        d_list.append(donor[0])
    print("\n".join(d_list))    

def thank_you_one(): # adding a new vendor
    while True:
        name = input("Please enter a full name (or 'list' for a list of current donors): ")
        name = name.title() #keeps capitalization format the same
        if name.lower() == "list":
            show_donors()
                
        elif name.lower() not in d_list: #adding new donor
            print("Adding {} to the donor list".format(name))
            donation = input("Enter the donation amount from {}: ".format(name)) #adding donation from new donor
            donation = float(donation) #converting to a float
            donor_db[name] = donation #adding new donor and donation to the list
            break
        elif name.lower() in d_list:
            name_index = d_list.index(name.lower())
            donation = input("Enter the new donation amount: ")
            donation = float(donation)
            donor_db[name_index][1].append(donation)
            # print(donor_db) #for testing
            print("\n \n The {} donation from {} was added".format(donation, name))
            break
        break       

# send the thank you letter
    print("\n \n Generating the letter for {}\n \n".format(name))
    print("Dear {}, \n\n On behalf of all of us, we thank your for your generous donation of ${:10.2f}. \n You have helped make a big impact on the community!".format(name, donation))

#send a thank you to all donors
def thank_you_all():





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
    break


def main():    
    while True:
        response = ''
        response = input("""
    Please enter a number from the following options:
        1 - Send a Thank You to One Donor
        2 - Send a Thank You to ALL Donors
        3 - Create a Report
        4 - Quit
    """)

        selection = {
        1: thank_you_one(), 
        2: thank_you_all(), 
        3: donor_report(), 
        4: quit_program()
        }
        selection.get(choice, num)
        # if response == "1":
        #     thank_you_one()
        # elif response == "2":
        #     thank_you_all()    
        # elif response == "3":
        #     donor_report()
        # elif response == "4":
        #     quit_program()
        #     break
        # else:
        #     print("Please select from the available options")   

if __name__ == "__main__": 

    donor_db = [("Eliza Sommers",[4000, 250, 70]),
                ("Tao Chien",[350, 1000, 225]), 
                ("Joaquin Andieta",[100, 25]), 
                ("Paulina Rodriguez",[50000]), 
                ("Jacob Todd",[75, 80])]   
    main()             