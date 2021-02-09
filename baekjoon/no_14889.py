# 2021-02-09
# url : https://www.acmicpc.net/problem/14889
# 14889 스타트와 링크
from itertools import permutations, combinations
from collections import deque
n = int(input())

k = [list(map(int, input().split())) for _ in range(n)]
t = [i for i in range(n)]

INF = 10000
ans = INF
q = deque(combinations(t, n//2))
start_team = deque()
link_team = deque()
for _ in range(len(q)//2):
    start_team.append(q.popleft())
    link_team.append(q.pop())
def calcStat(team):
    ln = len(team)
    s = 0
    for x in range(0, ln-1):
        for y in range(x+1, ln):
            s += k[team[x]][team[y]] + k[team[y]][team[x]]
    return s

for i in range(len(start_team)):
    ans = min(ans, abs(calcStat(start_team[i]) - calcStat(link_team[i])))
print(ans)
