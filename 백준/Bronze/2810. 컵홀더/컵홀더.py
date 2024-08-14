import sys
input = sys.stdin.readline

N = int(input())
seats = input().rstrip()

couple = seats.count('LL')

if couple == 0:
    print(N)
else:
    print(N-couple+1)
