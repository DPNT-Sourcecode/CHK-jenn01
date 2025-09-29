import pytest
from lib.solutions.SUM.sum_solution import SumSolution


class TestSum:
    def test_sum(self):
        assert SumSolution().compute(1, 2) == 3

    def test_sum_out_of_range(self):
        with pytest.raises(ValueError) as value_exception:
            SumSolution().compute(1, 'a')
        assert str(value_exception.value) == "Argument should be between 0 and 100"