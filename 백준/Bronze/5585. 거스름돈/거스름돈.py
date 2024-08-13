import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
result = 1000-n  # 잔돈가격
coins = [500, 100, 50, 10, 5, 1]  # 큰 단위부터

for i in coins:
    cnt += result // i
    result = result % i
print(cnt)
