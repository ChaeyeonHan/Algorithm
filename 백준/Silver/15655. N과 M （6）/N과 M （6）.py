import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

tmp = []
def dfs(start):
    if len(tmp) == M:
        for i in range(M):
            print(tmp[i], end=' ')
        print('')
        return
    for i in range(start, N):
        if nums[i] in tmp:
            continue
        tmp.append(nums[i])
        dfs(i)
        tmp.pop()

dfs(0)