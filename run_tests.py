import tests.homework.h_strings as h_strings

import unittest

suite = unittest.TestLoader().loadTestsFromModule(h_strings)
unittest.TextTestRunner(verbosity=2).run(suite)