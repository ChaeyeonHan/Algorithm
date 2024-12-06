import sys
input = sys.stdin.readline

N = int(input())
tops = list(map(int, input().split()))

answer = [0] * N
stack = []

for i in range(len(tops)):
    while stack:
        if tops[stack[-1][0]] < tops[i]:
            stack.pop()
        else:
           answer[i] = stack[-1][0] + 1
           break

    stack.append([i, tops[i]])

print(*answer)