#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    
    shared = 5
    
    cumulative = 2
    
    for i in range(2,n+1):
        
        shared = (shared // 2) * 3
        
        cumulative += (shared // 2)
        
    return cumulative

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
