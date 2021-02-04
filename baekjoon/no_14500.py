# 2021-02-04
# url : https://www.acmicpc.net/problem/14500
# 14500 테트로미노
n, m = map(int, input().split())
t = []
for i in range(n):
    t.append(list(map(int, input().split())))
#print(t)

ans = []
for i in range(n):  # 세로
    for j in range(m):  # 가로
        if j+3 < m:
            ans.append(t[i][j]+t[i][j+1]+t[i][j+2]+t[i][j+3])

        if i+3 < n:
            ans.append(t[i][j]+t[i+1][j]+t[i+2][j]+t[i+3][j])

        if j+1 < m and i+1 < n:  # 정사각형
            ans.append(t[i][j]+t[i+1][j]+t[i][j+1]+t[i+1][j+1])

        if j+1 < m and i+2 < n:
            ans.append(t[i][j] + t[i+1][j] + t[i+2][j] + t[i+2][j+1])
            ans.append(t[i][j] + t[i][j+1] + t[i+1][j+1] + t[i+2][j+1])
            ans.append(t[i][j+1] + t[i+1][j+1] + t[i+2][j] + t[i+2][j+1])
            ans.append(t[i][j] + t[i][j+1] + t[i+1][j] + t[i+2][j])
            ans.append(t[i][j] + t[i+1][j] + t[i+1][j+1] + t[i+2][j+1])
            ans.append(t[i][j+1] + t[i+1][j] + t[i+1][j+1] + t[i+2][j])
            ans.append(t[i][j] + t[i+1][j] + t[i+1][j+1] + t[i+2][j])
            ans.append(t[i][j+1] + t[i+1][j] + t[i+1][j+1] + t[i+2][j+1])

        if j+2<m and i+1<n:
            ans.append(t[i][j] + t[i+1][j] + t[i][j+1] + t[i][j+2])
            ans.append(t[i+1][j] + t[i+1][j+1] + t[i+1][j+2] + t[i][j+2])
            ans.append(t[i][j] + t[i][j+1] + t[i][j+2] + t[i+1][j+2])
            ans.append(t[i][j] + t[i+1][j] + t[i+1][j+1] + t[i+1][j+2])
            ans.append(t[i+1][j] + t[i+1][j+1] + t[i][j+1] + t[i][j+2])
            ans.append(t[i][j] + t[i][j+1] + t[i+1][j+1] + t[i+1][j+2])
            ans.append(t[i][j] + t[i][j+1] + t[i+1][j+1] + t[i][j+2])
            ans.append(t[i+1][j] + t[i][j+1] + t[i+1][j+1] + t[i+1][j+2])

print(max(ans))
