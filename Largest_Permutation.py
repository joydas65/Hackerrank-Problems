#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestPermutation function below.
def largestPermutation(k, arr):
    x,d,swaps = 0,dict(),0

    for i,j in enumerate(arr):

        d[j] = i 

    for i in range(max(arr),0,-1):

        if i == arr[x]:
            x += 1
            continue

        pos1,pos2 = d[i],x

        v1,v2 = arr[pos1],arr[pos2]

        arr[pos1],arr[pos2] = arr[pos2],arr[pos1]

        d[v1],d[v2] = pos2,pos1

        swaps += 1

        x += 1

        if swaps == k:

            break

    #print(d)

    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
