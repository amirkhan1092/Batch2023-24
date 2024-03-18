# Matrix Multiplication 

class array:
    def __init__(self, lst) -> None:
        self.lst = lst
    def reshape(self, m, n):
        M = []
        tmp = []
        for i in self.lst:
            tmp.append(i)
            if len(tmp) == n:
                M.append(tmp)
                tmp = []
        self.lst = M

    def __add__(self, other):
        r = len(self.lst)
        c = len(self.lst[0])
        M = eval(str([[0] * c] * r))   # [[0, 0, 0], [0, 0, 0]]
        for i in range(r):
            for j in range(c):
                M[i][j] = self.lst[i][j] + other.lst[i][j]
        return array(M)
    def __sub__(self, other):
        r = len(self.lst)
        c = len(self.lst[0])
        M = eval(str([[0] * c] * r))   # [[0, 0, 0], [0, 0, 0]]
        for i in range(r):
            for j in range(c):
                M[i][j] = self.lst[i][j] - other.lst[i][j]
        return array(M)
    def __mul__(self, other):
        r = len(self.lst)
        c = len(self.lst[0])
        M = eval(str([[0] * c] * r))   # [[0, 0, 0], [0, 0, 0]]
        for i in range(r):
            for j in range(c):
                M[i][j] = self.lst[i][j] * other.lst[i][j]
        return array(M)
    def __div__(self, other):
        r = len(self.lst)
        c = len(self.lst[0])
        M = eval(str([[0] * c] * r))   # [[0, 0, 0], [0, 0, 0]]
        for i in range(r):
            for j in range(c):
                M[i][j] = self.lst[i][j] / other.lst[i][j]
        return array(M)
    def dot(self, other):
        r1 = len(self.lst)
        c1 = len(self.lst[0])
        r2 = len(other.lst)
        c2 = len(other.lst[0])
        M = eval(str([[0] * c2] * r1))   # [[0, 0, 0], [0, 0, 0]]
        for i in range(r1):
            for j in range(c2):
                for k in range(c1):
                    M[i][j] += self.lst[i][k]  * other.lst[k][j]

        return array(M)
    def transpose(self):
        pass


    def disp_matrix(self):
        for i in self.lst:
            print(*i)

# raw array 
lst1 = list(map(int, input().split()))
r1, c1 = list(map(int, input().split()))
arr1 = array(lst1)
arr1.reshape(r1, c1)


lst2 = list(map(int, input().split()))
r2, c2 = list(map(int, input().split()))
arr2 = array(lst2)
arr2.reshape(r2, c2)

print('Matrix 1')
arr1.disp_matrix()
print('\nMatrix2')
arr2.disp_matrix()

if c1 == r2:
    print('\n Dot Multiplication')
    addition = arr1.dot(arr2)
    addition.disp_matrix()
else:
    print('Invalid Dimensions for operation')    



# 2 3 4 5 6 7
# 3 2

# 4 5 6 4 6 0
# 3 2


'''
M1
2 3
4 5
6 7

M2
4 5
6 4 
6 0

RE
6 8
10 9
12 7


'''