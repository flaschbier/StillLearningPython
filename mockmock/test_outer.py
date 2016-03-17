from mock import patch
import unittest

import myconst
import outer


class Tests(unittest.TestCase):

    # Mock injection works only when test and testee use the same name for the
    # mockee. So this will fail.
    @patch("myconst.get_db_name", side_effect=myconst.fun)
    def test_outer_1(self, mo):
        """mocking where it comes from, different path"""
        self.assertEqual(outer.functio(), myconst.TEST_VALUE)
        self.assertTrue(mo.called)

    # here we follow the path outer.py does use to access mockee
    @patch("outer.inner.get_db_name", return_value=myconst.TEST_VALUE)
    def test_outer_2(self, mo):
        """mocking where it comes from, same path"""
        self.assertEqual(outer.functio(), myconst.TEST_VALUE)
        self.assertTrue(mo.called)
