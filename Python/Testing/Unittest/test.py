import unittest
from main import do_something

class Test(unittest.TestCase):
    def test_do_something(self):
        test_param = 10
        result = do_something(test_param)
        self.assertEqual(result, 15)

    def test_do_something_2(self):
        test_param = 'davdhssjsns'
        result = do_something(test_param)
        self.assertEqual(isinstance(result, ValueError), True)

unittest.main()

# Ran 1 test in 0.000s
#
# OK

# when assertEqual param = 10, we get an error as 15 is expected result from test_param of 10
# AssertionError: 15 != 10
#
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# FAILED (failures=1)