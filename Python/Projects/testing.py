import unittest
import random_game

class TestGame(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = random_game.run_guess(guess, answer)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()


# Ran 1 test in 0.000s
# OK