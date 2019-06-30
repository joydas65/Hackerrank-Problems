#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):

    d,x = dict(),set()

    for i in s1:

        if i in d:

            d[i] += 1

        else:

            d[i] = 1

        x.add(i)

    #print(d)
    #print(x)

    for i in s2:

        if i in d:

            if i not in x:

                d[i] += 1

            else:

                d[i] -= 1

        else:

            d[i] = 1

        #print(d)

    #print(d)

    ans = 0

    for i in d:

        ans += abs(d[i])

    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
