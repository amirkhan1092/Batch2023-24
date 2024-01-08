lst = list(map(int, input().split()))
new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(lst.count(i))
print(max(new_lst))