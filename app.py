from deck import Deck
from hand import Hand

# set up

player_hand = Hand()
cpu_hand = Hand()
# prepare the deck

d = Deck()
d.shuffle()

def draw_hand(hand):
    for _ in range(5):
        hand.add_card(d.draw())

def main():
    
    
    draw_hand(player_hand)
    draw_hand(cpu_hand)

    print('Your Hand:',end='\n')
    player_hand.print_hand()
   
    print('\n')

    print("CPU's Hand: ",end='\n')
    cpu_hand.print_hand()

if __name__ == "__main__":
    
    main()

    while True:
        answer = input('Type "d" to draw; "q" to quit: ')
        if answer.lower() == 'd':
            main()
        elif answer.lower() == 'q':
            break
        else:
            print('{} is not a valid command! Type "d" to draw; "q" to quit'.format(answer))
