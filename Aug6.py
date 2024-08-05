def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# Example usage
print(add(5, 3))        # Output: 8
print(subtract(5, 3))   # Output: 2
print(multiply(5, 3))   # Output: 15
print(divide(5, 0))     # Output: Cannot divide by zero
