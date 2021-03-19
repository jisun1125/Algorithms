# 2021-03-19
# url : https://www.acmicpc.net/problem/17087
# 17087 숨바꼭질 6
def gcd(a, b):  # 최대공약수, 유클리드 호제법
    if b == 0:
        return a
    else:
        return dp(b, a%b)

n, s = map(int, input().split())  # n: 동생의 수, s: 수빈이의 현재 위치
a = list(map(int, input().split()))
ans = abs(s-a[0])

if s == 1:
    print(ans)
else:
    for i in range(1, n):
        ans = gcd(ans, abs(s-a[i]))
    print(ans)
