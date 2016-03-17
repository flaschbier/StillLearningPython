import unittest
import const
import prodcode

class Tests(unittest.TestCase):

    def test_prodcode_4(self):
        """uses production value again"""
        self.assertEqual(prodcode.functio(), "production value")
