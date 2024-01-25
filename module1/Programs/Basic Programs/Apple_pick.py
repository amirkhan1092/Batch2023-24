# apple problems

apples = 1
count = 1
while 1:
    if apples % 7 == 0  and apples % 2 == 1 and apples % 3 == 1 and apples % 4 == 1 and apples % 5 == 1 and apples % 6 == 1:
        print("The apples are", apples)
        if count == 4:
            break
        count += 1
    apples += 1