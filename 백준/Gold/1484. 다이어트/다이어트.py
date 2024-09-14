import sys
input = sys.stdin.readline

G = int(input())

# 제곱수-제곱수 = G
max_len = 100000
arr = [x**2 for x in range(100001)]
result = []
left, right = 1, 2

while right+left <= G:
    if arr[right]-arr[left] < G:
        right += 1
    elif arr[right]-arr[left] > G:
        left += 1
    else:
        result.append(right)
        left += 1

if result:
    print(*result)
else:
    print(-1)