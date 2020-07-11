from player import Player

class CPU(Player):
    def bet_strategy(self, player_bet_amt = 0, player_action = None):
        '''
            level 0 - will always copy what action is done
            player: checks -> cpu checks
            player: bets -> cpu call
            cpu first to act -> always check
        '''
        CHECK_BET_SIZE = 0
        # implies cpu is going first
        if player_action == 'check':
            self.bet(CHECK_BET_SIZE)
            print(f'CPU checks.')
        else:
            self.call(player_bet_amt)
            print(f'CPU calls a bet of {player_bet_amt}.')
    
    def discard_strategy(self):
        '''
            level 0 - will random discard an amount of cards
        '''
        pass
        # TODO - need to refactor function and moved into cpu class

        
        