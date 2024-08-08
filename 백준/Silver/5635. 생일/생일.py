import sys
input = sys.stdin.readline

N = int(input())
people = []
for _ in range(N):
    name, d, m, y = input().split()
    people.append((name, int(d), int(m), int(y)))
people.sort(key=lambda x: (x[3], x[2], x[1]))  # 나이 많은 사람순으로 정렬
print(people[-1][0])
print(people[0][0])