def add(a, b):
    return a + b
def sub(a, b):
    return a - b

# main code
val = 100
if __name__ == '__main__':
    num1 = int(input('Enter the first number '))
    num2 = int(input('Enter the second number '))

    out = add(num1, num2)
    print(f'Addition of {num1} and {num2} is {out}')