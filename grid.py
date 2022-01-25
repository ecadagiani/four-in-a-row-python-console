# -*- coding: utf-8 -*-
from constants import NB_COLUMN, NB_ROW, GRID_ICONS

cells = []


def initGrid():
    """initialise cells to empty
    """
    global cells
    cells = [[0 for i in range(NB_COLUMN)] for j in range(NB_ROW)]


def gridToStr(grid):
    """transform cells array into an beautiful string

    Args:
        grid (list<list<number>>): array of cells

    Returns:
        string: beautiful string representing the table
    """
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
    """directly print table in console
    """
    print(gridToStr(cells))


def getFirstEmptyRowInColumn(column):
    """Give the first empty row for a column

    Args:
        column (index): column index 0-6

    Returns:
        number: index of first empty row. -1 if column is full.
    """
    # run trought all row, in reverse (start at last row)
    for indexRow, row in reversed(list(enumerate(cells))):
        # check if the cell from the tested row, and the past column is free
        if(row[column] == 0):
            return indexRow
    return -1


def addToken(column, player):
    """add token to the grid

    Args:
        column (number): column index 0-6
        player (number): player id 1-2

    Raises:
        ValueError: if the column is full
    """
    global cells
    row = getFirstEmptyRowInColumn(column)
    if(row < 0):
        raise ValueError(f'can\'t add token, column is full')

    cells[row][column] = player


def isGridIsFull():
    """check if grid is full of token

    Returns:
        bool: True if the grid is full
    """
    for indexRow, row in enumerate(cells):
        if 0 in row:
            return False
    return True


def checkWinner(cells):
    """ get the winner of the party

    Args:
        cells (list<list<number>>): list of cells

    Returns:
        number: get the id of the winner. 1: player1 win, 2: player2 win, 0: equality, -1: game is not over
    """
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
    # check after winner, because if the game have a winner on the last token, we can detect it
    if isGridIsFull():
        return -1
    return 0
