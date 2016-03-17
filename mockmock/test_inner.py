from mock import patch
import unittest

import myconst
import inner


class Tests(unittest.TestCase):

    @patch("inner.myconst.get_db_name", side_effect=myconst.fun)
    def test_inner(self, mo):
        """mocking where used"""
        self.assertEqual(inner.functio(), myconst.TEST_VALUE)
        self.assertTrue(mo.called)
