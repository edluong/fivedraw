import unittest

import constants as con
import pokerengine as pe
import test_hand_constants as hc

class TestPokerEngine(unittest.TestCase):
    
    def test_high_card(self):
        rank_desc = 'high card'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe._hand_rank(hc.high_card), result)

    def test_pair(self):
        rank_desc = 'pair'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe._hand_rank(hc.pair), result)
    
    def test_two_pair(self):
        rank_desc = 'two pair'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe._hand_rank(hc.two_pair), result)

    def test_trips(self):
        rank_desc = 'trips'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe._hand_rank(hc.trips), result)

    def test_straight(self):
        rank_desc = 'straight'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe._hand_rank(hc.straight), result)

    # A2345
    def test_straight_wheel(self):
        rank_desc = 'straight'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe._hand_rank(hc.straight_wheel), result)

    # 10JQKA
    def test_straight_broadway(self):
        rank_desc = 'straight'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe._hand_rank(hc.straight_broadway), result)

    def test_flush(self):
        rank_desc = 'flush'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe._hand_rank(hc.flush), result)

    def test_full_house(self):
        rank_desc = 'full house'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe._hand_rank(hc.full_house), result)
    
    def test_quads(self):
        rank_desc = 'quads'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe._hand_rank(hc.quads), result)

    def test_straight_flush(self):
        rank_desc = 'straight flush'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe._hand_rank(hc.straight_flush), result)

if __name__ == '__main___':
    unittest.main()
