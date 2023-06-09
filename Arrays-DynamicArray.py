# For Task visit --> https://www.hackerrank.com/challenges/dynamic-array/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    last_answer = 0
    
    sequance = [[] for _ in range(n)]
    
    result = []

    for q in queries:
        con, x, y = q
        if con == 1:
            seq = (x ^ last_answer) % n
            sequance[seq].append(y)
        else:
            seq = (x ^ last_answer) % n
            last_answer = sequance[seq][y % len(sequance[seq])]
            result.append(last_answer)

    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
