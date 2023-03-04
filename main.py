# -*- coding: utf-8 -*-
"""
@author: Wen Tao Lin
"""
from eightPuzzle import EightPuzzle
import searches 
import argparse

# main method to read the commands for testing
if __name__ == '__main__':
    
    # Initialize the puzzle at goal state 
    puzzle = EightPuzzle(0)
    
    # current parser and arguments
    parser = argparse.ArgumentParser(description="Command for 8-Puzzle")
    parser.add_argument('-setState')
    parser.add_argument('-printState')
    parser.add_argument('-randomizeState')
    parser.add_argument('-move')
    parser.add_argument('-maxNodes')
    parser.add_argument('-solveAstar')
    parser.add_argument('-solveBeam')
    parser.add_argument('-readCommands')

    # args is all the arguments provided
    args = parser.parse_args()
    
    # actions
    if args.setState:
        puzzle.setState(args.setState)
        
    if args.printState:
        print("Current state:")
        puzzle.printState()
        
    if args.randomizeState:
        puzzle.randomizeState(args.randomizeState)
        
    if args.move:
        puzzle.move(args.move)
        
    if args.maxNodes:
        puzzle.maxNodes(args.maxNodes)
        
    if args.solveAstar:
        searches.solveAstar(args.solveAstar, puzzle, args.maxNodes)

    if args.solveBeam:
        searches.solveBeam(args.solveBeam, puzzle, args.maxNodes)   
        
    # iterate commands in text file
    if args.readCommands:
        
        # open file 
        with open(args.readCommands, "r") as file:
            
            # read each line
            for line in file:
                
                # split the commands by space
                arguments = line.split(" ")
                
                # removing new line
                arguments[-1] = arguments[-1].strip()
                
                for position, argument in enumerate(arguments):
                    
                    # process arguments 
                    if argument == "setState":
                        puzzle.setState(" ".join(arguments[position+1: position+4]))
                        
                    elif argument == "printState":
                        print("Current State: ")
                        puzzle.printState()
                    
                    elif argument == "randomizeState":
                        puzzle.randomizeState(int(arguments[position+1]))
                        
                    elif argument == "move":
                        puzzle.move(arguments[position+1])
                        
                    elif argument == "maxNodes":
                        puzzle.maxNodes(int(arguments[position+1]))
                        
                    elif argument == "solveAstar":
                        searches.solveAstar(arguments[position+1], puzzle, puzzle.node_limit)
                        
                    elif argument == "solveBeam":
                        searches.solveBeam(int(arguments[position+1]), puzzle, puzzle.node_limit)
                        
                    
                        
                        
                    
                        
                    
        
        
    

