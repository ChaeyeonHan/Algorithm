# def solution(progresses, speeds):
#     result = []
#     day, count = 0, 0  # 작업일수, 배포된 작업 갯수
    
#     while progresses:
#         if (progresses[0] + speeds[0] * day) >= 100:
#             progresses.pop(0)
#             speeds.pop(0)
#             count += 1
#         else:
#             if count > 0:  #현재작업은 끝나지 않았지만 앞에서 배포작업이 있었다면
#                 result.append(count)
#                 count = 0
#             day += 1
#     result.append(count)  #마지막 작업은 append 시키지않고 while문에서 빠져나옴
#     return result

def solution(progresses, speeds):
    days = []   # 남은 개발에 필요한 일수
    for i in range(len(progresses)):
        remain = 100-progresses[i]
        cnt = remain % speeds[i]
        # 더 짧게 작성. -1을 하면 올림 나눗셈.
        # day = (100 - progresses[i] + speeds[i] - 1) // speeds[i]
        if cnt == 0:
            cnt = remain // speeds[i]
        else:
            cnt = remain // speeds[i] + 1
        days.append(cnt)
    
    answer = []
    cur_day = days[0]
    cnt = 1
    
    for i in range(1, len(days)):
        if days[i] <= cur_day:
            cnt += 1
        else:
            answer.append(cnt)
            cur_day = days[i]
            cnt = 1
    answer.append(cnt)
    
    return answer