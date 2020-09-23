#Returns a board based on user input
def board(width, height):
    top_bot = ' ---'
    vertical = '|   '
    for i in range(height):
        print(top_bot*(width))
        print(vertical*(width + 1))
    print(top_bot*(width))

board(3, 3)