import sys
input = sys.stdin.readline

N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]


for person in people:
    rank = 1
    for i in range(N):
        if (people[i][0] > person[0]) and (people[i][1] > person[1]):
            rank += 1
    print(rank, end=' ')