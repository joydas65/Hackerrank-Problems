#!/bin/python3

import math
import os
import random
import re
import sys
#import numpy as np

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    
    l = [0 for i in range(n)]
    
    k = []
    
    max = f = 0
    
    for i in queries:
        l[i[0]-1] += i[2]
        if i[1] < len(l):
            l[i[1]] -= i[2]
        
    for i in l:
        f = f + i
        
        if (max < f):
            max = f
        
        
    
    return max
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
