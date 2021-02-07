# 2021-02-07
# url : https://www.acmicpc.net/problem/15650
# 15650 N과 M (2)
from itertools import permutations, combinations

n, m = map(int, input().split())
k = []
for i in range(n):
    k.append(i+1)
per = combinations(k, m)
for p in per:
    for i in p:
        print(i, end=' ')
    print('')
