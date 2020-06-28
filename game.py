import sys

from cpu import CPU
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
  
    def _draw_hand(self, hand, deck, numCards = 5):
        for _ in range(numCards):
            hand.add_card(deck.draw())

    def _display(self, player, playertype='p'):
        '''
            Prints out the stats

            Example Output:

            Your Hand:
            1: (2, 'Diamonds')
            2: (2, 'Spades')
            3: (5, 'Spades')
            4: ('King', 'Spades')
            5: ('Ace', 'Spades')
            You have: pair
            Stack Size: 200
        '''
        PLAYER_HAND = 'Your Hand:'
        CPU_HAND = 'CPU Hand:'
        PLAYER_RESULT = 'You have:'
        CPU_RESULT = 'CPU has:'
        
        # hand details
        _hand_msg = CPU_HAND if playertype == 'c' else PLAYER_HAND
        print(f'\n{_hand_msg}', end='\n')
        player.hand.print_hand()

        # get the ranking of the hand
        _rank = hand_rank(player.hand.hand)
        _result, _ = _rank
        _result_msg = CPU_RESULT if playertype == 'c' else PLAYER_RESULT
        print(f'{_result_msg} {_result}')

        # get stack size
        print(f'Stack Size: {player.stack}')
    
    def deal_cards(self):
        # deal the cards out the the players
        self._draw_hand(self.player.hand, self.deck)
        self._draw_hand(self.cpu.hand, self.deck)

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
        self.cpu = CPU(self.starting_stack)

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
            self.player.hand.discard(_indexes)

        # re-draw hand
        self._draw_hand(self.player.hand, self.deck, len(_indexes))
        self._display(self.player) # display the cards to the player
    
    def betting_round(self, player):
        try:
            action = input('Bet(b) Check(c) Fold(f): ').lower()
            if action == 'f':
                self.payout([self.cpu])
            elif action == 'c':
                self.cpu.cpu_decision()
            elif action == 'b':
                bet_amount = input('bet amount: ')
                self.game.add_pot_size(self.player.bet(bet_amount))
                print(f'You bet: {bet_amount}')
        except:
            raise Exception('There seems to be a problem...')
            
    def payout(self, players):
        '''
            finds the winner
            pay the winner with the pot
            set the pot to 0
            
            Parameters: List[Players]
            
            Returns: void
        '''
        payout_amount = self.pot_size / len(players)

        # pay all the winners
        for player in players:
            player.winpot(payout_amount)
        
        # reset the pot size
        self.pot_size = 0
  
    def current_turn_state(self):
        return self.states.get(self.turn_state)

    def add_pot_size(self, new_amt):
        self.pot_size += new_amt
    
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
        self.player.hand.reset_hand()
        self.cpu.hand.reset_hand()
