# program to find the area of rectangle with oop
class Rectangle:
    def __init__(self, l , w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w
    def perimeter(self):
        return 2 * (self.l + self.w)


# main code 
height = eval(input('Enter the height '))
width = eval(input('Enter the width '))
rec1 = Rectangle(height, width)
res1 = rec1.area()
res2 = rec1.perimeter()

print(f'Area of Rectangle with {height=} and {width=} is {res1}')

