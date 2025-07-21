import pandas as pd
import os

def view_contact():
    if os.path.exists("contact_book.csv"):
        entry = pd.read_csv("contact_book.csv")
        print("\nAll Contacts:\n", entry)
    else:
        print("No contact book found.")

def add_contact():
    name = input("Enter name: ").capitalize()
    while True:
        contact_number = input(f"Enter {name}'s contact number: ")
        if len(contact_number) != 11:
            print("Contact number must be 11 digits.")
        elif not contact_number.isdigit():
            print("Contact number must contain only digits.")
        else:
            break

    new_entry = pd.DataFrame([[name, contact_number]], columns=['Name', 'Ph#'])
    new_entry.to_csv('contact_book.csv', mode='a', index=False, header=not os.path.exists('contact_book.csv'))
    print("Contact added successfully.")

def search_contact():
    if not os.path.exists("contact_book.csv"):
        print("No contact book found.")
        return

    entry = pd.read_csv("contact_book.csv")
    search_name = input("Enter name to search: ").capitalize()
    results = entry[entry['Name'] == search_name]
    if not results.empty:
        print("\nSearch Result:\n", results)
    else:
        print("Contact not found.")

def delete_contact():
    if not os.path.exists("contact_book.csv"):
        print("No contact book found.")
        return

    entry = pd.read_csv("contact_book.csv")
    name_to_delete = input("Enter name to delete: ").capitalize()
    entry = entry[entry['Name'] != name_to_delete]
    entry.to_csv('contact_book.csv', index=False)
    print("Contact deleted if it existed.")

def user_choice():
    while True:
        try:
            choice = int(input("\n1. View contact\n2. Add contact\n3. Search contact\n4. Delete contact\n5. Exit\n\nEnter your choice (1-5): "))
            if choice == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                view_contact()
            elif choice == 2:
                add_contact()
            elif choice == 3:
                search_contact()
            elif choice == 4:
                delete_contact()
            elif choice == 5:
                print("Exiting Contact Book. Goodbye!")
                break
            else:
                print("Please enter a number between 1-5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Start the program
user_choice()
