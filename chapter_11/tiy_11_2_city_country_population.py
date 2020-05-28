# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-28
# --------------------------------------------------------------------------- #

import unittest
import test_cities

suite = unittest.TestLoader().loadTestsFromModule(test_cities)
unittest.TextTestRunner(verbosity=2).run(suite)

