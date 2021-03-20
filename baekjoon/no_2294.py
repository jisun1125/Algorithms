# 2021-03-20
# url : https://www.acmicpc.net/problem/2294
# 2294 동전 2
n, k = map(int, input().split())  # n: 동전의 종류, k: 가치의 합
c = []
for i in range(n):
    c.append(int(input()))
dp = [0] + [100001 for _ in range(k)]

for i in c:
    for j in range(1, k+1):
        if j - i >= 0:
            dp[j] = min(dp[j-i]+1, dp[j])
if dp[k] != 100001:
    print(dp[k])
else:
    print(-1)
