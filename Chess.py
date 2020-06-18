import os
import array
import numpy
import random


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
        os.system('cls')
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
    
def playermove(starter):
    global turn
    global startx
    global starty
    global endx
    global endy
    piecestring = input('Enter the location of the piece you want to move: ')
    pieceplace = input('Enter the coordinates of where you want to move that piece: ')
    piecestring.split(',')
    pieceplace.split(',')
    startx = int(piecestring[0])
    starty = int(piecestring[2])
    endx = int(pieceplace[0])
    endy = int(pieceplace[2])
    turn += 1
    


    

initializeboard(rows, columns)
placepieces(rows, columns)
startgame(choosestarter())
while ended == False:
    turntracker()
    renderboard(rows, columns)
    print('Current player: ' + currentplayer)
    print('Turn: '+ str(turn))
    playermove(startingplayer)