class Person:
    def __init__(self) -> None:
        print("This is contructor")
    def __del__(self):
        print("This is destructor")
    def __str__(self):
        return f'{self.__class__}'

obj1 = Person()
obj2 = Person()
print(obj1, obj2.__class__)

print(obj2)
# print(obj)