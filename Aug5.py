# Aug5.py

def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

if __name__ == "__main__":
    count = 10
    print(f"Fibonacci sequence ({count} terms): {fibonacci(count)}")
