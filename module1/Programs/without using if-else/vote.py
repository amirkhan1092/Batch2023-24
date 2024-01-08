# can vote or not without using if-else

age = int(input("Enter your age: "))
res = age >= 18
out = 'CAN VOTE' * res + 'CANNOT VOTE' * (1 - res)
print(out)