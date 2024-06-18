import json
import os

# Check if the file exists and is not empty
if os.path.exists('birthdays.json') and os.path.getsize('birthdays.json') > 0:
    with open('birthdays.json', 'r') as f:
        try:
            birthday = json.load(f)
        except json.JSONDecodeError:
            birthday = {}
else:
    birthday = {}

# Function to add an entry to the birthday dictionary
def add_entry():
    name = input('Who do you want to add to the Birthday Dictionary?\n').title()
    date = input('When is {} born?\n'.format(name))
    birthday[name] = date
    with open('birthdays.json', 'w') as f:
        json.dump(birthday, f)
    print(f"{name} was added to my birthday list\n")

# Function to find a birthday date by name
def find_date():
    name = input("Whose birthday do you want to know?\n").title()
    try:
        print(f'{name} is born on {birthday[name]}\n')
    except KeyError:
        print(f'{name} is not in the list\n')

# Function to list all entries in the birthday dictionary
def list_entries():
    print('The current entries in my birthday list are:\n============================================')
    for key in birthday:
        print(key.ljust(31), ':', birthday[key])
    print()

# Main loop to handle user input
while True:
    what_next = input('What do you want to do next? You can: Add, Find, List, Quit\n').capitalize()
    if what_next == 'Quit':
        print('Goodbye')
        break
    elif what_next == 'Add':
        add_entry()
    elif what_next == 'Find':
        find_date()
    elif what_next == 'List':
        list_entries()
    else:
        print("Invalid option. Please choose Add, Find, List, or Quit.")
