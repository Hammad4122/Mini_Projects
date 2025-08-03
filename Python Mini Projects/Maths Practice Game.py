import random as rd
import time
import os
def operationTOperform():
    if computer__operand__choice == '+':    return num1 + num2
    elif computer__operand__choice == '-':  return num1 - num2
    elif computer__operand__choice == '*':  return num1 * num2
    else:   return round(num1 / num2, 2)
while True:
    try:
        correct_answers = 0
        numberOfquestions = int(input("Enter number of questions : "))
        for i in range(1,numberOfquestions + 1): 
            operands = ['+','-','*','/']
            computer__operand__choice = rd.choice(operands)
            num1 = rd.randrange(1,30)
            num2 = rd.randrange(1,30)
            answer = operationTOperform()  
            while True: 
                try :
                    print(f"Question {i} : {num1} {computer__operand__choice} {num2} = ?")
                    if computer__operand__choice == '/':
                        print("Note: Answer to 2 decimal places.")
                    user_answer = float(input("Enter your answer : "))
                    print("Checking your answer....Please wait.") 
                    time.sleep(1.5)
                    if user_answer == answer :
                        print("Whoa! 100% Correct!✅\n")
                        correct_answers+=1
                        break
                    else:
                        print("Oops! Incorrect Answer.\n")
                        break
                except ValueError:
                    print("Please enter an integer value!!!")
                    time.sleep(2.5);os.system('CLS')
                    continue
    except ValueError:
        print("Please enter an integer value!!!")
        time.sleep(2.5);os.system('CLS')
        continue
    print(f"You have got {correct_answers} correct ✅ answers out of {numberOfquestions}.")
    user_exit_choice = input("Do you want to continue (y/n) : ")
    if user_exit_choice == 'y':
        os.system('CLS')
        continue
    elif user_exit_choice == 'n':
        print("Exiting...")
        time.sleep(3)
        break
    else :
        print("Invalid Input")
        print("Exiting automatically")
        time.sleep(3)
        break
