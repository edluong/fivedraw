from deck import Deck
# set up
hand = []
d = Deck()
d.shuffle()

def draw_hand():
    for _ in range(5):
        hand.append(d.draw())

def main():
    
    print('Your Hand:',end='\n')
    
    draw_hand()

    for card in hand:
        print(card)
    
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
