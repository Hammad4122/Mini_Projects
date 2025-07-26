# n=5
# for i in range(n+1):
#     print('*'*i)  
#                             #*
#                             # **
#                             # ***
#                             # ****
#                             # *****print('*'*i)
# n=7
# for i in range(1,n+1,2):
#     print(" "*(n-i)," *"*i) 
#         *
#       * * *
#     * * * * *
#   * * * * * * *

# n=7
# for i in range(n,0,-2):
#     print(" "*(n-i)," *"*i)
#   * * * * * * *
#     * * * * *
#       * * *
#         *

# Square
# n=5
# for i in range (n):
#     for j in range(n):
#         print("*",end="")
#     print()
import time
import os
def numberOfrows():
    ROWS = int(input("Enter number of rows : "))
    return ROWS
try : 
    while True:
        print("Chose a pattern (1-4) : ")
        print("1. Right-angled Triangle")
        print("2. Pyramid")
        print("3. Inverted Pyramid")
        print("4. Square")
        choice=input("Enter your choice (1-4) : ")
        rows=numberOfrows()
        if choice == '1':
            print("Generating the Pattern...")
            for i in range(rows+1):
                print('*'*i) 
                time.sleep(0.5)
            print("Pattern Generated Successfully.")
        elif choice == '2':
            print("Generating the Pattern...")
            for i in range(1,rows+1,2):
                print(" "*(rows-i)," *"*i)
                time.sleep(0.5)
            print("Pattern Generated Successfully.")
        elif choice == '3':
            print("Generating the Pattern...")
            for i in range(rows,0,-2):
                print(" "*(rows-i)," *"*i)
                time.sleep(0.5)
            print("Pattern Generated Successfully.")
        elif choice == '4':
            print("Generating the Pattern...")
            for i in range (rows):
                for j in range(rows):
                    print("*",end="")
                print()
                time.sleep(0.5)
            print("Pattern Generated Successfully.")
        cond=input("Do you want to exit (y/n) : ").lower()
        if cond == 'y':
            break
        else :
            os.system('CLS')
    print("Program finished successfully.")
except ValueError:
    print("Only Numeric Values are allowed")

