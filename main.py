# Tic tac toe game based on python

from helpers import draw_board , check_turn, check_for_win
import os    
# This module will be used to clear the screen with right command

spots = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5',
         6 : '6', 7 : '7', 8 : '8', 9 : '9'}

#draw_board(spots)    

# Was not working from this point then realised that i hadn't put spots as 
# an argument in draw board def functions

#spots[1] = "X"
#print("\nSecond Draw:")
#draw_board(spots)

playing = True
complete = False
turn = 0
prev_turn = -1

while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    # This will clear/reset the output screen everytime
    draw_board(spots) 
    if prev_turn == turn:
        print("\nPlease pick a valid spot!!")
    prev_turn = turn

    print (f"\nPlayer {str((turn % 2) +1)}'s turn : Pick your spot or press q to quit.")
    # Now create a input option for the players
    choice = input()
    if choice == 'q':
        playing = False
    elif str.isdigit(choice) and int(choice) in spots:
        if not spots[int(choice)] in {'X','O'}:
            turn += 1
            spots[int(choice)] = check_turn(turn)
    # Now whatever integer choice we choose from 1-9 will we used as
    # key for the dictionary 'spots'; and we equated this key pair with
    # output from turn function which can be X or O   
    
    # what this will do is when one loop is completed it will add +1
    # to the turn variable and the X and O will shuffle around at the
    # positions of key pair

    # Btw str.isdigit(choice) just ensures input is in digits and not decimals
    # and is required in line 34 because output would turn out wrong

# logic for win :
#  1. if (1,2,3) || (4,5,6) || (7,8,9) {basically x+1} is X then win for X or vice-versa for O
#  2. if (1,4,7) || (2,5,8) || (3,6,9) {basically x+3 }is X then win for X or vice-versa for O
#  3. if(1,5,9) || (3,5,7) {basically x+2 || x+4 }is X then win for X or vice-versa for O
    
    if check_for_win(spots): 
        playing = False
        complete = True
    # This checks if the game has been won and stops the playing
    if turn > 8: playing = False 
    # This checks for a draw to stop the playing and since there are only 9 spots
    # and turn starts from 0 to 8

# Now get out of the loop and show the results 
# Draw the board again for one last time
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)
# NOW if there was a winner, say who won
if complete: 
    if check_turn(turn) == 'X': print ("\nPlayer 1 WINS!!")
    else: print ("\nPlayer 2 WINS!!")
else:
    if not choice == 'q':
       # This will be case of tie 
       print ("\nIt's a tie :(")
    if choice == 'q':   
       print ("\nGame stopped.")

print ("\nThanks for playing!")
