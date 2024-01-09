# Tic Tac Toe

def print_stack(lst):
    print(f'''
{lst[0]}|{lst[1]}|{lst[2]}
----------
{lst[3]}|{lst[4]}|{lst[5]}
----------
{lst[6]}|{lst[7]}|{lst[8]}''')
    

# main code 
moves = [' '] * 9
print_stack(moves)

choice = 'X'
while 1:
    try:
        m_id = int(input(f'Turn {choice} Enter the move position (0-8) '))
        right_index = moves[m_id]
    except :
        print('Wrong move Try Again')
        continue
    if moves[m_id] == ' ':
        moves[m_id] = choice
    else:
        print('location already used ')
        continue
    print_stack(moves)


    choice = 'X' if choice == '0' else '0'
