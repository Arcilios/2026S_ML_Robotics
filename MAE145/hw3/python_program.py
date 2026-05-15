#!/usr/bin/env python3
# A17370336

import numpy as np
import random


def computeBFStree(AdjTable, start): 
    """Return the BFS visited order rooted at start."""
    
    ##########
    #### Your code goes here ####
    ##########
    
    # check whether AdjTable is valid
    if type(AdjTable) != dict:
        return 'AdjTable is invalid'
    
    for key in AdjTable:
        if type(AdjTable[key]) != list:
            return 'AdjTable is invalid'
    
    if start not in AdjTable:
        return 'No start node in the graph'
    
    # keep track of all visited nodes
    visited = []
    # keep track of nodes to be checked
    queue = [start]
    
    # keep looping until there are nodes still to be checked
    while queue:
        node = queue.pop(0)
        
        if node not in visited:
            visited.append(node)
            
            for neighbour in AdjTable[node]:
                if neighbour not in visited and neighbour not in queue:
                    queue.append(neighbour)
    
    # or a vector of pointers parents describing the BFS tree rooted at start
    # equivalently, a list of nodes in visited order, start from the 'start node' 
    return visited # list of visited node e.g. [ 'A', 'B', 'C', 'D']
    


def computeBFSpath(AdjTable, start, goal):
    """Return one BFS path from start to goal."""

    ##########
    #### Your code goes here ####
    ##########
    
    # check whether AdjTable is valid
    if type(AdjTable) != dict:
        return 'AdjTable is invalid'
    
    for key in AdjTable:
        if type(AdjTable[key]) != list:
            return 'AdjTable is invalid'
    
    if start not in AdjTable:
        return 'No start node in the graph'

    if goal not in AdjTable:
        return 'No goal node in the graph'

    # keep track of visited nodes
    visited = []
    # keep track of all the paths to be checked
    queue = [[start]]
    
    # return path if start is goal
    if start == goal:
        return [start]
    
    #Condition 1
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node not in visited:
            for neighbour in AdjTable[node]:
                new_path = list(path)
                new_path.append(neighbour)
                
                if neighbour == goal:
                    return new_path
                
                queue.append(new_path)
            
            # mark node as visited
            visited.append(node)
    
    # in case there's no path between the 2 nodes
    return "No path" # Condition 2
     
    

if __name__ == '__main__':
    """ 
    This is the place where you can test your function. 
    You can define variables, feed them into your function and check the output   
    """
    
    # AdjTable defined as a dictionary 
    
    #Testing with input of AdjTable
    AdjTable = {'A': ['B', 'D'],
                'B': ['A'],
                'C': ['D'],
                'D': ['A', 'F', 'C'],
                'E': ['F'],
                'F': ['D', 'E']}
    
      
    start='A'
    goal='C'
    
    myBFSTree=computeBFStree(AdjTable, start)
    print(myBFSTree)
    # output should be a list: 
    # ['A', 'B', 'D', 'F', 'C', 'E']

    myBFSPath=computeBFSpath(AdjTable, start, goal)
    print(myBFSPath)
    # output should be a list: 
    # ['A', 'D', 'C']
    
    
    #Writing maze graph in E2.8 as the AdjTable1 and testing based on the nodes marked 
    AdjTable1 = {1: [2,3],2: [1,4,17],3: [1,4,5],4: [2,4,6],5: [3,6,7],6: [4,5,8],7:[5,8,9],
                 8: [6,7,10],9: [7,10],10: [8,9,11],11: [10,12],12: [11,13],13:[12,14],
             14: [13,15],15: [14,26,16],16: [15,32],17: [2,18],18: [17,19], 
             19:[18,20,21],20: [19,22], 21: [19,22,23],22: [20,21,24],23: [21,24,27],
             24:[22,23,25],25: [24,26],26: [25,15],27: [23,28],28: [27,29],29: [28,30],
             30:[29,31],31: [30,32],32: [16,31]}
    start, goal = 1, 32
    myBFSTree=computeBFStree(AdjTable1, start)
    print(myBFSTree)
     
    myBFSPath=computeBFSpath(AdjTable1, start,goal)
    print(myBFSPath)
    
 
    
"""Test Result
['A', 'B', 'D', 'F', 'C', 'E']
['A', 'D', 'C']
[1, 2, 3, 4, 17, 5, 6, 18, 7, 8, 19, 9, 10, 20, 21, 11, 22, 23, 12, 24, 27, 13, 25, 28, 14, 26, 29, 15, 30, 16, 31, 32]
[1, 2, 4, 6, 8, 10, 11, 12, 13, 14, 15, 16, 32]
"""