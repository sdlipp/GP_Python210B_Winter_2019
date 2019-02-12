#!/usr/bin/env python3
def main():

    print('\noptions\n')
    print('A = Send a Thank You')
    print('\n')

    response = input('what do you want to do?').upper()
    if response == 'A':
        thankyou()
    pass

def thankyou():
    response2 = input('Do you want to see a list?').lower()
    if response2 == 'yes':
        row_format ="{:>15}" * 3
        print(row_format.format('Name','Donation','Amount'))
        for name,amount,time in zip(donors,cash,times):
            print(f'{name.title():>15}{"$ "+str(amount):>15}{time:>15}')

    response3 = input('Add a name?').lower()
    if response3 == 'yes':
        response4 = input('Add first and last').title()
        donors.append(response4)
        response5 = input('Donation amount?')
        cash.append(response5)
        times.append(1)

    response6 = input('Select name')
    for num,value in enumerate(donors):
        if response6 in value:
            print(f'Thank you {donors[num]} for total donations of {cash[num]} with total donations at {times[num]}!')




donors = ['art lang', 'harry scary', 'jigga boo']
cash = [1000,50,50000]
times = [1,5,3]
if __name__ == '__main__':
    main()
