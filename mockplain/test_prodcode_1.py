import unittest
import const
import prodcode

class Tests(unittest.TestCase):

    def test_prodcode_0(self):
        """uses production value"""
        self.assertEqual(prodcode.functio(), "production value")
