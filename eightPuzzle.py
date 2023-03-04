# -*- coding: utf-8 -*-
"""
@author: Wen Tao Lin
"""
import random

class EightPuzzle:
    def __init__(self, n):
        self.state = ['b',1,2,3,4,5,6,7,8]
        self.b_index = 0
        self.randomizeState(n)
        self.node_limit = 100 # place holder until user specify calling a search
        
    # method to edit the current state
    def setState(self, state):
        
        # remove space in the input
        state = state.replace(' ', '')
        
        # make it a list
        list_state = list(state)
        
        # convert numbers to int and store in a new list
        new_state = [int(x) if x.isdigit() else x for x in list_state]
        
        # update state and index of blank tile 
        self.state = new_state
        self.b_index = self.state.index('b')
        
    # print the current state stored 
    def printState(self):
        
        # convert int to str
        str_state = [str(x) for x in self.state]
        
        # add a space between every 3 values
        str_state = ''.join(str_state)
        str_state = ' '.join([str_state[i:i+3] for i in range(0, len(str_state), 3)])
        
        print(str_state)
                
    # make n random moves from the goal state
    def randomizeState(self, n):
        
        # set a set to ensure same random puzzle for same n
        random.seed(25)
        
        # use loop to make n moves
        for i in range(n):
            
            # store the valid moves in a list
            moves = []
            
            # check for valid moves in this current state
            if self.b_index >= 3:
                moves.append("up")
            if self.b_index <= 5:
                moves.append("down")
            if self.b_index not in [0,3,6]:
                moves.append("left")
            if self.b_index not in [2,5,8]:
                moves.append("right")
            
            # choose a random valid move
            direction = random.choice(moves)
            
            self.move(direction)

    # swap two tiles
    def swap(self, x, y):
        self.state[x], self.state[y] = self.state[y], self.state[x]
        
    # move the blank tile
    def move(self, direction):
        
        blank = self.b_index
        
        # move up
        if direction == "up":
            if blank >= 3:
                self.swap(blank, blank-3)
                self.b_index -= 3
            
        # move down
        if direction == "down":
            if blank <= 5:
                self.swap(blank, blank+3)
                self.b_index += 3
            
        # move left
        if direction == "left":
            if blank not in [0,3,6]:
                self.swap(blank, blank-1)
                self.b_index -= 1
        
        # move right
        if direction == "right":
            if blank not in [2,5,8]:
                self.swap(blank, blank+1)
                self.b_index += 1
        
    # set the max number of nodes to be considered during a search for this puzzle 
    def maxNodes(self, n):
        self.node_limit = n
