# Guess the number game

import random 
random.seed(100)
sys_num = random.randint(1, 100)

score = 20
attempt = 5
print('You have Total Attempt', attempt)
while attempt:
    user_num = int(input('Guess the number between 1 to 100 '))

    if user_num == sys_num:
        print('You Win')
        print('Score', score)
        break
    elif user_num < sys_num:
        print('Too small ')
    elif user_num > sys_num:
        print('Too Large')
    score -= 1  
    attempt -= 1
    print('Attempt left', attempt)   
else:
    print('Right number was', sys_num)