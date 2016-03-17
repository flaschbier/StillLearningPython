from mock import patch
import unittest

import myconst
import inner


class Tests(unittest.TestCase):

    @patch("inner.get_db_name", side_effect=myconst.fun)
    def test_inner_1(self, mo):
        """mocking where used"""
        self.assertEqual(inner.functio(), myconst.TEST_VALUE)
        self.assertTrue(mo.called)

    @patch("inner.get_db_name", return_value=myconst.TEST_VALUE)
    def test_inner_2(self, mo):
        """mocking where used"""
        self.assertEqual(inner.functio(), myconst.TEST_VALUE)
        self.assertTrue(mo.called)
