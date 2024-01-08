# looping 
'''
for loop : iteration over the sequence 
syntax:
for i in seq:
    # block of for loop

'''
n = int(input('Enter the value of n '))
s = 1
for i in range(1, n+1): # [1, 2, 3, 4, 5] 
    s = s * i

print(f'Factorail of num {n} is {s}')