# -*- coding: utf-8 -*-
"""
This is the code used for experiments section of the assignment 

*NOTE* for the portion of the experiment regarding the solution length,
the return statement in searches.solveAstar and solveBeam need to be changed
from node_count to len(sequences)

@author Wen Lin
"""
import searches
from eightPuzzle import EightPuzzle
import random
#%%
moves = []
generated_num = set()
random.seed(25)

# generate 100 distinct random numbers
for i in range(100):
    num = random.randint(1, 1000)
    
    if num not in generated_num:
        moves.append(num)
        generated_num.add(num)
#%%
# Astar with h1
a_h1_10 = 0
a_h1_100 = 0
a_h1_10000 = 0

# Astar with h2
a_h2_10 = 0
a_h2_100 = 0
a_h2_10000 = 0

# Beam with k=10
beam1_10 = 0
beam1_100 = 0
beam1_10000 = 0

# Beam with k=100
beam2_10 = 0
beam2_100 = 0
beam2_10000 = 0

# generate 100 states for max_node = 10 for each search
for num in moves:
    p = EightPuzzle(num)
    
    if searches.solveAstar("h1", p, 10) != 0:
        a_h1_10 += 1
        
    if searches.solveAstar("h2", p, 10) != 0:
        a_h2_10 += 1
        
    if searches.solveBeam(10, p, 10) != 0:
        beam1_10 += 1
    
    if searches.solveBeam(100, p, 10) != 0:
        beam2_10 += 1
    
    
# generate 100 states for max_node = 100 for each search
for num in moves:
    p = EightPuzzle(num)
    
    if searches.solveAstar("h1", p, 100) != 0:
        a_h1_100 += 1
        
    if searches.solveAstar("h2", p, 100) != 0:
        a_h2_100 += 1
        
    if searches.solveBeam(10, p, 100) != 0:
        beam1_100 += 1
        
    if searches.solveBeam(100, p, 100) != 0:
        beam2_100 += 1
    
# generate 100 states for max_node = 10000 for each search
for num in moves:
    p = EightPuzzle(num)
    
    if searches.solveAstar("h1", p, 10000) != 0:
        a_h1_10000 += 1
        
    if searches.solveAstar("h2", p, 10000) != 0:
        a_h2_10000 += 1
        
    if searches.solveBeam(10, p, 10000) != 0:
        beam1_10000 += 1
        
    if searches.solveBeam(100, p, 10000) != 0:
        beam2_10000 += 1

#%% 
# How does fraction of solvable puzzles from random initial states vary with the maxNodes limit?
print("A-star h1: ", a_h1_10/100, ", ", a_h1_100/100, ", ", a_h1_10000/100)
print("A-star h2: ", a_h2_10/100, ", ", a_h2_100/100, ", ", a_h2_10000/100)
print("Beam k=10: ", beam1_10/100, ", ", beam1_100/100, ", ", beam1_10000/100)
print("Beam k=100: ", beam2_10/100, ", ", beam2_100/100, ", ", beam2_10000/100)

#%%
# For each of the three search methods, what fraction of your generated problems were solvable?
a_h1 = [a_h1_10/100, a_h1_100/100, a_h1_10000/100]
a_h2 = [a_h2_10/100, a_h2_100/100, a_h2_10000/100]
beam = [beam1_10/100, beam1_100/100, beam1_10000/100, beam2_10/100, beam2_100/100, beam2_10000/100]

avg_h1 = sum(a_h1) / len(a_h1)
avg_h2 = sum(a_h2) / len(a_h2)
avg_beam = sum(beam) / len(beam)

print("A-star h1: ", avg_h1)
print("A-star h2: ", avg_h2)
print("Beam: ", avg_beam)

#%%

# For A* search, which heuristic is better, i.e., generates lower number of nodes?

# Astar with h1
h1_count_10 = 0
h1_count_100 = 0
h1_count_10000 = 0

# Astar with h2
h2_count_10 = 0
h2_count_100 = 0
h2_count_10000 = 0

# generate 100 states for max_node = 10 for each search
for num in moves:
    p = EightPuzzle(num)
    
    h1_count_10 += searches.solveAstar("h1", p, 10)
    h2_count_10 += searches.solveAstar("h2", p, 10) 
     
