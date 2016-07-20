from unittest import TestCase
from market import entry


class TestEntry(TestCase):
    def test_create(self):
        self.instance = entry.Entry(price=10, volume=1)
        self.assertIsNotNone(self.instance)

        self.assertEqual(10, self.instance.price)
        self.assertEqual(1, self.instance.volume)
