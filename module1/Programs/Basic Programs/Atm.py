# input section 
amount = int(input("Enter the amount to be withdrawn: "))

# logic Section
notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(notes)):
    count[i] = amount // notes[i]
    amount = amount % notes[i]


# output section
print("The denominations are: ")
for i in range(len(notes)):
    if count[i] != 0:
        print("{0} : {1}".format(notes[i], count[i]))

# Output:           
# Enter the amount to be withdrawn: 1234
# The denominations are:
# 500 : 2
# 200 : 1
# 20 : 1
# 10 : 1
# 2 : 2
# 1 : 0