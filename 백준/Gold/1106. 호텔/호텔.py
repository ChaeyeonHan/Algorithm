import sys
input = sys.stdin.readline

C, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]  # (비용, 고객)

MAX_COST = int(1e6)
dp = [1e9 for _ in range(MAX_COST+1)]  # dp[i]: 사람 i명 늘어나는데 최소 비용
dp[0] = 0

for cost, customer in arr:
    for i in range(customer, MAX_COST):
        dp[i] = min(dp[i], dp[i-customer]+cost)

print(min(dp[C:]))