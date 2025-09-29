import pytest
from lib.solutions.HLO.hello_solution import  HelloSolution

class TestHelloSolution:
    def test_hello(self):
        assert HelloSolution().hello("John") == "Hello, John!"

    def test_hello_with_empty_name(self):
        with pytest.raises(ValueError) as exception:
            HelloSolution().hello("")
        assert str(exception.value) == "Please provide friend name"

    def test_with_empty_not_string(self):
        with pytest.raises(ValueError) as exception:
            HelloSolution().hello(100)
        assert str(exception.value) == "Please give a friend name as a string"