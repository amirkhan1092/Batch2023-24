# leap year
# pylab01-1

'''
year % 400 == 0
year % 4 == 0 and year % 100 != 0 

'''

year = 2016

if year % 400 == 0:
    print("Leapp Year")
else:
    if year % 4 == 0:
        if year % 100 != 0:
            print("Leap Year")
        else:
            print('Not a leap year')
    else:
        print('Not a leap Year')            

