# Projet initiation Python

# Puissance 4

Ce projet consistera à mettre en place un jeu de puissance 4 en python. Le jeu permettra à 2 joueurs humains de joueur en local, l'affichage se fera sur la console, et il aura une vérification automatique du gagnant.

### 1. Grille et affichage
Mettre en place une grille de 7 colonnes / 6 lignes (`tableau à double entrée`). Cette grille représentera la grille de jeu. Par défaut la grille sera remplie de zero `0`. Les jetons jaune seront représentés par `1`, et les jetons rouges par `2`.

Créer une fonction qui permettra l'affichage de cette grille dans la console de façon esthétique (avec par exemple ⚪️ 🔴 🟡). Chaque colonne devra être numérotée de 1 à 7.

### 2. Gameplay
Au lancement du jeu, le joueur jaune est invité à donner la colonne où il souhaite déposer son jeton (le joueur jaune doit simplement écrire le numéro de la colonne ciblé dans la console). Puis le jeton tombe dans la colonne. On affiche ensuite la grille avec le nouveau jeton jaune.

Le joueur rouge est invité à faire de même. On affiche la nouvelle grille avec le jeton jaune et rouge, et ainsi de suite jusqu'à que la partie soit terminée, ou que les 2 joueurs ont joué leurs 21 jetons respectifs.

> ATTENTION si un joueur donne une mauvaise valeur, il faudra lui redemander une valeur de colonne cohérente.

### 3. Fin de partie
A chaque jeton joué il faudra vérifier qu'il n'y a pas 4 jetons de la même couleur alignés. Cet alignement peut ce faire en vertical, en horizontal ou en diagonale.

### 4. Enregistrement
Pour chaque partie, créer un fichier de sauvegarde du déroulement de la partie. Utiliser la date et l'heure dans le nom de fichier pour avoir un fichier de sauvegarde différent par partie. Dans ce fichier vous y stockerez l'évolution de la grille, et les coups joués. La grille doit être affichée de manière esthétique.

### 5. BONUS IA
Au début de la partie, il faudra proposer à l'utilisateur de choisir entre une partie 2 joueurs ou 1 joueur. S'il choisit une partie 1 joueur, il jouera les jaunes, et une IA jouera les rouges.

L'IA devra jouer les jetons rouges de façon intelligente et non aléatoire, elle devra bloquer les tentatives d'alignement de l'adversaire.


> Auteur Eden Cadagiani