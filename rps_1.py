#Neil Daterao

#Game of Rock-Paper-Scissors

import random as r


#Function that plays the game rock-paper-scissors 
def rps(): 
    
    #Starting text for the game
    print("Let's play Rock-Paper-Scissors!\nPlease type a number to make a choice:\n1 -> rock\n2 -> paper\n3 -> scissors\n")
    user_choice = int(input("What do you choose? "))
    
    
    #Sequence of if statements to show what choice the user picked
    if user_choice == 1:
        print("You chose:  1 (rock)")
    elif user_choice == 2: 
        print("You chose:  2 (paper)")   
    elif user_choice == 3:
        print("You chose:  3 (scissors)")   
    else:
        print("Not a valid choice, game over!")  #If the user gives an input that is not 1,2 or 3
        return
    
    #Choice of rock-paper-scissors for the computer
    computer_choice = r.randint(1,3)
   
   
    #Sequence of if statements to show what choice the computer picked
    if computer_choice == 1:
        print("I chose:  1 (rock)")
    elif computer_choice == 2: 
        print("I chose:  2 (paper)")   
    elif computer_choice == 3:
        print("I chose:  3 (scissors)")  
        
        
    #Test cases to determine winner (9 possible cases, 1,1 1,2 1,3 2,1 2,2 2,3 3,1 3,2 3,3) 
    
    
    #Games where it is a tie (1,1  2,2  3,3)
    if (user_choice == 1 and computer_choice == 1) or (user_choice == 2 and computer_choice == 2) or (user_choice == 3 and computer_choice == 3):
        print("It's a tie.")
        return
    
    #Games where user wins (1,3  2,1  3,2)
    elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
        print("You win.")
        return

    #Games where computer wins (1,2  2,3  3,1)
    elif (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 3) or (user_choice == 3 and computer_choice == 1):
        print("I win.")
        return
    
### DO NOT DELETE THIS LINE: beg testing

# Calling the function rps like this, should play one complete round of
# rock-paper-scissors.

rps()
