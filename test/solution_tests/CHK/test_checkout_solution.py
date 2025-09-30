import unittest

from parameterized import parameterized

from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckoutSolution(unittest.TestCase):
    def test_checkout_solution_with_empty_skus(self):
        assert 0 == CheckoutSolution().checkout("")

    def test_chk_bbb_solution(self):
        assert 180 == CheckoutSolution().checkout("AAAA")

    def test_checkout_solution_with_nonempty_skus(self):
        assert 340 == CheckoutSolution().checkout("AAABACCCCCDB")

    @parameterized.expand([
        ("AAAABBCCCCCDEEE", 440),
        ("AAAABBCCCCCDEEEE", 495)
    ])
    def test_checkout_solution_with_new_goods(self, expected, test_input):
        self.assertEqual(expected, CheckoutSolution().checkout(test_input))

    def test_checkout_solution_with_multiple_offers(self):
        # assert 330 == CheckoutSolution().checkout("AAAAAAAA")
        assert 380 == CheckoutSolution().checkout("AAAAAAAAA")

    def test_checkout_solution_with_invalid_skus(self):
        assert 0 == CheckoutSolution().checkout("")
        assert -1 == CheckoutSolution().checkout("a")
        assert -1 == CheckoutSolution().checkout("ABCa")
