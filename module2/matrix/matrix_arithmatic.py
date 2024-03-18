# matrix operation 
'''
2 3 4 5 6 8 
2 3


3 4
2 3 6 7 
2 3 5 7
1 2 3 0

'''

class array:
    def __init__(self, lst, r=0, c=0):
        self.lst = lst
        self.r = r
        self.c = c
        if r != 0 and c != 0:
            M = []
            tmp = []
            for i in self.lst:
                tmp.append(i)
                if len(tmp) == c:
                    M.append(tmp)
                    tmp = []
            self.lst = M


    def __add__(self, other):
        if (self.r, self.c) == (other.r, other.c):
            M = eval(str([[0] * self.c] * self.r)) # [[0, 0, 0], [0, 0, 0]]
            for i in range(self.r):
                for j in range(self.c):
                    M[i][j] = self.lst[i][j] + other.lst[i][j]
            return array(M)
        else:
            print('No campatible for Addition')

    def __sub__(self, other):
        if (self.r, self.c) == (other.r, other.c):
            M = eval(str([[0] * self.c] * self.r)) # [[0, 0, 0], [0, 0, 0]]
            for i in range(self.r):
                for j in range(self.c):
                    M[i][j] = self.lst[i][j] - other.lst[i][j]
            return array(M)
        else:
            print('No campatible for Subtraction')
    def __mul__(self, other):
        if (self.r, self.c) == (other.r, other.c):
            M = eval(str([[0] * self.c] * self.r)) # [[0, 0, 0], [0, 0, 0]]
            for i in range(self.r):
                for j in range(self.c):
                    M[i][j] = self.lst[i][j] * other.lst[i][j]
            return array(M)
        else:
            print('No campatible for Multiplication')        

    def dot(self, other):
        if self.c == other.r:
            M = eval(str([[0]*other.c]*self.r))
            for i in range(self.r):
                for j in range(other.c):
                    for k in range(self.c):
                        M[i][j] += self.lst[i][k]  * other.lst[k][j]
            return array(M)            
        else:
            print('Dimension not valid for Multilication')

    def transpose(self):
        M = eval(str([[0] * self.r] * self.c))
        for i in range(self.c):
            for j in range(self.r):
                M[i][j] = self.lst[j][i]
        return array(M)



    def disp_mat(self):
        for i in self.lst:
            print(*i)

# driver code 
lst1 = list(map(eval, input('Enter Matrix 1 elements \n').split()))
r1, c1 = list(map(eval, input('R x C\n').split()))
arr1 = array(lst1, r1, c1)

lst2 = list(map(eval, input().split()))
r2, c2 = list(map(eval, input().split()))
arr2 = array(lst2, r2, c2)


print('\nMatrix 1')
arr1.disp_mat()
print('\nMatrix 2')
arr2.disp_mat()

out = arr1.dot(arr2)

print('\nDot Multiplication ')
out.disp_mat()