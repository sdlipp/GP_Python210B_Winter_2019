# Mailroom Part1

donations = ["William Gates", [90000, 50000, 20000], "Mark Zuckerberg", [100000], "Jeff Bezos", [90000, 85000, 1000000], "Paul Allen", [11000, 9000000, 800, 5500], "Warren Buffet", [1000000, 40000]]
edge_str = "| "

# displays the menu
def display_menu():
    print("Welcome to the Donor Management Program")
    print("To send thank you notes enter 1\nTo create a report enter 2\nTo quit enter 3")
    choice = input(f"What would you like to do? > ")
    return choice
    
# prints list of donors from donations
def print_donor_list():
    print()
    print("List of Donors")
    print("-" * 14)
    
    for i in range(0, len(donations), 2):
        print (donations[i])
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
    
def process_donation(new_donor_flag, donor_index):
    amount = get_donation_amount()
    if new_donor_flag:
        donations.append(list(int(amount)))
    else:
        donations[donor_index + 1].append(int(amount))
    return

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
    max_index = len(donations) - 1
    for i in range(0, max_index, 2):
        line_str = edge_str
        # Donor Name
        line_str += "{:25}".format(donations[i]) + edge_str
        # Total Given
        sum_gifts = sum(donations[i+1])
        line_str += "{: 14.2f}".format(sum_gifts) + edge_str
        # Num Gifts
        num_gifts = len(donations[i+1])
        line_str += "{: 12d}".format(num_gifts) + edge_str
        # Average
        avg = sum_gifts/num_gifts
        line_str += "{: 14.2f}".format(avg) + edge_str
        # remove trailing blank
        print(line_str[:-1])
    print_border()
    return
        
        
if __name__ == "__main__":
    
    # Present the menu to the user until the user chooses to quit
    work = True
    while work:
        choice = display_menu()
        if (choice == '1'):
            name = input(f"Enter donor's name or enter 'list' for a list of donors? > ")
            if (name == "list"):
                print_donor_list()
                name = input(f"Enter donor's name > ")
            new_donor = False
            if name in donations:
                #get index in list and update tuple
                donor_index = donations.index(name)
            else:
                # add name and donation amount to donations
                new_donor = True
                add_donor(name)
            process_donation(new_donor, donor_index) 
            print("The donation was added successfully")
            #print(donations)
            #print("*" * 10)
            
        elif (choice == '2'):
                print_border()
                print_heading()
                print_border()
                
                print_donor_report()
                
                
                print()
                print()
                
        elif (choice == '3'):
            work = False
        else:
            print("invalid choice, please make a valid choice")  
    