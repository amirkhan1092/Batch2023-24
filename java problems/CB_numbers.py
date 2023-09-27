'''
Deepak and Gautam are having a discussion on a new type of number that they call Coding Blocks Number or CB Number. They use following criteria to define a CB Number.

1. 0 and 1 are not a CB number.
2. 2,3,5,7,11,13,17,19,23,29 are CB numbers.
3. Any number not divisible by the numbers in point 2( Given above) are also CB numbers.

Deepak said he loved CB numbers.Hearing it, Gautam throws a challenge to him.

Gautam will give Deepak a string of digits. Deepak's task is to find the number of CB numbers in the string.

CB number once detected should not be sub-string or super-string of any other CB number.
Ex- In 4991, both 499 and 991 are CB numbers but you can choose either 499 or 991, not both.

Further, the CB number formed can only be a sub-string of the string.
Ex - In 481, you can not take 41 as CB number because 41 is not a sub-string of 481.

As there can be multiple solutions, Gautam asks Deepak to find the maximum number of CB numbers that can be formed from the given string.

Deepak has to take class of Launchpad students. Help him by solving Gautam's challenge.

Input Format
First line contain size of the string.

Next line is A string of digits.

Constraints
1 <= Length of strings of digits <= 17

Output Format
Maximum number of CB numbers that can be formed.

Sample Input
5
81615
Sample Output
2
Explanation
61 and 5 are two CB numbers.

'''

def intersection(val1, val2):  # val1- 123  val2 = 12
    return str(val1) in str(val2) or str(val2) in str(val1)  

ndigit = int(input())  # 5
digits = input()   # 12345
lst = [2, 3, 5, 7, 11, 13, 17, 19, 23]
out_lst = []
for i in range(len(digits)):
    for j in range(i, len(digits)):
        num = int(digits[i:j+1])   # 
        if num in lst  or all(num % d != 0 for d in lst) and num != 0 and num!= 1 :
            for dt in out_lst:
                if intersection(num, dt):
                    break
            else:
                out_lst.append(num)
print(len(out_lst))

