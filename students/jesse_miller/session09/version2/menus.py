#!/usr/bin/env python3
'''
Version 2, I think I was once again overthinking things, so now I'm going to
get what I had in the standalone working, then work on paring it down from
there rather than a complete rewrite
'''
def main():
    '''
    Here we go!
    '''
    MainMenu.main()

class MainMenu:
    '''
    This will be the main menu, and the variable storage for menus displayed
    '''
    def __init__(self, name):
        self.name = name


    prompt = '\n'.join(('Welcome to mailroom 0.5!',
                        '',
                        'Please choose from below options:',
                        'report - If you would like a report of donations \
                        totals.',
                        'send - If you would like to send a thank you.',
                        'list - If you would like to see a list of donors.',
                        'delete - Remove a donor',
                        'quit   - Exit.',
                        '>>> '))

    valid_input = ('report', 'quit', 'list', 'send', 'all', 'delete')


    menu_choice = {'report': donor_report,
                   'send': donor_mail_choice,
                   'list': donor_list,
                   'delete': donor_del,
                   'quit': goodbye
                  }


    def donor_mail_choice(self):
        '''
        This section allows the user to mail a donor
        '''
        current_donor = ''
        donor_list()
        try:
            current_donor = str(input('Who would you like to mail \
            (all for all): '))
            if current_donor in donors:
                mail_send(current_donor)
            elif current_donor == 'all':
                mail_send(current_donor)
            else:
                donor_add(current_donor)
        except (KeyboardInterrupt, EOFError, ValueError):
            safe_input()

    def safe_input():
        '''
        This will be for handling keyboard exceptions
        '''
        return None


    def goodbye():
        '''
        Gracefully exits
        '''
        print('Goodbye!')
        sys.exit()


    def main():
        '''
        The main menu and the calls to other functions.
        '''
        while True:
            try:
                response = input(prompt)
            except (KeyboardInterrupt, EOFError):
                continue
            if response not in VALID_INPUT:
                print('\nERROR: Invalid option')
                continue
            menu_choice[response]()
