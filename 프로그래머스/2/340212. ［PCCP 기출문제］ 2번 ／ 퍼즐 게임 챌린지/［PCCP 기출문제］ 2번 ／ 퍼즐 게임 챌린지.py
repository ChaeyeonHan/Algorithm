def solution(diffs, times, limit):
    answer = 0
    left, right = 1, max(diffs)
    while left <= right:
        mid = (left+right) // 2
        if cal(diffs, times, limit, mid):
            answer = mid
            right = mid-1
        else:
            left = mid+1    
    return answer


def cal(diffs, times, limit, level):
    time_need = 0
    for i in range(len(diffs)):
        diff = diffs[i]
        time_cur = times[i]
        time_prev = 0
        if i != 0:
            time_prev = times[i-1]
        if diff <= level:
            time_need += time_cur
        else:
            time_need += (time_prev+time_cur)*(diff-level)+time_cur  
        if time_need > limit:
            return False
    return True