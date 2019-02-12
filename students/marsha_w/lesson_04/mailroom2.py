#!/usr/bin/env python3

'''Title: Mailroom exercise, part2
Dev: Marsha Wheeler
Date: 02/10/2019
'''


import datetime

donor_dict = {"William Gates":[653772.32, 12.17],
             "Jeff Bezos":[877.33],
             "Paul Allen":[663.23, 43.87, 1.32],
            "Mark Zuckerberg":[1663.23, 4300.87, 10432.0]
              }


user_prompt = "\n".join(("Please choose from the options below:",
          "1 = To view a list of donors type 'list'",
          "2 - Send a Thank You to a single donor",
          "3 - Create a Report",
          "4 - Write a Thank you note to all donors",
          "5 - Exit the Program",
          ">>> "))

def show_list():
    '''Show list of donors'''
    print("Current donors in the database include:")
    donors = list(donor_dict.keys())
    print(('{} \n' * len(donors)).format(*donors))

def send_thank_you():
    '''Ask user for donor name and donor amount'''

    user_name = input("Please enter a donor name:").title() #prompt for donor name

    #create a list of donor names to search
    donors = list(donor_dict.keys())

    #if donor is present is dict:
    if user_name  in donors:
        user_amount= float(input("This donor is already in the database, please enter a new donation amount:"))

        # Append to new amount to existing donor to dict
        donor_dict.setdefault(user_name, []).append(user_amount)

        # Generate an email using string formatting:
        print(
            "Dear Mr./Ms. {:s}, \n We are writing to thank you for your generous donation of ${:.2f} to our organization. \n Sincerely,".format(
                user_name, user_amount))

    else:
        # Append to new donor and new amount to existing donor to dict
        user_amount = float(input("This donor is NEW in the database, please enter a donation amount:"))
        donor_dict[user_name] = user_amount

        # Generate an email using string formatting:
        print(
            "Dear Mr./Ms. {:s}, \n We are writing to thank you for your generous donation of ${:.2f} to our organization. \n Sincerely, ".format(
                user_name, user_amount))

def create_report():
    '''create a new list with donor names, total donation, number of donations
        and average donations'''

    donor_summary = []
    donor_list = list(donor_dict.items())

    for donor in donor_list:
        donor_name = donor[0]
        donor_sum = float(sum(donor[1]))
        donation_num = int(len(donor[1]))
        donor_mean = float(donor_sum / donation_num)
        donor_summary.append([donor_name, donor_sum, donation_num, donor_mean])

        #print(donor_summary)

        def sort_key(donor_summary):
            return donor_summary[1]

        sorted_donor_summary = (sorted(donor_summary, key=sort_key, reverse=True))
        table_header = ["Name", "Total Given", "Numb of Gifts", "Average Gift"]
        sorted_donor_summary.insert(0, table_header)

        dash = '-' * 70
        for i in range(len(sorted_donor_summary)):
            if i == 0:
                print(dash)
                print('{:20} | {:>10s} | {:>15s} | {:>15s}'.format(sorted_donor_summary[i][0], sorted_donor_summary[i][1],
                                                                   sorted_donor_summary[i][2], sorted_donor_summary[i][3]))
                print(dash)
            else:
                print('{:20} ${:>10.1f}{:>20d} ${:>16.1f}'.format(sorted_donor_summary[i][0], sorted_donor_summary[i][1],
                                                                  sorted_donor_summary[i][2], sorted_donor_summary[i][3]))


def write_all():
    date = str(datetime.datetime.now()).split()
    print(date)

    donor_dict_copy = donor_dict
    print(donor_dict_copy)

    for keys in donor_dict:
        out_name = str(keys.strip() + '_' + date[0] + ".txt")
        out_file = open(out_name, 'w')
        print(keys)
        donor_sum = donor_dict_copy[keys] = sum(donor_dict_copy[keys])
        print(donor_sum)
        out_file.write("Dear {:s}, \n We are writing to thank you for your generous total donation of ${:.2f} to our organization. \n Sincerely, ".format(
                keys, donor_sum))
        out_file.close()






def exit_program():
    print("You chose to exit the program, Bye!")
    sys.exit() # exit the interactive script


def main():
    user_response = input(user_prompt)


    switch_func_dict = {
    '1': show_list,
    '2': send_thank_you,
    '3': create_report,
    '4': write_all,
    '5': exit_program,
    }

    switch_func_dict.get(user_response)()





if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()


