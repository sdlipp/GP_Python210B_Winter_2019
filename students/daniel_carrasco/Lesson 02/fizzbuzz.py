start = 0
end = 100
while start <=end:
    if start%3==0:
        print('Fizz')
    elif start%5==0:
        print('Buzz')
    else:
        print(start)
    start+=1

