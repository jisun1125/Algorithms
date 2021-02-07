# 2021-02-07
# url : https://www.acmicpc.net/problem/15657
# 15657 N과 M (8)
n, m = map(int, input().split())
k = sorted(list(map(int, input().split())))
ans = []

def solve(depth, idx, n, m):
    if depth == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(idx, n):
        ans.append(k[i])
        solve(depth+1, i, n, m)
        ans.pop()

solve(0, 0, n, m)
