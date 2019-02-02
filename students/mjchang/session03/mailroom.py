#!/usr/bin/env python3

donor_db = [("Eliza Sommers",[4000, 250, 70]),
("Tao Chien",[350, 1000, 225]), 
("Joaquin Andieta",[100, 25]), 
("Paulina Rodriguez",[50000]), 
("Jacob Todd",[75, 80])]

action = """
Please enter a number from the following options:
    1 - Send a Thank You
    2 - Create a Report
    3 - Quit
"""
print(action)


def donor_list():
    print("List of donors:\n")
    for donor in donor_db:
        print(donor[0])

def donor_search(name):
    for donor in donor_db:
        if name.title() == donor[0].title():
            return donor
    return None        





def thank_you()




def ty_letter()






def sort_key(data):
    return data[1]

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
        response = input(action)
        if response == "1":
            thank_you()
        elif response == "2":
            donor_report()
        elif response == "3":
            quit_program()
        else:
            print("Please select from the available options")                    