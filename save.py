import os
from datetime import datetime
import grid
from constants import PLAYER_NAME

fileName = ''
dirPath = os.path.dirname(__file__) + "/saves"


def initSave():
    """create the fileName based on datetime for save file
    """
    global fileName
    strDate = datetime.now().strftime("%d-%m-%y %H:%M:%S")
    fileName = f"connect4 - {strDate}"


def getFilePath():
    """get full path for save file

    Returns:
        string: the full file path for save file
    """
    return f"{dirPath}/" + fileName + ".log"


def addToSaveFile(text):
    """add text to save file (mode: append)

    Args:
        text (string): text to add
    """
    # Create save dir if not exist
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)

    filePath = getFilePath()

    # Create file if not exist
    if not os.path.exists(filePath):
        with open(filePath, "w") as f:
            pass

    # Save file status
    with open(filePath, "a") as f:
        f.write(text)


def saveTurn(player, column):
    """add turn summary to save file

    Args:
        player (number): player id 1/2
        column (number): column index 0-6
    """
    addToSaveFile(
        f'{grid.gridToStr(grid.cells)}\nLe joueur {PLAYER_NAME[player]} joue en {column+1}\n\n----------------------\n'
    )


def saveWin(winner, ia=False):
    """add win text to save file

    Args:
        winner (number): the id of the winner -1: equity, 1: player, 2: player or IA
        ia (bool, optional): if game use IA or player. Defaults to False.
    """
    addToSaveFile(
        f'{grid.gridToStr(grid.cells)}\n\n'
    )
    if winner == -1:
        addToSaveFile('\n\n Egalité. Merci d\'avoir joué')
    elif winner == 1 or (winner == 2 and not ia):
        addToSaveFile(f'\n\n Bravo joueur {PLAYER_NAME[winner] } tu as gagné!')
    elif winner == 2 and ia:
        addToSaveFile(f'\n\n Perdu l\'IA a gagné!')
