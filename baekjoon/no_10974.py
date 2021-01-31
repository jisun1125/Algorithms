# url : https://www.acmicpc.net/problem/10974
# 10974 모든 순열

from itertools import permutations
n = int(input())
m = []
for i in range(n):
    m.append(i+1)
per = permutations(m, n)
for p in per:
    print(*p)
