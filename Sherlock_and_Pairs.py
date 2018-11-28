#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(a):

    a = sorted(a)

    k = 1

    ans = 0

    for x in range(1,len(a)):

        if a[x] != a[x-1]:

            ans += (k * (k - 1))

            k = 1
        else:

            k += 1

    ans += (k * (k - 1))

    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        a_count = int(input())

        a = list(map(int, input().rstrip().split()))

        result = solve(a)

        fptr.write(str(result) + '\n')

    fptr.close()
