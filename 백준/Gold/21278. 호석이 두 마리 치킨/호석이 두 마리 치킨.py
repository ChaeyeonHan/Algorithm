import sys
input = sys.stdin.readline

N, M = map(int, input().split())
INF = int(1e9)

graph = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for a in range(1, N+1):
    for b in range(1, N+1):
        if a == b:
            graph[a][b] = 0

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

min_sum = INF
result = list()
for i in range(1, N):
    for j in range(2, N+1):
        total = 0
        for k in range(1, N+1):
            total = min(graph[k][i], graph[k][j])*2
        if total < min_sum:
            min_sum = total
            result = [i, j, total]
print(*result)