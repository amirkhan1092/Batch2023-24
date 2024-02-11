'''This problem was asked by Microsoft.

You have n fair coins and you flip them all at the same time. Any that come up tails you set aside. The ones that come up heads you flip again. How many rounds do you expect to play before only one coin remains?

Write a function that, given n, returns the number of rounds you'd expect to play until one coin remains.'''


def expected_rounds(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        expected_rounds = 0
        for i in range(1, n + 1):
            probability = (1 / (2 ** i)) * ((n - i + 1) / n)
            expected_rounds += probability * i
        return expected_rounds

# Test the function
n = 5
print("Expected rounds to play until one coin remains:", expected_rounds(n))
