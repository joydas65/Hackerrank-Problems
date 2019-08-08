#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jimOrders function below.
def jimOrders(orders):

    order = []

    num = 1

    for i in orders:

        order.append([num, i[0]+i[1]])

        num += 1

    order = sorted(order, key = lambda x : x[1])

    ans = []

    for i in order:

        ans.append(i[0])

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
