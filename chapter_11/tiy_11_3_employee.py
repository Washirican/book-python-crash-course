# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-28
# --------------------------------------------------------------------------- #

import unittest
import test_employee

suite = unittest.TestLoader().loadTestsFromModule(test_employee)
unittest.TextTestRunner(verbosity=2).run(suite)
