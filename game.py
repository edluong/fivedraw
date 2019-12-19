class Game:

    states = {
            1: 'predeal',
            2: 'deal',
            3: 'draw',
            5: 'showdown'
    }
            
    def __init__(self,turn_state,num_players,pot_size):
        self.turn_state = turn_state
        self.num_players = num_players
        self.pot_size = pot_size
    
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
