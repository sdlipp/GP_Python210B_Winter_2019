#!/usr/bin/env python3

donors = {'Robert Smith': [435.56, 125.23, 357.10],
          'JD Cronise': [123.12],
          'Chris Stapleton': [243.87, 111.32],
          'Dave Lombardo': [63.23, 422.87, 9432.01],
          'Randy Blythe': [223.50, 8120.32],
          'Devin Townsand': [431.12, 342.92, 5412.45],
          }


def donor_list():
    '''
    This when done properly, will print the list of donor names
    '''
    print(f"\n{'-'*15}\nList of Donors:\n{'-'*15}")
    for donor in donors:
        print(donor)
    print(f"{'-'*15}\n")


def donor_report():
    '''
    This will be the donation report section
    '''
    summary = []
    headers = ['Donor Name', 'Total Given', 'Times Donated', 'Average Gift']

    print(f"\n{'-'*80}\n{{:17}} | {{:<19}} | {{:<15}} | {{:<19}}\n{'-'*80}"\
    .format(headers[0], headers[1], headers[2], headers[3]))

    for k, v in donors.items():
        summary.append([k, (sum(v)), (len(v)), (sum(v) / len(v))])
    summary.sort(key=lambda d: d[1], reverse=True)

    for x_value in summary:
        print('{:17} | ${:<18,.2f} | {:<15} | ${:<16,.2f}'.format
              (x_value[0], x_value[1], x_value[2], x_value[3]))
    print(f"{'-'*80}\n")


def donor_add(current_donor):
    '''
    This allows addition of new donors
    '''
    donors[current_donor] = []
    while True:
        try:
            d_num = int(input('How many donations were made: '))
            while d_num > 0:
                new_don = float(input('Enter their donation: '))
                donors[current_donor].append(new_don)
                d_num -= 1
            mail_send(current_donor)
        except (KeyboardInterrupt, EOFError, ValueError):
            break


def donor_del():
    '''
    This section allows the user to delete a donor
    '''
    try:
        donor_list()
        del_donor = str(input('Enter the name of the donor to remove: '))
        del donors[del_donor]
        donor_list()
    except (KeyboardInterrupt, EOFError, ValueError):
        safe_input()
