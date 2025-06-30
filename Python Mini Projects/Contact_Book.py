import pandas as pd
import os
import time
print("===== Contact Book =====\n".center(120))
print("Welocome to your contact book.".center(120).upper())
print("==== Options ====")
print("1. Add Contact\n2. View All Contacts\n3. Search Contact\n4. Delete Contact\n5. Close \n========================")
# ===== Contact Book =====
# 1. Add Contact
# 2. View All Contacts
# 3. Search Contact
# 4. Delete Contact
# 5. Exit
# ========================
entry=pd.DataFrame()
contacts = pd.DataFrame()
choice = input("Enter you choice (1-5) : ")
if choice == '1':
    os.system('CLS')
    print("Add Contact".center(120).upper())
    name = input("Enter the name : ")
    ph_number = int(input(f"Enter {name} phone number : "))
    email = input(f"Enter {name} Email : ")
    contact_detail = {
        "Name" : [name],
        "Phone Number" : [ph_number],
        "Email" : [email]
    }
    entry = pd.DataFrame(contact_detail,index=[1])
    entry.to_csv("contact_book.csv", index=False, mode='a', header= not pd.io.common.file_exists("contact_book.csv"))
    for i in range(3,0,-1):
        print(f"Adding contact in {i}.")
        time.sleep(1)
    print("Contact added successfully.")
elif choice == '2':
    os.system('CLS')
    contacts = pd.read_csv("contact_book.csv")
    print("Contacts\n".center(120))
    print(contacts)
elif choice == '3':
    print("Search Contact".center(120))
    name = input("Search contact by name : ")
    for name in entry
