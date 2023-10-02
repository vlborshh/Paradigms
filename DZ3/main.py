field = [0, 1, 2, 3, 4, 5, 6, 7, 8]

wins = [[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]]

def printField():
    print(field[0], end = " ")
    print(field[1], end = " ")    
    print(field[2])

    print(field[3], end = " ")
    print(field[4], end = " ")    
    print(field[5])

    print(field[6], end = " ")
    print(field[7], end = " ")    
    print(field[8])

def moveCell(step, simbol):
    field[step] = simbol

def winGame():
    win = ""
    for i in wins:
        if field[i[0]] == "X" and field[i[1]] == "X" and field[i[2]] == "X":
            win = "X"
        if field[i[0]] == "O" and field[i[1]] == "O" and field[i[2]] == "O": 
            win = "O"   
    return win



gameOver = False
player = True
simbol = "X"

while gameOver == False:
    printField()
    step = int(input("Игрок делайте ваш ход: "))
    if player == True:
        simbol = "X"
    else:
        simbol = "O"
    player = not(player)
    moveCell(step, simbol) 
    win = winGame()      
    if win != "":
        gameOver = True
printField()
print("Победил: ", win)