# strange number 

num = int(input('Enter the number to check: '))
st = 0
for i in range(2, num):
    if num % i == 0:
        flag = 1
        for j in range(2, i):
            if i % j == 0:
                flag = 0
        if flag == 0:
            print('Not a Strange number')
            break
        st = i
else:
    if st > num ** .5:
        print('Strange number')
    else:
        print('Not a Strange number')
    
            