# 2021-02-15
# url : https://www.acmicpc.net/problem/1912
# 1912 연속합
n = int(input())
a = list(map(int, input().split()))
dp = [0 for _ in range(n)]
result = -1001
for i in range(n):
    dp[i] = max(a[i], a[i]+dp[i-1])
    result = max(result, dp[i])
print(result)
