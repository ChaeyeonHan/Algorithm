import sys
from collections import Counter
# 여러 형태의 데이터를 인자로 받아서, 각 원소가 몇번씩 나오는지 저장된 객체를 얻는다
# 데이터의 갯수를 셀때 유용
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

cnt = Counter(nums)
# print(cnt)
# Counter({10: 3, 3: 2, -10: 2, 6: 1, 2: 1, 7: 1})
for target in targets:
    print(cnt[target], end=' ')