import numpy as np

class Board:

    def __init__(self):
        # ligne, colonne, espèce(humains, loup-garous, vampires)
        self.grid = np.array([
            [[1, 2, 3], [3, 4, 6]],
            [[5, 9, 5], [2, 1, 1]]
        ], dtype=np.int32)
        self.currentPlayer = 0


    def play_action(grid, departure_case, target_cible):
        '''fonction qui prend en entrée la grille + la case de départ + la case cible
         + le nombre de personnes à bouger et qui retourne la nouvelle grille'''
        return None




