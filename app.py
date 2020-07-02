from game import Game

if __name__ == "__main__":
    # set up
    HAND_NUM_COUNTER = 1
    STARTING_STACK = 200 # 1/2 blinds
    game = Game(STARTING_STACK)

    while True:
        if HAND_NUM_COUNTER == 1:
            print('Welcome to fivedraw!')
        print(f'Hand Number #{HAND_NUM_COUNTER}')

        game.round()
        # game.deal_cards()
        # game.betting_round()
        # game.discard_choice()
        # # level 0 cpu should randomly discard
        # game.betting_round()
        # game.payout()
        # game.check_state()

        HAND_NUM_COUNTER += 1