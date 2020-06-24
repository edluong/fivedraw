import sys

from deck import Deck
from hand import Hand
import pokerengine as pe

class CardNumberDoesNotExistError(Exception):
    '''Card Number is Not Between 1 to 5! '''

# set up
player_hand = Hand()
cpu_hand = Hand()

# prepare the deck
d = Deck()
d.shuffle()

def draw_hand(hand, numCards = 5):
    for _ in range(numCards):
        hand.add_card(d.draw())

def main():

    draw_hand(player_hand)
    draw_hand(cpu_hand)
    
    # TODO - need to make this into a display function
    print('\n')
    print('Your Hand:',end='\n')
    player_hand.print_hand()
    player_rank = pe._hand_rank(player_hand.get_hand())

    player_result, _ = player_rank
    print(f'You have: {player_result}')
   
    print('\n')

    print("CPU's Hand: ",end='\n')
    cpu_hand.print_hand()
    cpu_rank = pe._hand_rank(cpu_hand.get_hand())

    cpu_result, _ = cpu_rank
    print(f'CPU has: {cpu_result}')   

    print('\n')

    _indexes = []

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
        player_hand.discard(_indexes)

    # re-draw hand
    draw_hand(player_hand, len(_indexes))

    print('\n')
    print('Your Hand:',end='\n')
    player_hand.print_hand()
    player_rank = pe._hand_rank(player_hand.get_hand())

    player_result, _ = player_rank
    print(f'You have: {player_result}')


if __name__ == "__main__":
    
    main()

    while True:
        answer = input('Type "d" to draw; "q" to quit: ')
        if answer.lower() == 'd':
            # reset everything
            d.reload()
            player_hand.reset_hand()
            cpu_hand.reset_hand()
            
            # load up the hands again 
            main()

        elif answer.lower() == 'q':
            break
        else:
            print(f'{answer} is not a valid command! Type "d" to draw; "q" to quit')
