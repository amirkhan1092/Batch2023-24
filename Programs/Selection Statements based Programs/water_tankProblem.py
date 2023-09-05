# water tank problem
# -----------------------------------------------

h = 10
r = 5
F = 15

Vtank = 3.14 * r * r * h
print("Volume of tank is: ", Vtank)
print("Tank is filled in ", Vtank / F, "minutes")
t = eval(input("Enter the time in minutes: "))
Vwater = F * t
print("Volume of water is: ", Vwater)

if round(Vwater, 4) == round(Vtank, 4):
    print("Tank is full")
elif Vwater > Vtank:
    print("Overflow condition")
    print("Volume of water overflowed is: ", Vwater - Vtank)
else:
    print("Underflow condition")
    ht = Vwater / (3.14 * r * r)
    hr = h - ht
    print("Height of water in tank is: ", ht)
    print("Height of air in tank is: ", hr)
