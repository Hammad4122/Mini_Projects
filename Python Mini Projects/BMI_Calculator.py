# # BMI Calculator with file handling
import os;import time
while True :
    try:
        weight=float(input("Please enter your weight in kilograms : "))
        height=float(input("Please enter your height in meters : "))
        BMI=weight / (height **2)
        bmi_value=f"Your BMI is : {BMI:.1f} kg/m^2"
        if BMI <= 18.4:
            result="You are Underweight."
        elif BMI >= 18.5 and BMI <=24.9:
            result="Your weight is Normal."
        elif BMI >= 25 and BMI <= 39.9:
            result="You are Overweight."
        elif BMI >=40 :
            result="Obese!"
        with open("BMI RESULT.txt", "w") as file:
            file.write(bmi_value + "\n" + result + "\n")
        with open("BMI RESULT.txt","r") as file:
                print(file.read())
        Exit = input("Do you want to exit (y/n) : ").lower()
        if Exit == 'y':
            break
        elif Exit == 'n':
            os.system('CLS');continue
    except ValueError:
        print("Please enter a Numerical Value.");time.sleep(2);os.system('CLS')
    except ZeroDivisionError:
        print("Height can not be zero.");time.sleep(2);os.system('CLS')


# BMI calculator with PANDAS Dataframes
# import pandas as pd

# try:
#     name = input("Enter your name: ")
#     weight = float(input("Enter your weight in kg: "))
#     height = float(input("Enter your height in meters: "))
#     BMI = weight / height ** 2
#     bmi_value = f"{BMI:.1f}"

#     if BMI <= 18.4:
#         result = "Underweight"
#     elif BMI <= 24.9:
#         result = "Normal"
#     elif BMI <= 39.9:
#         result = "Overweight"
#     else:
#         result = "Obese"

#     # Create a DataFrame row
#     entry = pd.DataFrame([[name, weight, height, bmi_value, result]],
#                          columns=["Name", "Weight (kg)", "Height (m)", "BMI", "Status"],index=[1])

#     # Append to CSV
#     entry.to_csv("bmi_log.csv", mode="a", index=False, header=not pd.io.common.file_exists("bmi_log.csv"))

#     print("BMI entry saved successfully!\n")
#     print(entry)
    

# except ValueError:
#     print("Please enter a numerical value.")
# except ZeroDivisionError:
#     print("Height cannot be zero.")
