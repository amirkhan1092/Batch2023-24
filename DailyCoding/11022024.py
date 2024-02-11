'''This problem was asked by Facebook.

Write a function that rotates a list by k elements. For example, [1, 2, 3, 4, 5, 6] rotated 
by two becomes [3, 4, 5, 6, 1, 2]. Try solving this without creating a copy of the list. 
How many swap or move operations do you need?'''

class rotary:
    def __init__(self, lst) -> None:
        self.lst = lst

    def lrotate(self, step):
        for _ in range(step):
            if self.lst:
                self.lst.append(self.lst.pop(0))

    def rrotate(self, step):
        for _ in range(step):
            if self.lst:
                self.lst.insert(0, self.lst.pop())
    def __str__(self):
        return str(self.lst)
array = [1, 2, 3, 4, 5, 6]
print('before rotate\n', array)
obj = rotary(array)
# obj.lrotate(2)
# print('After rotate left \n', obj)
obj.rrotate(2)
print('After rotate right \n', obj)