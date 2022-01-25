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
    global nbPlayer
    global iaLevel
    grid.initGrid()
    save.initSave()
    nbPlayer = askNbPlayer()
    if nbPlayer == 1:
        iaLevel = askIaLevel()


def run():
    winner = -1
    isGameOver = False
    playerTurn = 1  # which player to play
    while not isGameOver:
        grid.printGrid()
        columnIndex = int()

        # ask column to human player
        print(f'[JOUEUR { PLAYER_NAME[playerTurn] }] - À votre tour ')
        columnIndex = askColumn()
        # Envoie du jeton
        grid.addToken(columnIndex, playerTurn)

        # IA play
        if(nbPlayer == 1):
            columnIndex = ia.getIaColumnIndex(iaLevel)
            grid.addToken(columnIndex, 2)

        save.saveTurn(playerTurn, columnIndex)

        if playerTurn == 1 and nbPlayer == 2:
            playerTurn = 2
        else:
            playerTurn = 1

        winner = grid.checkWinner(grid.cells)
        isGameOver = winner != 0

    grid.printGrid()
    if winner == -1:
        print('\n\n Egalité. Merci d\'avoir joué')
    elif winner == 1 or (winner == 2 and nbPlayer == 2):
        print(f'\n\n Bravo joueur {PLAYER_NAME[winner] } tu as gagné!')
    elif winner == 2 and nbPlayer == 1:
        print(f'\n\n Perdu l\'IA a gagné!')
    save.saveWin(winner, nbPlayer == 1)


def askNbPlayer():
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
