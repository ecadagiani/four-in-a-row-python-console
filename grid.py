# -*- coding: utf-8 -*-
from constants import NB_COLUMN, NB_ROW, GRID_ICONS

cells = []


def initGrid():
    global cells
    cells = [[0 for i in range(NB_COLUMN)] for j in range(NB_ROW)]


def gridToStr(grid):
    gridStr = ''

    # add headers
    for i in range(len(grid[0])):
        gridStr += f'    {i + 1}'

    # add columns
    for indexRow, row in enumerate(grid):
        gridStr += '\n\n'
        for indexCol, cell in enumerate(row):
            gridStr += '   '
            if(cell == 1):
                gridStr += GRID_ICONS['player1']
            elif(cell == 2):
                gridStr += GRID_ICONS['player2']
            else:
                gridStr += GRID_ICONS['empty']
    return gridStr


def printGrid():
    print(gridToStr(cells))


# Give the first empty row for a column
def getFirstEmptyRowInColumn(column):
    # run trought all row, in reverse (start at last row)
    for indexRow, row in reversed(list(enumerate(cells))):
        # check if the cell from the tested row, and the past column is free
        if(row[column] == 0):
            return indexRow
    return -1


# add token to the grid
def addToken(column, player):
    global cells
    row = getFirstEmptyRowInColumn(column)
    if(row < 0):
        raise ValueError(f'can\'t add token, column is full')

    cells[row][column] = player


def isGridIsFull():
    for indexRow, row in enumerate(cells):
        if 0 in row:
            return False
    return True


# get the winner.
# return 1 if player 1 win
# return 2 if player 2 win
# return 0 if the game is full with no winner
# return -1 if the game is not full no winner
def checkWinner(cells):
    # Horizontal
    for j in range(0, NB_ROW):
        for i in range(3, NB_COLUMN):
            if (cells[j][i] == cells[j][i-1] ==
                    cells[j][i-2] == cells[j][i-3] != 0):
                return cells[j][i]
            else:
                continue
    # Vertical
    for i in range(0, NB_COLUMN):
        for j in range(3, NB_ROW):
            if (cells[j][i] == cells[j-1][i] ==
                    cells[j-2][i] == cells[j-3][i] != 0):
                return cells[j][i]
            else:
                continue
    # Diagonal
    for i in range(0, 4):
        for j in range(0, 3):
            if (cells[j][i] == cells[j+1][i+1] ==
                    cells[j+2][i+2] == cells[j+3][i+3] != 0):
                return cells[j][i]
            elif(cells[j+3][i] == cells[j+2][i+1] ==
                    cells[j+1][i+2] == cells[j][i+3] != 0):
                return cells[j+3][i]
            else:
                continue

    if isGridIsFull():
        return -1
    return 0
