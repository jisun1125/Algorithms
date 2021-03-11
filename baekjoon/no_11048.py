# 2021-03-11
# url : https://www.acmicpc.net/problem/11048
# 11048 이동하기

n, m = map(int, input().split())
board = []
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(n):
    board.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = board[i-1][j-1] + max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
print(dp[n][m])
