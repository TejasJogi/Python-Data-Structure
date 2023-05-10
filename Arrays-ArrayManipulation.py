# Task - https://www.hackerrank.com/challenges/crush/problem?isFullScreen=true


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    
    arr = [0]*n
    for i in queries:
        a, b, k = i
        arr[a - 1] += k
        if b < n:
            arr[b] -= k
    maxval = 0
    val = 0
    for i in arr:
        val += i
        if val > maxval:
            maxval = val
    return maxval

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
