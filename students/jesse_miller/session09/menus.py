#!/usr/bin/env python3

def goodbye():
    '''
    Gracefully exits
    '''
    print('Goodbye!')
    sys.exit()


MENU_CHOICE = {'report': donor_report,
               'send': donor_mail_choice,
               'list': donor_list,
               'delete': donor_del,
               'quit': goodbye
               }


def safe_input():
    '''
    This will be for handling keyboard exceptions
    '''
    return None


def donor_mail_choice():
    '''
    This section allows the user to mail a donor
    '''
    current_donor = ''
    donor_list()
    try:
        current_donor = str(input('Who would you like to mail (all for all): '))
        if current_donor in donors:
            mail_send(current_donor)
        elif current_donor == 'all':
            mail_send(current_donor)
        else:
            donor_add(current_donor)
    except (KeyboardInterrupt, EOFError, ValueError):
        safe_input()
