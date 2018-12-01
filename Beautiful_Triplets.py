#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(x, arr):

    s = set()

    for i in arr:

        s.add(i)

    ans = 0

    d = dict()

    for i in arr:

        d[i] = 0

    for i in arr:

        d[i] += 1

    if (arr[0] + x) in s and (arr[0] + 2*x) in s:

        ans += d[arr[0]]*d[arr[0] + x]*d[arr[0] + 2*x]

    for i in range(1,len(arr)-2):

        if arr[i] != arr[i - 1]:

            if (arr[i] + x) in s and (arr[i] + 2*x) in s:

                ans += d[arr[i]]*d[arr[i] + x]*d[arr[i] + 2*x]

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    x = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(x, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
