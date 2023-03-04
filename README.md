# 8-puzzle-solver

An implementation of A-star search and Beam search for the 8-puzzle.

I implemented two heuristic functions for A-star search: number of misplaced tiles (h1), the manhattan distance(h2). And for Beam search, I kept the manhattan distance as the evaluation function and allows the user to specific k, the beam width. 

To run, user can set up a puzzle state in a .txt file as shown in the 'simple_command.txt'. And then, can call a search funnction: 'solveAstar <heuristic h1/h2>' and 'solveBeam <beam_width>'. An example is shown in 'search_command.txt'.

The code is organized into 3 separate python files and 1 main function to run the command files for testing. The 3 files are 'eightPuzzle.py', 'node.py', and 'searches.py'. In addition, there is a 'experiment.py' where I ran experiments based on my implementation.

'eightPuzzle.py' contains functions to set up an initial puzzle state that is randomly generated from the goal state.
'node.py' contains helper functions that will be called in 'searches.py'
'searches.py' contains the two searches implemented. 

For the 'experiment.py', I ran a few experiments using the searches to answer the questions below:
Note, these experiment can be recreated and obtain the same outputs as below. Q3 requires a slight edit to the searches methods as discussed below.

1) How does fraction of solvable puzzles from random initial states vary with the maxNodes limit?

To answer this question. I generated 100 distinct random numbers from 1 to 1000 as the number of moves. From there, I used loops to initialize 100 puzzles each with those 100 random numbers, where the max_node is set for 10, 100, and 10000 respectively. Then I called the 4 search algorithms of each of the 300 puzzles and incremented their respective solved_count if the search functions did not return 0. Note, return 0 means no solution found. From that I was able to obtain the number of puzzles solved in 100, for each of the scenarios and then calculate the fractions as shown below. 
My experiment obtained the following results:

A-star h1: 0.0 , 0.01 , 0.45 

A-star h2: 0.0 , 0.06 , 0.93

Beam k=10: 0.0 , 0.05 , 0.05

Beam k=100: 0.0 , 0.05 , 0.05

The values above are corresponding to maxNode value 10, 100, 100000.

2) For A* search, which heuristic is better, i.e., generates lower number of nodes?

For this problem, I took a similar approach to the experiment I did in Q1. And instead of checking if there is a solution for each puzzle, I increment the total number of node_count returned by the puzzle. And then I found the average number of nodes generated across the 300 puzzles for each search. 0 is returned if there is no solution, so that will not affect our math. I concluded that A-star with h2 is better than A-star with h1 because it regenerates less nodes. Number of nodes are printed below.

A-star h1: 518.156
A-star h2: 443.72

3)  How does the solution length (number of moves needed to reach the goal state) vary across the three search methods?
