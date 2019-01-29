
# coding: utf-8

# In[54]:


#gird 1
# define the variables
box=2
bar=4
size=4
#for loop that creates the boxes acording to the variables
#the first being the cap of the box
for i in range(box):
    print ('+'+' -'*size+' +'+' -'*size+' +')
#defines the body of the box
    for row in range(bar):
                print('|'+'  '*size+' |'+'  '*size+' |')
#finish the box
print('+'+' -'*size+' +'+' -'*size+' +')


# In[77]:


# grid 3
# use of two veriables
# define the varaibles the number of boxes and their size
# tried a different porcess from the first and second as we cretae more boxes then 2
#the hoizonal of the box is determinde by the size multiplied by 3 with vertical being size of the box plus 1
numb =5
size =5
def grid(numb, size):
    for i in range(numb):
        row = "+" + " - " * size
        print(row * numb + "+")
        for i in range(size):
            colum = ("|" + (" " * size * 3)) * (numb + 1)
            print(colum)
    print(row * numb + "+")
grid(numb,size)


# In[1]:


#grid 2
#second exercise that changes the size of the boxes
#size determines the number of - the box will have
size=3
def grid_2(size):    
    for i in range(2):
        row = "+" + " - " * size
        print(row, row, "+")
        colum = "|" + " " * (size * 3)
        for i in range(size):
            print(colum, colum, "|")
    print(row, row, "+")
grid_2(size)

