# Given two numbers N and M. N indicates the number of elements in the array A[](1-indexed) and M indicates number of queries. You need to perform two types of queries on the array A[].

# You are given M queries. Queries can be of two types, type 1 and type 2.

# Type 1 queries are represented as 1 i j : Modify the given array by removing elements from i to j and adding them to the front.

# Type 2 queries are represented as 2 i j : Modify the given array by removing elements from i to j and adding them to the back.

# Your task is to simply print |A[1] -A[N]| of the resulting array after the execution of M queries followed by the resulting array.

# Note While adding at back or front the order of elements is preserved.

# Input Format

# First line consists of two space-separated integers, N and M.
# Second line contains N integers, which represent the elements of the array.
# M queries follow. Each line contains a query of either type 1 or type 2 in the form type i j

# Output Format

# Print the absolute value i.e. abs(A[1] - A[N]) in the first line.
# Print elements of the resulting array in the second line. Each element should be seperated by a single space.

# Sample Input

# 8 4
# 1 2 3 4 5 6 7 8
# 1 2 4
# 2 3 5
# 1 4 7
# 2 1 4

# Sample Output

# 1
# 2 3 6 5 7 8 4 1

import array

n, m = list(map(int, input().split()))

a = array.array('i', [int(s) for s in input().split()])

for _ in range(m):
        t, i, j = [int(s) for s in input().split()]
        if t == 1:
            a = a[i-1:j] + a[:i-1] + a[j:]
        else:
            a = a[:i-1] + a[j:] + a[i-1:j]

print(f'{abs(a[0] - a[-1])}')
print(' '.join([str(aa) for aa in a]))