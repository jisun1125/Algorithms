# 2021-02-07
# url : https://www.acmicpc.net/problem/15651
# 15651 N과 M (3)
n, m = map(int, input().split())
k = []
def solve(depth, n, m):
    if depth == m:
        print(' '.join(map(str, k)))
        return
    for i in range(n):
        k.append(i+1)
        solve(depth+1, n, m)
        k.pop()

solve(0, n, m)
