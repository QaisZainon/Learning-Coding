#Returns a board based on user input
empty = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

def drawboard(board):
    print ('   |   |   ')
    print (' ' +board[0][0]+ ' | ' +board[0][1]+ ' | ' +board[0][2] )
    print ('   |   |   ')
    print ('---+---+---')
    print ('   |   |   ')
    print (' ' +board[1][0]+ ' | ' +board[1][1]+ ' | ' +board[1][2] )
    print ('   |   |   ')
    print ('---+---+---')
    print ('   |   |   ')
    print (' ' +board[2][0]+ ' | ' +board[2][1]+ ' | ' +board[2][2] )
    print ('   |   |   ')

def TicTacToeDraw(list_):
    drawboard(list_)
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
        drawboard(list_)
        for i in list_:
            one_count = 0
            two_count = 0
            for a in i:
                if a == 'X':
                    one_count += 1
                if a == 'O':
                    two_count += 1
            if one_count == 3:
                return print('Player one wins (h)')
            if two_count == 3:
                return print('Player two wins (h)')
        #Checks for vertical win condition
        for i in range(3):
            one_count = 0
            two_count = 0
            for s in range(3):
                if list_[s][i] == 'X':
                    one_count += 1
                if list_[s][i] == 'O':
                    two_count += 1
            if one_count == 3:
                return print('Player one wins (v)')
            if two_count == 3:
                return print('Player two wins (v)')
        #Checks for diagonal win condition (2)
        b = [2,1,0]
        for i in range(2):
            one_count = 0
            two_count = 0
            for a, s in enumerate(b):
                if list_[a][a if i == 0 else s] == 'X':
                    one_count += 1
                if list_[a][a if i == 0 else s] == 'O':
                    two_count += 1
            if one_count == 3:
                return print('Player one wins (d)')
            if two_count == 3:
                return print('Player two wins (d)')

TicTacToeDraw(empty)