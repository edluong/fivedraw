import unittest

from player import Player, CantOverBetError

class TestPlayer(unittest.TestCase):

    def test_bet(self):
        starting_stack = 1
        p = Player(starting_stack)
        self.assertRaises(CantOverBetError, p.bet, 100) # need to pass in the param for raises


if __name__ == "__main__":
    unittest.main()

        
        
