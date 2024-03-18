# flatten list 

# nested list
lst = [2, [[[10]]], [1, 3], [], [1, [0]]]
lst = str([i for i in lst if i]).replace('[', '')
out = lst.replace(']', '')
print(list(eval(out)))
# output (flatten list)
p = 2, 10, 1, 3, 1, 0