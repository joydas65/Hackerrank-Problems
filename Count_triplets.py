#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the countTriplets function below.
def countTriplets(arr, r):
    
    ratio2 = Counter()
    ratio3 = Counter()
    ans = 0
    
    for i in arr:
        if i in ratio3:
            ans += ratio3[i]
        
        if i in ratio2:
            ratio3[i*r] += ratio2[i]
        
        ratio2[i*r] += 1
        
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
