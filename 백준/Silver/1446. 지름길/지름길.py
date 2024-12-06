import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)  # (거리, 현재노드)
        if dist > distance[now]:
            continue
        
        for i in graph[now]:  # 현재 노드에서 갈 수 있는 노드 확인(지름길 포함)
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]
distance = [INF] * (D+1)

for i in range(D):
    graph[i].append((i+1, 1))

for _ in range(N):
    start, end, length = map(int, input().split())
    if end > D:
        continue
    graph[start].append((end, length))

dijkstra(0)
print(distance[D])
