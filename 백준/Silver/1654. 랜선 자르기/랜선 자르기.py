# 기존에 갖고 있는 K개의 랜선을 잘라서 N개의 랜선 만들기
# 만들 수 있는 최대 랜선의 길이 구하기

# 이진탐색으로 최대 몇cm로 자를건지 찾아낸다
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
heights = [int(input()) for _ in range(K)]
# print(heights)

start, end = 1, max(heights)

while start <= end:
    cnt = 0
    mid = (start+end) // 2
    for i in heights:
        cnt += (i // mid)
    if cnt < N:  # 자른 갯수가 모자란 경우 -> 더 짧게 자르기
        end = mid -1
    else:
        start = mid + 1
        result = mid
print(result)
        