#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sumXor function below.
def sumXor(n):

    count_no_of_zeroes = 0

    while n != 0:

        if n % 2 == 0:

            count_no_of_zeroes += 1

        n //= 2

    return 2**count_no_of_zeroes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
