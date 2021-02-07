# 2021-02-07
# url : https://www.acmicpc.net/problem/15655
# 15655 N과 M (6)
from itertools import permutations, combinations

n, m = map(int, input().split())
k = sorted(list(map(int, input().split())))

C = combinations(k, m)
for c in C:
    for i in c:
        print(i, end=' ')
    print('')
