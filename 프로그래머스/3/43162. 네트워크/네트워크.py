# def solution(n, computers):
#     answer = 0
#     visited = [0 for _ in range(n)]

#     for i in range(n):
#         if visited[i] == 0:
#             dfs(n, computers, visited, i)
#             answer += 1  # 모두 방문하고 빠져나오면 네트워크 +1

#     return answer

# def dfs(n, computers, visited, v):
#     visited[v] = 1
#     for i in range(n):
#         if visited[i] == 0 and computers[v][i] == 1:
#             dfs(n, computers, visited, i)


def dfs(computers, i, n):
    visited[i] = True
    for  j in range(n):
        if not visited[j] and i != j and computers[i][j] == 1:
            dfs(computers, j, n)



def solution(n, computers):
    global visited
    visited = [0] * n
    cnt = 0  # 네트워크 갯수
    for i in range(n):
        if not visited[i]:
            dfs(computers, i, n)
            cnt += 1
    return cnt