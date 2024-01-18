class test:
    def __init__(self):
        print('This is Constructor')
    def details(self, name):
        self.name = name
    def __del__(self):
        print(f'{self.name} object is deleted')
# main code         
obj1 = test()
obj2 = test()
obj2.details('ravi')
obj1.details('saket')
del obj2


