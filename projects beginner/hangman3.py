word='ignore'
target='__n_re'
att=5

print("welcome to Hangman")
print(target)

i=0
g=0
o=0

while att>0:
    print("Guess the missing word")
    guess=input()

    if guess == 'i':
        i=True
    elif guess == 'g':
        g=True
    elif guess == 'o':
        o=True
    
    else:
        att-=1

    if i and g and o:
        print("ignore")
        print('Congrats! You Won.')
        break
    
    elif i and g:
        print("ign_re")
    elif g and o:
        print('_gnore')
    elif o and i:
        print("i_nore")

    elif i:
        print("i_n_re")
    elif g:
        print("_gn_re")
    elif o:
        print("ign_re")
    else:
        print("You Lost.")
        print("Try again.")
