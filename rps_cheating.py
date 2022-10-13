#Neil Daterao

#Game of Rock-Paper-Scissors that has the computer cheat 1/3 of the time 

import random as r


#Function that plays the game rock-paper-scissors 
def rps(): 
    
    #Starting text for the game
    print("Let's play Rock-Paper-Scissors!\nPlease type a number to make a choice:\n1 -> rock\n2 -> paper\n3 -> scissors\n")
    user_choice = int(input("What do you choose? "))
    computer_choice = None
    
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
    #Since the computer cheats 1/3 of the time, generate a number between (1-9) if num is divisible by 3 (3,6,9), then the computer will cheat, if not, it'll just make a random move. 
    
    cheat = r.randint(1,9)
    if (cheat % 3 == 0):
        if user_choice == 1: 
            computer_choice = 2
            print("I chose:  2 (paper)") 
            
        elif user_choice == 2:
            computer_choice = 3
            print("I chose:  3 (scissors)") 
            
        elif user_choice == 3:
            computer_choice = 1
            print("I chose:  1 (rock)")
            
    
    #If not divisible by 3, (66% chance), pick a random choice 
    else:
    
        computer_choice = r.randint(1,3)
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


#Function that asks if you want to play the game again

def play(game):
    """
    Call the function game again and again as long as the user
    says that they want to play again.
    """
    keep_playing = 'y'
    while keep_playing == 'y':
        game()
        keep_playing = input("Do you want to play again? Type y or n.    ")
        if keep_playing == 'y':
            print("Great!")

    print("Ok. See you next time. Bye, bye!")


### DO NOT DELETE THIS LINE: beg testing

# Calling the function play like this should play rock-paper-scissors
# and then ask the user whether they want to play again. The computer
# will repeat to do this until the user eventually answers 'n' to
# indicate that they don't want to play anymore.
play(rps)
