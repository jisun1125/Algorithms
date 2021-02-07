# 2021-02-07
# url : https://www.acmicpc.net/problem/15656
# 15656 N과 M (7)
n, m = map(int, input().split())
k = sorted(list(map(int, input().split())))
ans = []

def solve(depth, n, m):
    if depth == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(n):
        ans.append(k[i])
        solve(depth+1, n, m)
        ans.pop()

solve(0, n, m)
