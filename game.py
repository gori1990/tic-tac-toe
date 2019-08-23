def displayBoard(board2D):
    print("  1 2 3")
    lineNumber = 1
    for line in board2D:
        print(lineNumber, end=" ")
        for element in line:
            print(element, end=" ")
        print()
        lineNumber += 1

playCross = False

question = input("Jeżeli ma zacząć krzyżyk wpisz X, a jeżeli kółko wpisz O: ")
if question =="X":
    playCross = True

board = [["*","*","*"],["*","*","*"],["*","*","*"]]

displayBoard(board)