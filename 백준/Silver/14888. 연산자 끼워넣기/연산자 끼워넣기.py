import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

# 방법1: DFS 이용
max_result = -1e9
min_result = 1e9

def dfs(depth, total, add, sub, mul, div):
    global max_result, min_result
    if depth == N:  # 모든 연산 완료
        max_result = max(total, max_result)
        min_result = min(total, min_result)
        return
    if add:
        dfs(depth+1, total + nums[depth], add-1, sub, mul, div)
    if sub:
        dfs(depth+1, total - nums[depth], add, sub-1, mul, div)
    if mul:
        dfs(depth+1, total * nums[depth], add, sub, mul-1, div)
    if div:
        dfs(depth+1, int(total / nums[depth]), add, sub, mul, div-1)

dfs(1, nums[0], add, sub, mul, div)

print(max_result)
print(min_result)
