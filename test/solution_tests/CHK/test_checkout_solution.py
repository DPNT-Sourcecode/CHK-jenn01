import pytest
from lib.solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckoutSolution:
    def test_checkout_solution_with_empty_skus(self):
        assert 0 == CheckoutSolution().checkout("")

    def test_chk_bbb_solution(self):
        assert 180 == CheckoutSolution().checkout("AAAA")

    def test_checkout_solution_with_nonempty_skus(self):
        assert 340 == CheckoutSolution().checkout("AAABACCCCCDB")

    def test_checkout_solution_with_new_goods(self):
        assert 490 == CheckoutSolution().checkout("AAAABBCCCCCDEEE")
        assert 545 == CheckoutSolution().checkout("AAAABBCCCCCDEEEE")

    def test_checkout_solution_with_multiple_offers(self):
        assert 330 == CheckoutSolution().checkout("AAAAAAAA")

    def test_checkout_solution_with_invalid_skus(self):
        assert 0 == CheckoutSolution().checkout("")
        assert -1 == CheckoutSolution().checkout("a")
        assert -1 == CheckoutSolution().checkout("ABCa")


