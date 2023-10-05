n=int(input("Enter the no:"))
st = 0
for i in range (2,n):
    if n%i==0:
        flag=1
        for j in range (2,i):
            if i%j== 0 :
                # print("Not a strange no ")
                flag=0
                break
        if flag==0:
            print("Not Strange")
            break
        st=i
else:
    if st>n**0.5:
        print("strange no")
    else:
        print("Not a strange no ")


'''
Section CB1 Lab 04/10/2023 
9, 12, 14, 16, 18, 19, 20, 32
34, 

'''