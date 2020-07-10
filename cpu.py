from player import Player

class CPU(Player):

    def cpu_decision(self, player_action, player_bet_amt):
        '''
            level 0 - will always copy what action is done
            player: checks -> cpu checks
            player: bets -> cpu call
            cpu first to act -> always check
        '''
        return self.bet(player_bet_amt)
    
    def bet_strategy(self, player_bet_amt = 0, player_action = None):

        CHECK_BET_SIZE = 0
        # implies cpu is going first
        if not player_action:
            self.bet(CHECK_BET_SIZE)
        else:
            self.call(player_bet_amt)
            print(f'CPU calls {player_bet_amt}.')

        
        