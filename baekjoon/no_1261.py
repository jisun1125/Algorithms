# 2021-03-03
# url : https://www.acmicpc.net/problem/1261
# 1261 알고스팟

from collections import deque
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
m, n = map(int, input().split())  # 미로의 크기를 나타내는 가로 크기 M, 세로 크기 N
a = []
for i in range(n):
    a.append(list(input()))

q = deque()
q.append((1, 1))

visited = dict()
visited[(1, 1)] = 0

while q:
    x, y = q.popleft()  # 좌표
    
    if x == n and y == m:
        print(visited[(x, y)])
        break
        
    for i in range(4):
        tx = dx[i] + x
        ty = dy[i] + y

        if 0 <= tx-1 < n and 0 <= ty-1 < m and (tx, ty) not in visited.keys():
            if a[tx-1][ty-1] == '1':  # 벽을 부숴야 한다면
                visited[(tx, ty)] = visited[(x, y)] + 1
                q.append((tx, ty))
            else:  # 빈 방이라면
                visited[(tx, ty)] = visited[(x, y)]
                q.appendleft((tx, ty))
