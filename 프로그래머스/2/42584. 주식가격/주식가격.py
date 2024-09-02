from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    while queue:
        price = queue.popleft()
        sec = 0
        for next in queue:
            sec += 1
            if price > next:
                break
        answer.append(sec)
    return answer