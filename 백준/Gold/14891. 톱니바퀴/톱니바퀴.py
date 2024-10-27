import sys
from collections import deque
input = sys.stdin.readline

wheel = [deque(list(map(int, input().rstrip()))) for _ in range(4)]

# 맞닿는 idx: 2/26/26/6
# print(wheel)  # [[1, 0, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 0, 1], [1, 1, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 1, 0]]

K = int(input())  # 회전 횟수
# 번호, 방향
for _ in range(K):
    num, direction = map(int, input().split())
    x = []
    for i in range(4):
        x.append([wheel[i][6], wheel[i][2]])  # 맞닿는 idx에 속하는 톱니 저장
    num -= 1
    # 왼쪽 톱니 돌리기
    if num != 0:
        for i in range(num, 0, -1):
            if x[i][0] != x[i-1][1]:  # N극과 S극이면
                if (num-(i-1)) % 2 == 0:
                    wheel[i-1].rotate(direction)
                else:
                    wheel[i-1].rotate(-1*direction)
            elif x[i][0] == x[i-1][1]:  # 같은 값으로 맞물린다면 회전X, 더이상 확인할 필요X
                break


    # 오른쪽 톱니 돌리기
    if num !=3:
        for i in range(num, 3):
            if x[i][1] != x[i+1][0]:
                if (num-(i+1)) % 2 == 0:
                    wheel[i+1].rotate(direction)
                else:
                    wheel[i+1].rotate(-1*direction)
            elif x[i][1] == x[i+1][0]:
                break
    wheel[num].rotate(direction)

result = 0
if wheel[0][0] == 1:
    result += 1
if wheel[1][0] == 1:
    result += 2
if wheel[2][0] == 1:
    result += 4
if wheel[3][0] == 1:
    result += 8
print(result)