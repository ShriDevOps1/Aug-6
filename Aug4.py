# Aug4.py

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    num = 5
    print(f"Factorial of {num}: {factorial(num)}")
