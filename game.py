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

    def discard_choices_input(self):
        return input('Which cards to discard? (Type the number, e.g.: 1 2 3) or k to keep: ')

    def discard_choices_validate(self):
        _choices = []
        while True:
            try:
                discard_choices = self.discard_choices_input()
                if 'quit' in discard_choices:
                    sys.exit(0)

                for _choice in discard_choices.split(' '):
                    if _choice.lower() == 'k':
                        break
                    elif int(_choice) < 0 or int(_choice) > 5 :
                        raise CardNumberDoesNotExistError
                    else:
                        _choices.append(int(_choice))
                break
            except ValueError:
                print('Integer was not entered in!')
            except CardNumberDoesNotExistError:
                print("Card Number doesn't exist! Values must be between 1 through 5!")
        return _choices

    def discard_choice(self):
        _choices = self.discard_choices_validate()
        
        if _choices:
            self.player.hand.discard(_choices)
        
        # re-draw hand
        self._draw_hand(self.player.hand, self.deck, len(_choices))
        self._display(self.player) # display the cards to the player
        self._display(self.cpu, 'c')
    
    def betting_round(self):
        while True:
            action = input('>>> ')
            try:
                if action == 'fold':
                    # cpu wins the pot
                    # TODO - needs to get the blinds
                    self.cpu.winpot(self.pot_size)
                    print(f'CPU wins {self.pot_size}')
                    break
                elif action == 'check':
                    no_bet = 0
                    self.cpu.cpu_decision(action, no_bet) 
                    break
                elif action == 'bet':
                    while True:
                        bet_amount = input('Bet >>> ')
                        try:
                            bet = int(bet_amount)

                            self.player.bet(bet)
                            print(f'Player bets {bet}.')

                            self.cpu.cpu_decision(action, bet)
                            print(f'CPU bets {bet}.')

                            # pot should increase by the amount of the bet
                            self.pot_size += bet
                            break
                        except ValueError:
                            print(f'{bet_amount} was not an integer!')
                    break
                else:
                    raise ValueError
            except ValueError as e:
                print(f'{action} was not a valid command! Try again.')
                print(f'type help() for a list of commands')
            
    def payout(self):
        '''
            finds the winner
            pay the winner with the pot
            set the pot to 0
        '''
        _winner, _win_desc = winninghand([self.cpu, self.player])

        if isinstance(_winner, list):
            _num_of_winner = len(_winner)
            payout_amount = self.pot_size / _num_of_winners
            _winner_msg = 'Player and CPU tied.'

            for _w in _winner:
                _w.winpot(payout_amount)
        else:
            if _winner.hand == self.player.hand:
                _win_player_text = 'Player'  
                self.player.stack += self.pot_size
            else: 
                _win_player_text = 'CPU'
                self.cpu.stack += self.pot_size
                
        print(f'{_win_player_text} wins with {_win_desc}!')
        print(f'{_win_player_text} wins {self.pot_size}')

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
