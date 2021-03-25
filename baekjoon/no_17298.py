# 2021-03-25
# url : https://www.acmicpc.net/problem/17298
# 17298 오큰수
import sys
input = sys.stdin.readline
n = int(input())

a = list(map(int, input().split()))
neg = [-1 for _ in range(n)]
i = 1
stack = []
stack.append(0)
while stack and i<n:
    while stack and a[stack[-1]] < a[i]:
        neg[stack[-1]] = a[i]
        stack.pop()
    stack.append(i)
    i += 1

for i in neg:
    print(i, end=' ')
