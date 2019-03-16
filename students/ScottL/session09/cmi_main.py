#!/usr/bin/env python3

"""
Purpose: provide user interaction with Donor data
Developed by: Scott Lipp
Revision History
    3/16/19 -- Created
"""


import sys
import mailroom_donor as md


class CommLineInter:
    """For enabling the user to interface with Donor data."""

    MENU_HEADER_1 = "\nMenu Options:"
    MENU_HEADER_2 = f"\n{'-' * len(MENU_HEADER_1)}"
    MENU_SELECTIONS = {1: "Add new donation and send 'Thank You' note",
                       2: "Display a report",
                       3: "Send 'Thank You' letters to all donors",
                       4: "Quit"}
    REPORT_HEADER_1 = "\n{:<26}{:<12}{:^17}{:>11}".format("Donor Name", "Total Dollars",
                                                          "Number", "Avg Amount")
    REPORT_HEADER_2 = f"\n{'-' * len(REPORT_HEADER_1)}"
    DONOR_LIST_HEADER = f"\nDonor Name:\n{'-' * 20}"

    def display_user_menu(self):
        """Display the contents of the menu options for the user."""
        print(self.MENU_HEADER_1, self.MENU_HEADER_2)
        for item in self.MENU_SELECTIONS:
            print(f"{item}: {self.MENU_SELECTIONS[item]}")

    @staticmethod
    def get_donor_name(first_last):
        """
        :param first_last: string to indicate which name (first or last) to supply
        :return: string response to prompt
        """
        prompt = f"Please enter the {first_last} name of the donor, " \
                 "'List' to see a list of existing donors, " \
                 "or 'Quit' to return to the Main Menu: "
        return input(prompt)

    def display_donor_list(self):
        """Display all the stored donor names for the user."""
        if md.DonorCollection().name_list():
            print(self.DONOR_LIST_HEADER)
            for name in md.DonorCollection().name_list():
                print(name)
        else:
            print("\n\tThe name list is empty.")

    def validate_name(self):
        """
        Process the expected user input
        :return: 2-element tuple containing the first and last names
        """
        first = self.get_donor_name("FIRST")
        if first.strip().lower() not in ("quit", ""):
            if first.strip().lower() == "list":
                self.display_donor_list()
            else:
                last = self.get_donor_name("LAST")
                if last.strip().lower() == "list":
                    self.display_donor_list()
                else:
                    return first, last

    @staticmethod
    def get_donation_amount():
        """
        Receive and process input from user on the donation amount.
        :return: float-type number of donation amount
        """
        prompt = "Enter the amount of the donation: "
        amount = input(prompt)
        value_error_message = "\nThe entry for 'amount' count was not a valid number. " \
                              "Please try again."
        if amount.strip().lower() not in ("quit", ""):
            try:
                amount = "".join(amount.split(","))
                amount = float(amount.strip("$"))
            except ValueError:
                print(value_error_message)
            else:
                if amount < 0:
                    print("\nUser attempted to enter a negative number; "
                          "please input a positive number for the donation.")
                else:
                    return amount

    def new_donation(self):
        """Organize process flow for calling and validating user input for new donations"""
        try:
            first, last = self.validate_name()
        except TypeError:
            self.main_menu()
        else:
            if last.lower() not in ("quit", ""):
                first = first.capitalize()
                last = last.capitalize()
                amount = self.get_donation_amount()
                if amount is not None:
                    print(md.DonorCollection().new_donation(first, last, amount))

    def report(self):
        """Display donation data report to user."""
        print(self.REPORT_HEADER_1, self.REPORT_HEADER_2)
        report = md.DonorCollection().report()
        if report:
            for item in report:
                print("{:<26}${:>12,}{:^17}${:>11,}".format(item[0], item[1], item[2], item[3]))
        else:
            print("\t\t\t*** No data exists to display ***")

    @staticmethod
    def email():
        """Write text(s) to file simulating email(s) thanking donor(s)."""
        emails = md.DonorCollection().group_email()
        for email in emails:
            try:
                with open(f"{email}.txt", "w") as file:
                    file.write(emails[email])
            except KeyError:
                print("An error occurred with the preparation of the emails.")
            except TypeError:
                print("An invalid data type (i.e. not a string) was used and "
                      "could not be written to file.")

    def main_menu(self):
        """Loop through the main menu to receive and process user input."""
        menu_switch = {1: self.new_donation,
                       2: self.report,
                       3: self.email,
                       4: sys.exit}
        prompt = "\nSelect a number from the menu options (1-4): "
        error = "An invalid input was entered; " \
                "please enter a valid number from the menu."
        while True:
            self.display_user_menu()
            try:
                menu_selection = int(input(prompt))
            except ValueError:
                print(error)
            else:
                try:
                    menu_switch[menu_selection]()
                except KeyError:
                    print(error)


if __name__ == "__main__":
    CommLineInter().main_menu()
