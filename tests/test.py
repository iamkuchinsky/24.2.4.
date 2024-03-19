import pytest

from app.calculator import Calculator


class TestCalc:
    def setup_method(self):
        self.calc = Calculator()

    def test_multiply(self):
        assert self.calc.multiply(2, 3) == 6

    def test_division(self):
        assert self.calc.division(10, 2) == 5

    def test_subtraction(self):
        assert self.calc.subtraction(8, 3) == 5

    def test_adding(self):
        assert self.calc.adding(4, 6) == 10

    def teardown_method(self):
        print('Выполнение метода Teardown')
