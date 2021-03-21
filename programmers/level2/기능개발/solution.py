def solution(progresses, speeds):
    day = []
    for i in range(len(progresses)):
        temp = progresses[i]
        dayCnt = 0
        while temp < 100:
            temp += speeds[i]
            dayCnt += 1
        day.append(dayCnt)
    answer = []

    # for문 돌려서 day 배열 안에 있는 값 끼리 비교
    first = day[0]
    count = 1
    for i in range(1, len(day)):
        if first >= day[i]:  # 기다렸다가 같이 배포되는 경우
            count += 1
        else:
            answer.append(count)
            first = day[i]
            count = 1
    answer.append(count)
    return answer
