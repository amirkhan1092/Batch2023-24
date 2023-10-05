# strange number 

num = int(input('Enter the number to check: '))

for i in range(2, num):
    if num % i == 0:
        flag = 1
        for j in range(2, i):
            if i % j == 0:
                flag = 0
        if flag == 0:
            break
else:
    print('Strange number')
    
            