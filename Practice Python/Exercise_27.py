# Handling user inputs on tiles(list of lists)
# PLayer one always moves first 'X'
# Coordinates start from 1 eg 1,1 is 0,0
# Asks user to enter coordinates 'row, col'
# Forbid players from placing at the squares of other players
# Keep track of how many squares are full 
# Stop asking when there are no empty squares

def TicTacToeDraw(list_):
    print('Coordinates start at 1 and ends at 3, eg 1,1 means its the first row and first column.')
    counter = 0
    turn = 0
    while counter != 9:
        if turn == 0:
            move = input('Player 1\'s turn to move! Filled spaces {}.\n'.format(counter))
            sym = 'X'
            turn += 1
        elif turn == 1:
            move = input('Player 2\'s turn to move! Filled spaces {}.\n'.format(counter))
            turn -= 1
            sym = 'O'
        move = move.split(',')
        if list_[int(move[1])-1][int(move[0])-1] == '-':
            list_[int(move[1])-1][int(move[0])-1] = sym
            counter += 1
        else:
            print('Error this square already has a value, you dont get a turn')
        for i in list_:
            print(i)

empty = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

TicTacToeDraw(empty)