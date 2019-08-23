def displayBoard(board2D):
    print("  1 2 3")
    lineNumber = 1
    for line in board2D:
        print(lineNumber, end=" ")
        for element in line:
            print(element, end=" ")
        print()
        lineNumber += 1

def win(board2D):
    for x in range(0,3):
        if board2D[x][0] == board2D[x][1] and board2D[x][1] == board2D[x][2] and board2D[x][2] == "X" or board2D[x][2] == "O":
            return True

    for y in range(0,3):
        if board2D[0][y] == board2D[1][y] and board2D[1][y] == board2D[2][y] and board2D[y][2] == "X" or board2D[y][2] == "O":
            return True
    if board2D[0][0] == board2D[1][1] and board2D[1][1] == board2D[2][2] and board2D[2][2] == "X" or board2D[2][2] == "O":
        return True
    if board2D[0][2] == board2D[1][1] and board2D[1][1] == board2D[2][0] and board2D[2][0] == "X" or board2D[2][0] == "O":
        return True

    return False

def draw(board2D):
    if not  win(board2D):
        for line in board2D:
            for element in line:
                if element == "*":
                    return False
        return True
    else:
        return False


playCross = False

question = input("Jeżeli ma zacząć krzyżyk wpisz X, a jeżeli kółko wpisz O: ")
if question =="X":
    playCross = True

board = [["*","*","*"],["*","*","*"],["*","*","*"]]

displayBoard(board)

while(not draw(board)) and (not win(board)):
    displayBoard(board)
    x, y = [int (x) for x in input("Podaj współrzędne pola na którym chcesz postawić krzyżyk bądz kółko").split()]
    if board[x-1][y-1] == "*":
        if playCross:
            board[x-1][y-1] = "X"
            playCross = False
        else:
            board[x-1][y-1] ="O"
            playCross = True
if win(board):
    if playCross:
        print("Wygrał gracz grający kółkiem. Gratulujemy")
    else:
        print("Wygrał gracz grający Krzyżykiem. Gratulujemy")
else:
    print("Nastąpił remis")