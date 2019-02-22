from mailroom_part_4 import send_a_thank_you, add_donor, donors

def test_add_donor():
    # Testing whether new donors are added to donors dict.
    add_donor("Chomson", 1234)
    assert 'Chomson' in donors

def test_add_donor_new_donation():
    # Testing whether old donations will be overwritten by new ones.
    add_donor('Lemon Grass', 2020)
    add_donor('Lemon Grass', 3030)
    assert donors['Lemon Grass'][-1] == 3030