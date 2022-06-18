#!/bin/python3

import sys


grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)

prod = ((grid[0][0] * grid[0][1]) * (grid[0][2] * grid[0][3]))

answer = prod

for i in range(20):
    
    j = 4
    prod = (grid[i][0] * grid[i][1]) * (grid[i][2] * grid[i][3])
    answer = max(answer, prod)
    
    while j < 20:
        
        if prod == 0:
            prod = ((grid[i][j] * grid[i][j-1]) * (grid[i][j-2] * grid[i][j-3]))
        else:
            prod *= grid[i][j]
            prod //= grid[i][j-4]
        
        answer = max(answer, prod)
        
        j += 1
        
prod = ((grid[0][0] * grid[1][0]) * (grid[2][0] * grid[3][0]))

answer = max(prod, answer)
        
for i in range(20):
    
    j = 4
    prod = (grid[0][i] * grid[1][i]) * (grid[2][i] * grid[3][i])
    answer = max(answer, prod)
    
    while j < 20:
        
        if prod == 0:
            prod = ((grid[j][i] * grid[j-1][i]) * (grid[j-2][i] * grid[j-3][i]))
        else:
            prod *= grid[j][i]
            prod //= grid[j-4][i]
        
        answer = max(answer, prod)
        
        j += 1

for i in range(17):
    
    for j in range(17):
        
        prod = ((grid[i][j] * grid[i+1][j+1]) * (grid[i+2][j+2] * grid[i+3][j+3]))
        
        answer = max(prod, answer)
        
i,j = 19,19

while i >= 3:
    
    j = 19
    
    while j >= 3:
        
        prod = ((grid[i][j] * grid[i-1][j-1]) * (grid[i-2][j-2] * grid[i-3][j-3]))
        
        answer = max(answer, prod)
        
        j -= 1
        
    i -= 1
    
i,j = 0,19

while i <= 16:
    
    j = 19
    
    while j >= 3:
        
        prod = ((grid[i][j] * grid[i+1][j-1]) * (grid[i+2][j-2] * grid[i+3][j-3]))
        
        answer = max(prod, answer)
        
        j -= 1
        
    i += 1
    
i,j = 19,0

while i >= 3:
    
    j = 0
    
    while j <= 16:
        
        prod = ((grid[i][j] * grid[i-1][j+1]) * (grid[i-2][j+2] * grid[i-3][j+3]))
        
        answer = max(answer, prod)
        
        j += 1
        
    i -= 1
    
print(answer)
