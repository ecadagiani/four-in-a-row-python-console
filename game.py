# -*- coding: utf-8 -*-
import os
import datetime
import json
import grid
import save
import ia
from constants import PLAYER_NAME, NB_COLUMN, NB_ROW


nbPlayer = int()
iaLevel = int()


def start():
    """ Initialise game before launch. Ask for the number of player and the IA level
    """
    global nbPlayer
    global iaLevel
    grid.initGrid()
    save.initSave()
    nbPlayer = askNbPlayer()
    if nbPlayer == 1:
        iaLevel = askIaLevel()


def run():
    """Launch the game return only when the game is over (exec start() before)
    """
    winner = -1
    isGameOver = False
    playerTurn = 1  # which player to play
    while not isGameOver:
        grid.printGrid()
        columnIndex = int()

        # ask column to human player
        print(f'[JOUEUR { PLAYER_NAME[playerTurn] }] - À votre tour ')
        columnIndex = askColumn()
        # send the token
        grid.addToken(columnIndex, playerTurn)

        # IA play
        if(nbPlayer == 1):
            # get the column from the IA
            columnIndex = ia.getIaColumnIndex(iaLevel)
            # add ia token to the gris
            grid.addToken(columnIndex, 2)

        # add this turn to a save file
        save.saveTurn(playerTurn, columnIndex)

        # if two player, change playerTurn for next player
        if playerTurn == 1 and nbPlayer == 2:
            playerTurn = 2
        else:
            playerTurn = 1

        # check if the game is over
        winner = grid.checkWinner(grid.cells)
        isGameOver = winner != 0

    # Game is over, display grid one more time
    grid.printGrid()
    # Display success message
    if winner == -1:
        print('\n\n Egalité. Merci d\'avoir joué')
    elif winner == 1 or (winner == 2 and nbPlayer == 2):
        print(f'\n\n Bravo joueur {PLAYER_NAME[winner] } tu as gagné!')
    elif winner == 2 and nbPlayer == 1:
        print(f'\n\n Perdu l\'IA a gagné!')
    # save succes message to the save file
    save.saveWin(winner, nbPlayer == 1)


def askNbPlayer():
    """ask for the number of player

    Returns:
        number: the number of player 1(IA) or 2
    """
    nb = 0
    try:
        userResponse = input("Combien de joueur 1 ou 2: ")
        nbPlayer = int(userResponse)
        if not (0 < nbPlayer <= 2):
            raise(ValueError('wrong number'))
        return nbPlayer
    except ValueError:
        print('\nErreur - Vous devez entrer un nombre entre 1 et 2\n')
        return askNbPlayer()


def askIaLevel():
    """ask for the level of IA

    Returns:
        number: the level of IA 1-3
    """
    nb = 0
    try:
        userResponse = input("Niveau de l'IA 1 à 3 : ")
        iaLevel = int(userResponse)
        if not (0 < iaLevel <= 3):
            raise(ValueError())
        return iaLevel
    except ValueError:
        print('\nErreur - Vous devez entrer un nombre entre 1 et 3\n')
        return askIaLevel()


def askColumn():
    """ask user for a column to add token

    Returns:
        number: column index 0-6
    """
    nb = 0
    try:
        userResponse = input("Choisissez une colonne où jouer: ")
        columnIndex = int(userResponse) - 1
        if not (0 <= columnIndex < NB_COLUMN):
            raise(ValueError())
        if grid.getFirstEmptyRowInColumn(columnIndex) < 0:
            raise(ValueError())
        return columnIndex
    except ValueError:
        print(
            f'\nErreur - Vous devez choisir une colonne vide entre 1 et {NB_COLUMN}\n'
        )
        return askColumn()
