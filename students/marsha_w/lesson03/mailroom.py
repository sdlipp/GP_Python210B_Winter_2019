#!/usr/bin/env python3

'''Title: Mailroom exercise, part1
Dev: Marsha Wheeler
Date: 01/29/2019
'''

import sys

#data structure stored as a global namespace

donorList = [("William Gates", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ]

#print(donorList)

userPrompt = "\n".join(("Please choose from the options below:",
          "1 = To view a list of donors type 'list'",
          "2 - Send a Thank You",
          "3 - Create a Report",
          "4 - Exit the Program",
          ">>> "))
#print(userPrompt)

def showList():
    '''Show list of donors'''
    print("Current donors in the database include:")
    for names in range(len(donorList)):
        print(donorList[names][0])

def sendThankYou():
    '''Ask user for donor name and donor amount'''

    userNameResponse = input("Please enter a donor name:").title() #prompt for donor name
    #create a list of donor names to search
    donorNames = []
    for names in range(len(donorList)):
        donorNames.append(donorList[names][0])
    #print(donorNames)

    # if donor is present in the donor list
    if userNameResponse in donorNames:
        userDonationAmt = float(input("This donor is already in the database, please enter a new donation amount:"))

        #Append to new amount to existing donor in list
        for index, donor in enumerate(donorList):
            if userNameResponse in donor:
                donor[1].append(userDonationAmt)

        # Generate an email using string formatting:
        print("Dear Mr./Ms. {:s}, \n We are writing to thank you for your generous donation of ${:.2f} to our organization. \n Sincerely,".format(userNameResponse, userDonationAmt))
    # if donor is not present in donor list
    else:
        userDonationAmt = float(input("This donor is NEW in the database, please enter a donation amount:"))
        donorList.append((userNameResponse, [userDonationAmt]))

        # Generate an email using string formatting:
        print("Dear Mr./Ms. {:s}, \n We are writing to thank you for your generous donation of ${:.2f} to our organization. \n Sincerely, ".format(
                userNameResponse, userDonationAmt))

def createReport():
    '''create a new list with donor names, total donation, number of donations
    and average donations'''
    donorSummary = []
    for index, donor in enumerate(donorList):
        donorName = donor[0]
        donorSum = float(sum(donor[1]))
        donationNum = int(len(donor[1]))
        donorMean = float(donorSum / donationNum)
        donorSummary.append([donorName, donorSum, donationNum, donorMean])

    def sort_key(donorSummary):
        return donorSummary[1]
    sortedDonorSummary = (sorted(donorSummary, key=sort_key, reverse=True))
    tableHeader = ["Name", "Total Given", "Numb of Gifts", "Average Gift"]
    sortedDonorSummary.insert(0,tableHeader)

    dash = '-' * 70
    for i in range(len(sortedDonorSummary)):
        if i == 0:
            print(dash)
            print('{:20} | {:>10s} | {:>15s} | {:>15s}'.format(sortedDonorSummary[i][0], sortedDonorSummary[i][1], sortedDonorSummary[i][2], sortedDonorSummary[i][3]))
            print(dash)
        else:
            print('{:20} ${:>10.1f}{:>20d} ${:>16.1f}'.format(sortedDonorSummary[i][0], sortedDonorSummary[i][1], sortedDonorSummary[i][2],  sortedDonorSummary[i][3]))




def exitProgram():
    print("You chose to exit the program, Bye!")
    sys.exit() # exit the interactive script



def main():
    while True:
        userResponse = input(userPrompt)
        if userResponse == '1':
            showList()
        elif userResponse == '2':
            sendThankYou()
        elif userResponse == '3':
            createReport()
        elif userResponse == '4':
            exitProgram()

        else:
            print("Not a valid option!")

if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()




