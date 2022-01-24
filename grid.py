# -*- coding: utf-8 -*-
from constants import nbCol, nbRow, gridIcons

cells = []


def initGrid():
    global cells
    cells = [[0 for i in range(nbCol)] for j in range(nbRow)]


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
                gridStr += gridIcons['player1']
            elif(cell == 2):
                gridStr += gridIcons['player2']
            else:
                gridStr += gridIcons['empty']
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
