# 2021-02-07
# url : https://www.acmicpc.net/problem/15652
# 15652 N과 M (4)
n, m = map(int, input().split())
k = []
def solve(depth, idx, n, m):
    if depth == m:
        print(' '.join(map(str, k)))
        return
    for i in range(idx, n):
        k.append(i+1)
        solve(depth+1, i, n, m)
        k.pop()

solve(0, 0, n, m)
