#!/usr/bin/env python3

"""
Purpose: store data for Donors and provide useful functionality with the data
Developed by: Scott Lipp
Revision History:
    3/16/19 -- Created
"""


class Donor:
    """Store and process data regarding individual donors."""

    def __init__(self, first, last):
        """
        Initialize new donor object with name and list to record donations.
        :param first: string, first name
        :param last: string, last name
        """
        self.first_name = first.capitalize()
        self.last_name = last.capitalize()
        self.donations = []

    def add_donation(self, amount):
        """
        Add new donation to an existing donor in the system.
        :param amount: float, donation amount
        :return string, personalized 'thank-you' email
        """
        self.donations.append(amount)
        return self.solo_email(amount)

    @property
    def count(self):
        """:return integer, the number of donations for a particular donor."""
        return len(self.donations)

    @property
    def total(self):
        """:return float, the total dollar amount of donations for a single donor."""
        return sum(self.donations)

    @property
    def full_name(self):
        """:return string, the first and last name in a single string."""
        return f"{self.first_name} {self.last_name}"

    def solo_email(self, amount):
        """
        Generate the text simulating a 'Thank You' email for a donation.
        :param amount: float, amount of donation
        :return string, personalized 'thank-you' text
        """
        return "\nDear {} {},\nThanks for the generous donation of ${:,.2f}." \
               "\n\nSincerely,\nFundraising Team".format(
                   self.first_name, self.last_name, amount)


class DonorCollection:
    """Store the collection of donor objects, analyze and manipulate the data set."""

    donor_list = []

    def new_donor(self, first, last):
        """
        Create new donor object and store in donor list.
        :param first: string, first name of donor
        :param last: string, last name of donor
        """
        self.donor_list.append(Donor(first, last))

    def new_donation(self, first, last, amount):
        """
        Add new donation to an existing donor object.
        :param first: string, first name
        :param last: string, last name
        :param amount: float, donation amount
        :return: string, text for a 'thank-you' email
        """
        email = ""
        if self.search(first, last) is False:
            self.new_donor(first, last)
        for donor in self.donor_list:
            if donor.first_name == first and donor.last_name == last:
                email = donor.add_donation(amount)
        return email

    def search(self, first, last):
        """
        Return a boolean if a donor name already exists in the list.
        :param first: string, first name
        :param last: string, last name
        :return: Boolean
        """
        found = False
        for donor in self.donor_list:
            if donor.first_name == first and donor.last_name == last:
                found = True
        return found

    def name_list(self):
        """
        :return: list of names sorted by 1) last name, 2) first name
        """
        donors = [[donor.last_name, donor.first_name] for donor in self.donor_list]
        donors.sort(key=lambda x: x[1])
        donors.sort(key=lambda x: x[0])
        return [f"{donor[0]}, {donor[1]}" for donor in donors]

    def report(self):
        """
        :return: list, summarizing all donors sorted by total donation amount.
        """
        sorted_list = []
        for donor in self.donor_list:
            try:
                avg_amount = donor.total / donor.count
            except ZeroDivisionError:
                avg_amount = 0
            finally:
                sorted_list.append([donor.full_name, round(donor.total, 0),
                                    donor.count, round(avg_amount, 0)])
        sorted_list.sort(key=lambda x: x[1], reverse=True)
        return sorted_list

    def group_email(self):
        """
        :return: dict, key is donor name, value is string of 'thank-you' text
        """
        email_dict = {}
        for donor in self.donor_list:
            if donor.count not in (None, 0):
                if donor.count > 1:
                    plurality = "s totaling"
                else:
                    plurality = " of"
                email_dict[donor.full_name] = "Dear {},\n\nThank you so much for your very " \
                                              "generous donation{} ${:,}.\nWe wouldn't be " \
                                              "able to do this without you.\n\nSincerely," \
                                              "\nFundraising Team" \
                                              "".format(donor.full_name, plurality, donor.total)
        return email_dict
