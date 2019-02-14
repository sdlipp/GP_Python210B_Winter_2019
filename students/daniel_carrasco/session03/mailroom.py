#!/usr/bin/env python3
def main():
    print('\nChoose an action(1 - 3):\n\n\
            1 - Send a Thank You to a single donor.\n\
            2 - Create a Report.\n\
            3 - Quit\n')
    choice = int(input(''))
    if choice == 1:
        thankyou()
    elif choice == 2:
        report()
    elif choice == 3:
        quit()
    else:
        main()


def thankyou():
    choice = ''
    while choice != 3 :
        choice = int(input('\nChoose an action(1-3):\n\
                1 - See Donor List.\n\
                2 - Enter Name.\n\
                3 - Quit submenu\n'))
        if choice == 1:
            for keys in donors.keys():
                print(keys)
        if int(choice) == 2:
            new_name = input('Enter full name\n').title()
            donors.setdefault(new_name,[0,1])
        if int(choice) == 3:
            main()

    return choice
def report():
    row_format ="{:>15}" * 4
    print(row_format.format('Name','Donation ($)','Amount','Average ($)'))
    for key,value in donors.items():
        print(f'{key.title():>15}{value[0]:>15.2f}{value[1]:>15}{value[0]/value[1]:>15.2f}')
    main()


if __name__ == '__main__':
    donors ={'art bart':[1000,1], 'harry scary':[50,5], 'hay boo':[50000,3]}



    main()





donors = ['art lang', 'harry scary', 'jigga boo']
cash = [1000,50,50000]
times = [1,5,3]
if __name__ == '__main__':
    main()
