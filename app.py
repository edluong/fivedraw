from deck import Deck
from hand import Hand
import pokerengine as pe

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

    # TODO - need defensive checking around input
    # TODO - need to write logic if dont want to discard
    # TODO - hand is not sorted (see example below)
    # example: 
    # Your Hand:
    # 1: (2, 'Hearts')
    # 2: (10, 'Clubs')
    # 3: (8, 'Clubs')
    # 4: (4, 'Clubs')
    # 5: (2, 'Clubs')
    # You have: pair
    discard_choices = input('Which cards to discard? (Type the number, e.g.: 1 2 3): ')
    _indexes = [int(_index) for _index in discard_choices.split(' ')]

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
