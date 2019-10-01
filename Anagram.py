#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):

    n = len(s)

    if n % 2 == 1:

        return -1

    s1,s2 = s[:n//2],s[n//2:]

    d = dict()

    for i in s2:

        if i in d:

            d[i] += 1

        else:

            d[i] = 1

    ans = 0

    for i in s1:

        if i in d and d[i] > 0:

            d[i] -= 1

    for i in d:

        if d[i] > 0:

            ans += d[i]

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
