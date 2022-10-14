# RPS-Project for CSC-106
Rock-Paper-Scissors Project. Different variants include the game. 

This project has different variants of rock-paper-scissors

rps_1 is just a plain game of rock-paper-scissors

rps_2 is the same game that asks the user if they want to play again

rps_anti_human is a game that plays against human bias, making the computer more guaranteed to win.
  - > When a user loses, they are going to pick the move that beats the play they just lost to. Therefore, the computer makes a play according to that. 
  - > When a user wins, they generally pick the same move again, so the computer will pick a move that beats the move they just lost to. 
  - > This file needs game_history because it uses a memory object to keep track of the previous games
  
rps_cheating is a game of rock-paper-scissors where the computer cheats 33% of the time. 
