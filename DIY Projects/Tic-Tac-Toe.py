# Tic Tac Toe Implementations 
import random

def print_board(lst):
    st = '''
        {} | {} | {}     
      -----------------
        {} | {} | {}
      ------------------    
        {} | {} | {}
        '''.format(*lst)
    print(st)

print('Welcome To Tic_Tac_Toe'.center(100))
choices = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
player1_name = input("Enter name of player 1: ")
player2_name = input("Enter name of player 2: ")
user_1 = input(f"What do you want to choose {player1_name} [X or O]: ").upper()
user_2 = 'O' if user_1 == 'X' else 'X'
print(f"{player2_name}, you are {user_2}")
turn = random.randint(1, 2)
print("Let's Toss which Player will go first")
print(f'Player {turn} will start the game')
print("Here Is Your Board.......")
print_board(choices)

def check_win(choices):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for a, b, c in win_conditions:
        if choices[a] == choices[b] == choices[c] and choices[a] != " ":
            return True
    return False

# main code....
turns = user_1 if turn == 1 else user_2
for i in range(9):
    while True:
        mv = int(input(f'Its Your turn Player {turn}, Your Move [0-8]: '))
        if 0 <= mv < 9 and choices[mv] == " ":
            choices[mv] = turns
            break
        else:
            print("Invalid move. Try again.")
    
    print_board(choices)
    if check_win(choices):
        print(f'Game Over. Player {turn} ({turns}) wins!')
        break
    turns = "X" if turns == "O" else "O"
    turn = 1 if turn == 2 else 2
else:
    print("It's a tie!")

print_board(choices)
