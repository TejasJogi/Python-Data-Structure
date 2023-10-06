# Task
# Given the borders of array subsegment [L, R], find its decomposition into a minimal number of nodes of a square-ten tree. In other words, you must find a subsegment sequence [l1,r1], [l1,r2],..., [lm,rm] such as li+1 = ri for every 1 <= i < m, l1 = L, rm = R, where every [li,ri] belongs to any of the square-ten tree levels and m is minimal amongst all such variants.

# Input Format

# The first line contains a single integer denoting L.
# The second line contains a single integer denoting R.

# The numbers in input do not contain leading zeroes.

# Output Format

# As soon as array indices are too large, you should find a sequence of m square-ten tree level numbers, s1, s2, s3, ...., sm, meaning that subsegment [li, ri] belongs to the si'th level of the square-ten tree.

# Sample Input 0

# 1
# 10

# Sample Output 0

# 1
# 1 1