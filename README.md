# 8-puzzle-solver

**An implementation of A-star search and Beam search for the 8-puzzle.**

I implemented two heuristic functions for A-star search: number of misplaced tiles (h1), the manhattan distance(h2). And for Beam search, I kept the manhattan distance as the evaluation function and allows the user to specific k, the beam width. 

To run, user can set up a puzzle state in a .txt file as shown in the 'simple_command.txt'. And then, can call a search funnction: 'solveAstar <heuristic h1/h2>' and 'solveBeam <beam_width>'. An example is shown in 'search_command.txt'.

The code is organized into 3 separate python files and 1 main function to run the command files for testing. The 3 files are 'eightPuzzle.py', 'node.py', and 'searches.py'. In addition, there is a 'experiment.py' where I ran experiments based on my implementation.

'eightPuzzle.py' contains functions to set up an initial puzzle state that is randomly generated from the goal state.
'node.py' contains helper functions that will be called in 'searches.py'
'searches.py' contains the two searches implemented. 

For the 'experiment.py', I ran a few experiments using the searches to answer the questions below:
Note, these experiment can be recreated and obtain the same outputs as below. Q3 requires a slight edit to the searches methods as discussed below.

_1) How does fraction of solvable puzzles from random initial states vary with the maxNodes limit?_

To answer this question. I generated 100 distinct random numbers from 1 to 1000 as the number of moves. From there, I used loops to initialize 100 puzzles each with those 100 random numbers, where the max_node is set for 10, 100, and 10000 respectively. Then I called the 4 search algorithms of each of the 300 puzzles and incremented their respective solved_count if the search functions did not return 0. Note, return 0 means no solution found. From that I was able to obtain the number of puzzles solved in 100, for each of the scenarios and then calculate the fractions as shown below. 
My experiment obtained the following results:

A-star h1: 0.0 , 0.01 , 0.45 

A-star h2: 0.0 , 0.06 , 0.93

Beam k=10: 0.0 , 0.05 , 0.05

Beam k=100: 0.0 , 0.05 , 0.05

The values above are corresponding to maxNode value 10, 100, 100000.

_2) For A* search, which heuristic is better, i.e., generates lower number of nodes?_

For this problem, I took a similar approach to the experiment I did in Q1. And instead of checking if there is a solution for each puzzle, I increment the total number of node_count returned by the puzzle. And then I found the average number of nodes generated across the 300 puzzles for each search. 0 is returned if there is no solution, so that will not affect our math. I concluded that A-star with h2 is better than A-star with h1 because it regenerates less nodes. Number of nodes are printed below.

A-star h1: 518.156

A-star h2: 443.72

_3)  How does the solution length (number of moves needed to reach the goal state) vary across the three search methods?_

For this problem, I took a similar approach to the experiment I ran in Q2, and also added beam search with k=10 as the 3rd search. The big difference is that I went back to the return function of my search algorithms, and changed the return value from ‘node_count’ to ‘len(sequences)’ so that the solution length would be incremented this time. And I also only incremented the solution length if there is a solution, and incremented the number of solutions found. 

A-star h1: 17.54  |  solved count: 46

A-star h2: 20.15  |  solved count: 99

Beam k=10: 14.00  |  solved count: 46

The result above shows that Beam Search has the average lowest solution length, followed by A-star h1, and A-star h2. However, it is important to note that A-star h2 solved more than double the amount of puzzles that A-star h1 solved. And also almost 10 times the amount Beam K=10 solved. And if A-star h2 is able to solve more puzzles, it is likely that some of those additional puzzles could have a longer solution length which is why the other two algorithms could not find a solution. Therefore, it might bring up the average solution length for A-star h2.

_4) For each of the three search methods, what fraction of your generated problems were solvable?_

Taking the average of the fractions I obtained in Q1 as shown in the image previously, I obtained the following results:

A-star h1: 0.153

A-star h2: 0.333

Beam: 0.033

I did that by adding the fractions into 3 Lists that corresponded to their respective search, and then took the average of each List. Note for Beam Search, I took the average of the 6 fractions (both k=10 and k=100).

The result suggests that A-star with manhattan distance has the highest solved rate.
