#!/usr/bin/env python3

import sys

global_donation_list = {"Tom Petty": [5000, 15000],
                        "Neil Diamond": [20000, 30000],
                        "Elton John": [25000, 25000, 40000],
                        "John Lennon": [25000],
                        "Mick Jagger": [20000, 10000]}
MENU_HEADER_1 = "\nMenu Options:"
MENU_HEADER_2 = "\n" + "-" * len(MENU_HEADER_1)
MENU_SELECTIONS = {1: "Send a 'Thank You' note to individual donor",
                   2: "Display a report",
                   3: "Send 'Thank You' letters to all donors",
                   4: "Quit"}
REPORT_HEADER_1 = "\n{:<26}{:<12}{:^17}{:>11}".format(
                    "Donor Name", "Total Dollars", "Number", "Avg Amount")
REPORT_HEADER_2 = "\n" + "-" * len(REPORT_HEADER_1)
DONOR_LIST_HEADER = "\nDonor Name:\n" + "-" * 20


def display_user_menu():
    """Display the contents of the menu options for the user."""
    print(MENU_HEADER_1, MENU_HEADER_2)
    for item in MENU_SELECTIONS:
        print(item, ": ", MENU_SELECTIONS[item])


def donation_calcs():
    """
    Calculate the number of donations, and the total and average amounts.
    :return: Return a list of donors with their total donations in descending order.
    """
    sorted_donation_list = []
    for item in global_donation_list:
        try:
            total_donation = round(sum(global_donation_list[item]))
        except TypeError:
            print("Error: A value other than a number is listed as a "
                  "donation 'amount' for '{}'.".format(item))
        else:
            number_of_donations = len(global_donation_list[item])
            try:
                sorted_donation_list.append([item, total_donation, number_of_donations,
                                            round(total_donation / number_of_donations)])
            except ZeroDivisionError:
                sorted_donation_list.append([item, total_donation, number_of_donations, 0])
    sorted_donation_list.sort(key=lambda x: x[1], reverse=True)
    return sorted_donation_list


def display_donor_names():
    """Print the list of full donor names for the user."""
    print("\n", DONOR_LIST_HEADER)
    for entry in global_donation_list:
        print(entry)


def draft_email(name, amount):
    """
    Display text reminiscent of an email thanking a donor.
    :param name: donor name
    :param amount: amount of donation
    """
    print("\nDear {},\nThanks for the generous donation of ${:,.2f}."
          "\n\nSincerely,\nFundraising Team".format(name, amount))


def input_donation_amount(donor_name):
    """
    Receive input from user on amount of donation. Process accordingly.
    :param donor_name: name of donor
    """
    donation_amount = input("Please enter the donation amount "
                            "(or enter 'Quit' to return to Main Menu): ").strip("$")
    if donation_amount.strip().lower() != "quit":
        try:
            donation_amount = float(donation_amount)
        except ValueError:
            print("The entry for 'amount' count was not a valid number. Please try again.")
            input_donation_amount(donation_amount)
        else:
            if donor_name in global_donation_list:
                global_donation_list[donor_name].append(float(donation_amount))
            else:
                global_donation_list[donor_name] = [float(donation_amount)]
            draft_email(donor_name.title(), float(donation_amount))


def input_donor_name():
    """Prompt the user to enter the donor name."""
    donor_name = input("\nPlease enter the full name of the donor, "
                       "'List' to see a list of existing donors, "
                       "or 'Quit' to return to the Main Menu: ")
    if donor_name.strip().lower() != "quit":
        if donor_name.strip().lower() == "list":
            display_donor_names()
            input_donor_name()
        else:
            input_donation_amount(donor_name)


def display_report():
    """Call the function to calculate total & avg donations and then display a report."""
    print(REPORT_HEADER_1, REPORT_HEADER_2)
    for item in donation_calcs():
        print("{:<26}${:>12,}{:^17}${:>11,}".format(item[0], item[1], item[2], item[3]))


def write_emails():
    """Write 'Thank You' emails to all donors for all donations."""
    for donor in donation_calcs():
        if donor[2] > 1:
            donation_plurality = "s totaling"
        else:
            donation_plurality = " of"
        with open("{}.txt".format(donor[0]), "w") as file:
            file.write("Dear {},\n\nThank you so much for your very generous donation{} "
                       "${:,}.\nWe wouldn't be able to do this without you." 
                       "\n\nSincerely,\nFundraising Team".
                       format(donor[0], donation_plurality, donor[1]))


def main_menu():
    """Loop through the main menu to receive and process user input."""
    menu_switch = {1: input_donor_name,
                   2: display_report,
                   3: write_emails,
                   4: sys.exit}
    while True:
        display_user_menu()
        try:
            menu_selection = int(input("\nSelect a number from the menu options (1-4): "))
        except ValueError:
            print("An invalid input was entered; please enter a valid number from the menu.")
        else:
            menu_switch[menu_selection]()


if __name__ == "__main__":
    main_menu()
