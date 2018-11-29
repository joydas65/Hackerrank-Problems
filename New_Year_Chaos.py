#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes():

    if __name__ == '__main__':
        t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))
        
        s = 0
        flag = 0
        isSwapped = False
        
        for i,j in enumerate(q):
            if (j-1) - i > 2:
                print('Too chaotic')
                flag = 1
                break
        if flag == 0:
            for i in range(0,len(q)-1):
                for j in range(0,len(q)-1-i):
                    if q[j] > q[j+1]:
                        q[j],q[j+1]=q[j+1],q[j]
                        isSwapped = True
                        s += 1
                if not isSwapped:
                    break
                isSwapped = False
            print(s)        
minimumBribes()
