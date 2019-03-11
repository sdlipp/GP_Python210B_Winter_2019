
# coding: utf-8

# In[5]:


# print of the main menu
def menu():
    print('''Menu
    Please choose from below options:
    1 - Send a Thank You
    2 - Create a Report
    3 - Exit the program''')
#first it will ask to choose a name whoom you would want to send the mail
#along side that when typing list it will give you all the names on the current list
#second if the name is not in the list then it will prompt to add the name into the data base
#lastly it will print the message of the email
## have a problem here where when asked for the amount of donation if the value type is not a number we get a error how to loop around this?
def send_a_thankyou():
    donor_list = []
    for donor in donor_db:
        donor_list.append(donor[0].lower())
    while True:
        fullname = input("Enter the full name of the donor typing list will give the names of current doners ")
        if fullname.lower() == 'list':
            for donor in donor_db:
                print(donor[0])
        elif fullname.lower() not in donor_list:
            print(f'{fullname} does not exist in the donor data, '
                  f'we will add {fullname} to the donor data.')
            amount = float(input("Please enter the donation amount: "))
            donor_db.append((fullname, [amount, 1]))
            print(f"{amount} has been added to {fullname}'s donation history.")
            break
        elif fullname.lower() in donor_list:
            fullname = donor_list.index(fullname.lower())
            amount = float(input("Please Enter the donation amount: "))
            donor_db[fullname][1][0] = donor_db[fullname][1][0] + amount
            donor_db[fullname][1][1] = donor_db[fullname][1][1] + 1
            print(f"{amount} has been added to {fullname}'s donation history.")
            break
    print("Creating a Thank You email:")
    print(f'Thank you {fullname} for your donation of {amount:^10.2f}!')
    print()
    menu()
#this prints out the database of the donors with their total amaounts and average amount donated
def create_a_report():
    donor_db.sort(key=sort_total_donation, reverse=True)
    print("Printing report:")
    title = ('Donor Name', 'Total Given', "Num Gifts", 'Average Gift')
    print("{:<19} | {:^13} | {:^13} | {:^11}".format(*title))
    print("-"*70)
    for i, row in enumerate(donor_db):
        print("{:<21} ${:>13.2f} {:>13}  ${:>12.2f}"
              .format(donor_db[i][0], donor_db[i][1][0], donor_db[i][1][1],
                      donor_db[i][1][0]/donor_db[i][1][1]))
    print()
    menu()
def sort_total_donation(number):
    return number[1][0]
#the main frame of the console 
def main():
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

if __name__ == "__main__":

    donor_db = [("William Gates, III", [ 653784.49, 2]),
                ("Mark Zuckerberg", [16396.10, 3]),
                ("Jeff Bezos", [877.33, 1]),
                ("Paul Allen", [708.42, 3]),
                ]
    main()

