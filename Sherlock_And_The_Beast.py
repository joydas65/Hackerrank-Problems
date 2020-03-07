#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the decentNumber function below.
def decentNumber(n):

    fives,threes,f = n,0,0

    while fives >= 0 and threes <= n:

        if fives % 3 == 0 and threes % 5 == 0:

            f = 1

            print(("5"*fives) + ("3"*threes))

            break

        fives -= 1

        threes += 1

    if f == 0:
        print(-1)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
