#!/usr/bin/env python3

if __name__ == "__main__":
        
    #series 1
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    
    print("Series 1")
    print(fruits)
    response = input("Please add another fruit > ")
    fruits.append(response)
    print(fruits)
    print()
    
    length = len(fruits)
    response = input(f"Please choose a number between 1 and {length} > ")
    choice = fruits[int(response)-1]
    print(f"The fruit at the number {response} in the list is {choice}")
    print()   

    # adding pineapple using +
    print("Adding Pineapples to the beginning of the list using '+' and display the list")
    fruits = ["Pineapples"] + fruits
    print(fruits)
    print()
    
    #adding guava using insert
    print("Adding Guavas to the beginning of the list using insert() and display the list")
    fruits.insert(0, "Guavas")
    print(fruits)
    print()
    
    # displaying fruits beginning with 'P'
    print("The fruits beginning with the letter 'p' are:")
    for i in range(len(fruits)):
        if (fruits[i][0] == "P"):
            print(fruits[i])
    print()

    # ----------------------------------------------------------------------------------------------
    #series 2
    #Removing last fruit from the list
    print("Series 2")
    print(fruits)
    del fruits[-1]
    print("deleted last fruit in  the list")
    print(fruits)
    
    response = input(f"Which fruit would you like to delete > ")
    if response in fruits:
        fruits.remove(response)
    else:
        print("invalid response, unable to delete. Here's the list again")
        print()
    print(fruits)
    print()
    
    # ----------------------------------------------------------------------------------------------
    # series 3 - Working now!
    print("Series 3")
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    disliked_fruits = []
    for i in range(len(fruits)):
        fruit = fruits[i].lower()
        no_ans = True
        while no_ans:
            ans = input(f"Do you like {fruit}? > ")
            if (ans == 'yes'):
                no_ans = False
                #keep the fruit in the list
            elif (ans == 'no'):
                no_ans = False
                #add to list of fruits to delete
                disliked_fruits = [fruits[i]] + disliked_fruits
            else:
                print("invalid answer, please answer yes or no")
        
    # Now delete fruits
    if len(disliked_fruits) == 0:
        print("You like them all! Nothing to delete")
    else:
        for i in range(len(disliked_fruits)):
            #del_fruit = disliked_fruits[i]
            fruits.remove(disliked_fruits[i])
    
        print("the list with disliked fruits deleted")
        print(fruits)
    print()

    
    # ----------------------------------------------------------------------------------------------
    # series 4
    print("Series 4")
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    new_list = []
    for i in range(len(fruits)):
        new_list.append(fruits[i][::-1])
    print("New list with the contents of the original, but with all the letters in each item reversed")
    print(new_list)
    
    del fruits[len(fruits)-1]
    print("Fruits with last element deleted")
    print(fruits)
    print()
    print("New list again")
    print(new_list)