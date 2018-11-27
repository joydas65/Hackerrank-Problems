#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrings function below.
def substrings(n):

    ans = 0

    ones = 1

    x = len(n)

    INDEX = x - 1

    while INDEX >= 0:

        temp = int(n[INDEX])

        sum_from_digit = temp * ones * (INDEX + 1)

        ans += sum_from_digit

        ans %= ((10 ** 9) + 7)

        ones = ((ones * 10) + 1) % ((10 ** 9) + 7)

        INDEX -= 1

    return ans 




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
