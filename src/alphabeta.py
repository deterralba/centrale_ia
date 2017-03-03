from board import Action, Board
import numpy as np
from const import RACE_ID, HUM, WOLV, VAMP
from algo_mini_max import evaluate, get_available_moves

infinity = float("inf")

def estfeuille(board, tree_depth, curr_depth):
    return curr_depth >= tree_depth or board.is_over()


#Evaluation niveau AMI
### Marche pas ###
def maxvalue(board, race, race_ennemi, alpha, beta, tree_depth, curr_depth):
    if estfeuille(board, tree_depth, curr_depth):
        return evaluate(board, race, race_ennemi)
    for (action, next_board) in successors(board, race):
        '''ordre race/race_ennemi ?'''
        alpha = max(alpha, minvalue(next_board, race, race_ennemi, alpha, beta, tree_depth, curr_depth+1))
        if alpha >= beta:
            return beta
    return alpha


#Evaluation niveau ENNEMI
### Marche pas ###
def minvalue(board, race, race_ennemi, alpha, beta, tree_depth, curr_depth):
    if estfeuille(board, tree_depth, curr_depth):
        return evaluate(board, race, race_ennemi)
    for (action, next_board) in successors(board, race):
        '''ordre race/race_ennemi ?'''
        beta = min(beta, maxvalue(next_board, race, race_ennemi, alpha, beta, tree_depth, curr_depth+1))
        if alpha >= beta:
            return beta
       
    return alpha


### Vérifié ###
def successors(board, race):
    board_successors = []
    actions  = get_available_moves(board, race)
    for action in actions:
        clone_board = board.copy()
        clone_board.do_actions([action])
        board_successors = board_successors + [(action, clone_board)]
    return board_successors

        

def alphabeta(board, race, race_ennemi, tree_depth):
    
    old_skip = Board.SKIP_CHECKS
    Board.SKIP_CHECKS = True
    ##

    i = -1
    board_successors = successors(board, race)
    best_successor = board_successors[0]
    for (ac, s) in board_successors:
        #print(minvalue(s, race, race_ennemi, -infinity, infinity, tree_depth, 0))
        if minvalue(s, race, race_ennemi, -infinity, infinity, tree_depth, 0) > minvalue(best_successor[1], race, race_ennemi, -infinity, infinity, tree_depth, 0):
            best_successor = (ac, s)
            i+=1
    #print(i)
    return [best_successor[0]]
    
    
