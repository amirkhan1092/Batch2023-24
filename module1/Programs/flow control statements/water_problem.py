# water tank problem 


# input section 
h = 10
r = 5
F = 15
t = eval(input('Enter the time for the pump to be on '))
# logic section 
Vtank = 3.14  * r ** 2 * h
Vwtr = F * t
if Vtank == Vwtr:
    print('Water Tank Full')
elif Vtank < Vwtr:
    print('Overflow Condition ')
    print('Volume', Vwtr - Vtank)
else:
    print('Underflow Condition ')
    ht = Vwtr / (3.14 * r ** 2)
    hr = h - ht 
    print(f"Filled Height {ht:.2f}\nRemaining Height {hr:.2f}")