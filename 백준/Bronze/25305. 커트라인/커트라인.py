import sys
input = sys.stdin.readline

N, k = map(int, input().split())
nums = sorted(list(map(int, input().split())), reverse=True)
# 상을 받는 K명
print(nums[k-1])