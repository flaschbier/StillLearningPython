import unittest
import const
import prodcode

class Tests(unittest.TestCase):

    # class constant
    TEST_VALUE = "test value"

    @classmethod
    def setUpClass(cls):
        cls.ORIG_VALUE = const.CONST
        const.CONST = cls.TEST_VALUE

    @classmethod
    def tearDownClass(cls):
        const.CONST = cls.ORIG_VALUE

    def test_prodcode_1(self):
        """use test value"""
        self.assertEqual(prodcode.functio(), self.__class__.TEST_VALUE)

    def test_prodcode_2(self):
        """uses test value also in second test"""
        self.assertEqual(prodcode.functio(), self.__class__.TEST_VALUE)

class MoreTests(unittest.TestCase):

    def test_prodcode_3(self):
        """uses production value in other TestCase in the same file before"""
        self.assertEqual(prodcode.functio(), "production value")

class ZMoreTests(unittest.TestCase):

    def test_prodcode_3(self):
        """uses production value in other TestCase in the same file after"""
        self.assertEqual(prodcode.functio(), "production value")
