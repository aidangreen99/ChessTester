import os
import array
import numpy


rows = 7
columns = 7


def initializeboard(rows, columns):
    global board
    board = [['_' for x in range(rows)] for y in range(columns)]
    return board

def renderboard(rows, columns):
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
    
    
initializeboard(rows, columns)
placepieces(rows, columns)
renderboard(rows, columns)
