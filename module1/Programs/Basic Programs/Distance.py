# Write a program to calculate the distance between two points (x1, y1) and (x2, y2).
# input section 

x1 = int(input("Enter the x coordinate of the first point: "))
y1 = int(input("Enter the y coordinate of the first point: "))
x2 = int(input("Enter the x coordinate of the second point: "))
y2 = int(input("Enter the y coordinate of the second point: "))

# logic Section
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# output section
print("The distance between ({0}, {1}) and ({2}, {3}) is {4}".format(x1, y1, x2, y2, distance))