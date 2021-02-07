# 2021-02-07
# url : https://www.acmicpc.net/problem/15649
# 15649 N과 M (1)
from itertools import permutations

n, m = map(int, input().split())
k = []
for i in range(n):
    k.append(i+1)
per = permutations(k, m)
for p in per:
    for i in p:
        print(i, end=' ')
    print('')
