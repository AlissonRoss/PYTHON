#Alisson Leiva Assignment 5 Question 2 ATTEMPT
count=0
i=0
winP1=0
winP2=0
p1=()
p2=()
#Arrays

row1=[' ',' ',' ']
                  
row2=[' ',' ',' ']

row3=[' ',' ',' ']

allRows=(row1,row2,row3)
#Graphic for Tic-Tac-Toe
def tictactoeGraph():
    for i in range (0,3):
        for x in range(0,1):
            print(allRows[i][0],chr(124),allRows[i][1],chr(124),allRows[i][2])
        if i < 2:
            print(chr(45),chr(43),chr(45),chr(45))
        
                  
                                                                  
#Inputs for players
def inputIn():
    print("Player #1")
    name1=input("Enter name for player 1:")
    p1.append(name1)
    print("Player #2")
    name2=input("Enter name for player 2:")
    p2.append(name2)
    
    (rowsColsIn())
def rowsColsIn():
    #For player 1
    print("Player",p1,"'s Turn")
    row=int(input("Enter row:"))
    col=int(input("Enter column:"))
    return row, col
    print("Player",p2,"'s Turn")
    row=input(int("Enter row:"))
    col=input(int("Enter column:"))
    return row, col
def invalidLocation(allRows,row,col):
    while allRows [row-1] [col-1] == "X" or allRows [rows-1] [col-1] == '0':
        print("Invalid Location")
        row=int(input("Input valid location for row:"))
        col=int(input("Input valid location for column:"))

    allRows[row-1][col-1] = inputPlay
def checkWin(allRows,playId):
    winCon = 0
    if allRows [0][0] == player and allRows[0][1] == player and allRows[0][2] == player:
        winCon=1
    elif allRows [1][0] == player and allRows[1][1] == player and allRows[1][2] == player:
        winCon=1
    elif allRows [2][0] == player and allRows[2][1] == player and allRows[2][2] == player:
        winCon=1
    elif allRows [0][1] == player and allRows[1][0] == player and allRows[2][1] == player:
        winCon=1
    elif allRows [0][0] == player and allRows[1][1] == player and allRows[2][2] == player:
        winCon=1
    elif allRows [0][2] == player and allRows[1][1] == player and allRows[2][0] == player:
        winCon=1
    return winCon
while count < 9 and winP1 == 0 and winP2 == 0:
    row,col=rowsColsIn()
    invalidLocation(allRows,row,col,"X")
    (tictactoeGraph())
    winP1 = checkWin(allRows,"X")
    

    count=count+1

    if winP1 != 1:
        row,col = rowsColsIn()
        invalidLocation(allRows,row,col,"O")
        (tictactoeGraph())
        winP2 = checkWin(allRows,"O")

        turn=1
        count=count+1
if winP1 == 1:
    print(p1[i],"is the winner!")
elif winP2 == 2:
    print(p2[i],"is the winner!")
else:
    print("The game ends in a tie!")
    
    
    
#Printing Functions
(tictactoeGraph())
(inputIn())
