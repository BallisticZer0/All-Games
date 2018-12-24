import Guess_the_numbers
import age_guesser
import Flip_a_Coin
import TIC
import time


game_list = ('Number guesser = 1\n' 'Age Guesser = 2\n' 'Coin flip = 3\n' 'Tic Tac Toe = 4\n' 'Quit = 8\n')

def Games():
    time.sleep(1)
    print("\n\nAlright what game do you want to play\n")
    time.sleep(0.5)
    print(game_list)

if input("Shall we play a game?  [y|n]") == 'y':
    Games()

else:
    print("Too bad.",quit())





time.sleep(1)
games = input("Type the the number next to the game you want to play__:\n\n")
games = int(games)

while(games<= 6 and games>=1): 
    
    if games == 1:
        Guess_the_numbers.The_Number_guessing_game()
        Games()

        
    elif games == 2:
        age_guesser.AGE()        
        Games()

    elif games == 3:
        Flip_a_Coin.COIN()
        Games()

    elif games == 4:
        TIC.tic()
        Games()

    elif games == 5:
        print()

    elif games == 6:
        print()

    elif games == 7:
        print()

    elif games == 8:
        print("Well maybe next time. Good bye")
        time.sleep(1)
        print("\n",quit())

    else:
        quit()
        
        
        



# if input("Press Y if you want to you want to play again. OR press N to play a different game") == 'y':


 #           else:
#                print(game_list)




    


