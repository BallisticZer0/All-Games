
import Guess_the_numbers
import ageguesser
import time


def Games():
    print("What game would you like to play?")
    time.sleep(2)
    game_list(['Number Guesser'],)
    
              
               
    

while input("Shall we play a game?  [y|n]") == 'y':
    Games()

else:
    print("Too Bad.")



