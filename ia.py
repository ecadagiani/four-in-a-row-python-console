from random import seed
from random import randint
from copy import deepcopy
import time
import grid
from constants import NB_COLUMN, NB_ROW

seed(time.time())
IA_PLAYER_ID = 2
HUMAN_PLAYER_ID = 1


def getIaColumnIndex(iaLevel):
    """get column index of the IA play

    Args:
        iaLevel (number): level of ia 1-3

    Returns:
        number: column index
    """
    if iaLevel == 1:
        return randomIA()
    if iaLevel == 2:
        return bestMove(grid.cells, searchDepth=2)
    if iaLevel == 3:
        return bestMove(grid.cells, searchDepth=5)


def randomIA():
    """get an random empty column

    Returns:
        number: column index 0-6
    """
    columnIndex = randint(0, NB_COLUMN-1)
    if grid.getFirstEmptyRowInColumn(columnIndex) < 0:
        return randomIA()
    return columnIndex


def bestMove(_cells, searchDepth):
    """ Method that executes the first call of the minimax method and
        returns the move to be executed by the computer. It also verifies
        if any immediate wins or loses are present.

    Args:
        _cells (list<list<number>>): cells of the game
        searchDepth (number): depth of the min-max search

    Returns:
        number: column index 0-6
    """
    cells = deepcopy(_cells)
    for i in range(0, NB_COLUMN):
        # If moves cannot be made on column, skip it
        if cells[0][i] != 0:
            continue

        currentMove = [0, i]

        for j in range(0, NB_ROW - 1):
            if cells[j + 1][i] != 0:
                cells[j][i] = IA_PLAYER_ID
                currentMove[0] = j
                break
            elif j == NB_ROW - 2:
                cells[j+1][i] = IA_PLAYER_ID
                currentMove[0] = j+1

        winner = grid.checkWinner(cells)
        cells[currentMove[0]][currentMove[1]] = 0

        if winner == IA_PLAYER_ID:
            return currentMove[1]

    for i in range(0, NB_COLUMN):
        # If moves cannot be made on column, skip it
        if cells[0][i] != 0:
            continue

        currentMove = [0, i]

        for j in range(0, NB_ROW - 1):
            if cells[j + 1][i] != 0:
                cells[j][i] = HUMAN_PLAYER_ID
                currentMove[0] = j
                break
            elif j == NB_ROW - 2:
                cells[j+1][i] = HUMAN_PLAYER_ID
                currentMove[0] = j+1

        winner = grid.checkWinner(cells)
        cells[currentMove[0]][currentMove[1]] = 0

        if winner == HUMAN_PLAYER_ID:
            return currentMove[1]

    move, score = minimax(cells, searchDepth)
    return move[1]


def minimax(cells, depth):
    availableMoves = NB_COLUMN
    for i in range(0, NB_COLUMN):
        if cells[0][i] != 0:
            availableMoves -= 1

    if depth == 0 or availableMoves == 0:
        score = evaluateScore(cells)
        return None, score

    bestScore = None
    bestMove = None

    for i in range(0, NB_COLUMN):
        # If moves cannot be made on column, skip it
        if cells[0][i] != 0:
            continue

        currentMove = [0, i]

        for j in range(0, NB_ROW - 1):
            if cells[j + 1][i] != 0:
                cells[j][i] = IA_PLAYER_ID
                currentMove[0] = j
                break
            elif j == NB_ROW - 2:
                cells[j+1][i] = IA_PLAYER_ID
                currentMove[0] = j+1

        # Recursive minimax call, with reduced depth
        move, score = minimax(cells, depth - 1)

        cells[currentMove[0]][currentMove[1]] = 0

        if bestScore == None or score > bestScore:
            bestScore = score
            bestMove = currentMove

    return bestMove, bestScore


def evaluateScore(cells):
    """ Method that calculates the heuristic value of a given
        board state. The heuristic adds a point to a player
        for each empty slot that could grant a player victory.

    Args:
        cells (list<list<number>>): cells of the game

    Returns:
        number: potential of win score. infinity+ on IA win, infinity- on player win
    """
    score = grid.checkWinner(cells)

    if score == IA_PLAYER_ID:
        return float("inf")
    elif score == HUMAN_PLAYER_ID:
        return float("-inf")
    else:
        score = 0

    for i in range(0, NB_ROW):
        for j in range(0, NB_COLUMN):
            if cells[i][j] == 0:
                score += scoreOfCoordinate(cells, i, j)

    return score


