import sys
from itertools import permutations
input = sys.stdin.readline

A, B = input().split()  # permutation함수에 반복가능한 객체 넣기 위해 int로 받으면X

# B보다는 작으면서 가장 큰 값. A의 숫자를 섞어서 새로운 C 만들기
# 첫번째 숫자가 0인거 제외하기
"""
파이썬 순열: 반복가능한 객체에 대해 중복을 허용하지 않고 r개 뽑아서 나열
뒤에 숫자 생략하면 모든 원소를 사용하는 순열이 생성됨
1. from itertools import permutations

2. import itertools -> 근데 이렇게 쓰면 반드시 itertools. 붙여야 한다
result = list(itertools.permutations(반복 객체, 2))
print(result)
"""
B = int(B)
C_list = list(permutations(A))
answer = -1

for case in C_list:
    if case[0] == '0':
        continue
    num = int("".join(case))
    if num < B:
        answer = max(answer, num)
print(answer)