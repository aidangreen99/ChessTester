import os
import array
import numpy
import random
import time

rows = 7
columns = 7
ended = False 
turn = 0

def initializeboard(rows, columns):
    global board
    board = [['_' for x in range(rows)] for y in range(columns)]
    return board

def renderboard(rows, columns):
    if turn > 0:
        # os.system('cls')
        print('Your turn, ' + currentplayer + '!')
    for i in range(rows):
        for j in range(columns):
                print(board[i][j], end='   ')
        print("\n")

def placepieces(rows, columns):
    for i in range(2):
        for j in range(columns):
            board[i][j] = 'O'
    
    for i in range(2):
        for j in range(columns):
            f = rows - (i+1)
            board[f][j] = 'X'

def choosestarter():
    global startingplayer
    global players
    players = ['X','O']
    startingplayer = random.choice(players)
    return startingplayer

def startgame(starter):
    os.system('cls')
    print('Player ' + starter + ', you go first!')

def turntracker():
    global currentplayer
    if turn == 0:
        currentplayer = startingplayer
    else:
        if currentplayer == 'X':
            currentplayer = 'O' 
        else:
            currentplayer = 'X'
    
def playerinput(starter):
    global turn
    global startx
    global starty
    global endx
    global endy
    piecestring = input('Enter the location of the piece you want to move: ')
    pieceplace = input('Enter the coordinates of where you want to move that piece: ')
    piecestring.split(',')
    pieceplace.split(',')
    startx = (int(piecestring[0]) - 1 )
    starty = (int(piecestring[2]) - 1)
    endx = (int(pieceplace[0]) - 1)
    endy = (int(pieceplace[2]) - 1)
    turn += 1
    
def movecheck():
    global valid
    valid = False
    validmove = False
    validpiece = False
    print('Location: ' + str(startx + 1) + ', ' + str(starty + 1))
    print('Piece: ' + board[startx][starty])
    print('Start x: ' + str(startx))
    print('Start y: ' + str(starty))
    print('end x: ' + str(endx))
    print('end y: ' + str(endy))
    if board[startx][starty] != currentplayer:
       validpiece = False
    if board[startx][starty] == currentplayer:
        validpiece = True
    if startx - 1 == endx or startx + 1 == endx:
        if currentplayer == 'X':
            if endy - starty == 1:
                validmove = True
        if currentplayer == 'O':
            if endy - starty == 1:
                validmove = True 
    print('Valid move: ' + str(validmove))
    print('Valid piece ' + str(validpiece))
    if validmove == True and validpiece == True:
        return True
    else: 
        return False 

def playermove(valid):
    if valid == True:
        board[endx][endy] = currentplayer
        board[startx][starty] = '_'
    

initializeboard(rows, columns)
placepieces(rows, columns)
startgame(choosestarter())
while ended == False:
    turntracker()
    renderboard(rows, columns)
    print('Current player: ' + currentplayer)
    print('Turn: '+ str(turn))
    playerinput(startingplayer)
    print('Valid is ' + str(movecheck()))
    time.sleep(5)
    playermove(movecheck())