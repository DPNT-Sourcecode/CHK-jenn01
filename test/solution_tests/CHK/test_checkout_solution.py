import unittest

from parameterized import parameterized

from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckoutSolution(unittest.TestCase):

    @parameterized.expand([
        # ("", 0),
        # ("a", -1),
        # ("ABCa", -1),
        # ("AAAA", 180),
        # ("BBB", 75),
        # ("AAAAAAAA", 330),
        # ("EE", 110),
        # ("EEB", 125),
        # ("AAABACCCCCDB", 340),
        # ("AAAABBCCCCCDEEE", 490),
        # ("AAAABBCCCCCDEEEE", 545)
        ("EE", 110)
    ])
    def test_checkout_solution_with_new_goods(self, test_input, expected):
        self.assertEqual(CheckoutSolution().checkout(test_input), expected)

if __name__ == '__main__':
    unittest.main()



