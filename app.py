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
        
        HAND_NUM_COUNTER += 1