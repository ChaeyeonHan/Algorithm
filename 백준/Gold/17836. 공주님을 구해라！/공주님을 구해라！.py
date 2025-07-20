import sys
from collections import deque
input = sys.stdin.readline

N, M, T = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 0빈공간 1벽 2그람
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

def bfs():
    gram = 10001
    q = deque()
    q.append([0,0])
    visited[0][0]=1
    while q:
        x, y = q.popleft()
        if x == N-1 and y == M-1:  #  공주에게 도착
            return min(gram, visited[x][y]-1)
        if graph[x][y] == 2:
            gram = visited[x][y]-1 + N-1-x + M-1-y
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if graph[nx][ny] == 0 or graph[nx][ny] == 2:
                    visited[nx][ny] = visited[x][y]+1
                    q.append([nx, ny])
    return gram

result = bfs()
if result > T:
    print("Fail")
else:
    print(result)