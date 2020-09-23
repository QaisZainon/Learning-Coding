#Write a code that checks whether someone has won a game of tic-tac-toe
#Given a 3x3 list, check whether someone has won, 1 & 2 is players, 0 is null

def win_checker(list_):
    #Checks for horizontol win condition
    for i in list_:
        one_count = 0
        two_count = 0
        for a in i:
            if a == 1:
                one_count += 1
            if a == 2:
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
            if list_[s][i] == 1:
                one_count += 1
            if list_[s][i] == 2:
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
            if list_[a][a if i == 0 else s] == 1:
                one_count += 1
            if list_[a][a if i == 0 else s] == 2:
                two_count += 1
        if one_count == 3:
            return print('Player one wins (d)')
        if two_count == 3:
            return print('Player two wins (d)')

winner_is_2 = [
    [2, 2, 0],
    [2, 1, 0],
    [2, 1, 1]
    ]

winner_is_1 = [
    [1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]
    ]

winner_is_also_1 = [
    [0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]
    ]

no_winner = [
    [1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]
    ]

also_no_winner = [
    [1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]
    ]

win_checker(winner_is_2)
win_checker(winner_is_1)
win_checker(winner_is_also_1)
win_checker(no_winner)
win_checker(also_no_winner)