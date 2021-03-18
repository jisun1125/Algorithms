# 2021-03-18
# url : https://www.acmicpc.net/problem/1525
# 1525 퍼즐
from collections import deque
def bfs():
    q = deque()
    q.append(aa)
    visited[aa] = 0

    while q:
        v = q.popleft()
        if v == 123456789:
            return visited[v]
        s = str(v)
        target = s.find('9')
        tx = target // 3
        ty = target % 3
        # 123485796 인 경우, 리스트 내 인덱스는 7
        # 123
        # 485   
        # 796  <- (2, 1)
        
        for i in range(4):
            x = dx[i] + tx
            y = dy[i] + ty
            if 0 <= x < 3 and 0 <= y < 3:
                t = x*3 + y  # 3x3표에서 좌표를 리스트로 바꿨을 떄의 인덱스 값
                ts = list(s)
                ts[target], ts[t] = ts[t], ts[target]  # swqp
                ti = int(''.join(ts))
                if not visited.get(ti):
                    visited[ti] = visited[v] + 1
                    q.append(ti)
    return -1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = dict()
aa = ''
for i in range(3):
    a = input()
    a = a.replace(' ', '')  # 공백 제거
    aa += a  # 문자열 더하기 연산 하려면 split() 으로 값 받을 수 x

aa = int(aa.replace('0', '9'))
print(bfs())
