import pandas as pd
import time
while True:
    try:
        name=input("Enter your name : ")
        subjects=int(input("Enter the number of subjects : "))
        print("Enter the marks for each subject")
        total_marks=0
        sub_marks=[]
        for i in range(subjects):
            marks=int(input(f"Enter subject {i+1} marks : "))
            sub_marks.append(marks)
        [total_marks:=total_marks+i for i in sub_marks]
        avg=total_marks/subjects
        grade=(
            'A' if avg >= 90
            else 'B' if avg >= 80
            else 'C' if avg >= 70
            else 'F'
        )
        # #storing in a file.
        # with open("grades.txt",'w') as file:
        #     file.write(f"\nName : {name}\n")
        #     file.write(f"Subjects : {subjects}\n")
        #     file.write(f"Marks : {sub_marks}\n")
        #     file.write(f"Total Marks : {total_marks}\n")
        #     file.write(f"Average : {avg:.2f}\n")
        #     file.write(f"Grade : {grade}\n")
        # with open ("grades.txt",'r') as file:
        #     print(file.read())
        #storing in a csv format
        for i in range (3,0,-1):
            print(f"Saving your data in {i}")
            time.sleep(1)
        student_data=pd.DataFrame([[name,subjects,sub_marks,total_marks,avg,grade]],
                                columns=["Name","Subjects","Marks","Total Marks","Average","Grade"],index=[1])
        student_data.to_csv("Result.csv",mode='a',index=False,header=not pd.io.common.file_exists("Result.csv"))
        print("Data saved succesfully...\n")
        print(student_data)
        condition = input("Do you want to enter another student? (y/n): ")
        if condition.lower() != 'y':
            break

    except ZeroDivisionError:
        print("Subjects can't be Zero.")
    except ValueError:
        print("Only Numeric Values are allowed.")