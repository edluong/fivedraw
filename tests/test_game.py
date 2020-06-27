from game import Game
import unittest




class TestGame(unittest.TestCase):
    
    def setUp(self):
        self.game = Game(1,2,0) # turn_state, player count, pot size
    
    def test_update_turn_state(self): 
       self.game.update_turn_state(2) 
       self.assertEqual('deal',self.game.current_turn_state()) 
    
    def test_add_pot_size(self):
        self.game.add_pot_size(10)
        self.assertEqual(10,self.game.current_pot_size())

    def test_reset_game(self):
        self.game.reset_game()
        self.assertEqual(0,self.game.current_pot_size())
        self.assertEqual('predeal',self.game.current_turn_state())

    if __name__ == '__main__':
        unittest.main()
