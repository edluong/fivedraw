import sys

from deck import Deck
from player import Player
import pokerengine as pe

class CardNumberDoesNotExistError(Exception):
    '''Card Number is Not Between 1 to 5! '''

# set up
STARTING_STACK = 200 # 1/2 blinds

player = Player(STARTING_STACK)
cpu = Player(STARTING_STACK)

# prepare the deck
d = Deck()
d.shuffle()

def draw_hand(hand, numCards = 5):
    for _ in range(numCards):
        hand.add_card(d.draw())

def _display(hand, playertype='p'):
    PLAYER_HAND = 'Your Hand:'
    CPU_HAND = 'CPU Hand:'
    PLAYER_RESULT = 'You have:'
    CPU_RESULT = 'CPU has:'
    
    print('\n')
    _hand_msg = CPU_HAND if playertype == 'c' else PLAYER_HAND
    print(_hand_msg,end='\n')
    hand.print_hand()
    _rank = pe.hand_rank(hand.get_hand())
    
    # get the ranking of the hand
    _result, _ = _rank
    _result_msg = CPU_RESULT if playertype == 'c' else PLAYER_RESULT
    print(f'{_result_msg} {_result}')

def main():

    # pass out the cards
    draw_hand(player.get_hand())
    draw_hand(cpu.get_hand())
    
    # display the cards
    _display(player.get_hand())
    _display(cpu.get_hand(), 'c')

    _indexes = [] # input for cards to discard
    while True:

        try:
            discard_choices = input('Which cards to discard? (Type the number, e.g.: 1 2 3) or k to keep: ')

            if 'quit' in discard_choices:
                sys.exit(0)

            for _index in discard_choices.split(' '):
                if _index.lower() == 'k':
                    break
                elif int(_index) < 0 or int(_index) > 5 :
                    raise CardNumberDoesNotExistError
                else:
                    _indexes.append(int(_index))
            break
        except ValueError:
            print('Integer was not entered in!')
        except CardNumberDoesNotExistError:
            print("Card Number doesn't exist! Values must be between 1 through 5!")
    
    if _indexes:    
        player.get_hand().discard(_indexes)

    # re-draw hand
    draw_hand(player.get_hand(), len(_indexes))

    _display(player.get_hand()) # display the card to the player


if __name__ == "__main__":
    
    main()

    while True:
        answer = input('Type "d" to draw; "q" to quit: ')
        if answer.lower() == 'd':
            # reset everything
            d.reload()
            player.get_hand().reset_hand()
            cpu.get_hand().reset_hand()
            
            # load up the hands again 
            main()

        elif answer.lower() == 'q':
            break
        else:
            print(f'{answer} is not a valid command! Type "d" to draw; "q" to quit')
