def solution(a, b, g, s, w, t):
    start = 0
    # 금은 최대 무게: 10**9*2 
    # 도시 1개에서 최대 1씩 옮길 수 있을 때: 10**5*2(왕복)
    answer = end = (10**9) * (10**5) * 4
    while start <= end:
        mid = (start+end) // 2
        gold, silver, total  = 0, 0, 0
        
        for i in range(len(g)):
            cur_gold = g[i]
            cur_silver = s[i]
            cur_weight = w[i]
            cur_time = t[i]
            
            # 이동 횟수(왕복 횟수)
            move =  mid // (cur_time*2)
            if mid % (cur_time*2) >= cur_time:  # 편도 이동 횟수
                move += 1
            
            possible = move * cur_weight
            gold += min(cur_gold, possible)  # 도시에 있는것보다 초과해서 가져올 수 없으니까
            silver += min(cur_silver, possible)
            
            total += min(cur_gold+cur_silver, possible)
            
        if total >= a+b and gold >= a and silver >= b:
            end = mid-1  # 더 짧은 시간 가능한지 확인
            answer = min(answer, mid)
        else:
            start = mid+1  # 시간 더 필요
    return answer