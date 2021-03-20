from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque(priorities)
    while queue:
        if location < 0:
            location = len(queue) - 1
        if queue[0] < max(queue):
            queue.append(queue.popleft())
            location -= 1
        else:
            queue.popleft()
            answer += 1
            if location == 0:
                return answer
            location -= 1
