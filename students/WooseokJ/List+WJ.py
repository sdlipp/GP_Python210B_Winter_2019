
# coding: utf-8

# In[10]:


# Series 1
print("Series 1")
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)
newfruit = input("Please type in a new fruit ")
fruits.append(newfruit)
print(fruits)
index = input("Please enter a number from 0 to 4 ")
selected = fruits[int(index)]
print("You have selected fruit number", index, '"'+selected+'"', "from the list.")
persimmon = ["Persimmon"]
fruits = persimmon + fruits
fruits.insert(0, "Papayas")
for i in fruits:
    if i.startswith("P|p"):
        print(i)

# Series 2
print("Series 2")
print(fruits)
fruits.pop()
print(fruits)
delete = input("Please choose a fruit to delete ")
wrongdelete = input("Enter a fruit to delete from the list:")
while wrongdelete not in fruits:
    wrongdelete = input("That fruit is not on the list. re-enter a valid fruit: ")
    
# Series 3
print("Series 3:")
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
for item in fruits[::]:
        answer = input(f"Do you like {item.lower()}?: ")
        while answer.lower() not in ('yes', 'no'):
            print("Please enter yes or no")
            answer = input(f"Do you like {item.lower()}?: ")
        if answer.lower() == "no":
            fruits.remove(item)
        print(fruits)

# Series 4
print("Series 4")
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
new_fruits = []
for i in fruits:
    reverse = i[::-1]
    new_fruits.append(reverse)
fruits.pop()
print(fruits)
print(new_fruits)

