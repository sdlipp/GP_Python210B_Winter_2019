#!/usr/bin/env python3
'''
This is where we start.  Building out the donor database and manipulation
Everything else in this program will be dependent on this one.
'''
class Donor():
    '''
    Hello, I am new.  Anything below "donors =" is old and can be ignored
    '''
    def __init__(self, name):
        self.name = name
        self.donation = []

    def donation_add(self, new_don):
        '''
        Adding donations
        '''
        self.donation.append(new_don)

    @property
    def num_dons(self):
        '''
        Number of donations made
        '''
        return len(self.donation)

    @property
    def total_dons(self):
        '''
        Total of donations
        '''
        return sum(self.donation)

    @property
    def avg_don(self):
        '''
        Average of donations
        '''
        try:
            return self.total_dons / self.num_dons
        except ZeroDivisionError:
            return 0


class DonorListings:
    """
    This is what contains the donor lists, and allows us to query for single
    or total donors.  This is also where the report function resides.
    """

    def __init__(self):
        self.donors_dict = {'Robert Smith': [435.56, 125.23, 357.10],
                            'JD Cronise': [123.12],
                            'Chris Stapleton': [243.87, 111.32],
                            'Dave Lombardo': [63.23, 422.87, 9432.01],
                            'Randy Blythe': [223.50, 8120.32],
                            'Devin Townsand': [431.12, 342.92, 5412.45],
                           }

    def donor_creation(self, donor_name):
        '''
        Here we can create a new donor
        '''
        new_donor = Donor(donor_name)
        self.donors_dict[donor_name] = new_donor
        return new_donor


    def donor_delete(self, del_donor):
        '''
        Deleting donors as required
        '''
        del self.donors_dict[del_donor]


    def donor_find(self, donor_name):
        '''
        This is the search function for donors
        '''
        try:
            return self.donors_dict[donor_name]
        except KeyError:
            return self.donor_creation(donor_name)


    def donor_list(self):
        '''
        Finally here is our listing function for donors
        '''
        donor_list = [donor.name for donor in self.donors_dict.values()]
        sorted_donors = sorted(donor_list)
        return sorted_donors


    def donor_report(self):
        '''
        This will be the donation report section
        '''
        summary = []
        headers = ['Donor Name', 'Total Given', 'Times Donated', 'Average Gift']

        print(f"\n{'-'*80}\n{{:17}} | {{:<19}} | {{:<15}} | {{:<19}}\n{'-'*80}"\
        .format(headers[0], headers[1], headers[2], headers[3]))

        #pylint: disable=C0103
        for k, v in self.donors_dict.items():
            summary.append([k, (sum(v)), (len(v)), (sum(v) / len(v))])
        summary.sort(key=lambda d: d[1], reverse=True)

        for x_value in summary:
            print('{:17} | ${:<18,.2f} | {:<15} | ${:<16,.2f}'.format
                  (x_value[0], x_value[1], x_value[2], x_value[3]))
        print(f"{'-'*80}\n")
