import sys, math
input = sys.stdin.readline


max_num = 100000
dp = [float('inf')] * (max_num+1)
for i in range(1, int(math.sqrt(len(dp)))+1):  # 내림처리
    dp[i*i] = 1

for i in range(1, len(dp)):
    if dp[i] == 1:  # 제곱수인 경우는 넘어감
        continue
    for j in range(1, int(math.sqrt(i))+1):
        dp[i] = min(dp[i], dp[i-j*j]+1)

N = int(input())
print(dp[N])