# Python initiation project

# Connect4

This project will consist of setting up a connect4 game in python. The game will allow 2 human players to play locally, display will be on console, and it will have automatic winner verification.

### 1. Grid and display
Set up a 7 column / 6 row grid (`double entry table`). This grid will represent the game grid. By default the grid will be filled with zero `0`. Yellow tokens will be represented by `1`, and red tokens by `2`.

Create a function that will display this grid in the console in an aesthetic way (with for example ⚪️ 🔴 🟡'). Each column should be numbered from 1 to 7.


### 2. Gameplay
When the game is launched, the yellow player is asked to give the column where he wishes to deposit his token (the yellow player must simply write the number of the targeted column in the console). Then the token falls into the column. The grid is then displayed with the new yellow token.

The red player is invited to do the same. The new grid is displayed with the yellow and red tokens, and so on until the game is over, or the 2 players have played their respective 21 tokens.

> ATTENTION if a player gives a bad value, he will have to ask him for a consistent column value.


### 3. Endgame
With each token played, it will be necessary to check that there are not 4 tokens of the same color aligned. This alignment can be done vertically, horizontally or diagonally.


### 4. Registration
For each game, create a backup file of the progress of the game. Use date and time in the filename to have a different save file per game. In this file you will store the evolution of the grid, and the moves played. The grid should be displayed aesthetically.


### 5. BONUS AI
At the start of the game, the user must be offered the choice between a 2-player or 1-player game. If he chooses a 1 player game, he will play the yellow, and an AI will play the reds.

The AI will have to play the red chips intelligently and not randomly, it will have to block the opponent's alignment attempts.

> Author Eden Cadagiani