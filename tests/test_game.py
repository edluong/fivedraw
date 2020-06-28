import sys
import unittest
from unittest.mock import patch

from game import Game, CardNumberDoesNotExistError

class TestGame(unittest.TestCase):
    
    def setUp(self):
        self.game = Game(100) # starting stack
    
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

    # resources used to get this to work
    # https://stackoverflow.com/a/47690244/4376173
    # https://www.youtube.com/watch?v=ClAdw7ZJf5E
    @patch('game.input')
    def test_discard_choice_bad_input(self, m_input):
        '''
            @patch('game.input') - want to patch game module's input() function, watch yt vid for more info
            m_input - is the mock object being passed into the test
            discard_choice() is run in a loop, so needed a list of mock side_effect
            the loop will run the first entry, run discard_choice(), then the assert first exception
            after will then choose the next entry in the array, run discard_choice(), then assert again
            try except is used to make sure it hits the end of the inputs or side_effect will throw a StopIteration
        '''
        m_input.side_effect = ['-1','test','1 12']
        result = self.game.discard_choice()
        self.assertRaises(result, CardNumberDoesNotExistError)
        self.assertRaises(result, ValueError)
        self.assertRaises(result, CardNumberDoesNotExistError)


    def test_add_pot_size(self):
        self.game.add_pot_size(10)
        self.assertEqual(10, self.game.pot_size)

    def test_reset_game(self):
        self.game.reset_game()
        self.assertEqual(0, self.game.pot_size)
        self.assertEqual('predeal', self.game.current_turn_state())

    if __name__ == '__main__':
        unittest.main()
