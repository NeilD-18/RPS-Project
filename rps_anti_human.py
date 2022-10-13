#Neil Daterao
#Rock-Paper-Scissors Game that makes moves according to human bias.

import game_history
import random as r 

# Please do not change the following function definitions.
#
# Use these functions to remember a game's result or moves until the
# next round of the game. For example, simply call
# record_computer_win() to store the information that the computer
# just won, and then call previous_result() in the next round to find
# out what the outcome of the previous round was.


#Function definitions utilizing memory object 

def record_computer_win():
    """Record that the computer won."""
    game_history.memory.record_result(1)

def record_human_win():
    """Record that the human won."""
    game_history.memory.record_result(2)    

def record_draw():
    """Record that the game ended in a draw."""
    game_history.memory.record_result(0)

def record_computer_move(move):
    """Record a move by the computer."""
    game_history.memory.record_move("computer", move)

def record_human_move(move):
    """Record a move by the human player."""
    game_history.memory.record_move("human", move)

def previous_result():
    """Return the last recorded result. 0 indicates a draw; 1 indicates a
    computer win; and 2 indicates a human win.
    """
    return game_history.memory.get_previous_result()

def previous_computer_move():
    """Return the last recorded move by the computer."""
    return game_history.memory.get_previous_move("computer")

def previous_human_move():
    """Return the last recorded move by the human player."""
    return game_history.memory.get_previous_move("human")



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






#Rock-Paper-Scissors game 

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
   
   #In case of it being the first time you're running the program, or the previous game was a draw 
    if (previous_result() == None) or (previous_result() == 0): 
        
        computer_choice = r.randint(1,3)
        
        if computer_choice == 1:
            print("I chose:  1 (rock)")
            record_computer_move(computer_choice) 
        elif computer_choice == 2: 
            print("I chose:  2 (paper)")
            record_computer_move(computer_choice)    
        elif computer_choice == 3:
            print("I chose:  3 (scissors)")  
            record_computer_move(computer_choice)
    
    #In case of previous result of being a computer win 
    elif previous_result() == 1:            
       
       #If we won with ROCK last time, we assume that the user is going to pick PAPER the next time. Therefore, we go with SCISSORS to beat the user.
        if previous_computer_move() == 1:
            computer_choice = 3
            print("I chose:  3 (scissors)")
            record_computer_move(computer_choice)
        
        #If we won with PAPER last time, we assume that the user is going to pick SCISSORS the next time. Therefore, we go with ROCK to beat the user 
        elif previous_computer_move() == 2:
            computer_choice = 1
            print("I chose:  1 (rock)")
            record_computer_move(computer_choice)   
        
        #If we won with SCISSORS last time, we assume that the user is going to pick ROCK the next time. Therefore, we go with PAPER to beat the user
        elif previous_computer_move() == 3:
            computer_choice = 2
            print("I chose:  2 (paper)")
            record_computer_move(computer_choice)   
            
   
    #In case of previous result of being a human win 
    elif previous_result() == 2:
       
       #If the user won with ROCK last time, they will generally pick the same again. Therefore the computer will go with PAPER this time to beat the user. 
        if previous_human_move() == 1:
            computer_choice = 2
            print("I chose:  2 (paper)")
            record_computer_move(computer_choice)
        
        #If the user won with PAPER last time, they will generally pick the same again. Therefore the computer will go with SCISSORS this time to beat the user.
        elif previous_human_move() == 2:
            computer_choice = 3
            print("I chose:  3 (scissors)")
            record_computer_move(computer_choice)   
        
        #If the user won with SCISSORS last time, they will generally pick the same again. Therefore the computer will go with ROCK this time to beat the user.
        elif previous_human_move() == 3:
            computer_choice = 1
            print("I chose:  1 (rock)")
            record_computer_move(computer_choice)        
        
        
        
        
    #Test cases to determine winner (9 possible cases, 1,1 1,2 1,3 2,1 2,2 2,3 3,1 3,2 3,3) 
    
    
    #Games where it is a tie (1,1  2,2  3,3)
    if (user_choice == 1 and computer_choice == 1) or (user_choice == 2 and computer_choice == 2) or (user_choice == 3 and computer_choice == 3):
        print("It's a tie.")
        record_human_move(user_choice)
        record_draw()
        return
    
    #Games where user wins (1,3  2,1  3,2)
    elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
        print("You win.")
        record_human_move(user_choice)
        record_human_win()
        return

    #Games where computer wins (1,2  2,3  3,1)
    elif (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 3) or (user_choice == 3 and computer_choice == 1):
        print("I win.")
        record_human_move(user_choice)
        record_computer_win()
        return
    




### DO NOT DELETE THIS LINE: beg testing


play(rps)
