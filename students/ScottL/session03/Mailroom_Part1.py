
global_donation_list = [("Tom Petty", 5000), ("Tom Petty", 15000), ("Neil Diamond", 20000), ("Neil Diamond", 30000),
                        ("Elton John", 25000), ("Elton John", 25000), ("Elton John", 40000), ("John Lennon", 10000),
                        ("Mick Jagger", 20000), ("Mick Jagger", 10000)]

MENU_HEADER_1 = "\nMenu Options:"
MENU_HEADER_2 = "\n" + "-" * len(MENU_HEADER_1)
MENU_SELECTIONS = {1: "Send a 'Thank You' note", 2: "Print a report", 3: "Quit"}

REPORT_HEADER_1 = "\n{:<26}{:<12}{:^17}{:>11}".format("Donor Name", "Total Dollars", "Number", "Avg Amount")
REPORT_HEADER_2 = "\n" + "-" * len(REPORT_HEADER_1)

DONOR_LIST_HEADER = "\nDonor Name:\n" + "-" * 20


def display_menu_selections():
    """Display the contents of the menu options for the user."""
    print(MENU_HEADER_1, MENU_HEADER_2)
    for item in MENU_SELECTIONS:
        print(item, ": ", MENU_SELECTIONS[item])


def get_user_input():
    """Prompt user to make a selection from the menu and return back to Main Menu."""
    return input("\nSelect a number from the menu options (1-3): ")


def calculate_total_donations_per_donor():
    """Return a list of donors with their total donations in descending order."""
    sorted_donation_list = []
    for item in global_donation_list:
        bool_flag = False
        for entry in sorted_donation_list:
            if entry[0] == item[0]:
                entry[1] += item[1]
                bool_flag = True
        if bool_flag is False:
            sorted_donation_list.append([item[0], item[1]])
    sorted_donation_list.sort(key=lambda x: x[1], reverse=True)
    return sorted_donation_list


def count_number_of_donations_per_donor():
    """Return a dictionary of donors and their respective number of donations."""
    number_of_donations = {}
    for item in global_donation_list:
        if item[0] in number_of_donations:
            number_of_donations[item[0]] += 1
        else:
            number_of_donations[item[0]] = 1
    return number_of_donations


def calculate_average_donation_per_donor(list_of_donations, donation_number):
    """
    Return a dictionary of the mean donation size for each donor.
    arg1 = list containing a string of names in the first element and an integer/float in the second element
    arg2 = list containing a string of names in the first element and an integer in the second element
    """
    average_donation_dict = {}
    for item in list_of_donations:
        average_donation = item[1] / donation_number[item[0]]
        average_donation_dict[item[0]] = average_donation
    return average_donation_dict


def display_donor_report(donors, donations_count, average_donations):
    """
    Display the donors names, total donations, number of donations, and mean donation size.
    arg1 = a list containing names in the first element and a float of total donations in the second
    arg2 = a dictionary with donor names as the key to correspond with donor names in arg1
    arg3 = a dictionary with donor names as the key to correspond with donor names in arg1
    """
    print(REPORT_HEADER_1, REPORT_HEADER_2)
    for item in donors:
        print("{:<26}${:>12}{:^17}${:>11}".format(item[0], item[1], donations_count[item[0]],
                                                  round(average_donations[item[0]])))


def display_donor_names():
    """Print the list of full donor names for the user."""
    print("\n", DONOR_LIST_HEADER)
    donor_list = calculate_total_donations_per_donor()
    for entry in donor_list:
        print(entry[0])


def send_email(name, amount):
    """
    Print a statement thanking the donor for their new donation.
    arg1 = a string containing the donor's name
    arg2 = a number containing the amount of the donation
    """
    print("\nDear {},\nThanks for the generous donation of ${}.\n\nSincerely,\nDonations Staff".format(name, amount))


def add_donation(donor_name):
    """
    Return an appended donation list.
    arg1 = a string containing the donor's name
    """
    donation_amount = input("Please enter the donation amount (or enter 'Quit' to return to "
                                "Main Menu): ").strip("$")
    if donation_amount.strip().lower() == "quit":
        pass
    else:
        global_donation_list.append((donor_name.title(), int(donation_amount)))
        send_email(donor_name.title(), donation_amount)


def receive_new_donation_info():
    """Prompt the user to enter the donor name."""
    user_input = input("\nPlease enter the full name of the donor, 'List' to see a list of existing donors, "
                       "or 'Quit' to return to the Main Menu: ")
    if user_input.strip().lower() == "list":
        display_donor_names()
        receive_new_donation_info()
    elif user_input.strip().lower() == "quit":
        pass
    else:
        add_donation(user_input)


def main_menu():
    """Loop through the main menu to receive and process user input."""
    while True:
        display_menu_selections()
        user_input = get_user_input()
        if user_input == "1":
            receive_new_donation_info()
        elif user_input == "2":
            display_donor_report(calculate_total_donations_per_donor(), count_number_of_donations_per_donor(),
                                 calculate_average_donation_per_donor(calculate_total_donations_per_donor(),
                                                                    count_number_of_donations_per_donor()))
        elif user_input == "3":
            break
        else:
            print("Invalid selection; please try again.")


if __name__ == "__main__":
    main_menu()

