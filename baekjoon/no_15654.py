# 2021-02-07
# url : https://www.acmicpc.net/problem/15654
# 15654 N과 M (5)
from itertools import permutations, combinations

n, m = map(int, input().split())
k = list(map(int, input().split()))
P = sorted(permutations(k, m))

for p in P:
    for i in p:
        print(i, end=' ')
    print('')
