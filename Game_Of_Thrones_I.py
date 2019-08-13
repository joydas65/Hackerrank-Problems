#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):

    d,x = dict(),0

    n = len(s)

    for i in s:

        if i in d:

            d[i] += 1

        else:

            d[i] = 1

            x += 1 

    if x == n:

        return "NO"

    if n % 2 == 0:

        for i in d:

            if d[i] % 2 == 1:

                return "NO"

        return "YES"

    c = 0

    for i in d:

        if d[i] % 2 == 1:

            c += 1

        if c > 1:

            return "NO"

    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
