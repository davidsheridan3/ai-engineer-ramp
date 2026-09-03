import unittest

from pygame.macosx import Video_AutoInit

from main import do_something

class Test(unittest.TestCase):
    def test_do_something(self):
        test_param = 10
        result = do_something(test_param)
        self.assertEqual(result, 15)

    def test_do_something_2(self):
        test_param = 'davdhssjsns'
        result = do_something(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_something_3(self):
        test_param = None
        result = do_something(test_param)
        self.assertEqual(result, 'please enter a number')

unittest.main()
