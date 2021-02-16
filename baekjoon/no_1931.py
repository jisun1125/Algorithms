# 2021-02-16
# url : https://www.acmicpc.net/problem/1931
# 1931 회의실 배정
n = int(input())

meeting = list()
cnt = 0
start_time = 0
for i in range(n):
    a1, a2 = map(int, input().split())  # 시작시간, 종료시간
    meeting.append((a1, a2))

#정렬에 람다 사용
meeting = sorted(meeting, key=lambda time: time[0])  # 시작시간 기준 정렬
meeting = sorted(meeting, key=lambda time: time[1])  # 그 상태에서 종료시간 기준 정렬

for i in range(n):
    if meeting[i][0] >= start_time:
        start_time = meeting[i][1]  # 바로 시작할 수 있으므로
        cnt += 1
print(cnt)
