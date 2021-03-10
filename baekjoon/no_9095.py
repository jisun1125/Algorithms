# 2021-03-10
# url : https://www.acmicpc.net/problem/9095
# 9095 1, 2, 3 더하기
n = int(input())
dp = [1, 2, 4]  # n이 1, 2, 3일 때 방법의 수
for i in range(3, 11):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])
    # 동적계획법 : 미리 배열에 저장해둔(구해둔) 값을 이용해 처리하는 것 => 규칙찾기
for j in range(n):
    m = int(input())
    print(dp[m-1])
