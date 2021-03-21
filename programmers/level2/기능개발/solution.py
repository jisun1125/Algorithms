def solution(progresses, speeds):
    day = []
    temp = 0
    for i in range(len(progresses)):
        # temp = (100-progresses[i])
        temp = progresses[i]
        tempDay = 0
        dayCnt = 0
        while temp < 100:
            temp += speeds[i]
            dayCnt += 1
        day.append(dayCnt)
    print(day)
    answer = []

    # for문 돌려서 day 배열 안에 있는 값 끼리 비교
    first = day[0]
    count = 1
    for i in range(1, len(day)):
        # 마지막인 경우를 따로 빼야하나
        if first >= day[i]:  # 기다렸다가 같이 배포되는 경우
            count += 1
        else:
            answer.append(count)
            first = day[i]
            count = 1
    answer.append(count)
    return answer
