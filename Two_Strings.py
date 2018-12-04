#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    
    d = dict()
    
    for i in "abcdefghijklmnopqrstuvwxyz":
        
        d[i] = 0
        
    for i in s1:
        
        d[i] += 1
        
    for i in s2:
        
        if d[i] > 0:
            
            return "YES"
        
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
