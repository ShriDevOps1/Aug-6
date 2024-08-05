# Aug3.py

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

if __name__ == "__main__":
    x, y = 10, 2
    print(f"Multiplication: {multiply(x, y)}")
    print(f"Division: {divide(x, y)}")
