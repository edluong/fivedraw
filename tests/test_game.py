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
        self.assertEqual(self.game.state, 0)
        self.assertEqual(self.game.pot_size, 0)

        # check cpu and player obj
        self.assertEqual(self.game.player.stack, 100)
        self.assertEqual(self.game.cpu.stack, 100)

    def test_deal_cards(self):
        pass

    @patch('game.Game.discard_choices_input', return_value ='1 2 3')
    def test_discard_choices_validate(self, m_input):
        '''
            mock discard_choices_input to return 1 2 3
            expecting the result to equal the array [1,2,3]
        '''
        result = self.game.discard_choices_validate()
        self.assertEqual(result, [1, 2, 3])
    
    @patch('game.Game.discard_choices_input', return_value =' 1 2 3 ')
    def test_discard_choices_validate_spaces_before_and_after(self, m_input):
        '''
            mock discard_choices_input to return 1 2 3 (with spaces before and after)
            expecting the result to equal the array [1,2,3]
        '''
        result = self.game.discard_choices_validate()
        self.assertEqual(result, [1, 2, 3])
    
    @patch('game.Game.discard_choices_input', return_value ='5 1')
    def test_discard_choices_validate_2(self, m_input):
        '''
            mock discard_choices_input to return 5 1
            expecting the result to equal the array [5, 1]
        '''
        result = self.game.discard_choices_validate()
        self.assertEqual(result, [5, 1])
    
    # inspiration: https://stackoverflow.com/a/61941348/4376173
    @patch('builtins.input', return_value = 'test')
    @patch('builtins.print', side_effect = ValueError('Integer was not entered in!'))
    def test_discard_choices_validate_value_error(self, mocked_input, mocked_print):
        '''
            Need to mock the input and type in "test"
            this would then create a side effect in print where ValueError is raised
            check if this happens with the method
        '''
        with self.assertRaises(ValueError):
            self.game.discard_choices_validate()
     
    # inspiration: https://stackoverflow.com/a/61941348/4376173
    @patch('builtins.input', return_value='123')
    @patch('builtins.print', side_effect = CardNumberDoesNotExistError("Card Number doesn't exist! Values must be between 1 through 5!"))
    def test_discard_choices_validate_cardnumberDNE_error(self, mocked_input, mocked_print):
        with self.assertRaises(CardNumberDoesNotExistError):
            self.game.discard_choices_validate()

    def test_add_pot_size(self):
        self.game.add_pot_size(10)
        self.assertEqual(10, self.game.pot_size)

    def test_reset_game(self):
        self.game.reset_game()
        self.assertEqual(0, self.game.pot_size)
    if __name__ == '__main__':
        unittest.main()
