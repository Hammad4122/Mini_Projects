import random as rd
import time
def operationTOperform():
    if computer__operand__choice == '+':    return num1 + num2
    elif computer__operand__choice == '-':  return num1 - num2
    elif computer__operand__choice == '*':  return num1 * num2
    else:   return round(num1 / num2, 2)
correct_answers = 0
numberOfquestions = int(input("Enter number of questions : "))
for i in range(1,numberOfquestions + 1): 
    operands = ['+','-','*','/']
    computer__operand__choice = rd.choice(operands)
    num1 = rd.randrange(1,30)
    num2 = rd.randrange(1,30)
    answer = operationTOperform()  
    print(f"Question {i} : {num1} {computer__operand__choice} {num2} = ?")
    while True: 
        if computer__operand__choice == '/':
            print("Note: Answer to 2 decimal places.")
        user_answer = float(input("Enter your answer : "))
        print("Checking your answer....Please wait.")
        if user_answer == answer :
            time.sleep(1.5)
            print("Whoa! 100% Correct!✅\n")
            correct_answers+=1
            break
        else:
            time.sleep(1.5)
            print("Oops! Incorrect Answer.\n")
            break
print(f"You have got {correct_answers} correct ✅ answers out of {numberOfquestions}.")
