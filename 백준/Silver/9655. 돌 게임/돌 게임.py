import sys
input = sys.stdin.readline

N = int(input())
max_num = 1000
dp = [0] * (max_num+1)
dp[1] = 1  # 상근 win
dp[2] = 0
dp[3] = 1

for i in range(4, N+1):
    if dp[i-1] or dp[i-3]:
        dp[i] = 0
    else:
        dp[i] =1

if dp[N]:
    print("SK")
else:
    print("CY")