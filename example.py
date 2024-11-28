import pytest

class Calculator:

    def sum(x, y):
        return x + y

    def difference(x, y):
        return x - y

    def product(x, y):
        return x * y

    def quotient(x, y):
        return x / y

# vvvvvvvvvvvvvvvvvvvvv TESTS vvvvvvvvvvvvvvvvvvvvv

def test_sum():
    c = Calculator
    assert c.sum(1,1) == 2

def test_sum_big_numbers():
    c = Calculator
    assert c.sum(1000,10000) == 11000

def test_difference():
    c = Calculator
    assert c.difference(64, 32) == 32

def test_difference_big_numbers():
    c = Calculator
    assert c.difference(100000, 50000) == 50000

def test_procuct():
    c = Calculator
    assert c.product(2,2) == 4

def test_procuct_big_numbers():
    c = Calculator
    assert c.product(1000, 1000) == 1000000

def test_quotient():
    c = Calculator
    assert c.quotient(10, 2) == 5


def test_quotient_big_numbers():
    c = Calculator
    assert c.quotient(150000, 50000) == 3