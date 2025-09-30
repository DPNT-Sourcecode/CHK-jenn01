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
        # ("AAAAAAAA", 330),
        # ("BBB", 75),
        # ("ABCDE", 155),
        # ("EE", 80),
        # ("EEB", 80),
        # ("EEEB", 120),
        # ("EEEEBB", 160),
        # ("BEBEEE", 160),
        # ("AAABACCCCCDB", 340),
        # ("AAAABBCCCCCDEEE", 445),
        # ("AAAABBCCCCCDEEEE", 455),
        # ("F", 10),
        # ("FF", 20),
        # ("FFF", 20),
        # ("AAFFF", 120),
        # ("AAFFFF", 130),
        # ("AAFFFFF", 140),
        # ("HHH", 30),
        # ("HHHHH", 45),
        # ("HHHHHH", 55),
        # ("HHHHHHHHH", 85),
        # ("HHHHHHHHHH", 80),
        # ("AAAHHHHHHHHHH", 210),
        # ("V", 50),
        # ("VV", 90),
        # ("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ", 1880),
        # ("AAAAAPPPPPUUUUEEBRRRQAAAHHHHHHHHHHVVVBBNNNMFFFKKQQQVVHHHHH", 1640),
        # ('A', 50),
        ('STX', 45),
        ('STXSTX', 90),
        ('STXS', 62),
        ('STXZ', 62),
        ('ASTXYZ', 132),
        ('AASTXYZ', 182),
        ('AASTTXYZSTXYZ', 269),
    ])
    def test_checkout_solution_with_new_goods(self, test_input, expected):
        self.assertEqual(CheckoutSolution().checkout(test_input), expected)

if __name__ == '__main__':
    unittest.main()

