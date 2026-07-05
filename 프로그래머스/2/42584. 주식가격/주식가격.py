# from collections import deque

# def solution(prices):
#     answer = []
#     queue = deque(prices)
#     while queue:
#         price = queue.popleft()
#         sec = 0
#         for next in queue:
#             sec += 1
#             if price > next:
#                 break
#         answer.append(sec)
#     return answer


from collections import deque
def solution(prices):
    answer = []
    queue = deque(prices)
    while queue:
        cur = queue.popleft()
        time = 0
        for next in queue:
            time += 1
            if cur > next:  # 가격 떨어짐
                break
        answer.append(time)
    return answer
