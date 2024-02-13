'''Good morning! Here's your coding interview problem for today.

Given a real number n, find the square root of n. For example, given n = 9, return 3.'''


def square_root(n):
    if n < 0:
        raise ValueError("Cannot compute square root of a negative number")

    if n == 0:
        return 0

    x = n / 2  # Initial guess can be any positive value
    epsilon = 0.000001  # Threshold for precision

    while True:
        root = 0.5 * (x + n / x)  # Newton's method formula
        if abs(root - x) < epsilon:
            break
        x = root

    return root

# Test the function
n = 9
print("Square root of", n, "is:", square_root(n))