# import random as rd
# items = ['Rock','Paper','Scissor']
# computer_choice = rd.choice(items)
# user_choice = input("Enter you choice [Rock,Paper,Scissor] : ")
# user_choice = user_choice.capitalize()
# if user_choice not in items:
#     print("Invalid Input")
# else:
#     if user_choice == computer_choice:
#         print("It's a tie.")
#     elif ((user_choice == 'Rock' and computer_choice == 'Scissor') or
#           (user_choice == 'Paper' and computer_choice == 'Rock') or
#           (user_choice == 'Scissor' and computer_choice == 'Paper')):
#         print("You win! Hurrah!")
#     else:
#         print("Computer Wins!")

# My code : 
import random as rd
import os
import time as t
# GAME MENU :
while True:
    while True:
        print()
        print("\033[1mMENU\033[0m\n".center(120))
        print("1. Play")
        print("2. Exit")
        options = ['Play','Exit']
        user_request = input("Enter your choice : ").capitalize()
        if user_request not in options:
            print("Invalid Choice")
            print("Please enter correct Choice.")
            continue
        else : 
            break 
    if user_request == options[0] :
        os.system('CLS')
        items = ['Rock','Paper','Scissor']
        computer_choice = rd.choice(items)
        while True:
            user_choice = input("Enter you choice [Rock,Paper,Scissor] : ")
            if user_choice.capitalize() not in items : 
                print("Invalid Choice")
                print("Please enter correct Choice.")
                continue
            else :
                break
         
        if user_choice == computer_choice :
            print("It's a tie.")
        elif (  (user_choice.capitalize() == 'Rock' and computer_choice.capitalize() == 'Scissor') or
                (user_choice.capitalize() == 'Paper' and computer_choice.capitalize() == 'Rock') or
                (user_choice.capitalize() == 'Scissor' and computer_choice.capitalize() == 'Paper')
            ): 
            print("You win! Hurrah!")
        else: 
            print("Computer Wins!")
    elif user_request == options[1] :
        print("Exiting game in:", end=" ", flush=True)
        for i in range(3, 0, -1):
            print(f"{i}", end=" ", flush=True)
            t.sleep(1)
        break
print("\nExited Game Successfully.")
#GAME :
# while True:
#     items = ['Rock','Paper','Scissor']
#     computer_choice = rd.choice(items)
#     user_choice = input("Enter you choice [Rock,Paper,Scissor] : ")
#     if user_choice.capitalize() not in items : 
#         print("Invalid Input")
#     else : 
#         if user_choice == computer_choice :
#             print("It's a tie.")
#         elif ((user_choice.capitalize() == 'Rock' and computer_choice.capitalize() == 'Scissor') or
#             (user_choice.capitalize() == 'Paper' and computer_choice.capitalize() == 'Rock') or
#             (user_choice.capitalize() == 'Scissor' and computer_choice.capitalize() == 'Paper')
#             ) : 
#             print("You win! Hurrah!")
#         else: 
#             print("Computer Wins!")
#     cond = input("Do you want to play again (yes/no) : ").capitalize()
#     if cond != 'yes' : 
#         break
# print("Game End!")
