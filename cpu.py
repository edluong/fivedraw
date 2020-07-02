from player import Player

class CPU(Player):

    def cpu_decision(self, player_action, player_bet_amt):
        '''
            level 0 - will always copy what action is done
            player: checks -> cpu checks
            player: bets -> cpu call
            cpu first to act -> always check
        '''

        if player_action == 'bet':
            return self.bet(player_bet_amt)
        