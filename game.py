# -*- coding: utf-8 -*-
import os
import datetime
import json
import grid
from constants import playerName, nbCol, nbRow


nbPlayer = int()
iaLevel = int()


def start():
    global nbPlayer
    global iaLevel
    grid.initGrid()
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
        print(f'[JOUEUR { playerName[playerTurn] }] - À votre tour ')
        columnIndex = askColumn()
        # Envoie du jeton
        grid.addToken(columnIndex, playerTurn)

        # IA play
        if(nbPlayer == 1):
            print('ia turn')

        # todo: save

        if playerTurn == 1 and nbPlayer == 2:
            playerTurn = 2
        else:
            playerTurn = 1

        winner = getWinner(grid.cells)
        isGameOver = winner != -1

    grid.printGrid()
    if winner == 0:
        print('\n\n Egalité. Merci d\'avoir joué')
    elif winner == 1 or (winner == 2 and nbPlayer == 2):
        print(f'\n\n Bravo joueur {playerName[winner] } tu as gagné!')
    elif winner == 2 and nbPlayer == 1:
        print(f'\n\n Perdu l\'IA a gagné!')


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
        if not (0 <= columnIndex < nbCol):
            raise(ValueError())
        if grid.getFirstEmptyRowInColumn(columnIndex) < 0:
            raise(ValueError())
        return columnIndex
    except ValueError:
        print(
            f'\nErreur - Vous devez choisir une colonne vide entre 1 et {nbCol}\n'
        )
        return askColumn()


# get the winner.
# return 1 if player 1 win
# return 2 if player 2 win
# return 0 if the game is full with no winner
# return -1 if the game is not full no winner
def getWinner(cells):
    # Horizontal
    for j in range(0, nbRow):
        for i in range(3, nbCol):
            if (cells[j][i] == cells[j][i-1] ==
                    cells[j][i-2] == cells[j][i-3] != 0):
                return cells[j][i]
            else:
                continue
    # Vertical
    for i in range(0, nbCol):
        for j in range(3, nbRow):
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

    if grid.isGridIsFull():
        return 0
    return -1
