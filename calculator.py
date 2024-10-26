class Calculator():
    def __init__(self):
        pass

    def calculate(x, y, op):
        try:
            x = float(x)
            y = float(y)
        
        except ValueError:
            return None
        
        if op == '+':
            return x + y
        
        elif op == '-':
            return x - y
        
        elif op == '*':
            return x * y
        
        elif op == '/':
            if y == 0:
                return None
            return x / y
        
        elif op == '^':
            return x ** y

        else:
            return None