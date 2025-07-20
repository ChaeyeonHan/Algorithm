def solution(players, m, k):
    answer = 0
    # m명 늘어날때마다 서버 1대 추가. 서버는 k시간 운영 후 반납
    server = [0 for _ in range(len(players))]
    for i in range(len(players)):
        if players[i] >= m:
            n = players[i] // m  # 필요한 서버 수
            
            if server[i] < n:  # 서버가 부족한 경우
                require = n-server[i]  # 필요한 서버 수
                answer += require
                
                for j in range(k):  # k시간 동안만 유효. 그 시간 범위에만 더해서 추가
                    if i+j < len(server):
                        server[i+j] += require
                    else:
                        break
                    
        
    return answer