# leap year or not without using if-else

year = int(input("Enter a year: "))

res = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
out = 'LEAP YEAR' * res + 'NOT LEAP YEAR' * (1 - res)

print(out)