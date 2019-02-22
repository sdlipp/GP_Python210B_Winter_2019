from mailroom_part_4 import donors, add_donor, sum_donors_donations, sort_by_values

def test_add_donor():
    # Testing whether new donors are added to donors dict.
    add_donor("Chomson", 1234)
    assert 'Chomson' in donors

def test_add_donor_new_donation():
    # Testing whether old donations will be overwritten by new ones.
    add_donor('Lemon Grass', 2020)
    add_donor('Lemon Grass', 3030)
    assert donors['Lemon Grass'][-1] == 3030

def test_sum_donors_donations():
    add_donor('Flutter By', 3)
    add_donor('Flutter By', 2)
    assert sum_donors_donations()['Flutter By'] == 5

def test_sort_by_values():
    test_dict = {'one': 1, 'two': 2, 'three': 3}
    sorted_test_dict = sort_by_values(test_dict)
    assert sorted_test_dict[0][0] == 1
