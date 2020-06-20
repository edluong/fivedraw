import unittest

import pokerengine as pe
import hand_constants as hc

class TestPokerEngine(unittest.TestCase):
    
    def test_nothing(self):
        player_hands = []
        player_hands.append(hc.nothing)
        self.assertEqual(pe.winninghand(player_hands), 'nothing')

    def test_pair(self):
        player_hands = []
        player_hands.append(hc.pair)
        self.assertEqual(pe.winninghand(player_hands), 'pair')

    def test_two_pair(self):
        player_hands = []
        player_hands.append(hc.two_pair)
        self.assertEqual(pe.winninghand(player_hands), 'two pair')

    def test_trips(self):
        player_hands = []
        player_hands.append(hc.trips)
        self.assertEqual(pe.winninghand(player_hands), 'trips')


if __name__ == '__main___':
    unittest.main()
