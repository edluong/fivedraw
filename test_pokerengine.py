import unittest

import pokerengine as pe
import hand_constants as hc

class TestPokerEngine(unittest.TestCase):
    
    def test_nothing(self):
        player_hands = []
        player_hands.append(hc.nothing)
        self.assertEqual(pe.winninghand(player_hands), 'nothing')


if __name__ == '__main___':
    unittest.main()