def scoreOfCoordinate(cells, i, j):
    """ Method that evaluates if a given coordinate has a possible win
        for any player. Each coordinate evaluates if a possible win can be
        found vertically, horizontally or in both diagonals.

    Args:
        cells (list<list<number>>): cells of the game
        i (number): row index 
        j (number): column index

    Returns:
        number: score of the coordinate
    """
    score = 0

    # Check vertical line
    score += scoreOfLine(
        cells=cells,
        i=i,
        j=j,
        rowIncrement=-1,
        columnIncrement=0,
        firstRowCondition=-1,
        secondRowCondition=NB_ROW,
        firstColumnCondition=None,
        secondColumnCondition=None
    )

    # Check horizontal line
    score += scoreOfLine(
        cells=cells,
        i=i,
        j=j,
        rowIncrement=0,
        columnIncrement=-1,
        firstRowCondition=None,
        secondRowCondition=None,
        firstColumnCondition=-1,
        secondColumnCondition=NB_COLUMN
    )

    # Check diagonal /
    score += scoreOfLine(
        cells=cells,
        i=i,
        j=j,
        rowIncrement=-1,
        columnIncrement=1,
        firstRowCondition=-1,
        secondRowCondition=NB_ROW,
        firstColumnCondition=NB_COLUMN,
        secondColumnCondition=-1
    )

    # Check diagonal \
    score += scoreOfLine(
        cells=cells,
        i=i,
        j=j,
        rowIncrement=-1,
        columnIncrement=-1,
        firstRowCondition=-1,
        secondRowCondition=NB_ROW,
        firstColumnCondition=-1,
        secondColumnCondition=NB_COLUMN
    )

    return score


def scoreOfLine(
    cells,
    i,
    j,
    rowIncrement,
    columnIncrement,
    firstRowCondition,
    secondRowCondition,
    firstColumnCondition,
    secondColumnCondition,
):
    """ Method that searches through a line (vertical, horizontal or
        diagonal) to get the heuristic value of the given coordinate.

    Args:
        cells (list<list<number>>): cells of the game
        i (number): row index
        j (number): column index
        rowIncrement (number): number to add to i (+1 / -1)
        columnIncrement (number): number to add to j (+1 / -1)
        firstRowCondition (number): condition to stop loop on row increment
        secondRowCondition (number): condition to stop loop on row increment for the second side
        firstColumnCondition (number): condition to stop loop on column increment
        secondColumnCondition (number): condition to stop loop on column increment for the second side

    Returns:
        number: score of the line
    """
    score = 0
    currentInLine = 0
    valsInARow = 0
    valsInARowPrev = 0

    # Iterate in one side of the line until a move from another
    # player or an empty space is found
    row = i + rowIncrement
    column = j + columnIncrement
    firstLoop = True
    while (
        row != firstRowCondition and
        column != firstColumnCondition and
        cells[row][column] != 0
    ):
        if firstLoop:
            currentInLine = cells[row][column]
            firstLoop = False
        if currentInLine == cells[row][column]:
            valsInARow += 1
        else:
            break
        row += rowIncrement
        column += columnIncrement

    # Iterate on second side of the line
    row = i - rowIncrement
    column = j - columnIncrement
    firstLoop = True
    while (
        row != secondRowCondition and
        column != secondColumnCondition and
        cells[row][column] != 0
    ):
        if firstLoop:
            firstLoop = False

            # Verify if previous side of line guaranteed a win on the
            # coordinate, and if not, continue counting to see if the
            # given coordinate can complete a line from in between.
            if currentInLine != cells[row][column]:
                if valsInARow == 3 and currentInLine == IA_PLAYER_ID:
                    score += 1
                elif valsInARow == 3 and currentInLine == HUMAN_PLAYER_ID:
                    score -= 1
            else:
                valsInARowPrev = valsInARow

            valsInARow = 0
            currentInLine = cells[row][column]

        if currentInLine == cells[row][column]:
            valsInARow += 1
        else:
            break
        row -= rowIncrement
        column -= columnIncrement

    if valsInARow + valsInARowPrev >= 3 and currentInLine == IA_PLAYER_ID:
        score += 1
    elif valsInARow + valsInARowPrev >= 3 and currentInLine == HUMAN_PLAYER_ID:
        score -= 1

    return score
