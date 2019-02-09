#!/usr/local/bin/python3

import sys

donors = {
    "Anne Ant": [1.00],
    "Bonnie Bug": [20.00, 10.00],
    "Chuck Cat": [2.00, 2.00, 2.00],
    "Donna Dog": [5000.00, 2500.00, 1.50],
    "Edna Ent": [.30, .50, .10]
}

email = {
    "greeting": "\nHello {}\n\n",
    "body": "We would like to thank you for your generous donation of ${}.\n\n",
    "closing": "Best Regards,\n",
    "signature": "The Foundation\n"
}


def create_report():
    """
    This function prints out a report with the following parameters:
    Donor Name, Total Given, Number of Gifts, Average Gift Amount
    """
    header = ("Donor Name", "| Total Given", "| Num Gifts", "| Average Gift")
    row = " ".join(["{:20s} {:>20s} {:>20s} {:>20s}"]).format(*header)
    header_length = len(row)
    print("\n" + row)
    print("=" * header_length)
    for key, value in sorted(donors.items()):
        value_sum = str(sum(value))
        value_len = str(len(value))
        value_ave = str(sum(value)/(len(value)))
        row_format = (key, "$" + value_sum, value_len, "$" + value_ave)
        donor_row = " ".join(["{:20s} {:>20s} {:>20s} {:>20s}"]).format(*row_format)
        print(donor_row)
    print("\n")


def send_email(input_name, donation):
    """
    Function to send automated "Thank you" email to donor.
    :param input_name: User provided full name of donor.
    :param donation: Donation amount in dollars.

    This function uses a dictionary as a template for the letter.
    """
    print('{greeting}' '{body}' '{closing}' '{signature}'.format(**email).format(input_name, donation))


def list_donors():
    # Provides a list of donor names when "list" is chosen in send_thankyou().
    print("\nDonor List:")
    print(", ".join(donors.keys()))
    print("\n")


def add_donation(input_name):
    """
    Function to add new donations to accounts.
    :param input_name: User provided full name of donor.
    """
    donation_amount = float(input("Please enter " + input_name + "'s donation:  "))
    donors[input_name].append(donation_amount)
    print(str(donation_amount) + " added to " + input_name)
    send_email(input_name, str(donation_amount))


def add_donor(input_name):
    """
    Function to add new donors if they are not in the donors dictionary.
    :param input_name: User provided full name of donor
    """
    # Adds new donors if their name is not found in the donors dictionary.
    donor_list = []
    donors.update({input_name: donor_list})
    print(input_name + " has been added to the list.")
    add_donation(input_name)


def send_thankyou():
    # Provides user options for send thank you prompt.
    while True:
        input_name = input("Please provide the full name of the donor. Use or use 'list' to see a list of donors, "
                           "or use q to return to main menu.\nEnter full name here:  ")
        if input_name == "q":
            break
        elif input_name in donors.keys():
            add_donation(input_name)
            break
        elif input_name == 'list':
            list_donors()
        elif input_name not in donors.keys():
            add_donor(input_name)
            break


def exit_system():
    print("Exiting program.")
    sys.exit()


def main():
    """
    Function to provide a main menu. A dictionary is used as a dispatch table for the rest of the program.
    """
    main_menu = {
        "1": send_thankyou,
        "2": create_report,
        "3": exit_system,
    }
    while True:
        user_input = input("Choose the number of the operation you wish to perform:"
                           "\n(1) Send a Thank You\n(2) Create a Report\n(3) quit\nEnter here: ")

        if user_input in main_menu.keys():
            main_menu.get(user_input)()
            continue
        else:
            print("Please try again.")
            continue


if __name__ == '__main__':
    main()
