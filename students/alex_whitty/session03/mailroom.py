import sys  # imports go at the top of the file


# Data Structure
donor_db = {"William Gates, III": [653772.32, 12.17],
            "Jeff Bezos": [877.33],
            "Paul Allen": [663.23, 43.87, 1.32],
            "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
            "Elon Musk": [2263.23, 3300.87, 15432.0],
            }



# Input/Output
prompt = "\n".join(("Thanking your donors for their generous gifts!",
          "Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Exit",
          ">>> "))

# Features

def view_donor_names():

    for donor in donor_db.keys():
        print(donor)


def thank_you():

    answer = input("Please enter Full Name.>>>")
    if answer.lower() == 'list':
        for donor in donor_db.keys():
            print(donor)
    else:
        if answer in donor_db:
            current_donor(answer)
        else:
            add_donor(answer)


def current_donor(donor):

    amount = input("Please enter donor amount.>>>")
    donor_db[donor].append(float(amount))


def sort_key(donor_db):
    return donor_db[:]


def add_donor(new_donor):

    donor_amount = input("What is the donation amount?")
    donor_db[new_donor] = [float(donor_amount)]
    print(donor_db)
    print('Thanks, {} for your generous donation.'.format(new_donor))



def report():
    summary = []
    headers = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    print()
    print("{:20} | {:10} | {:10} | {}".format(headers[0], headers[1], headers[2], headers[3]))
    print("-" * 80)

    for k, v in donor_db.items():
        total = (sum(v))
        times = (len(v))
        avg = (sum(v) / len(v))
        summary.append([k, total, times, avg])
    summary.sort(key=lambda d: d[1], reverse=True)
    for i in summary:
        print("{:20}  ${:>12,.2f}{:>10}     ${:>14,.2f}".format(i[0], i[1], i[2], i[3]))
        print("")


def exit_program():
    print("Good-Bye!")
    sys.exit()  # exit the interactive script

# Processing
def main():
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "1":
            thank_you()
        elif response == "2":
            report()
            pass
        elif response == "3":
            exit_program()
        else:
            print("Not a valid option!")


if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()

sorted(donor_db, key=sort_key)