
# coding: utf-8

# In[9]:


#a simple fibonacci series
#first we need to state what happens if the number of numbers is zero to return zero
#as definition of fibonacci the thrid number will be the addtion of the two number that came before it hence n-2 and n-1 where n is the
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)
    pass


# In[10]:


#the lucas number series
#a similar process to the fibonacci series but this time we will be starding with 2 and 1 instead of 0
#the next prcoess is the same as the fibonacci
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    return lucas(n-2) + lucas(n-1)
    pass


# In[11]:


#here we will make a sum of series that compile both the fibonacci and lucas
#the defult here is the fibonacci which starts from 0 and 1
#other wise when given the parameteres that start with 2 and 1 then it returns the lucas series
def sum_series(n, n0=0, n1=1):
        if n0 == 0 and n1 == 1:
            return fibonacci(n)
        elif n0 == 2 and n1 == 1:
            return lucas(n)
        pass


# In[12]:


if __name__ == "__main__":
    # run some tests
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1

    assert lucas(4) == 7

    assert sum_series(5) == fibonacci(5)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    print("tests passed")

