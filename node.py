# -*- coding: utf-8 -*-
"""
@author: Wen Tao Lin
"""
class Node:
    goal_state = ['b',1,2,3,4,5,6,7,8]
    
    def __init__(self, state, b_index, parent, direction, g, heuristic):
        self.state = state
        self.b_index = b_index
        self.parent = parent
        self.direction = direction
        self.g = g
        self.h = (self.h1() if heuristic == "h1" else self.h2())
        
    # calculate the h1 heuristic 
    def h1(self):
        misplaced_count = 0
        
        # loop to count misplaced tiles
        for i in range(9):
            if self.state[i] != self.goal_state[i]:
                if self.state[i] != 'b':
                    misplaced_count += 1
        
        return misplaced_count
            
        
    # calculate the h2 heuristic using manhattan distance 
    def h2(self):
        distance = 0
        
        # loop to find distance for each misplaced tile 
        for i in range(9):
            if self.state != self.goal_state[i]:
                if self.state[i] != 'b':
                    
                    # find row and column of the tile in current state 
                    curr_row = i // 3
                    curr_col = i % 3
                    
                    # find row and column of the tile in goal state
                    goal_index = self.goal_state.index(self.state[i])
                    goal_row = goal_index // 3
                    goal_col = goal_index % 3
                    
                    # calculate the distance 
                    distance += (abs(curr_row - goal_row) + abs(curr_col - goal_col))
             
        return distance 
    
    # get the state resulted from the possible moves in the current state
    def getChild(self, heuristic):
        children = []
        blank = self.b_index
        
        # if "up" is a valid move
        if blank >= 3:
            child_state = self.state.copy()
            child_state[blank], child_state[blank-3] = child_state[blank-3], child_state[blank]
            child = Node(child_state, blank-3, self, "up", self.g+1, heuristic)
            children.append(child)
        
        # if "down" is a valid move
        if blank <= 5:
            child_state = self.state.copy()
            child_state[blank], child_state[blank+3] = child_state[blank+3], child_state[blank]
            child = Node(child_state, blank+3, self, "down", self.g+1, heuristic)
            children.append(child)
            
        # if "left" is a valid move
        if blank not in [0,3,6]:
            child_state = self.state.copy()
            child_state[blank], child_state[blank-1] = child_state[blank-1], child_state[blank]
            child = Node(child_state, blank-1, self, "left", self.g+1, heuristic)
            children.append(child)
        
        # if "right" is a valid move
        if blank not in [2,5,8]:
            child_state = self.state.copy()
            child_state[blank], child_state[blank+1] = child_state[blank+1], child_state[blank]
            child = Node(child_state, blank+1, self, "right", self.g+1, heuristic)
            children.append(child)
            
        return children 

    
    
    
    
