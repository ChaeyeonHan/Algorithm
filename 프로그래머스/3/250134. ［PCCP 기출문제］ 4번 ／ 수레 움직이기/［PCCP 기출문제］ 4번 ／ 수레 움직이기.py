from collections import deque
import copy

def solution(maze):
    answer = 0  # 움직인 횟수
    red_visited = [[0]*4 for _ in range(4)]
    blue_visited = [[0]*4 for _ in range(4)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    n, m = len(maze), len(maze[0])
    red, blue = [], []  # 시작 위치
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                red = [i, j]
                red_visited[i][j] = 1
            elif maze[i][j] == 2:
                blue = [i, j]
                blue_visited[i][j] = 1
    
    q = deque()
    q.append([red[0], red[1], blue[0], blue[1], red_visited, blue_visited, answer])
    
    while q:
        rx, ry, bx, by, red_visited, blue_visited, answer = q.popleft()
        if maze[rx][ry] == 3 and maze[bx][by] == 4:  # 수레 모두 도착한 경우
            return answer
        else:
            if maze[rx][ry] == 3:  # 빨간색만 도착
                for i in range(4):
                    nx, ny = bx+dx[i], by+dy[i]
                    if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != 5 and blue_visited[nx][ny] == 0:
                        if not (nx == rx and ny == ry):  # 겹치지 않아야 함
                            blue_visited[nx][ny] = 1
                            q.append([rx, ry, nx, ny, red_visited, blue_visited, answer+1])
            elif maze[bx][by] == 4:  # 파란색만 도착
                for i in range(4):
                    nx, ny = rx+dx[i], ry+dy[i]
                    if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != 5 and red_visited[nx][ny] == 0:
                        if not (nx == bx and ny == by):  # 겹치지 않아야 함
                            red_visited[nx][ny] = 1
                            q.append([nx, ny, bx, by, red_visited, blue_visited, answer+1])
            else:
                for i in range(4):
                    rnx, rny = rx+dx[i], ry+dy[i]
                    rc_visited = copy.deepcopy(red_visited)
                    bc_visited = copy.deepcopy(blue_visited)
                    
                    if not (0 <= rnx < n and 0 <= rny < m and maze[rnx][rny] != 5 and red_visited[rnx][rny] == 0):
                        continue
                    for j in range(4):
                        bnx, bny = bx+dx[j], by+dy[j]
                        if (0 <= bnx < n and 0 <= bny < m and maze[bnx][bny] != 5 and blue_visited[bnx][bny] == 0):
                            if not (rnx == bnx and rny == bny) and not (rnx == bx and rny == by and bnx == rx and bny == ry):  # 동시에 같은 칸으로 X, 자리 바꾸며 움직일 수 X
                                rc_visited[rnx][rny] = 1
                                bc_visited[bnx][bny] = 1
                                q.append([rnx, rny, bnx, bny, rc_visited, bc_visited, answer+1])
    return 0