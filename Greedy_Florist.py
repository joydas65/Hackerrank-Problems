#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c, n):
    
    c = sorted(c)
    
    ans = 0
    
    x = 1
    
    index = n - 1
    
    while index >= 0:
        
        temp = 0
        
        for i in range(k):
            
            temp += c[index]
            
            index -= 1
            
            if index == -1:
                
                break
                
        ans += (x * temp)
        
        x += 1
        
    return ans
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c, n)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
