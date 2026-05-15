
"""
Guidelines for program submission: 
    
A) To ensure readability by the grader, 
    please make sure the following submission format:

    1-- Please change the file name to python_program.py 
        ---(The file name is case sensitive, make sure it's identical)---
               
    2-- Please submit only the python_program.py to the autograder
        descriptions of the function should be added in .py file as comments 
                        
                        
B) Your homework should follow the similar structure as this template

C) Keep in mind some minor points:
    
    0-- Your code should not have any debug error before submission!!!

    1-- make sure the function name is identical to that in the problem set (HW2)
            ---(function names are case sensitive! )---
    
    2-- The order of the function arguments should be the same as that in HW 

    2a-- The data type of the argument should be the same as that in template
                      
    3-- make sure your function return the value which the HW requested
    
    4-- make sure the order of the output arguments the same as those in template
    
    5-- Do not round up your output values
    
    6-- Do not use input function in your function
        
    7-- if you need uncommon modules, contact TA before submission or post it on Piazza
    


If you had any question about the guideline, 
    contact TAs or post questions on piazza for response.
        
@author: Dan Li (lidan@ucsd.edu) & Yunhai Han (y8han@eng.ucsd.edu) at UCSD
@date: Jan 2021
"""



"""
The template starts from here
"""

# A432432 #PID

# import all modules here if you need any more
import numpy as np
import random
# your file should always start from definition of functions 

def create_board():
    board = np.zeros((3,3), dtype = int)
    return board

def place(board,player,position):
    if board[position] == 0:
        board[position] = player
    return board

def possibilities(board):
    ind = []
    z = np.array(np.where(board == 0))
    s = z.shape[1]
    for i in range(s):
        ind.append((z[(0,i)],z[(1,i)]))
    return ind

def random_place(board,player):
    selection = possibilities(board)
    position = random.choice(selection)
    board = place(board,player,position)
    return board

def repeat(n):
    random.seed(1)
    board = create_board()
    for k in range(n):
        board = random_place(board,1)
        board = random_place(board,2)
    return board

def row_win(board, player):
    
    return np.any(np.all(board == player, axis = 1)) 

def col_win(board, player):
    
    return np.any(np.all(board == player, axis = 0))  

   

def diag_win(board, player):
    
    return np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player)
   
def evaluate(board):
        
    winner = 0
    win1 = False
    win2 = False
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            if player == 1:
                win1 = True
            else:
                win2 = True
    if win1 and not win2:
        winner = 1
    elif win2 and not win1:
        winner = 2
        
    if np.all(board != 0) and winner == 0:
        winner = -1
        
    return winner


def play_game():
    board = create_board()
    while evaluate(board) == 0:
        board = random_place(board,1)
        if evaluate(board) != 0:
            break
        board = random_place(board,2)
    return evaluate(board)

    
def play_game_1000():
    random.seed(9999999)
    results=[]
    for i in range(1000):
        results.append(play_game())
    return  results


def play_strategic_game():
    board = create_board()
    board[1,1] = 1
    while evaluate(board) == 0:
        board = random_place(board,2)
        if evaluate(board) != 0:
            break
        board = random_place(board,1)
    return evaluate(board)

    
def play_strategic_game_1000():
    random.seed(9999999)
    results=[]
    for i in range(1000):
        results.append(play_strategic_game())
    return results


    
if __name__ == '__main__':

    results = play_game_1000()
    print("Number of normal games:", len(results))
    print("Normal game results count:")
    print("Player 1 wins:", results.count(1))
    print("Player 2 wins:", results.count(2))
    print("Draws:", results.count(-1))

    strategic_results = play_strategic_game_1000()
    print("Number of strategic games:", len(strategic_results))
    print("Strategic game results count:")
    print("Player 1 wins:", strategic_results.count(1))
    print("Player 2 wins:", strategic_results.count(2))
    print("Draws:", strategic_results.count(-1))

# Number of normal games: 1000
# Normal game results count:
# Player 1 wins: 585
# Player 2 wins: 288
# Draws: 127
# Number of strategic games: 1000
# Strategic game results count:
# Player 1 wins: 695
# Player 2 wins: 191
# Draws: 114