#  balanced parentheses with * as wildcard
'''This problem was asked by Google.









You're given a string consisting solely of (, ), and *. * can represent either a (, ), or an empty string. 
Determine whether the parentheses are balanced.
For example, (()* and (*) are balanced. )*( is not balanced.









'''








def is_balanced(s):
    count = 0
    for i in s:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count < 0:
            return False
    if count == 0:
        return True
    else:
        return False
    

st = input()
out = is_balanced(st)
print(out)

