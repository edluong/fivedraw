import unittest

from game import Game

class TestGame(unittest.TestCase):
    
    def setUp(self):
        self.game = Game(100) # starting stack, turn_state, pot_size
    
    def test_init_load_correctly(self):
        # testing init loaded up correctly        
        self.assertEqual(self.game.starting_stack, 100)
        self.assertEqual(self.game.turn_state, 1)
        self.assertEqual(self.game.pot_size, 0)

        # check cpu and player obj
        self.assertEqual(self.game.player.stack, 100)
        self.assertEqual(self.game.cpu.stack, 100)
        
        # testing deal_cards()
        # card amounts are good for cpu and player
        self.assertEqual(self.game.player.hand.hand_size(), 5)
        self.assertEqual(self.game.cpu.hand.hand_size(), 5)
        # card amounts is correct in the deck, 10 cards are passed out
        self.assertEqual(self.game.deck.deck_size(), 42)

    def test_discard_choice(self):
        pass

    def test_add_pot_size(self):
        self.game.add_pot_size(10)
        self.assertEqual(10, self.game.current_pot_size())

    def test_reset_game(self):
        self.game.reset_game()
        self.assertEqual(0, self.game.current_pot_size())
        self.assertEqual('predeal', self.game.current_turn_state())

    if __name__ == '__main__':
        unittest.main()
