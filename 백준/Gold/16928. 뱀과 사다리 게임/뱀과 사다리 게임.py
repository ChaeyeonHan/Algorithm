from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [0] * 101
visited = [0] * 101

ladder = dict()
for _ in range(N):  # 사다리
    i, j = map(int, input().split())
    ladder[i] = j

snack = dict()
for _ in range(M):  # 뱀
    i, j = map(int, input().split())
    snack[i] = j
    
def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    
    while q:
        current = q.popleft()
        
        for i in range(1, 7):  # 주사위 1~6
            next = current+i
            if 0 <= next <= 100 and not visited[next]:
                if next in ladder:
                    next = ladder[next]
                if next in snack:
                    next = snack[next]
                if not visited[next]:
                    q.append(next)
                    visited[next] = True
                    board[next] = board[current]+1

bfs(1)
print(board[100])