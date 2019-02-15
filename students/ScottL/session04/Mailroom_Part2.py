
global_donation_list = [{"Name": "Tom Petty", "Amount": 5000},
                        {"Name": "Tom Petty", "Amount": 15000},
                        {"Name": "Neil Diamond", "Amount": 20000},
                        {"Name": "Neil Diamond", "Amount": 30000},
                        {"Name": "Elton John", "Amount": 25000},
                        {"Name": "Elton John", "Amount": 25000},
                        {"Name": "Elton John", "Amount": 40000},
                        {"Name": "John Lennon", "Amount": 10000},
                        {"Name": "Mick Jagger", "Amount": 20000},
                        {"Name": "Mick Jagger", "Amount": 10000}]
MENU_HEADER_1 = "\nMenu Options:"
MENU_HEADER_2 = "\n" + "-" * len(MENU_HEADER_1)
MENU_SELECTIONS = {1: "Send a 'Thank You' note to individual donor",
                   2: "Print a report",
                   3: "Send 'Thank You' letters to all donors",
                   4: "Quit"}
REPORT_HEADER_1 = "\n{:<26}{:<12}{:^17}{:>11}".format(
                    "Donor Name", "Total Dollars", "Number", "Avg Amount")
REPORT_HEADER_2 = "\n" + "-" * len(REPORT_HEADER_1)
DONOR_LIST_HEADER = "\nDonor Name:\n" + "-" * 20


def display_menu_selections():
    """Display the contents of the menu options for the user."""
    print(MENU_HEADER_1, MENU_HEADER_2)
    for item in MENU_SELECTIONS:
        print(item, ": ", MENU_SELECTIONS[item])


def get_user_input():
    """Prompt user to make a selection from the menu and return back to Main Menu."""
    return input("\nSelect a number from the menu options (1-4): ")


def calc_total_donations_per_donor():
    """Return a list of donors with their total donations in descending order."""
    sorted_donation_list = []
    for item in global_donation_list:
        bool_flag = False
        for entry in sorted_donation_list:
            if entry["Name"] == item["Name"]:
                entry["Amount"] += item["Amount"]
                bool_flag = True
        if bool_flag is False:
            sorted_donation_list.append({"Name": item["Name"], "Amount": item["Amount"]})
    sorted_donation_list.sort(key=lambda x: x["Amount"], reverse=True)
    return sorted_donation_list


def count_num_of_donations_per_donor():
    """Return a dictionary of donors and their respective number of donations."""
    number_of_donations = {}
    for item in global_donation_list:
        if item["Name"] in number_of_donations:
            number_of_donations[item["Name"]] += 1
        else:
            number_of_donations[item["Name"]] = 1
    return number_of_donations


def calc_avg_donation_per_donor(list_of_donations, donation_number):
    """
    Return a dictionary of the mean donation size for each donor.
    arg1 = list containing a string of names in the first element
            and an integer/float in the second element
    arg2 = list containing a string of names in the first element
            and an integer in the second element
    """
    average_donation_dict = {}
    for item in list_of_donations:
        average_donation = item["Amount"] / donation_number[item["Name"]]
        average_donation_dict[item["Name"]] = average_donation
    return average_donation_dict


def display_donor_report(donors, donations_count, average_donations):
    """
    Display the donors names, total donations, number of donations, and mean donation size.
    arg1 = a list containing names in the first element and the total donation in the second
    arg2 = a dictionary with donor names as the key to correspond with donor names in arg1
    arg3 = a dictionary with donor names as the key to correspond with donor names in arg1
    """
    print(REPORT_HEADER_1, REPORT_HEADER_2)
    for item in donors:
        print("{:<26}${:>12}{:^17}${:>11}".format(item["Name"], item["Amount"],
                                                  donations_count[item["Name"]],
                                                  round(average_donations[item["Name"]])))


def display_donor_names():
    """Print the list of full donor names for the user."""
    print("\n", DONOR_LIST_HEADER)
    donor_list = calc_total_donations_per_donor()
    for entry in donor_list:
        print(entry["Name"])


def send_email(name, amount):
    """
    Print a statement thanking the donor for their new donation.
    arg1 = a string containing the donor's name
    arg2 = a number containing the amount of the donation
    """
    print("\nDear {},\nThanks for the generous donation of ${}."
          "\n\nSincerely,\nDonations Staff".format(name, amount))


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
        global_donation_list.append({"Name": donor_name.title(), "Amount": int(donation_amount)})
        send_email(donor_name.title(), donation_amount)


def receive_new_donation_info():
    """Prompt the user to enter the donor name."""
    user_input = input("\nPlease enter the full name of the donor, "
                       "'List' to see a list of existing donors, "
                       "or 'Quit' to return to the Main Menu: ")
    if user_input.strip().lower() == "list":
        display_donor_names()
        receive_new_donation_info()
    elif user_input.strip().lower() == "quit":
        pass
    else:
        add_donation(user_input)


def menu1_thank_you():
    """Exercise the 1st option from the main menu.  Return 'True' to keep loop active."""
    receive_new_donation_info()
    return True


def menu2_print_report():
    """Exercise the 2nd option from the main menu. Return 'True' to keep loop active."""
    display_donor_report(calc_total_donations_per_donor(),
                         count_num_of_donations_per_donor(),
                         calc_avg_donation_per_donor(calc_total_donations_per_donor(),
                                                     count_num_of_donations_per_donor()))
    return True


def menu3_print_emails():
    """Write 'Thank You' emails to all donors for all donations.  Return True to maintain loop"""
    for donor in calc_total_donations_per_donor():
        with open("{}.txt".format(donor["Name"]), "w") as file:
            file.write("Dear {},\n\nThank you so much for your very generous donation(s) "
                     "totaling ${}.\nWe wouldn't be able to do this without you." 
                     "\n\nSincerely,\nExecutive Team".format(donor["Name"], donor["Amount"]))
    return True


def menu4_break_loop():
    """Return a boolean False to break the loop."""
    return False


def main_menu():
    """Loop through the main menu to receive and process user input."""
    break_indicator = True
    menu_switch = {1: menu1_thank_you,
                   2: menu2_print_report,
                   3: menu3_print_emails,
                   4: menu4_break_loop}
    while break_indicator is True:
        display_menu_selections()
        try:
            user_input = int(get_user_input())
            break_indicator = menu_switch[user_input]()
        except ValueError:
            print("An invalid input was entered; please enter a valid number from the menu.")


if __name__ == "__main__":
    main_menu()
    pass
