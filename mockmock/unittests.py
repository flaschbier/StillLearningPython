"""Deeply mock a database name..."""

import unittest

print(__doc__)
suite = unittest.TestLoader().discover('.', pattern='test_*.py')
unittest.TextTestRunner(verbosity=2).run(suite)
