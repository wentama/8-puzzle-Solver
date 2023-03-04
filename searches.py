# -*- coding: utf-8 -*-
"""
@author: Wen Tao Lin
"""
from node import Node

# Astar search
def solveAstar(heuristic, puzzle, max_node):
    node_count = 1 # the root counts as one 
    
    # creating the root node
    root_node = Node(puzzle.state, puzzle.b_index, None, "", 0, heuristic)
    
    # set the max_node to the input
    puzzle.maxNodes(max_node)
    
    # create frontier and expanded lists
    frontier = [root_node]
    expanded = []
    
    # loop to process frontier 
    while frontier:
        
        # sort the states by f value which is g+h
        frontier.sort(key=lambda node: node.g + node.h)
        
        # obtain the first node
        current_node = frontier[0]
        
        # check if this node is the goal state
        if current_node.state == ['b',1,2,3,4,5,6,7,8]:
            
            # backtrace to record the direction stored in each node
            sequences = []
            while current_node.parent:
                sequences.append(current_node.direction)
                current_node = current_node.parent
                
            # reverse the list so the move is from start to goal
            sequences.reverse()
                
            # print outcomes
            print("Number of moves: ", len(sequences))
            print("Total number of nodes generated: ", node_count)
            print("Move Sequences: ", sequences)
            return node_count
            
        # get all the next states from all the valid moves    
        children = current_node.getChild(heuristic)
        
        # add unvisited node to frontier 
        for child in children:
            if child.state not in [node.state for node in expanded]:
                frontier.append(child)
                
                # add node count and check if we exceeded limit or not
                node_count += 1
                if node_count >= puzzle.node_limit:
                    print("Number of nodes generated has exceeded the limit")
                    return 0
            
        # pop the frontier since it is not the goal state
        expanded.append(frontier.pop(0))
        
# beam search
def solveBeam(k, puzzle, max_node):  # let the evulation be h2, the manhattan distance
    node_count = 1 # the root counts as one 
        
    # creating the root node
    root_node = Node(puzzle.state, puzzle.b_index, None, "", 0, "h2")
    
    # set the max_node to the input
    puzzle.maxNodes(max_node)
    
    # create frontier and expanded lists
    frontier = [root_node] # note, beam search limit the size of frontier to k
    
    # process the frontier 
    while frontier: 
        
        # obtain the root node
        current_node = frontier.pop(0)
        
        # check if this node has an evaluation score of 0, aka goal state 
        if current_node.h == 0:
            
            # backtrace to record the direction stored in each node
            sequences = []
            while current_node.parent:
                sequences.append(current_node.direction)
                current_node = current_node.parent
                
            # reverse the list so the move is from start to goal
            sequences.reverse()
                
            # print outcomes
            print("Number of moves: ", len(sequences))
            print("Total number of nodes generated: ", node_count)
            print("Move Sequences: ", sequences)
            return node_count
            
        # get all the next states from all the valid moves    
        children = current_node.getChild("h2")
        
        # add unvisited node to frontier 
        for child in children:
            frontier.append(child)
                
            # add node count and check if we exceeded limit or not
            node_count += 1
            if node_count >= puzzle.node_limit:
                print("Number of nodes generated has exceeded the limit")
                return 0
            
        # sort the states by our evluation function which is h2
        frontier.sort(key=lambda node: node.h)
        
        # keep the k states with the best scores and continue until we find the goal
        frontier = frontier[:k]
    
    
    
            
        
        

    
     
    
         

