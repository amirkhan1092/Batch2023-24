# tic tac toe 

def print_board(board):
    s = '''
    {}|{}|{}
    -+-+-
    {}|{}|{} 
    -+-+-
    {}|{}|{} 

    '''. format(*board)
    print(s)



# main code 

print('Welocome to the Tic Toe Game ')
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
turn = 'X'
for i in range(10):

    print_board(board)
    
    print(f'Its your turn {turn}. move to which place ?')
    choice = int(input())

    if board[choice] == ' ':
        board[choice] = turn
    else:
        print('Place Already Filled Move to next place ')
        continue


    if board[0] == board[1] == board[2] != ' ':
        print_board(board)
        print('Game Over')
        print(f'*****{turn} Won *****')
        break
    elif board[0] == board[3] == board[6] != ' ':
        print_board(board)
        print('Game Over')
        print(f'*****{turn} Won *****')
        break


    # change the player after every move 
    turn = 'X' if turn != 'X' else 'O'


