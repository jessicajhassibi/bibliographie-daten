import unittest

from bibliographiedaten import utils


class TestUtils(unittest.TestCase):

    def test_should_find_pairs(self):
        items = [1, 2, 3, 4]
        actual = utils.pairs(items)
        expected = [
            (1, 2),
            (1, 3),
            (1, 4),
            (2, 3),
            (2, 4),
            (3, 4),
        ]
        self.assertEqual(len(actual), 6)
        self.assertListEqual(actual, expected)
