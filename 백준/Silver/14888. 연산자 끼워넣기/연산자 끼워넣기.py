import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())  # 덧셈/뺄셈/곱셈/나눗셈
max_result = -int(1e9)
min_result = int(1e9)

def dfs(depth, total, add, sub, mul, div):
    global max_result, min_result
    if depth == N:
        max_result = max(max_result, total)
        min_result = min(min_result, total)
        return
    if add:
        dfs(depth + 1, total + nums[depth], add-1, sub, mul, div)
    if sub:
        dfs(depth + 1, total - nums[depth], add, sub-1, mul, div)
    if mul:
        dfs(depth + 1, total * nums[depth], add, sub, mul - 1, div)
    if div:
        dfs(depth + 1, int(total / nums[depth]), add, sub, mul, div - 1)

dfs(1, nums[0], add, sub, mul, div)

print(max_result)
print(min_result)