from calculator import Calculator

calculator = Calculator()

def sum_test():
    assert calculator.calculate(1, 2, '+') == 3
    assert calculator.calculate(-4, -4, '+') == -8
    assert calculator.calculate(6.0, 1.5, '+') == 7.5

def minus_test():
    assert calculator.calculate(1, 2, '-') == -1
    assert calculator.calculate(-4, -4, '-') == 0
    assert calculator.calculate(6.0, 1.5, '-') == 4.5

def mult_test():
    assert calculator.calculate(1, 2, '*') == 2
    assert calculator.calculate(-4, -4, '*') == 16
    assert calculator.calculate(6.0, 1.5, '*') == 9

def div_test():
    assert calculator.calculate(1, 2, '/') == 0.5
    assert calculator.calculate(-4, -4, '/') == 1
    assert calculator.calculate(6.0, 1.5, '/') == 4

def exp_test():
    assert calculator.calculate(1, 2, '^') == 1
    assert calculator.calculate(-4, 2, '^') == 16
    assert calculator.calculate(6.0, 1, '^') == 6

def error_test():
    assert calculator.calculate(1, 2, '$') == None
    assert calculator.calculate('abc', 2, '^') == None
    assert calculator.calculate('--1', 1, '-') == None