#!/usr/bin/env python3

"""
Purpose: test features from mailroom_donor module
Developed by: Scott Lipp
Revision History:
    3/16/19 -- Created
"""


import mailroom_donor as md


def test_new_donor_creation():
    """Test donor attributes in new donor object."""
    donor = md.Donor("Garth", "Brooks")
    assert donor.first_name == "Garth"
    assert donor.last_name == "Brooks"
    assert donor.full_name == "Garth Brooks"


def test_new_donor_donation():
    """Test adding donation to existing donor object."""
    donor = md.Donor("Toby", "Keith")
    donor.add_donation(25000)
    assert donor.count == 1
    assert donor.total == 25000


def test_new_donor_email():
    """Test that a string is correctly returned and augmented when a new donation is made"""
    donor = md.Donor("Tim", "McGraw")
    email = donor.add_donation(40000)
    assert "Sincerely" in email
    assert "$40,000" in email


def test_donor_collection_list():
    """Test that donor list correctly stores donors as objects"""
    donor = md.DonorCollection()
    donor.new_donor("George", "Strait")
    assert len(donor.donor_list) == 1
    assert isinstance((donor.donor_list[0]), object)


def test_donor_collection_add_donation_existing_donor():
    """Tests that a donation can be correctly attributed to an existing donor."""
    donor = md.DonorCollection()
    donor.donor_list = []
    donor.new_donor("Eric", "Church")
    donor.new_donation("Eric", "Church", 5000)
    assert donor.donor_list[0].total == 5000


def test_donor_collection_add_donation_new_donor():
    """Tests that a new donor can be created and then credited with the donations."""
    donor = md.DonorCollection()
    donor.donor_list = []
    donor.new_donation("Montgomery", "Gentry", 12000)
    assert donor.donor_list[0].total == 12000


def test_donor_collection_search():
    """Tests that existing donors return True and non-existent return False"""
    donor = md.DonorCollection()
    donor.donor_list = []
    donor.new_donor("Jon", "Pardi")
    assert donor.search("Jon", "Pardi") is True
    assert donor.search("Trisha", "Yearwood") is False


def test_donor_collection_list_multiple():
    """
    Tests that donor list is a class attribute as intended, such that multiple
    instances of 'DonorCollection' objects can access the same donor list.
    """
    donor1 = md.DonorCollection()
    donor1.donor_list = []
    donor1.new_donor("JoDee", "Messina")
    donor2 = md.DonorCollection()
    donor2.new_donor("Reba", "MacIntire")
    assert len(donor2.donor_list) == 2


def test_donor_collection_return_list():
    """Tests that strings of donor names are correctly returned"""
    donor = md.DonorCollection()
    donor.donor_list = []
    donor.new_donor("Faith", "Hill")
    donor_list = donor.name_list()
    assert "Faith" in donor_list[0]


def test_donor_collection_report():
    """
    Tests that all donor calcs for the report are made correctly for
    both types of donors: those who have made donations, and those who
    are in the system but haven't made a donation.
    """
    donor = md.DonorCollection()
    donor.donor_list = []
    donor.new_donor("Alan", "Jackson")
    donor.new_donor("Chris", "Stapleton")
    donor.new_donation("Chris", "Stapleton", 15000)
    donor.new_donation("Chris", "Stapleton", 5000)
    assert donor.report()[0] == ["Chris Stapleton", 20000, 2, 10000]
    assert donor.report()[1] == ["Alan Jackson", 0, 0, 0]


def test_donor_collection_email():
    """
    Tests that strings are correctly formatted to personalize emails to be sent to donors.
    Also verifies that names in the donor list who haven't made donations do not
    receive emails (i.e. they're not in the keys of the dictionary).
    """
    donor = md.DonorCollection()
    donor.donor_list = []
    donor.new_donor("Dierks", "Bentley")
    donor.new_donor("Thomas", "Rhett")
    donor.new_donor("Luke", "Bryan")
    donor.new_donation("Dierks", "Bentley", 10000)
    donor.new_donation("Dierks", "Bentley", 10000)
    donor.new_donation("Thomas", "Rhett", 5000)
    emails = donor.group_email()
    assert "donations totaling $20,000" in emails["Dierks Bentley"]
    assert "donation of $5,000" in emails["Thomas Rhett"]
    assert "Luke Bryan" not in emails.keys()
