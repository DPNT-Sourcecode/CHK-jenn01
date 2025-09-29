import pytest
from lib.solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckoutSolution:
    def test_checkout_solution_with_empty_skus(self):
        with pytest.raises(ValueError) as exception:
            CheckoutSolution().checkout("")
        assert str(exception.value) == "Please provide skus"

    def test_checkout_solution_with_nonempty_skus(self):
        assert CheckoutSolution().checkout("AAABACCCDB") == 4

