import unittest

from parameterized import parameterized

from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckoutSolution(unittest.TestCase):

    @parameterized.expand([
        ("", 0),
        ("a", -1),
        ("ABCa", -1),
        ("AAAA", 180),
        ("AAAAAAAA", 380),
        ("AAABACCCCCDB", 340),
        ("AAAABBCCCCCDEEE", 440),
        ("AAAABBCCCCCDEEEE", 495)
    ])
    def test_checkout_solution_with_new_goods(self, expected, test_input):
        self.assertEqual(expected, CheckoutSolution().checkout(test_input))

if __name__ == '__main__':
    unittest.main()
