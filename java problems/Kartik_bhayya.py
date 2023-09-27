# 
'''We can swap the a's to b using the 2 swaps and obtain the string "bbbb". This would have all the b's and hence the answer 4.
Alternatively, we can also swap the b's to make "aaaa". The final answer remains the same for both cases.'''


k = int(input())
st = input()
a_count = st.count('a')
b_count = st.count('b')

max_chr = max(a_count, b_count)
min_chr = min(a_count, b_count)
if min_chr >= k:
    out = max_chr + k  
else:
    out =  max_chr + min_chr
print(out)