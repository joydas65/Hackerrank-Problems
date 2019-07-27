#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridChallenge function below.
def gridChallenge(grid):

    arr,x = [],0

    for i in grid:

        arr.append([])

        for j in "abcdefghijklmnopqrstuvwxyz":

            for k in i:

                if k == j:

                    arr[x].append(k)

        x += 1

    for i in range(len(grid[0])):

        for j in range(1,len(grid)):

            if ord(arr[j][i]) < ord(arr[j-1][i]):

                return "NO"

    return "YES"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
