from random import random, randint
import numpy as np
from draw import start_GUI, draw

RACE_ID = {
    'hum': 0,
    'vamp': 1,
    'wolv': 2,
}

SKIP_CHECKS = False

class ActionInvalidError(Exception):
    pass

class Board:
    def __init__(self, dimensions, initial_pop):
        shape = (dimensions[0], dimensions[1], 3)
        self.grid = np.zeros(shape, dtype=np.int32)
        self.update_grid(initial_pop)
        self.currentPlayer = None

    def enumerate_squares(self):
        line, column, _ = self.grid.shape
        return [(i, j) for i in range(line) for j in range(column)]

    def is_over(self):
        nb_w = 0
        nb_v = 0
        for square in self.enumerate_squares():
            nb_v += self.grid[square][RACE_ID['vamp']]
            nb_w += self.grid[square][RACE_ID['wolv']]
            if nb_w and nb_v:
                return False
        return 'vamp'*(bool(nb_v)) + 'wolv'*(bool(nb_w)) or 'hum'

    def update_grid(self, changed_squares):
        for square in changed_squares:
            x = square['x']
            y = square['y']
            # x, y server representation is not equal to our line column matrix model
            self.grid[y, x, RACE_ID['hum']] = square['hum']
            self.grid[y, x, RACE_ID['vamp']] = square['vamp']
            self.grid[y, x, RACE_ID['wolv']] = square['wolv']

    def moves(self, action):
        ''' Moves the units, do not resolve any fight'''
        if SKIP_CHECKS or action.is_valid(self):
            self.grid[action._from][RACE_ID[action.race]] -= action.number
            self.grid[action.to][RACE_ID[action.race]] += action.number
        else:
            print(action)
            raise ActionInvalidError('action not valid')

    def do_actions(self, actions):
        print(actions)
        for action in actions:
            self.moves(action)
        for square in self.enumerate_squares():
            self.resolve_square(square)

    def resolve_square(self, square):
        nb_zeros = list(self.grid[square]).count(0)
        if nb_zeros >= 2:
            return
        elif nb_zeros == 0:
            raise ValueError('impossible to resolve 3 races on one square')
        elif nb_zeros == 1:
            if self.grid[square][RACE_ID['hum']] > 0:
                print(square, RACE_ID['hum'])
                result = attack_humans(self.currentPlayer, self.grid[square])
            else:
                result = attack_monsters(self.currentPlayer, self.grid[square])
            self.grid[square] = result

class Action:
    def __init__(self, from_square, to_square, number, race):
        self._from = from_square
        self.to = to_square
        self.number = number
        self.race = race
        self.race_ennemi = 'wolv' if self.race == 'vamp' else 'vamp'

    def __repr__(self):
        return '{} {} {} {}'.format(self._from, self.to, self.number, self.race)

    @staticmethod
    def square_is_on_grid(square, grid):
        return all([
            0 <= square[0] < grid.shape[0], # line played <= number of lines
            0 <= square[1] < grid.shape[1], # column played <= number of columns
        ])

    def is_valid(self, board, actions=None):
        dif_x = abs(self._from[0] - self.to[0])
        dif_y = abs(self._from[1] - self.to[1])
        return all([
            dif_x <= 1,
            dif_y <= 1,
            self._from != self.to,
            self.race in ['vamp', 'wolv'],
            Action.square_is_on_grid(self.to, board.grid),
            Action.square_is_on_grid(self._from, board.grid) and \
                0 < self.number <= board.grid[self._from][RACE_ID[self.race]],
            not actions or self.to not in [ac._from for ac in actions]
        ])

def attack_humans(attacker, square, probabilistic=False):
    print(square)
    units = square[RACE_ID[attacker]]
    enemies = square[RACE_ID['hum']]
    if units/enemies >= 1:
        units += enemies
        enemies = 0
    else:
        p = units / (2 * enemies)
        sort = random()
        if sort > p:
            units = 0
            enemies = int(enemies * (1-p))
        else:
            units += enemies
            units = int(p*units)
            enemies = 0
    res = [0, 0, 0]
    res[RACE_ID[attacker]] = units
    res[RACE_ID['hum']] = enemies
    return res

def attack_monsters(attacker, square, probabilistic=False):
    print(square)
    units = square[RACE_ID[attacker]]
    enemy_race = 'wolv' if attacker == 'vamp' else 'vamp'
    enemies = square[RACE_ID[enemy_race]]
    print('Enemies : {} {}'.format(enemy_race, enemies))
    if units/enemies >= 1.5:
        enemies = 0
    else:
        #si victoire (proba p) : chaque attaquant a une proba (p) de survivre
        #                        chaque humain a une proba (p) de devenir allié
        #si défaite (1-p) : aucun survivant coté attaquant
        #                   chaque humain a une proba (1-p) de survivre
        if units >= enemies:
            p = units / enemies - 0.5
        else:
            p = units / (2 * enemies)
        sort = random()
        if sort > p:  # defeat of attacker
            units = 0
            enemies = int(enemies * (1-p))
        else:
            units = int(p*units)
            enemies = 0
    res = [0, 0, 0]
    res[RACE_ID[attacker]] = units
    res[RACE_ID[enemy_race]] = enemies
    return res

def get_random_adjacent_square(grid, square):
    not_on_grid = True
    to = None
    while not_on_grid or to == square:
        to = (square[0] + randint(-1, 1), square[1] + randint(-1, 1))
        not_on_grid = not Action.square_is_on_grid(to, grid)
    return to

class Player:
    def __init__(self, race):
        self.race = race
        print(race)

    def get_next_move(self, board):
        raise NotImplementedError()

class RamdomPlayer(Player):
    def get_next_move(self, board):
        actions = []
        for square in board.enumerate_squares():
            units = board.grid[square][RACE_ID[self.race]]
            if units > 0:
                print(square)
                to = get_random_adjacent_square(board.grid, square)
                print(Action(square, to, units, self.race))
                return [Action(square, to, units, self.race)]
                #actions.append(Action(square, to, square[RACE_ID[self.race]], self.race))
                #print(actions[-1])
        print(actions)
        return actions

def play(*args):
    global p1, p2, b
    p = p1
    game_over = False
    while not game_over:
        b.currentPlayer = p.race
        actions = p.get_next_move(b)
        print(actions)
        b.do_actions(actions)
        draw(b.grid)
        from time import sleep
        sleep(0.3)
        p = p2 if p == p1 else p1
        game_over = b.is_over()
    print(b.is_over() + 'won !')

if __name__ == '__main__':

    initial_pop = [{'x': 0, 'y': 0, 'hum': 0, 'vamp': 4, 'wolv': 0},
                   {'x': 1, 'y': 3, 'hum': 5, 'vamp': 0, 'wolv': 0},
                   {'x': 3, 'y': 1, 'hum': 3, 'vamp': 0, 'wolv': 0},
                   {'x': 4, 'y': 3, 'hum': 0, 'vamp': 0, 'wolv': 3}]

    global p1, p2, b
    b = Board((4,5), initial_pop)
    p1 = RamdomPlayer('vamp')
    p2 = RamdomPlayer('wolv')
    start_GUI(b.grid, play)

    #a1 = Action((0,0), (0,1), 1, 'wolv')
    #a2 = Action((1,1), (1, 0), 2, 'wolv')
    #a3 = Action((1,1), (0,1), 2, 'wolv')
    #actions = [a1, a2]

    #print(b2.board_modification(actions))

