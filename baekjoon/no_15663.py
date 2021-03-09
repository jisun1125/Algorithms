# 2021-03-09
# url : https://www.acmicpc.net/problem/15663
# 15663 N과 M (9)
from itertools import combinations, permutations, product

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
cmb = list(permutations(a, m))
ans = []

for c in cmb:
    ans.append(c)
ans = sorted(list(set(ans)))  #중복 제거 후 정렬

for c in ans:
    for i in c:
        print(i, end=' ')
    print()
