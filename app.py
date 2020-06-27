from game import Game

if __name__ == "__main__":
    # set up
    STARTING_STACK = 200 # 1/2 blinds
    game = Game(STARTING_STACK)
    game.discard_choice()

    while True:
        answer = input('Type "d" to draw; "q" to quit: ')
        if answer.lower() == 'd':
            # reset everything
            game.reset()
            game.deal_cards()
            
            # load up the hands again 
            game.discard_choice()

        elif answer.lower() == 'q':
            break
        else:
            print(f'{answer} is not a valid command! Type "d" to draw; "q" to quit')
