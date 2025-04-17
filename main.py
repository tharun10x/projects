import random as rd
import time

def comp_input(chances, data):
    print("Computer's turn..")
    #setting the range for rows and columns for the computer to decided
    if len(chances) !=0:
        inpt = rd.choice(chances)
        #Checking the index range condition
        data [inpt[0]][inpt[1]] ='0' 
        chances.remove(inpt)
    time.sleep(1.5)
    display(data)
        

def display(data):
    print("-------")
    for row in data:
        row_display =f"|{row[0]}|{row[1]}|{row[2]}|"
        print(row_display)
    print("-------")

def user_input():
    
    time.sleep(0.5)
    print("Your turn")
        #Checking the index range condition
    while True:
        try:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if row not in range(3) or col not in range(3):
                print("Index out of range! Please enter a valid row and column (0-2).")
            #Checking the index range condition
            elif [row,col] in chances:
                data[row][col]='X' 
                chances.remove([row,col])
                break                
            else:
                print("That position is already taken.")
        except ValueError:
            print("Invalid input! Please enter a number between 0 and 2.")
    
    display(data)
       
# Initialize game board and available moves
data = [[" " for _ in range(3)] for _ in range(3)]
chances = [[i, j] for i in range(3) for j in range(3)]


display(data)
while chances:
    user_input()
    if chances:  
        comp_input(chances, data)
    