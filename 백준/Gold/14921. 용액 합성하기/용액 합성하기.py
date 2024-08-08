import sys
input = sys.stdin.readline

def find_closest(nums):
    start, end = 0, len(nums) - 1
    answer = float('inf')
    while start < end:
        two_sum = nums[start] + nums[end]
        if abs(two_sum) < abs(answer):
            answer = two_sum
        if answer == 0:
            return 0
        elif two_sum < 0:
            start += 1
        else:
            end -= 1
    return answer

N = int(input())
nums = list(map(int, input().split()))
answer = find_closest(nums)
print(answer)