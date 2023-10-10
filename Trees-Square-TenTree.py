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

# work with big numbers as strings
L = input()
R = input()

# look for largest possible level
d = len(R)
level = 0
n = 1
tree = [n]
# chunk dimension
while d >= n + 1:
    tree.append(n)
    level += 1
    n = 2 ** level

# go backwards from largest level
def breakdown(N, k):
    if k == 0:
        return [int(N)]

    div = tree[k]
    chunks = breakdown(N[-div:], k - 1)
    chunks.append(N[:-div].lstrip('0') or 0)
    return chunks

divL = breakdown(L, level)
divR = breakdown(R, level)
seq = []

# add up to higher level for L
carry = 0
for k, n in enumerate(map(int, divL)):
    if k == 0:
        carry = -1
        # add up lowest number

    n += carry
    carry = 0

    if k < level:
        if n > 0:
            n = 10 ** tree[k] - n
            carry = 1
        elif n < 0:
            n = 1
            # if lowest was zero

        seq.append((k, n))

# sum up last level of L and R
if n != 0:
    divR[k] = int(divR[k]) - n
    while divR[-1] == 0:
        del divR[-1]
        n = seq.pop()[1]
        if n != 0:
            divR[-1] = int(divR[-1]) + n

# add R in reversed order
seq.extend(reversed(list(enumerate(divR))))

# exclude empty levels
seq = [s for s in seq if s[1] != 0]
print(len(seq))

for s in seq:
    print(*s)