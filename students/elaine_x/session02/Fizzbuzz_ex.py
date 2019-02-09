##########################
#Python 210
#Session 02 - Fizz Buzz
#Elaine Xu
#Jan 21,2019
###########################

#Write a program that prints the numbers from 1 to 100 inclusive.
#But for multiples of three print “Fizz” instead of the number.
#For the multiples of five print “Buzz” instead of the number.
#For numbers which are multiples of both three and five print “FizzBuzz” instead.

for i in range(1,100+1):
    #checking for numbers which are multiples of both three and five
    if i%3 == 0 and i%5 == 0:
        print('FizzBuzz')
    #checking for multiples of three
    elif i%3 == 0:
        print('Fizz')
    # checking for multiples of five
    elif i%5 == 0:
        print('Buzz')
    else:
        print(i)


