from calculator import Calculator

calculator = Calculator()

def test_sum():
    assert calculator.calculate(1, 2, '+') == 3
    assert calculator.calculate(-4, -4, '+') == -8
    assert calculator.calculate(6.0, 1.5, '+') == 7.5

def test_minus():
    assert calculator.calculate(1, 2, '-') == -1
    assert calculator.calculate(-4, -4, '-') == 0
    assert calculator.calculate(6.0, 1.5, '-') == 4.5

def test_mult():
    assert calculator.calculate(1, 2, '*') == 2
    assert calculator.calculate(-4, -4, '*') == 16
    assert calculator.calculate(6.0, 1.5, '*') == 9

def test_div():
    assert calculator.calculate(1, 2, '/') == 0.5
    assert calculator.calculate(-4, -4, '/') == 1
    assert calculator.calculate(6.0, 1.5, '/') == 4

def test_exp():
    assert calculator.calculate(1, 2, '^') == 1
    assert calculator.calculate(-4, 2, '^') == 16
    assert calculator.calculate(6.0, 1, '^') == 6

def test_error():
    assert calculator.calculate(1, 2, '$') == None
    assert calculator.calculate('abc', 2, '^') == None
    assert calculator.calculate('--1', 1, '-') == None