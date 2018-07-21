import Guess_the_numbers
import age_guesser
import Flip_a_Coin
import tic_tac_tow
import time

game_list = ('Number guesser = 1\n' 'Age Guesser = 2\n' 'Coin flip = 3' 'Tic Tac Toe = 4')

def Games():
    print("Alright what game do you want to play\n")
    time.sleep(1)
    print(game_list)

if input("Shall we play a game?  [y|n]") == 'y':
    Games()

else:
    print("Too bad.",quit())






    
time.sleep(2)
games = input("Type the the number next to the game you want to play__:\n\n")
games = int(games)

while(games<= 6 and games>=1): 
    
    if games == 1:
        Guess_the_numbers.The_Number_guessing_game()

        
    elif games == 2:
        age_guesser.AGE()

    elif games == 3:
        Flip_a_Coin.COIN()
        



# if input("Press Y if you want to you want to play again. OR press N to play a different game") == 'y':


 #           else:
#                print(game_list)




    
