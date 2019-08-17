#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):

    d,tens = dict(),dict()

    d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8],d[9],d[0] = "one","two","three","four","five","six","seven","eight","nine","zero"

    d[10],d[11],d[12],d[13],d[14],d[15],d[16],d[17],d[18],d[19] = "ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"

    tens[10],tens[20] = "ten","twenty"

    flag = 0
    if m > 30:

        m = 60 - m
        flag = 1

    v = m // 10

    if flag == 1 and m in tens:

        print("{one} minutes to {two}".format(one = tens[m],two = d[h+1]))

    elif flag == 1 and m not in tens:

        if m == 15 and h == 12:

            print("quarter to one")

        elif m == 15 and h != 12:

            print("quarter to {one}".format(one = d[h+1]))

        elif v == 2:

            if h != 12:

                print("{one} {two} minutes to {three}".format(one = tens[v*10],two = d[m%10], three = d[h+1]))

            else:

                print("{one} {two} minutes to one".format(one = tens[v*10], two = d[m%10]))

        elif v == 1:

            if h == 12:

                print("{one} minutes to one".format(one = d[m]))

            else:

                print("{one} minutes to {two}".format(one = d[m], two = d[h+1]))

        elif v == 0:

            if m >= 2 and m <= 9:

                print("{one} minutes to {two}".format(one = d[m],two = d[h+1]))

            else:

                print("{one} minute to {two}".format(one = d[m], two = d[h+1]))

    elif flag == 0:

        if m == 30:

            print("half past {one}".format(one = d[h]))

        elif m == 10 or m == 20:

            print("{one} minutes past {two}".format(one = tens[m],two = d[h]))

        elif m == 0:

            print("{one} o' clock".format(one = d[h]))

        elif m == 1:

            print("one minute past {one}".format(one = d[h]))

        elif m == 15:

            print("quarter past {one}".format(one = d[h]))

        else:

            if v == 2:

                print("{one} {two} minutes past {three}".format(one = tens[v*10], two = d[m%10], three = d[h]))

            else:

                print("{one} minutes past {two}".format(one = d[m], two = d[h]))

h = int(input())

m = int(input())

timeInWords(h, m)
