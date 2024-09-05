import sys
input = sys.stdin.readline

N = int(input())
graph = [[]]

for _ in range(N):
    graph.append([0] + list(map(int, sys.stdin.readline().split())))

# print(graph)

def count_people(x, y, d1, d2):
    count = [0, 0, 0, 0, 0]
    # 경계구역 설정(5번 구역)
    fifth = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(d1+1):
        fifth[x+i][y-i] = 1
        fifth[x+d2+i][y+d2-i] = 1
    for i in range(d2+1):
        fifth[x+i][y+i] = 1
        fifth[x+d1+i][y-d1+i] = 1
    # 경계선 내부 채우기
    for i in range(x+1, x+d1+d2):
        flag = False
        for j in range(N+1):
            if fifth[i][j] == 1:  # 경계선인 경우
                if flag == True:  # 이거 다음부터 경계선 밖으로 벗어남
                    flag = False
                else:
                    flag = True
            else:
                if flag == True:  # 경계선 안
                    fifth[i][j] = 1
    # 갯수 카운트
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i < x+d1 and j <= y and fifth[i][j] != 1: # 1번 선거구
                count[0] += graph[i][j]
            elif i <= x + d2 and y < j and fifth[i][j] != 1:
                count[1] += graph[i][j]
            elif x + d1 <= i and j < y - d1 + d2 and fifth[i][j] != 1:
                count[2] += graph[i][j]
            elif x + d2 < i and y - d1 + d2 <= j and fifth[i][j] != 1:
                count[3] += graph[i][j]
            elif fifth[i][j] == 1:
                count[4] += graph[i][j]
    return max(count)-min(count)


# 경계선 완전탐색
result = float('inf')
for x in range(1, N+1):
    for y in range(1, N+1):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                if 1 <= x < x+d1+d2 <= N and 1 <= y-d1 < y < y+d2 <= N:
                    result = min(result, count_people(x,y,d1,d2))
print(result)