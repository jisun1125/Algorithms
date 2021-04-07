# 2021-04-07
# url : https://www.acmicpc.net/problem/5557
# 5557 1학년
n = int(input())
s = list(map(int, input().split()))
dp = [[0 for _ in range(21)]for _ in range(n+1)]
dp[0][s[0]] = 1

for i in range(1, n-1):
    for j in range(21):
        if dp[i-1][j]:
            if j+s[i] <= 20:
                dp[i][j+s[i]] += dp[i-1][j]
            if j-s[i] >= 0:
                dp[i][j-s[i]] += dp[i-1][j]

print(dp[n-2][s[-1]])
