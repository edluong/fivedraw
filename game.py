import sys

from cpu import CPU
from deck import Deck
from player import Player
from pokerengine import hand_rank, winninghand

QUIT_COMMANDS = ['quit','q']

class CardNumberDoesNotExistError(Exception):
    '''Card Number is Not Between 1 to 5! '''

class Game:
    states = {
            0: 'setup', # when players don't have cards
            1: 'betround1', # first betting round when player have cards 
            2: 'draw', # discard/drawing phase
            3: 'betround2', # second betting round
            4: 'showdown' # find winner
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
            
    def __init__(self, starting_stack, state = 0, pot_size = 0):
        
        # initial game values
        self.starting_stack = starting_stack
        self.state = state
        self.pot_size = pot_size

        # initialize players
        self.player = Player(self.starting_stack)
        self.cpu = CPU(self.starting_stack)

        # prepare the deck
        self.deck = Deck()
        self.deck.shuffle()

    def discard_choices_input(self):
        return input('Which cards to discard? (Type the number, e.g.: 1 2 3) or k to keep: ')

    def discard_choices_validate(self):
        _choices = []
        while True:
            try:
                discard_choices = self.discard_choices_input()
                if  discard_choices in QUIT_COMMANDS:
                    sys.exit(0)

                for _choice in discard_choices.strip().split(' '):
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
                if action in QUIT_COMMANDS:
                    sys.exit(0)
                elif action == 'fold':
                    # cpu wins the pot
                    # TODO - needs to get the blinds working
                    self.cpu.winpot(self.pot_size)
                    print(f'CPU wins {self.pot_size}\n')
                    self.reset() # soft reset
                    break
                elif action == 'check':
                    no_bet = 0
                    self.cpu.cpu_decision(action, no_bet) 
                    self.state = 1 if self.state == 0 else 3
                    break
                elif action == 'bet':
                    while True:
                        bet_amount = input('Bet >>> ')
                        try:
                            bet = int(bet_amount)

                            self.player.bet(bet)
                            print(f'Player bets {bet}.')
                            # pot should increase by the amount of the bet of the player
                            self.pot_size += bet

                            self.cpu.cpu_decision(action, bet)
                            print(f'CPU bets {bet}.')

                            # pot should increase by the amount of the bet
                            self.pot_size += bet
                            break
                        except ValueError:
                            print(f'{bet_amount} was not an integer!')
                    self.state = 1 if self.state == 0 else 3
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
        _win_player_text = ''
        _winner, _win_desc = winninghand([self.cpu, self.player])

        if isinstance(_winner, list):
            _num_of_winner = len(_winner)
            split_pot = self.pot_size / _num_of_winner
            _win_player_text = 'Player and CPU tied.'

            # TODO - need to make this more generalized for more than two players
            self.player.stack += split_pot
            self.cpu.stack += split_pot
        else:
            if _winner.hand.hand == self.player.hand:
                _win_player_text = 'Player'  
                self.player.stack += self.pot_size
            elif _winner.hand.hand == self.cpu.hand: 
                _win_player_text = 'CPU'
                self.cpu.stack += self.pot_size
            else:
                print('there is something wrong...')

        print(f'{_win_player_text} wins with {_win_desc}!')
        print(f'{_win_player_text} wins {self.pot_size} from the pot')
        print(f'Player Stack Size: {self.player.stack}')
        print(f'CPU Stack Size: {self.cpu.stack}\n')

        # reset the pot size
        self.pot_size = 0
        self.state = 4
    
    def check_busted(self):
        # make sure no players busted
        if self.player.stack == 0 or self.cpu.stack == 0:
            while True:
                print('game over.')
                action = input('>>> ')
                if action in QUIT_COMMANDS:
                    sys.exit(0)
                elif action in {'restart','r'}:
                    self.reset('full')
                    break
                else:
                    print(f'{action} is not a valid command! please try again.')
        else:
            self.reset()

    def add_pot_size(self, new_amt):
        self.pot_size += new_amt
    
    def reset_pot_size(self):
        self.pot_size = 0

    def reset_game(self):
        self.reset_pot_size()
        self.state = 1

    def get_players_bet(self):
        wager = input('wager: ')
        self.player.bet(int(wager))
    
    def reset(self, type=None):
        # game state
        self.state = 0

        # reset players stuff
        self.player.hand.reset_hand()
        self.cpu.hand.reset_hand()
        if type == 'full':
            self.player.stack = self.starting_stack
            self.cpu.stack = self.starting_stack
    
        # reset deck
        self.deck.reload()
    
    def round(self):
        self.deal_cards()
        self.betting_round()
        if self.state > 0: # folding will trigger state to be 0
            self.discard_choice()
            # level 0 cpu should randomly discard
            self.betting_round() # folding will trigger state to be 0
            if self.state > 0:
                self.payout()
                self.check_busted()
            else:
                return
        else:
            return


