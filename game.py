import sys
import random

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
            hand.append(deck.draw())

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
        print(f'{_hand_msg}', end='\n')
        player.print_hand()

        # get the ranking of the hand
        _rank = hand_rank(player.hand)
        _result, _ = _rank
        _result_msg = CPU_RESULT if playertype == 'c' else PLAYER_RESULT
        print(f'{_result_msg} {_result}')

        # get stack size
        print(f'Stack Size: {player.stack}')

        # dealer status
        if self.player.isDealer and playertype == 'p':
            print('You are dealer.')
        elif self.cpu.isDealer:
            print('CPU is dealer.')
        
        print(f'Pot: {self.pot_size}\n')
    
    def deal_cards(self):
        # deal the cards out the the players
        self._draw_hand(self.player.hand, self.deck)
        self._draw_hand(self.cpu.hand, self.deck)

        # display the cards
        self._display(self.player)
        self._display(self.cpu, 'c') # TODO - remove when dealer functionality is in
            
    def __init__(self, starting_stack, current_bet = 0, state = 0, pot_size = 0):
        
        # initial game values
        self.starting_stack = starting_stack
        self.big_blind = self.starting_stack // 100
        self.small_blind = self.big_blind // 2
        self.state = state
        self.pot_size = pot_size
        self.current_bet = current_bet

        # initialize players
        self.player = Player(self.starting_stack)
        self.cpu = CPU(self.starting_stack)

        # prepare the deck
        self.deck = Deck()
        self.deck.shuffle()

        # pick dealer
        players = [self.player, self.cpu]
        dealer = random.choice(players)
        dealer.isDealer = True

    def pay_blinds(self):
        # dealer will pay small blind
        # non-dealer pays big blind
        if self.player.isDealer == True:
            self.player.bet(self.small_blind)
            self.cpu.bet(self.big_blind)
            self.cpu.last_action = 'blind'

            print(f'Player pays small blind for {self.small_blind}.')
            print(f'CPU pays big blind for {self.big_blind}.\n')
        else:
            self.cpu.bet(self.small_blind)
            self.player.bet(self.big_blind)
            self.player.last_action = 'blind'

            print(f'CPU pays small blind for {self.small_blind}.')
            print(f'Player pays big blind for {self.big_blind}.\n')

        # self.pot_size += self.small_blind
        # self.pot_size += self.big_blind
        self._bet_state_management(self.cpu)
        self._bet_state_management(self.player)

        self.current_bet = self.big_blind

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
            self.player.discard(_choices)
        
        # re-draw hand
        self._draw_hand(self.player.hand, self.deck, len(_choices))
        self._display(self.player) # display the cards to the player
        self._display(self.cpu, 'c')  # TODO - remove when dealer functionality is in
    
    def cpu_discard(self):
        _indexes = [1, 2, 3, 4, 5]
        num_discards = random.randint(0, 5)
        _choices = random.sample(_indexes, num_discards) # random select without replacement

        if _choices:
            self.cpu.discard(_choices)
        
        self._draw_hand(self.cpu.hand, self.deck, len(_choices))
        self._display(self.player)
        self._display(self.cpu, 'c')

        print(f'CPU discards {num_discards} card(s).')

    def betting_round(self):
        while True:
            action = input('>>> ')
            try:
                if action in QUIT_COMMANDS:
                    sys.exit(0)
                elif action == 'fold':
                    # cpu wins the pot
                    # TODO - needs to get the blinds working
                    self.player.last_action = action
                    self.cpu.stack += self.pot_size
                    print(f'CPU wins {self.pot_size}\n')
                    self.reset() # soft reset
                    break
                elif action == 'check':
                    self.player.last_action = action
                    self.state = 1 if self.state == 0 else 3
                    break
                elif action == 'call':
                    self.player.last_action = 'call'
                    self.state = 1 if self.state == 0 else 3
                    self.player.call(self.current_bet)
                    print(f'Player calls a bet of {self.current_bet}.')
                    self._bet_state_management(self.player)
                    break
                elif action == 'bet':
                    if self.cpu.last_action not in  {'blind','check'}:
                        raise ValueError
                    self.player.last_action = action
                    while True:
                        bet_amount = input('Bet >>> ')
                        try:
                            bet = int(bet_amount)
                            self.player.bet(bet)
                            print(f'Player bets {bet}.')
                            # pot should increase by the amount of the bet of the player
                            self._bet_state_management(self.player)
                            break
                        except ValueError:
                            print(f'{bet_amount} was not an integer!')
                    self.state = 1 if self.state == 0 else 3
                    break
                elif action == 'cb':
                    print(f'Current Bet: {self.current_bet}')
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
        if self.state > 0:
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
                if _winner == self.player:
                    _win_player_text = 'Player'  
                    self.player.stack = self.player.stack + self.pot_size
                elif _winner == self.cpu: 
                    _win_player_text = 'CPU'
                    self.cpu.stack = self.cpu.stack + self.pot_size
                else:
                    print('there is something wrong...')

            print(f'{_win_player_text} wins with {_win_desc}!')
            print(f'{_win_player_text} wins {self.pot_size} from the pot\n')
            print(f'Player Stack Size: {self.player.stack}')
            print(f'CPU Stack Size: {self.cpu.stack}\n')

            # reset the pot size
            self.pot_size = 0
            self.state = 4
        else:
            return
    
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
        self.pot_size = 0

        # reset players stuff
        self.player.hand.clear()
        self.cpu.hand.clear()
        self.player.last_action = None
        self.cpu.last_action = None
        self.player.last_bet = None
        self.cpu.last_action = None
        if type == 'full':
            self.player.stack = self.starting_stack
            self.cpu.stack = self.starting_stack
    
        # reset deck
        self.deck.reload()
    
    def reset_bet_trackers(self):
        # reset the tracker vars
        self.cpu.last_bet = 0
        self.cpu.last_action = None
        self.player.last_bet = 0
        self.player.last_action = None

    def _round_cpu_dealer(self):
        '''
            Order of the round if cpu is dealer
        '''
        # CPU calls the blinds
        self.cpu.bet_strategy(self.current_bet, self.player.last_action)
        self._bet_state_management(self.cpu)
        print(f'Pot: {self.pot_size}')
        print(f'CPU Stack: {self.cpu.stack}\n')


        # player has the chance to either raise or check the blinds
        # TODO - player has option to raise
        self.betting_round()
        self.cpu.bet_strategy(self.current_bet, self.player.last_action)
        self._bet_state_management(self.cpu)
        self.reset_bet_trackers()


        # betting round 2
        # checking if player folded
        if self.state > 0: 
            self.discard_choice()
            self.cpu_discard()
            self.betting_round() # folding will trigger state to be 0
            self.cpu.bet_strategy(self.current_bet, self.player.last_action)
            self._bet_state_management(self.cpu)
            self.reset_bet_trackers()
            print(f'Pot: {self.pot_size}')

            if self.state > 0:
                self.payout()
                self.check_busted()
            else:
                return
        else:
            return
    
    def _round_player_dealer(self):

        # player can call the blind, raise or fold
        self.betting_round()
        if self.state > 0: # verify player folded
            # continue the round
            self.cpu.bet_strategy(self.current_bet, self.player.last_action)
            self._bet_state_management(self.cpu) # used to sync pot and bets
            self.reset_bet_trackers()
            
            # continue to discarding cards
            self.cpu_discard()
            self.discard_choice()

            # betting round after discarding
            self.cpu.bet_strategy(self.current_bet, self.player.last_action)  # level 0 always check
            self._bet_state_management(self.cpu)
            self.betting_round()

            if self.state > 0:
                self.cpu.bet_strategy(self.current_bet, self.player.last_action) # player may bet
                self._bet_state_management(self.cpu) # used at the end of betting round for clean up
                self.reset_bet_trackers()
                print(f'Pot: {self.pot_size}')

                # payout the winner
                # checks if the game can continue
                self.payout()
                self.check_busted()
            else:
                return
        else:
            return

    def round(self):
        # always happens in this order
        self.pay_blinds()
        self.deal_cards()

        # choose the round based on who is dealer
        if self.cpu.isDealer:
            self._round_cpu_dealer()
        else:
           self._round_player_dealer()

        # switch states for dealer
        self.cpu.isDealer = not self.cpu.isDealer
        self.player.isDealer = not self.player.isDealer

    def _bet_state_management(self, player):
        '''
            helper method to make sure the pot
            and current bet are in sync
        '''
        if player.last_action != 'check':
            self.pot_size += player.last_bet
            if self.current_bet < player.last_bet:
                self.current_bet = player.last_bet
