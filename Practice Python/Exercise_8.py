'''
Make a two-player Rock-Paper-Sciossors game based on two inputs
compare them, print out a message to congratulate 
ask them whether to start a new game
'''


player_1 = ''
player_2 = ''

def game_loop():
    while True:
        global player_1
        global player_2
        player_1 = input('Player_1 move\n')
        player_2 = input('Player_2 move\n')
        rps_logic()
        reply = input('Do you still want to continue? type \'quit\' to exit\n')
        if reply == 'quit':
            break

def rps_logic():
    win = 'player_1 wins'
    loss = 'player_1 losses'
    tie = 'Tie'
    if player_1 == 'rock':
        if player_2 == 'paper':
            print(loss)
        if player_2 == 'scissor':
            print(win)
        if player_2 == 'rock':
            print(tie)
    if player_1 == 'paper':
        if player_2 == 'paper':
            print(tie)
        if player_2 == 'scissor':
            print(loss)
        if player_2 == 'rock':
            print(win)
    if player_1 == 'scissors':
        if player_2 == 'paper':
            print(win)
        if player_2 == 'scissor':
            print(tie)
        if player_2 == 'rock':
            print(loss)

game_loop()