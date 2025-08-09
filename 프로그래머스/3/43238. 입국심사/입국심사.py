def solution(n, times):
    start, end = 0, max(times) * n
    # 시간을 탐색해서 딱 적절하게 심사할 수 있는 시간을 찾아준다
    
    # 최소 시간을 찾기 위해 시간을 범위로 잡고 이분탐색
    while start <= end:
        mid = (start + end) // 2
        people = 0  #  mid 시간동안 심사한 사람 수
        for t in times:
            people += mid // t  # 심사관이 처리할 수 있는 사람 수 계산
            if people >= n:
                break
        if people >= n:  # 모든 사람 처리 가능. 더 최소시간 찾기
            answer = mid
            end = mid - 1
        else:  # 시간 부족
            start = mid + 1
                
    return answer