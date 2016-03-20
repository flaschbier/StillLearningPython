from mock import patch
import unittest

import myconst
import outer


@patch("myconst.get_db_name", side_effect=myconst.fun)
class Tests(unittest.TestCase):

    def test_outer(self, mo):
        """mocking where it comes from"""
        self.assertEqual(outer.functio(), myconst.TEST_VALUE)
        self.assertTrue(mo.called)
