# even odd without using if-else

num = int(input("Enter a number: "))

res = num % 2
out = 'ODD' * res + 'EVEN' * (1 - res)
print(out)
# print("The number is {0}".format("even" if num % 2 == 0 else "odd"))