import sys
input = sys.stdin.readline

N = int(input())
max_N = 1000

dp = [False] * (max_N+1)  # dp[i]는 돌이 i개 있을 때, 상근이가 이기는지 여부
dp[1] = True
dp[2] = False
dp[3] = True
dp[4] = True

for i in range(5, N+1):
    # 돌이 i개 남았을 때, 선공이 이기려면 남은 돌 갯수에서 상대방이 모두 질 수 있는 경우여야 한다
    # 후공이 이기는 경우가 하나라도 있으면 선공이 이기지 못함
    if dp[i-1] and dp[i-3] and dp[i-4]:
        dp[i] = False
    else:
        dp[i] = True

if dp[N]:
    print("SK")
else:
    print("CY")