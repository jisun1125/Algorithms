# 2021-03-10
# url : https://www.acmicpc.net/problem/15664
# 15664 N과 M (10)
from itertools import combinations

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
cmb = list(combinations(a, m))
ans = []

for c in cmb:
    ans.append(c)
# 중복 제거를 for문으로 직접 했을때엔 시간초과 나왔음
ans = sorted(list(set(ans)))  #중복 제거 후 정렬

for c in ans:
    for i in c:
        print(i, end=' ')
    print()
