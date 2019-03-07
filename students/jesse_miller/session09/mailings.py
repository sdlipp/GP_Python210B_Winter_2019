#!/usr/bin/env python3

import datetime

MAIL = ('\nHello {}, \n'
        '\n'
        'We are writing to thank you for you generous donation\n'
        'to our foundation.  Your contributions for the year \n'
        'total ${:,.2f} in {} disbursements. \n'
        '\n'
        'Again, the foundation thanks you for your support, \n'
        'and we hope to remain in contact with you in this new \n'
        'year.\n'
        '\n'
        'Sincerely, \n'
        'Ecumenical Slobs LLC \n')


def mail_send(current_donor):
    '''
    This function now contains both the singular and the all mails.  I am
    planning on rewriting it to print to terminal and mail for single or all.
    '''
    path = os.getcwd()

    if current_donor in donors:
        donor_math = donors[current_donor]
        directory = path + '/donors/' + current_donor + '/'
        filename = current_donor + ' - ' \
            + datetime.datetime.now().strftime('%s') + '.txt'
        mail_format(current_donor, donor_math, directory, filename)
        print('\nFile created\n')

    else:
        for k in donors:
            current_donor = k
            donor_math = donors[current_donor]
            directory = path + '/donors/' + current_donor + '/'
            filename = current_donor + ' - ' \
                + datetime.datetime.now().strftime('%s') + '.txt'
            mail_format(current_donor, donor_math, directory, filename)
        print('\nFiles created\n')


def mail_format(current_donor, donor_math, directory, filename):
    '''
    This is the formating for the mail print and file.  This allows us to
    have both files and terminal output for single donors as well as multiple
    '''
    print('\n')
    print(MAIL.format(current_donor, (sum(donor_math)), (len(donor_math))))

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(directory + filename, 'w+') as outfile:
        outfile.write('{}\n'.format(MAIL.format(current_donor,\
        (sum(donor_math)), (len(donor_math)))))
