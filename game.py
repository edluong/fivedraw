import sys

from deck import Deck
from player import Player
from pokerengine import hand_rank, winninghand

class CardNumberDoesNotExistError(Exception):
    '''Card Number is Not Between 1 to 5! '''

class Game:

    states = {
            1: 'predeal',
            2: 'deal',
            3: 'draw',
            5: 'showdown'
    }

    def print_players_stack(self, player):
        print(f'Stack Size: {player.stack_size()}')
    
    def _draw_hand(self, hand, deck, numCards = 5):
        for _ in range(numCards):
            hand.add_card(deck.draw())

    def _display(self, player, playertype='p'):
        PLAYER_HAND = 'Your Hand:'
        CPU_HAND = 'CPU Hand:'
        PLAYER_RESULT = 'You have:'
        CPU_RESULT = 'CPU has:'
        
        print('\n')
        _hand_msg = CPU_HAND if playertype == 'c' else PLAYER_HAND
        print(_hand_msg, end='\n')
        player.get_hand().print_hand()
        _rank = hand_rank(player.get_hand().get_hand())

        # get the ranking of the hand
        _result, _ = _rank
        _result_msg = CPU_RESULT if playertype == 'c' else PLAYER_RESULT
        print(f'{_result_msg} {_result}')

        # get stack size
        self.print_players_stack(player)
    
    def deal_cards(self):
        # deal the cards out the the players
        self._draw_hand(self.player.get_hand(), self.deck)
        self._draw_hand(self.cpu.get_hand(), self.deck)

        # display the cards
        self._display(self.player)
        self._display(self.cpu, 'c')
            
    def __init__(self, starting_stack, turn_state = 1, pot_size = 0):
        
        # initial game values
        self.starting_stack = starting_stack
        self.turn_state = turn_state
        self.pot_size = pot_size

        # initialize players
        self.player = Player(self.starting_stack)
        self.cpu = Player(self.starting_stack)

        # prepare the deck
        self.deck = Deck()
        self.deck.shuffle()

        # deal the cards
        self.deal_cards()

    def discard_choice(self):
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
            self.player.get_hand().discard(_indexes)

        # re-draw hand
        self._draw_hand(self.player.get_hand(), self.deck, len(_indexes))
        self._display(self.player) # display the card to the player


    def update_turn_state(self,state):
        self.turn_state = state
    
    def current_turn_state(self):
        return self.states.get(self.turn_state)

    def add_pot_size(self, new_amt):
        self.pot_size+=new_amt
    
    def current_pot_size(self):
        return self.pot_size

    def reset_pot_size(self):
        self.pot_size = 0

    def reset_game(self):
        self.reset_pot_size()
        self.turn_state = 1

    def get_players_bet(self):
        wager = input('wager: ')
        self.player.bet(int(wager))
    
    def reset(self):
        self.deck.reload()
        self.player.get_hand().reset_hand()
        self.cpu.get_hand().reset_hand()
