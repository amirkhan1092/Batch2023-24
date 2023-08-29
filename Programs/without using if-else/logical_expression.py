# there three values a, b and c. based on the value of c display the value of a or b.

a = 10
b = 20
c = int(input("Enter the value of c: 1 or 0: "))

print("value by choice is {0}".format(a * c + b * (1 - c)))