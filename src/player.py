from random import randint
from const import RACE_ID, WOLV, VAMP
from board import Action
from threading import Thread
from containers import ContainerBool


class Player(object):
    def __init__(self, race):
        self.race = race
        self.race_ennemi = WOLV if self.race == VAMP else VAMP
        self.depth = None
        self.esperance = None
        self.threads_containers = []

    def get_next_move(*args, **kwargs):
        raise NotImplementedError()

    def evaluate(*args, **kwargs):
        raise NotImplementedError()

    def start_search(self, board, actions_container):
        self.threads_containers = []
        should_continue_container = ContainerBool(True)
        thread = Thread(
            target=self.run,
            args=(actions_container, should_continue_container, board, self.race, self.race_ennemi, self.depth, self.evaluate, self.esperance)
        )
        thread.start()
        self.threads_containers.append(should_continue_container)

    def stop_search(self):
        for container in self.threads_containers:
            container.set(False)

    @staticmethod
    def run(actions_container, should_continue_container, board, race, race_ennemi, depth, evaluate, esperance):
        raise NotImplementedError()


class RandomPlayer(Player):
    def get_next_move(self, board):
        actions = []
        for square in board.enumerate_squares():
            units = board.grid[square][RACE_ID[self.race]]
            if units > 0:
                to = get_random_adjacent_square(board.grid, square)
                actions.append(Action(square, to, units, self.race))
        return actions

    @staticmethod
    def run(actions_container, should_continue_container, board, race, race_ennemi, depth, evaluate, esperance):
        p = RandomPlayer(race)
        actions = p.get_next_move(board)
        actions_container.set(actions)


def get_random_adjacent_square(grid, square):
    not_on_grid = True
    to = None
    while not_on_grid or to == square:
        to = (square[0] + randint(-1, 1), square[1] + randint(-1, 1))
        not_on_grid = not Action.square_is_on_grid(to, grid)
    return to
