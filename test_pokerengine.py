import unittest

import pokerengine as pe
import test_hand_constants as hc

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

    def test_straight(self):
        player_hands = []
        player_hands.append(hc.straight)
        self.assertEqual(pe.winninghand(player_hands), 'straight')

    def test_flush(self):
        player_hands = []
        player_hands.append(hc.flush)
        self.assertEqual(pe.winninghand(player_hands), 'flush')

    def test_fullhouse(self):
        player_hands = []
        player_hands.append(hc.full_house)
        self.assertEqual(pe.winninghand(player_hands), 'full house')

    def test_quads(self):
        player_hands = []
        player_hands.append(hc.quads)
        self.assertEqual(pe.winninghand(player_hands), 'quads')

    def test_straight_flush(self):
        player_hands = []
        player_hands.append(hc.straight_flush)
        self.assertEqual(pe.winninghand(player_hands), 'straight flush')
    


if __name__ == '__main___':
    unittest.main()