# generate 100 states for max_node = 100 for each search
for num in moves:
    p = EightPuzzle(num)
    
    h1_count_100 += searches.solveAstar("h1", p, 100)
    h2_count_100 += searches.solveAstar("h2", p, 100)  
    
# generate 100 states for max_node = 10000 for each search
for num in moves:
    p = EightPuzzle(num)
    
    h1_count_10000 += searches.solveAstar("h1", p, 10000)
    h2_count_10000 += searches.solveAstar("h2", p, 10000) 

#%%
# For A* search, which heuristic is better, i.e., generates lower number of nodes?
h1_count_tot = [h1_count_10/100, h1_count_100/100, h1_count_10000/100]
h2_count_tot = [h2_count_10/100, h2_count_100/100, h2_count_10000/100]

avg_h1_count = sum(h1_count_tot) / len(h1_count_tot)
avg_h2_count = sum(h2_count_tot) / len(h2_count_tot)

print("A-star h1: ", avg_h1_count)
print("A-star h2: ", avg_h2_count)

#%%

# How does the solution length (number of moves needed to reach the goal state)
# vary across the three search methods?

# Astar with h1
h1_sol_10 = 0
h1_sol_100 = 0
h1_sol_10000 = 0
h1_sol_count = 0

# Astar with h2
h2_sol_10 = 0
h2_sol_100 = 0
h2_sol_10000 = 0
h2_sol_count = 0

# Beam search with k=10
# Astar with h2
beam_sol_10 = 0
beam_sol_100 = 0
beam_sol_10000 = 0
beam_sol_count = 0

# generate 100 states for max_node = 10 for each search
for num in moves:
    p = EightPuzzle(num)
    
    if searches.solveAstar("h1", p, 10) != 0 :
        h1_sol_10 += searches.solveAstar("h1", p, 10)
        h1_sol_count += 1
    if searches.solveAstar("h2", p, 10) != 0:
        h2_sol_10 += searches.solveAstar("h2", p, 10)
        h2_sol_count += 1
    if searches.solveBeam(10, p, 10) != 0:
        beam_sol_10 += searches.solveBeam(10, p, 10)
        beam_sol_count += 1
     
# generate 100 states for max_node = 100 for each search
for num in moves:
    p = EightPuzzle(num)
    
    if searches.solveAstar("h1", p, 100) != 0 :
        h1_sol_100 += searches.solveAstar("h1", p, 100)
        h1_sol_count += 1
    if searches.solveAstar("h2", p, 100) != 0:
        h2_sol_100 += searches.solveAstar("h2", p, 100)
        h2_sol_count += 1
    if searches.solveBeam(10, p, 100) != 0:
        beam_sol_100 += searches.solveBeam(10, p, 100)
        beam_sol_count += 1
    
# generate 100 states for max_node = 10000 for each search
for num in moves:
    p = EightPuzzle(num)
    
    if searches.solveAstar("h1", p, 10000) != 0 :
        h1_sol_10000 += searches.solveAstar("h1", p, 10000)
        h1_sol_count += 1
    if searches.solveAstar("h2", p, 10000) != 0:
        h2_sol_10000 += searches.solveAstar("h2", p, 10000)
        h2_sol_count += 1
    if searches.solveBeam(10, p, 10000) != 0:
        beam_sol_10000 += searches.solveBeam(10, p, 10000)
        beam_sol_count += 1

#%% 
h1_sol = [h1_sol_10, h1_sol_100, h1_sol_10000]
h2_sol = [h2_sol_10, h2_sol_100, h2_sol_10000]
beam_sol = [beam_sol_10, beam_sol_100, beam_sol_10000] 

avg_h1_sol = sum(h1_sol) / h1_sol_count
avg_h2_sol = sum(h2_sol) / h2_sol_count
avg_beam_sol = sum(beam_sol) / beam_sol_count

print("A-star h1: ", avg_h1_sol)
print("A-star h2: ", avg_h2_sol)
print("Beam k=10: ", avg_beam_sol)

print("A-star h1 solved count: ", h1_sol_count)
print("A-star h2 solved count: ", h2_sol_count)
print("Beam k=10 solved count: ", beam_sol_count)

