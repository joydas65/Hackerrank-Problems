#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):

    time = 0

    val = 3

    while time < t:

        time += val

        val *= 2

    val //= 2

    time -= val

    k = time + 1

    f = k + 2

    return f - t + k

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
