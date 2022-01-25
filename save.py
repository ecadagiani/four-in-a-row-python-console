import os
from datetime import datetime
import grid
from constants import PLAYER_NAME

fileName = ''
dirPath = os.path.dirname(__file__) + "/saves"


def initSave():
    global fileName
    strDate = datetime.now().strftime("%d-%m-%y %H:%M:%S")
    fileName = f"connect4 - {strDate}"


def getFilePath():
    return f"{dirPath}/" + fileName + ".log"


def addToSaveFile(text):
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
    addToSaveFile(
        f'{grid.gridToStr(grid.cells)}\nLe joueur {PLAYER_NAME[player]} joue en {column+1}\n\n----------------------\n'
    )


def saveWin(winner, ia=False):
    addToSaveFile(
        f'{grid.gridToStr(grid.cells)}\n\n'
    )
    if winner == 0:
        addToSaveFile('\n\n Egalité. Merci d\'avoir joué')
    elif winner == 1 or (winner == 2 and not ia):
        addToSaveFile(f'\n\n Bravo joueur {PLAYER_NAME[winner] } tu as gagné!')
    elif winner == 2 and ia:
        addToSaveFile(f'\n\n Perdu l\'IA a gagné!')
