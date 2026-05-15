#!/usr/bin/env python3

# A17370336 #PID


import numpy as np
import random

def create_board():
    """ Add illustrations here, if needed """
    
    
    board = np.zeros((3,3))
    
    return board


def place(board, player, position):
    """ Add illustrations here, if needed """
    if board[position] == 0:
        board[position] = player
    
    return board 

def possibilities(board):

    ind = np.where(board == 0)
    return list(zip(ind[0], ind[1]))

def random_place(board, player):  
    random.seed(1)                
    board = place(board, player, random.choice(possibilities(board)))
    
    return board

def repeat(n):                     
    board = create_board()
    random.seed(1)
    for i in range(n):
        board = random_place(board, 1)
        print(board)
        board = random_place(board, 2)
        print(board)
    return board
    
if __name__ == '__main__':
    
    board = create_board()
    
    board = place(board, 1, (0,0))  
    
    empty_positions = possibilities(board)
    board = random_place(board, 1)
 
    n = 2   # an integer n < 5 since there are only 9 cells in the board and two players in turn place the mark
                  # repeat n times
    board = repeat(n)
