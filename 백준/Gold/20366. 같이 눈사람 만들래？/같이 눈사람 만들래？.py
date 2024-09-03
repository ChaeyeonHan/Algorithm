import sys
input = sys.stdin.readline

N = int(input())
H = sorted(list(map(int, input().split())))
diff = float('inf')

for i in range(N-3):
    for j in range(i+3, N):
        fix = H[i]+H[j]
        left, right = i+1, j-1
        while left < right:
            now = H[left]+H[right]
            if diff > abs(fix-now):
                diff = abs(fix-now)

            if now > fix:
                right -= 1
            elif fix > now:
                left += 1
            else:  # 값이 동일
                print(0)
                sys.exit(0)
print(diff)