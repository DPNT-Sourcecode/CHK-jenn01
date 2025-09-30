import unittest

from parameterized import parameterized

from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckoutSolution(unittest.TestCase):

    @parameterized.expand([
        # ("", 0),
        # ("a", -1),
        # ("A", 50),
        # ("B", 30),
        # ("C", 20),
        # ("D", 15),
        # ("E", 40),
        # ("ABCa", -1),
        # ("AxB", -1),
        # ("AAAA", 180),
        # ("BBB", 75),
        # ("AAAAAAAA", 330),
        # ("EE", 80),
        # ("EEB", 80),
        # ("EEEB", 120),
        ("EEEEBB", 120),
        # ("AAABACCCCCDB", 340),
        # ("AAAABBCCCCCDEEE", 445),
        # ("AAAABBCCCCCDEEEE", 455)
    ])
    def test_checkout_solution_with_new_goods(self, test_input, expected):
        self.assertEqual(CheckoutSolution().checkout(test_input), expected)

if __name__ == '__main__':
    unittest.main()



