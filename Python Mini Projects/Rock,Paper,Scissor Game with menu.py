# ROCK, PAPER, SCISSOR GAME WITH MENU 
import random as rd
import os
import time as t
# GAME WITH MENU :
while True:
    while True:
        print("\033[1m==== MENU ====\033[0m\n".center(120))
        print("1. Play")
        print("2. Exit")
        options = ['Play','Exit']
        user_request = input("Enter your choice : ").capitalize()
        if user_request not in options:
            print("Invalid Choice.")
            print("Please enter correct Choice.")
            continue
        else : 
            break 
    if user_request == options[0] :
        print("Loading Game...")
        t.sleep(3)
        print("Game loaded Successfully.")
        t.sleep(2)
        os.system('CLS')
        items = ['Rock','Paper','Scissor']
        computer_choice = rd.choice(items)
        while True:
            user_choice = input("Enter your choice [Rock,Paper,Scissor] : ").capitalize()
            if user_choice not in items : 
                print("Invalid Choice.")
                print("Please enter correct Choice.")
                continue
            else :
                break
         
        if user_choice == computer_choice :
            print("It's a tie.")
        elif (  (user_choice == 'Rock' and computer_choice == 'Scissor') or
                (user_choice == 'Paper' and computer_choice == 'Rock') or
                (user_choice == 'Scissor' and computer_choice == 'Paper')
            ): 
            print("You win! Hurrah!")
        else:
            print("Computer Wins!")
        print(f"Computer Choice : {computer_choice}")
        while True:
            go_back = input("\nPress enter to go back to menu.")
            if go_back != "":
                print("Error!!!!\n")
                continue
            else :
                print("\nLoading Menu...")
                t.sleep(3.5)
                os.system('CLS')
                break
    elif user_request == options[1] :
        print("Exiting game in:", end=" ", flush=True)
        for i in range(3, 0, -1):
            print(f"{i}", end=" ", flush=True)
            t.sleep(1)
        break
print("\nExited Game Successfully.")