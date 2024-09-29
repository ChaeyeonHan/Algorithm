import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())  # 세로선, 놓여진 가로선 갯수, 놓을 수 있는 가로선 갯수
board = [[0]*N for _ in range(H)]

if M == 0:  # 출발점에서 바로 도착점으로
    print(0)
    exit(0)

# 가로선 정보: a,b
for _ in range(M):
    a, b = map(int, input().split())
    board[a-1][b-1] = True

def check():  # i번 세로선 결과가 i인지 체크
    for start in range(N):
        k = start  # 세로선의 시작점
        for j in range(H):
            if board[j][k]:  # 가로선 있으면
                k += 1  # 가로선 오른쪽으로 이동
            elif k > 0 and board[j][k-1]:
                k -= 1  # 왼쪽으로 이동
        if k != start:  # 세로선의 도착점과 시작점이 다른 경우
            return False
    return True


def dfs(cnt, x, y):
    global answer
    if check():
        answer = min(answer, cnt)
        return
    elif cnt == 3 or answer <= cnt:  # 조건 위반(3개 이상 추가하면 X)
        return
    for i in range(x, H):  # 행. 탐색한 높이랑 중복되지 않게 x부터 시작
        if i == x:
            k = y
        else:  # 행이 변경되면 가로선 처음부터 탐색
            k = 0
        for j in range(k, N - 1):  # 열.가로선 넣을 수 있는지 탐색
            if not board[i][j] and not board[i][j + 1]:  # 현재 위치랑 오른쪽에 사다리 없는 경우
                if j > 0 and board[i][j - 1]:  # 왼쪽에 가로선 있으면 continue
                    continue
                board[i][j] = True  # 가로선 놓기
                dfs(cnt + 1, i, j + 2)  # 연속된 가로선 만들지 않기위해 +2
                board[i][j] = False  # 가로선 제거

answer = 4
dfs(0, 0, 0)
print(answer if answer < 4 else -1)