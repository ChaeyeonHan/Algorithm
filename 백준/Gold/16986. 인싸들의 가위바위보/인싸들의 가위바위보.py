import sys
from itertools import permutations
input = sys.stdin.readline

N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

p2 = list(map(int, input().split()))
p3 = list(map(int, input().split()))
hands = [x for x in range(1, N+1)]

def simulate(py1, py2, wins, players, index):
    global result
    if wins[0] == K:
        result = 1
        return
    if wins[1] == K or wins[2] == K:
        return
    if index[0] == N:
        return
    py3 = 3-(py1+py2)  # 그다음에 출전할 선수
    a = players[py1][index[py1]]-1  # 각자 낸 손모양
    b = players[py2][index[py2]]-1
    index[py1] += 1
    index[py2] += 1
    if A[a][b] == 2 or (A[a][b] == 1 and py1 > py2):
        wins[py1] += 1
        simulate(py1, py3, wins, players, index)
    elif A[a][b] == 0 or (A[a][b] == 1 and py1 < py2):
        wins[py2] += 1
        simulate(py2, py3, wins, players, index)


for p1 in permutations(hands, N):
    wins = [0, 0, 0]  # 지우/경희/민호 각각 몇번 우승했는지
    players = [p1, p2, p3]  # 각각 내는 손모양 이중리스트
    index = [0, 0, 0]  # 각 게임에서 어떤 손모양을 낼지(그 다음에 어떤 손모양 낼지 결정해주려고)
    result = 0
    simulate(0, 1, wins, players, index)
    if result:
        print(1)
        sys.exit(0)  # 이거!!
print(0)