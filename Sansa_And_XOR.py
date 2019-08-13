#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sansaXor function below.
def sansaXor(arr):

    n = len(arr)

    if n%2 == 0:

        return 0

    else:

        ans = 0

        for i in range(0,n,2):

            ans = ans ^ arr[i]

        return ans 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
