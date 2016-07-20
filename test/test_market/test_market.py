import unittest
from market import market


class MarketTest(unittest.TestCase):
    def setUp(self):
        self.instance = market.Market()
        self.assertIsNotNone(self.instance)

    def test_transactions(self):
        self.assertIsNotNone(self.instance.transactions)
        self.assertEqual([], self.instance.transactions)

    def test_bids(self):
        self.assertIsNotNone(self.instance.bids)
        self.assertEqual([], self.instance.bids)
        self.instance.bid(price=10, volume=1)
        self.assertEqual(1, len(self.instance.bids))

    def test_asks(self):
        self.assertIsNotNone(self.instance.asks)
        self.assertEqual([], self.instance.asks)
        self.instance.ask(price=10, volume=1)
        self.assertEqual(1, len(self.instance.asks))

    def test_execute_transaction(self):
        self.assertEqual(0, len(self.instance.bids))
        self.assertEqual(0, len(self.instance.asks))
        self.assertEqual(0, len(self.instance.transactions))

        self.instance.bid(price=10)
        self.instance.ask(price=10)

        self.assertEqual(0, len(self.instance.bids))
        self.assertEqual(0, len(self.instance.asks))
        self.assertEqual(1, len(self.instance.transactions))

if __name__ == '__main__':
    unittest.main()
