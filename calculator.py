class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

# Example usage
if __name__ == "__main__":
    calc = Calculator()
    print(calc.add(5, 3))
    print(calc.divide(10, 2)) 
