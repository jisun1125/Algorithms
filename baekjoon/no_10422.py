# 2021-04-08
# url : https://www.acmicpc.net/problem/10422
# 10422 괄호
import math
def catalan(n):
    return math.factorial(2*n) // (math.factorial(n) * math.factorial(n+1))

t = int(input())
n = []
for i in range(t):
    n.append(int(input()))
for i in n:
    if i % 2 == 1:
        print(0)
    else:
        print(catalan(i//2)%1000000007)
