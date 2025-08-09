import pandas as pd
import time
import os
import colorama as cm
def menu():
    print("1. Show A+ Grade Students")
    print("2. Show Students from a Specific City")
    print("3. Show Students who Passed (Marks ≥ 60)")
    print("4. Show Students with Grade C or lower")
    print("5. Exit")
    
def loadingTomenu():
    os.system('CLS')
    print("Loading to menu...")
    time.sleep(2)
    os.system('CLS')

def Aplus_Students ():
    print("Students with A+ grade : \n",df.loc[df['Grade'] == 'A+', ['Name', 'Grade']])

def passed_students():
    print("Passed Students : \n",df.loc[df['Marks'] >= 60,['Name','Marks','Status']])

def specified_city():
    global City
    global studentsOfcity
    global city_list
    global see_student_record
    City = input("Enter the name of the city : ").capitalize()
    city_list = [city_names for city_names in df["City"]]
    if City in city_list:
        studentsOfcity = [name for name,city in zip(df['Name'],df['City']) if city == City]
        print("\nSearching....Please Wait!")
        time.sleep(2)
        print(f"Founded {len(studentsOfcity)} students.")
        time.sleep(2)
        studentsOfcity_df = pd.DataFrame(studentsOfcity)
        print(f"These are the students from {City} : {studentsOfcity_df}")
        see_student_record = input("\nEnter name to see the record of the student : ").capitalize()
        if see_student_record in studentsOfcity:
            print("Loading...\n")
            time.sleep(2)
            print(df[df["Name"] == see_student_record])
        else:
            print("Invalid name entered.")
    else:
        print("No student found!")

def lowerGrade_students():
    print("Students with C grade or lower : \n",df.loc[(df['Grade'] == 'C') | (df['Grade'] == 'F'), ['Name', 'Grade']])

def exit_program():
    print("Closing...")
    time.sleep(3)
    print("Program closed successfully.")
    time.sleep(1.5)

df = pd.read_csv(r"C:\Coding Journey\Pyhton Journey\Mini_Projects\Python Mini Projects\assets\interactive_students_filter_app_data.csv")
while True:
    menu()
    while True:
        try:
            user_choice = int(input("Enter your choice (1-5) : "))
            if user_choice in [1,2,3,4,5]:
                os.system('CLS')
                break
            else:
                print("Please select from 1-5.")
                time.sleep(2)
                os.system('CLS')  
                menu()
                continue       
        except ValueError:
            print("Only numeric Values are Allowed from 1-5.")
            time.sleep(2)
            os.system('CLS')
            menu()
            continue
    if user_choice == 1:
        Aplus_Students()
    if user_choice == 2:
        specified_city()
    if user_choice == 3:
        passed_students()
    if user_choice == 4:
        lowerGrade_students()
    if user_choice == 5:
        os.system('CLS')
        exit_program()
        break
    input("\nPress Enter to go back to menu.")
    loadingTomenu()