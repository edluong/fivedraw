import sys
import unittest
from unittest.mock import patch, call

from game import Game, CardNumberDoesNotExistError

class TestGame(unittest.TestCase):
    
    
    def setUp(self):
        STARTING_STACK = 100
        self.game = Game(STARTING_STACK) # starting stack
    
    def test_init_load_correctly(self):
        # testing init loaded up correctly        
        self.assertEqual(self.game.starting_stack, 100)
        self.assertEqual(self.game.state, 0)
        self.assertEqual(self.game.pot_size, 0)

        # check cpu and player obj
        self.assertEqual(self.game.player.stack, 100)
        self.assertEqual(self.game.cpu.stack, 100)

    def test_deal_cards(self):

        self.game.deal_cards()

        # make sure 10 cards are missing from deck
        self.assertEqual(self.game.deck.deck_size(), 42)
        # player and cpu has five cards
        self.assertEqual(self.game.cpu.hand.hand_size(), 5)
        self.assertEqual(self.game.player.hand.hand_size(), 5)

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
    def test_discard_choices_validate_value_error(self, mocked_print, mocked_input):
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
    def test_discard_choices_validate_cardnumberDNE_error(self, mocked_print, mocked_input):
        with self.assertRaises(CardNumberDoesNotExistError):
            self.game.discard_choices_validate()
    
    def test_betting_round(self):
        pass

    def test_payout(self):
        pass 
    
    
    @patch('game.sys.exit',side_effect = SystemExit)
    @patch('builtins.input', return_value='q')
    def test_check_busted_quit(self, m_input, m_exit):
        '''
            higher the patch, the variable is on the right
            example: patch(input) -> m_input
        '''
        self.game.player.stack = 0
        self.game.cpu.stack = 400

        # tests
        with self.assertRaises(SystemExit):
            self.game.check_busted()

    
    @patch('game.Game.reset')
    @patch('builtins.input', return_value='restart')
    def test_check_busted_restart(self, m_input, m_reset):
        # set up
        self.game.player.stack = 0
        self.game.cpu.stack = 400
        self.game.check_busted()
        # tests
        m_reset.assert_called_once()
        m_reset.assert_called_with('full')
        
    @patch('game.Game.reset')
    def test_check_busted_stacks_not_zero(self, m_reset):
        # set up
        self.game.player.stack = 100
        self.game.cpu.stack = 300
        self.game.check_busted()
        # tests
        m_reset.assert_called_once()
        m_reset.assert_called_with()
    

    @patch('deck.Deck.reload')
    def test_check_reset_full(self, m_deck):
        # setup
        self.game.state = 4
        self.game.player.stack = 300
        self.game.cpu.stack = 50
        self.game.player.hand.hand = [(14,'Clubs')] # could list all cards, but only wanted to check empty
        self.game.cpu.hand.hand = [(13,'Clubs')]
        
        self.game.reset('full')

        # tests
        self.assertEqual(self.game.state, 0)
        self.assertEqual(self.game.player.stack, 100)
        self.assertEqual(self.game.cpu.stack, 100)
        self.assertEqual(self.game.player.hand.hand, [])
        self.assertEqual(self.game.cpu.hand.hand, [])
        m_deck.assert_called_once()
    
    @patch('deck.Deck.reload')
    def test_check_reset(self, m_deck):
        # setup
        self.game.state = 4
        self.game.player.hand.hand = [(14,'Clubs')]
        self.game.cpu.hand.hand = [(13,'Clubs')]
        
        self.game.reset()

        # tests
        self.assertEqual(self.game.state, 0)
        self.assertEqual(self.game.player.hand.hand, [])
        self.assertEqual(self.game.cpu.hand.hand, [])
        m_deck.assert_called_once()
        

    def test_add_pot_size(self):
        self.game.add_pot_size(10)
        self.assertEqual(10, self.game.pot_size)

    def test_reset_game(self):
        self.game.reset_game()
        self.assertEqual(0, self.game.pot_size)
    if __name__ == '__main__':
        unittest.main()
