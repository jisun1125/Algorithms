# url : https://www.acmicpc.net/problem/10972

n = int(input())
m = list(map(int, input().split()))
find = False
for i in range(n-1, 0, -1):
    if m[i-1] < m[i]:  # 뒷 값이 앞 값보다 크다면
        for j in range(n-1, 0, -1):
            if m[i-1] < m[j]:
                m[i-1], m[j] = m[j], m[i-1]  # swap
                m = m[:i] + sorted(m[i:])  
                find = True
                break
    if find:
        print(*m)  
        break
if not find:
    print(-1)
