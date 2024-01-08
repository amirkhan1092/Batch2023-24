# perfect number

n = int(input("enter any number"))
s = 0
for i in range(1,n):
    if n%i==0:
        s =  s + i 
if s==n:
  print(f"{n} is a perfect number")
else:
   print(f"{n} is not a perfect number")
  