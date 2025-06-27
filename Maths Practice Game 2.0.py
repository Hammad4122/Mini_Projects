import random as rd
import time
import os
import platform
user_mode_choice = None
TIME =[]

def clear_screen():
    if platform.system() == "Windows":
        os.system('CLS')
    else:
        os.system('clear')
def selectingOperand():
    global computer__operand__choice
    global operands
    operands = ['+','-','*','/']
    rd.shuffle(operands)
    computer__operand__choice = rd.choice(operands)
def easy():
    global num1
    global num2
    num1 = rd.randrange(1,10)
    num2 = rd.randrange(1,10)
def medium():
    global num1
    global num2
    num1 = rd.randrange(10,50)
    num2 = rd.randrange(10,50)
def hard():
    global num1
    global num2
    num1 = rd.randrange(50,100)
    num2 = rd.randrange(50,100)
def performingOperations():
    if computer__operand__choice == '+':   return num1 + num2
    elif computer__operand__choice == '-': return num1 - num2
    elif computer__operand__choice == '*': return num1 * num2
    elif computer__operand__choice == '/' : return round(num1 / num2, 2)
def numberOfquestions():
    global number_of_questions
    while True:
        try :
            number_of_questions = int(input("\nEnter number of Questions you want to attempt : "))
            clear_screen()
            break
        except ValueError:
            print("\nInvalid Input...\nPlease enter a numerical value...")
            time.sleep(2)
            continue

print("\033[1m==== MATH PRACTICE GAME ====\033[0m\n".center(120))
while True:
    correct_answers = 0
    print("\033[1m==== Menu ====\033[0m\n".center(120))
    print("1. Play")
    print("2. Mode")
    print("3. Exit")
    options =['Play','Mode','Exit']
    user_choice = input("Enter your choice : ").capitalize()
    if user_choice not in options:
        print("Invlaid Choice.\nPlease Enter correct choice.\n")
        time.sleep(2)
        clear_screen()
        continue
    elif user_choice == options[1]:
        modes = ['Easy','Medium','Hard']
        while True:
            print("1. Easy\n2. Medium\n3. Hard")
            user_mode_choice = input("Enter the mode you want to select : ").capitalize()
            if user_mode_choice not in modes:
                print("\nPlease select a valid mode.")
                time.sleep(2)
                clear_screen()
                continue
            break
    elif user_choice == options[0]:
        numberOfquestions()
        if number_of_questions !=0:
            for i in range(1,number_of_questions+1):
                start_time = 0
                end_time = 0
                total_time = 0
                selectingOperand()
                if user_mode_choice == 'Easy':
                    easy()
                elif user_mode_choice == 'Medium':
                    medium()
                elif user_mode_choice == 'Hard':
                    hard()
                elif user_mode_choice == None:
                    easy()
                answer = performingOperations()
                print("\nYour Question should be displaying on the screen in : ",end=" ",flush=True)
                for j in range(5,0,-1):
                    print(j,end=" ",flush=True)
                    time.sleep(1)
                print(f"\nQuestion {i} : {num1} {computer__operand__choice} {num2}")
                while True:
                    try:
                        if computer__operand__choice == '/':
                            print("\nNote : Enter your answer upto two decimal places.")
                        start_time = time.time()
                        user_answer = float(input("Enter Your Answer : "))
                        break
                    except ValueError:
                        print("\nInvalid Input...\nPlease Enter a Numerical Value")
                        time.sleep(1.5)
                        continue
                print("Checking your Answer....")
                if user_answer == answer:
                    end_time = time.time()
                    time.sleep(1.5)
                    print("\nWhoa! 100% Correct!✅")
                    total_time = round(end_time - start_time,2)
                    TIME.append(total_time)
                    print(f"Time taken to solve this Question : {total_time:.2f} seconds")
                    correct_answers +=1           
                else:
                    time.sleep(1.5)
                    print("Oops! Incorrect...\n")
        else :
            clear_screen()
            continue
        print(f"\nYou have got {correct_answers} correct ✅ answers out of {number_of_questions}.")
        sum_of_time = sum(TIME)
        avg_time_per_question = sum_of_time / (number_of_questions)
        print(f"\nAverage time per question is : {avg_time_per_question:.2f}")
        TIME.clear()
        while True:
            user_input = input("\nPress Enter Key to go back to Menu. ")
            if user_input == '':
                print("\nLoading to menu...")
                time.sleep(2)
                print("Menu Loaded Successfully...")
                clear_screen() 
                break
            else: 
                print("Invalid Input!")
                continue
    elif user_choice == options[2]:
        clear_screen()
        print("Exiting in: ",end=" ",flush=True)
        for i in range(3,0,-1):
            print(i,end=" ",flush=True)
            time.sleep(1)
        break
print("\nGame Exited Successfully...")
time.sleep(2)