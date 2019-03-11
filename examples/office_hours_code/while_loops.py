'''
A few examples of using while loops in Python
'''

MENU_OPTIONS = [
    '1. New file',
    '2. Save',
    '3. Save As',
    '4. Quit'
]

while True:
    for menu_item in MENU_OPTIONS:
        print(menu_item)
    option = input("Select an option:")
    if option == '4':
        print("Goodbye!")
        break

inventory = 1
while inventory > 0:
    option = input("Would you like to add or remove an item? ")
    if option.lower() == "add":
        inventory += 1
        print(f"Inventory increased to {inventory}")
        continue
    if option.lower() == "remove":
        inventory -= 1
        print(f"Inventory reduced to {inventory}")
        continue
    print(f"Invalid selection. Inventory remains at {inventory}.")
