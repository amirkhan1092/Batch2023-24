class Rectangle:
    def __init__(self,height,breadth):
        self.height=height
        self.breadth=breadth
    def Area(self):
        return self.height*self.breadth
    def Perimeter(self):
        return 2*(self.height+self.breadth)

# main code or driven code   
l = int(input('Enter the length '))
b = int(input('Enter the breadth '))
obj1=Rectangle(l, b)
print(obj1.Area())
print(obj1.Perimeter())