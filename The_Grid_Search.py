#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridSearch function below.

def Search(grid, row, col, r1, c1, pattern):

    r,c = len(pattern),len(pattern[0])

    cx = col
    #print(row,col)

    for i in range(r):

        for j in range(c):

            if pattern[i][j] != grid[row][col]:

                return False

            col += 1

        row += 1

        col = cx

    return True

def gridSearch(G, P):

    r1,c1,c2,r2 = len(G),len(G[0]),len(P[0]),len(P)

    if r2 > r1:

        return "NO"

    if c2 > c1:

        return "NO"

    val,res = P[0][0],False

    for i in range(r1-r2+1):

        for j in range(c1-c2+1):

            if G[i][j] == val:

                res = Search(G,i,j,r1,c1,P)

                if res == True:

                    return "YES"

    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
