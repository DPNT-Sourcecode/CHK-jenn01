import pytest
from lib.solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckoutSolution:
    def test_checkout_solution_with_empty_skus(self):
        assert -1 == CheckoutSolution().checkout("")

    def test_checkout_solution_with_nonempty_skus(self):
        assert 98 == CheckoutSolution().checkout("AAABACCCCCDB")


