import sys
input = sys.stdin.readline

N = int(input())
balls = []  # 각 층에서 필요한 공 갯수  balls = [1, 4, 10, 20 ..]
a = 1
num = 0

while N > num:
    num += (a*(a+1))//2
    balls.append(num)
    a += 1

dp = [300001 for _ in range(N+1)]
for i in range(1, N+1):
    for b in balls:
        if b in balls:
            if b == i:
                dp[i] = 1  # 사면체 한개 만들 수 있음
            if b > i:
                break
            dp[i] = min(dp[i], dp[i-b]+1)
print(dp[N])