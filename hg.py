import pandas as pd
import os

FILENAME = "student_records.csv"

# Create file with correct structure if it doesn't exist
if not os.path.exists(FILENAME):
    pd.DataFrame(columns=["RollNo", "Name", "Age", "Marks"]).to_csv(FILENAME, index=False)


def add_students():
    df = pd.read_csv(FILENAME)
    n = int(input("How many students do you want to add? "))
    new_entries = []

    for _ in range(n):
        roll = input("Enter Roll Number: ")
        if roll in df["RollNo"].astype(str).values:
            print("❌ Roll Number already exists. Skipping.")
            continue
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))
        new_entries.append({"RollNo": roll, "Name": name, "Age": age, "Marks": marks})

    if new_entries:
        pd.DataFrame(new_entries).to_csv(FILENAME, mode='a', index=False, header=False)
        print(f"✅ {len(new_entries)} student(s) added.\n")
    else:
        print("⚠️ No new student added.\n")


def view_students():
    df = pd.read_csv(FILENAME)
    if df.empty:
        print("📂 No student records found.")
    else:
        print("\n📋 Current Student Records:\n")
        print(df.to_string(index=False))
    print()


def delete_student():
    df = pd.read_csv(FILENAME)
    roll = input("Enter Roll Number to delete: ")

    if roll not in df["RollNo"].astype(str).values:
        print("❌ Roll Number not found.\n")
        return

    df = df[df["RollNo"].astype(str) != roll]
    df.to_csv(FILENAME, index=False)
    print(f"✅ Student with Roll No {roll} deleted.\n")


def update_student():
    df = pd.read_csv(FILENAME)
    roll = input("Enter Roll Number to update: ")

    if roll not in df["RollNo"].astype(str).values:
        print("❌ Roll Number not found.\n")
        return

    idx = df[df["RollNo"].astype(str) == roll].index[0]
    print("Leave field empty to keep current value.")

    new_name = input(f"Enter new name (current: {df.at[idx, 'Name']}): ") or df.at[idx, 'Name']
    new_age = input(f"Enter new age (current: {df.at[idx, 'Age']}): ") or df.at[idx, 'Age']
    new_marks = input(f"Enter new marks (current: {df.at[idx, 'Marks']}): ") or df.at[idx, 'Marks']

    df.at[idx, 'Name'] = new_name
    df.at[idx, 'Age'] = int(new_age)
    df.at[idx, 'Marks'] = float(new_marks)

    df.to_csv(FILENAME, index=False)
    print("✅ Student record updated.\n")


# === Main Program Loop ===
while True:
    print("=== Student Record Manager ===")
    print("1. Add Student(s)")
    print("2. View Records")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_students()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("👋 Exiting. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please try again.\n")
