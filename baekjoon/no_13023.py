# 2021-02-04
# url : https://www.acmicpc.net/problem/13023
# 13023 ABCDE
finished = False
visited = [False]*2001
def dfs(here, depth):
    global finished

    visited[here] = True
    if depth == 4:
        finished = True
        return
    for i in f[here]:
        if not visited[i]:
            dfs(i, depth+1)
            visited[i] = False  # dfs에서 빠져나왔다는건 제일 안쪽까지 파고들었다가 다시 나오는 것이기 때문에 방문표시를 풀어줌

n, m = map(int, input().split())
f = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    f[a].append(b)
    f[b].append(a)

for i in range(n):
    dfs(i, 0)
    visited[i] = False
    if finished:
        break
if finished:
    print(1)
else:
    print(0)
