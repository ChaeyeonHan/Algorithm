import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
positions = [0] + list(map(int, input().split())) + [L]
positions.sort()

start, end = 1, L-1
result = 0
while start <= end:
    mid = (start+end) // 2
    required = 0
    for i in range(1, len(positions)):
        distance = positions[i]-positions[i-1]
        if distance > mid:  # mid보다 더 멀면
            required += (distance-1) // mid  # 현재 설치된 지점 제외(위치 중복X)
    if required > M:
        start = mid + 1
    else:
        end = mid - 1
        result = mid
print(result)