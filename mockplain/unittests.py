#!/usr/bin/python -u
# encoding: UTF-8

"""
Verify that I can change a global constant in a import-everywhere module
in set up and tear down of a TestCase class.

Alternatively use function returning constant and use mock framework to point
code to other datbase in test...
"""

import unittest

print(__doc__)
suite = unittest.TestLoader().discover('.', pattern='test_*.py')
unittest.TextTestRunner(verbosity=2).run(suite)
